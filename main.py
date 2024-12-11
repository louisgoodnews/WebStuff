import asyncio
from debug import test_get, test_post

async def main() -> None:
    # Make a GET request
    response = await test_get()
    if response:
        print("GET Response:", response)
    
    # Make a POST request
    post_response = await test_post()
    if post_response:
        print("POST Response:", post_response)

if __name__ == "__main__":
    asyncio.run(main())