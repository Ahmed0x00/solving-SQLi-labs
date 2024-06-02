from headers import get_user_headers, process_headers
from user_choice import get_user_choice
from password_retrieval import retrieve_password

def main():
    option = get_user_choice()
    headers_text = get_user_headers()
    headers, url, tracking_id, session_id = process_headers(headers_text)
    print("Retrieving the password..")
    retrieve_password(headers, url, tracking_id, session_id, option)

if __name__ == "__main__":
    main()
