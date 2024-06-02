def get_user_headers():
    print("Please enter the headers starting from the Host header (Press Enter twice to finish):")
    user_input = []
    while True:
        line = input()
        if line == "":
            break
        user_input.append(line)
    headers_text = "\n".join(user_input)
    return headers_text

def process_headers(headers_text):
    # Split the input text into lines
    lines = headers_text.strip().split('\n')
    
    # Initialize an empty dictionary to store the headers
    headers_dict = {}
    url = None
    tracking_id = None
    session_id = None
    
    # Process each line to extract the header name and value
    for line in lines:
        if ": " in line:
            key, value = line.split(": ", 1)
            if key.strip().lower() == 'host':
                url = f"https://{value.strip()}"
            elif key.strip().lower() == 'cookie':
                cookies = value.strip().split('; ')
                for cookie in cookies:
                    if cookie.startswith('TrackingId='):
                        tracking_id = cookie.split('=', 1)[1]
                    elif cookie.startswith('session='):
                        session_id = cookie.split('=', 1)[1]
            else:
                headers_dict[key.strip()] = value.strip()
    
    return headers_dict, url, tracking_id, session_id
