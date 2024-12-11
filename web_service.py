import aiohttp

from typing import *

from logger import Logger


class WebService:
    """
    A utility class providing static methods to perform HTTP requests.

    Attributes:
        logger (Logger): An instance of the Logger class for logging messages.
    """
    logger: Logger = Logger.get_logger(name="WebService")


    @classmethod
    async def delete(cls, url: str, log: bool = False, **kwargs,) -> Dict[str, Any] | None:
        """
        Performs a DELETE request to the given URL with any additional keyword arguments.

        Args:
            url (str): The URL to which the DELETE request is sent.
            log (bool): Whether to log the request and response. Defaults to False.
            **kwargs: Additional keyword arguments to be passed to the DELETE request.

        Returns:
            Dict[str, Any] | None: The JSON response from the server, or None on failure.
        """
        try:
            async with aiohttp.ClientSession() as session:
                async with session.delete(url=url, **kwargs,) as response:
                    if log:
                        cls.logger.info(message=f"Received response from {url}: {response.status}")
                    return await response.json()
        except aiohttp.ClientError as e:
            cls.logger.error(message=f"Caught an exception while making a DELETE request to {url}: {e}")
            return None


    @classmethod
    async def get(cls, url: str, log: bool = False, **kwargs,) -> Dict[str, Any] | None:
        """
        Performs a GET request to the given URL with any additional keyword arguments.

        Args:
            url (str): The URL to which the GET request is sent.
            log (bool): Whether to log the request and response. Defaults to False.
            **kwargs: Additional keyword arguments to be passed to the GET request.

        Returns:
            Dict[str, Any] | None: The JSON response from the server, or None on failure.
        """
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url=url, **kwargs,) as response:
                    if log:
                        cls.logger.info(message=f"Received response from {url}: {response.status}")
                    return await response.json()
        except aiohttp.ClientError as e:
            cls.logger.error(message=f"Caught an exception while making a GET request to {url}: {e}")
            return None
    
    @classmethod
    async def post(cls, url: str, log: bool = False, **kwargs,) -> Dict[str, Any] | None:
        """
        Performs a POST request to the given URL with any additional keyword arguments.

        Args:
            url (str): The URL to which the POST request is sent.
            log (bool): Whether to log the request and response. Defaults to False.
            **kwargs: Additional keyword arguments to be passed to the POST request.

        Returns:
            Dict[str, Any] | None: The JSON response from the server, or None on failure.
        """
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url=url, **kwargs,) as response:
                    if log:
                        cls.logger.info(message=f"Received response from {url}: {response.status}")
                    return await response.json()
        except aiohttp.ClientError as e:
            cls.logger.error(message=f"Caught an exception while making a POST request to {url}: {e}")
            return None
    
    @classmethod
    async def put(cls, url: str, log: bool = False, **kwargs,) -> Dict[str, Any] | None:
        """
        Performs a PUT request to the given URL with any additional keyword arguments.

        Args:
            url (str): The URL to which the PUT request is sent.
            log (bool): Whether to log the request and response. Defaults to False.
            **kwargs: Additional keyword arguments to be passed to the PUT request.

        Returns:
            Dict[str, Any] | None: The JSON response from the server, or None on failure.
        """
        try:
            async with aiohttp.ClientSession() as session:
                async with session.put(url=url, **kwargs,) as response:
                    if log:
                        cls.logger.info(message=f"Received response from {url}: {response.status}")
                    return await response.json()
        except aiohttp.ClientError as e:
            cls.logger.error(message=f"Caught an exception while making a PUT request to {url}: {e}")
            return None
