# solving-SQLi-labs
this script was created to solve these 3 portswigger’s Blind SQLi labs:
1. Blind SQL injection with conditional responses
2. Blind SQL injection with conditional errors
3. Blind SQL injection with time delays and information retrieval

## How to run
**1. Install Dependencies**: Install the required Python libraries using pip:
```sh
pip install requests
```
**2. Run the Script**:
Execute the main script:
```sh
python main.py
```
or run it in your IDE
**3. Follow the Prompts**:
- Choose the SQL injection method (1 for Conditional Response, 2 for Conditional Errors, 3 for Time Delays).
- Enter the headers starting from the Host header (press Enter twice to finish).

## Explaining libraries and modules used
### requests
**What it does**: Allows the script to interact with web servers by making HTTP requests and handling responses.
**How it's used**:
1. **Making HTTP Requests**:
   - `session = requests.Session()`
   - Creates a session object to manage cookies and other parameters across multiple requests.
2. **Sending GET Requests**:
   - `response = session.get(url, headers=headers, cookies=cookie)`
   - Sends a GET request to the specified URL.
   - Custom headers and cookies can be passed as parameters.
3. **Accessing Response**:
   - `response.text`: Retrieves the response body as a string.
   - `response.status_code`: Retrieves the HTTP status code of the response.

### Concurrent.futures
**What it does**: Provides a way to run tasks concurrently (at the same time).
**How it's used**:
1. **Creating Executor**: 
   - `with concurrent.futures.ThreadPoolExecutor() as executor:`
   - Creates a pool of worker threads to execute tasks.
2. **Submitting Tasks**:
   - `executor.submit(task_function, args)`
   - Submits a task (function) to be executed asynchronously.
   - Example: `executor.submit(test_function, arg1, arg2)`
3. **Waiting for Tasks to Complete**:
   - `for future in concurrent.futures.as_completed(futures):`
   - Waits for submitted tasks to complete.
   - Example: `for future in concurrent.futures.as_completed(futures): pass`

### threading 
**What it does**: Allows the script to execute multiple tasks concurrently by creating and managing multiple threads of execution.
**How it's used**:
1. **Creating a Lock**:
   - `lock = threading.Lock()`
   - Creates a lock object to synchronize access to a shared resource.
2. **Acquiring and Releasing the Lock**:
   - `with lock:`
   - Acquires the lock before accessing the shared resource and releases it afterward.
   - Ensures that only one thread can access the critical section (shared resource) at a time to prevent data corruption.
3. **Example**:
   - In the script, a lock is used to ensure thread-safe access to the `found_password` list.
   - Before modifying or accessing `found_password`, a thread acquires the lock using `with lock:`.
   - Once the critical section is executed, the lock is released automatically.
   - This ensures that only one thread can modify `found_password` at a time, preventing race conditions and ensuring data integrity.

## How the Script Works
1. **Get User Headers**: The script prompts the user to input HTTP headers. This information is crucial for making authenticated requests to the target application.
2. **Process Headers**: The headers are processed to extract essential details such as the target URL, `TrackingId`, and `session` values from the cookies.
3. **Choose Injection Method**: The user is prompted to choose one of three SQL injection methods:
    - **Conditional Response**: Determines if a condition is true based on changes in the HTTP response body.
    - **Conditional Errors**: Uses server errors to infer information.
    - **Time Delays**: Uses time-based SQL injections to determine if a condition is true by measuring response times.
4. **Retrieve Password**: The script tests each character of the password for the administrator user. It constructs SQL injection payloads and sends requests in parallel to speed up the process. The correct character for each position is determined based on the chosen method.
5. **Output**: The script outputs the retrieved password and the time taken to find it.
