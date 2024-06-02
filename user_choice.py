def get_user_choice():
    while True:
        print("Choose an option:")
        print("1. Conditional Response")
        print("2. Conditional Errors")
        print("3. Time Delays and information retrieval")
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
