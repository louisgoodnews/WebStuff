import asyncio
import json
from typing import *

from headers import Headers
from url_builder import URLBuilder
from web_service import WebService
from logger import Logger


async def test_get() -> Dict[str, Any] | None:
    """Test GET request with custom headers"""
    url = URLBuilder(base_url="https://httpbin.org/").build_url("get")
    headers = Headers()
    headers.update(**{"X-Test-Header": "test-value"})
    
    response = await WebService.get(url, headers=headers.headers, log=True)
    return response


async def test_post() -> Dict[str, Any] | None:
    """Test POST request with JSON data"""
    url = URLBuilder(base_url="https://httpbin.org/").build_url("post")
    headers = Headers()
    data = {"test_key": "test_value", "timestamp": "2024-12-11T13:42:47+01:00"}
    
    response = await WebService.post(url, headers=headers.headers, json=data, log=True)
    return response


async def debug() -> None:
    """Debug function to test WebStuff functionality"""
    logger = Logger.get_logger(name="Debug")
    logger.info("Starting debug tests...")

    try:
        # Test GET request
        logger.info("Testing GET request...")
        get_result = await test_get()
        logger.info(f"GET response: {json.dumps(get_result, indent=2)}")

        # Test POST request
        logger.info("Testing POST request...")
        post_result = await test_post()
        logger.info(f"POST response: {json.dumps(post_result, indent=2)}")

    except Exception as e:
        logger.error(f"Error during debug: {str(e)}")
        raise
    
    logger.info("Debug tests completed successfully!")


if __name__ == "__main__":
    asyncio.run(debug())