
#Python OpenAI Chat with Asynchronous Completion Calls

This `README.md` explains how to use the OpenAI's post endpoint ` 'https://api.openai.com/v1/chat/completions',` asynchronously with the provided Python script using `aiohttp` and `asyncio`. The API key is securely stored as an environment variable using **PowerShell**.

## Getting an API Key

You must purchase a subscription to **OpenAI** in order to generate an API key. Once subscribed, you will be able to create API keys from the OpenAI dashboard for use with their services. The cost is $20 per month which we find acceptable.  ChatGPT alone is able to replace many tools on your desktop.

## Important Warning: Store Your API Key Immediately

**Warning**: You must immediately store your API key when it is issued by OpenAI. **OpenAI does not allow you to view your API key again** after it has been generated. If you lose the key, you will need to create a new one. Make sure to store it securely in an environment variable or a password manager.

---

## Setting the API Key in PowerShell

### 1. **Set Environment Variable Temporarily (Current Session)**:
If you're using **PowerShell**, use the following command to set the environment variable for the current session:

```powershell
$env:OPENAI_API_KEY = "your-api-key-here"
```

This will set the variable `OPENAI_API_KEY` temporarily, and it will only be available during this session.

### 2. **Check the Variable**:
To verify that the variable has been set, use the following command:

```powershell
echo $env:OPENAI_API_KEY
```

This will print the value of the `OPENAI_API_KEY`.

### 3. **Set Environment Variable Permanently**:
To set the environment variable permanently (so it remains available across PowerShell sessions), use:

```powershell
[System.Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "your-api-key-here", "User")
```

After setting it permanently, restart PowerShell or open a new session to access the variable.

### 4. **List All Environment Variables**:
To list all environment variables in PowerShell, use:

```powershell
Get-ChildItem Env:
```

This command will display all environment variables and their values.

### 5. **Display a Single Environment Variable**:
If you want to display the value of a specific environment variable, such as `OPENAI_API_KEY`, use:

```powershell
echo $env:OPENAI_API_KEY
```

---

## Using the OpenAI API in Python

Here’s a Python script that asynchronously calls the OpenAI API using the `aiohttp` library. This script retrieves the API key from the environment and sends a question to the `gpt-4` model.

### Install Required Packages:

Make sure you install the necessary libraries first:

```powershell
pip install aiohttp
```

### Python Code Example:

```python
import aiohttp
import asyncio
import os

# Get the OpenAI API key from environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

# Asynchronous function to call OpenAI API
async def call_openai_api(question, model="gpt-4", temperature=0.7, max_tokens=150):
    async with aiohttp.ClientSession() as session:
        async with session.post(
            'https://api.openai.com/v1/chat/completions',
            headers={
                'Authorization': f'Bearer {openai_api_key}',
                'Content-Type': 'application/json'
            },
            json={
                'model': model,
                'messages': [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": question}
                ],
                'max_tokens': max_tokens,
                'temperature': temperature
            }
        ) as response:
            result = await response.json()
            error = result.get('error')
            if error is not None:
                return error['message']
            return result['choices'][0]['message']['content']

# Example usage
async def main():
    question = "What is the capital of France?"
    answer = await call_openai_api(question)
    print(answer)

# Run the example
asyncio.run(main())
```

### Explanation of the Code:

- **aiohttp**: Used for making asynchronous HTTP requests.
- **asyncio**: Used to run asynchronous functions in Python.
- **call_openai_api**: This function makes a POST request to the OpenAI API, sends the user’s question, and retrieves the response.
- **Authorization**: The API key is retrieved from the environment variable and passed in the request headers for authentication.

---

## Important Security Note

Storing your API key in an environment variable keeps it out of your source code, ensuring that it's not exposed if your code is shared or committed to version control systems like Git.

