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
            if(error != None):
                return  error['message']
            return result['choices'][0]['message']['content']

# Example usage
async def main():
    # You may put this in a loop to ask multiple questions
    question = "What is the capital of France?"
    answer = await call_openai_api(question)
    print(answer)

# Run the example
asyncio.run(main())