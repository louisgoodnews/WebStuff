"""
Author: lodego
Date: 2024-03-13
"""

import aiohttp
import asyncio

from typing import *

from utils.logger import Logger

__all__: List[str] = ["web_service"]


class WebService:
    """
    A class that provides methods for sending HTTP requests.

    Attributes:
        logger: Logger
            The logger instance for the WebService class.
    """
    logger: Logger = Logger.get_logger(name="WebService")

    @classmethod
    def delete(
        cls,
        url: str,
        log: bool = False,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Sends a DELETE request to the specified URL and returns the response as a JSON.

        :param url: The URL to send the DELETE request to.
        :type url: str

        :param log: A flag indicating whether to log the response status (Defaults to False).
        :type log: bool

        :param kwargs: Additional keyword arguments for the DELETE request.
        :type kwargs: dict

        :return: The JSON response from the URL, or None if an error occurs.
        :rtype: Optional[Dict[str, Any]]
        """
        try:

            async def __delete__(
                url: str,
                log: bool = False,
                **kwargs,
            ) -> Optional[Dict[str, Any]]:
                """
                Sends a DELETE request to the specified URL and returns the response as a JSON.

                :param url: The URL to send the DELETE request to.
                :type url: str

                :param log: A flag indicating whether to log the response status (Defaults to False).
                :type log: bool

                :param kwargs: Additional keyword arguments for the DELETE request.
                :type kwargs: dict

                :return: The JSON response from the URL, or None if an error occurs.
                :rtype: Optional[Dict[str, Any]]
                """
                async with aiohttp.ClientSession() as session:
                    async with session.delete(
                        url=url,
                        **kwargs,
                    ) as response:
                        if log:
                            # Log the response status
                            cls.logger.info(
                                message=f"Received response from {url}: {response.status}"
                            )

                        # Return the JSON response
                        return await response.json()

            # Run the asynchronous __delete__ function
            return asyncio.run(
                __delete__(
                    log=log,
                    url=url,
                    **kwargs,
                )
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            cls.logger.error(message=f"Caught an exception while attempting to send 'DELETE' request to URL: '{url}': {e}")

            # Re-raise the exception to the caller
            raise e

    @classmethod
    def get(
        cls,
        url: str,
        log: bool = False,
        **kwargs,
    ) -> Optional[Union[Dict[str, Any], str, bytes]]:
        """
        Sends a GET request to the specified URL and returns the response as a JSON.

        :param url: The URL to send the GET request to.
        :type url: str

        :param log: A flag indicating whether to log the response status (Defaults to False).
        :type log: bool

        :param kwargs: Additional keyword arguments for the GET request.
        :type kwargs: dict

        :return: The response from the URL, or None if an error occurs.
        :rtype: Optional[Union[Dict[str, Any], str, bytes]]
        """
        try:

            async def __get__(
                url: str,
                log: bool = False,
                **kwargs,
            ) -> Optional[Union[Dict[str, Any], str, bytes]]:
                """
                Asynchronously sends a GET request and returns the response JSON.

                :param url: The URL to send the GET request to.
                :type url: str

                :param log: A flag indicating whether to log the response status.
                :type log: bool

                :param kwargs: Additional keyword arguments for the GET request.
                :type kwargs: dict

                :return: The response from the URL, or None if an error occurs.
                :rtype: Optional[Union[Dict[str, Any], str, bytes]]
                """
                async with aiohttp.ClientSession() as session:
                    async with session.get(
                        url=url,
                        **kwargs,
                    ) as response:
                        if log:
                            cls.logger.info(
                                message=f"Received response from {url}: {response.status}"
                            )
                        
                        content_type: str = response.headers.get("Content-Type", "")

                        if content_type.startswith("application/json"):
                            
                            # Return the JSON response
                            return await response.json()
                        elif content_type.startswith("text/"):

                            # Return the text response
                            return await response.text()
                        else:

                            # Return the binary response
                            return await response.read()


            # Run the asynchronous __get__ function
            return asyncio.run(
                __get__(
                    log=log,
                    url=url,
                    **kwargs,
                )
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            cls.logger.error(message=f"Caught an exception while attempting to send 'GET' request to URL: '{url}': {e}")

            # Re-raise the exception to the caller
            raise e

    @classmethod
    def post(
        cls,
        url: str,
        log: bool = False,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Sends a POST request to the specified URL and returns the response as a JSON.

        :param url: The URL to send the POST request to.
        :type url: str

        :param log: A flag indicating whether to log the response status (Defaults to False).
        :type log: bool

        :param kwargs: Additional keyword arguments for the POST request.
        :type kwargs: dict

        :return: The JSON response from the URL, or None if an error occurs.
        :rtype: Optional[Dict[str, Any]]
        """
        try:

            async def __post__(
                url: str,
                log: bool = False,
                **kwargs,
            ) -> Optional[Dict[str, Any]]:
                """
                Asynchronously sends a POST request to the specified URL and returns the response as a JSON.

                :param url: The URL to send the POST request to.
                :type url: str

                :param log: A flag indicating whether to log the response status (Defaults to False).
                :type log: bool

                :param kwargs: Additional keyword arguments for the POST request.
                :type kwargs: dict

                :return: The JSON response from the URL, or None if an error occurs.
                :rtype: Optional[Dict[str, Any]]
                """
                async with aiohttp.ClientSession() as session:
                    async with session.post(
                        url=url,
                        **kwargs,
                    ) as response:
                        if log:
                            cls.logger.info(
                                message=f"Received response from {url}: {response.status}"
                            )
                        # Return the JSON response
                        return await response.json()

            # Run the asynchronous __post__ function
            return asyncio.run(
                __post__(
                    log=log,
                    url=url,
                    **kwargs,
                )
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            cls.logger.error(message=f"Caught an exception while attempting to send 'POST' request to URL: '{url}': {e}")

            # Re-raise the exception to the caller
            raise e

    @classmethod
    def put(
        cls,
        url: str,
        log: bool = False,
        **kwargs,
    ) -> Optional[Dict[str, Any]]:
        """
        Sends a PUT request to the specified URL and returns the response as a JSON.

        :param url: The URL to send the PUT request to.
        :type url: str

        :param log: A flag indicating whether to log the response status (Defaults to False).
        :type log: bool

        :param kwargs: Additional keyword arguments for the PUT request.
        :type kwargs: dict

        :return: The JSON response from the URL, or None if an error occurs.
        :rtype: Optional[Dict[str, Any]]
        """
        try:

            async def __put__(
                url: str,
                log: bool = False,
                **kwargs,
            ) -> Optional[Dict[str, Any]]:
                """
                Asynchronously sends a PUT request to the specified URL and returns the response as a JSON.

                :param url: The URL to send the PUT request to.
                :type url: str

                :param log: A flag indicating whether to log the response status (Defaults to False).
                :type log: bool

                :param kwargs: Additional keyword arguments for the PUT request.
                :type kwargs: dict

                :return: The JSON response from the URL, or None if an error occurs.
                :rtype: Optional[Dict[str, Any]]
                """
                async with aiohttp.ClientSession() as session:
                    async with session.put(
                        url=url,
                        **kwargs,
                    ) as response:
                        if log:
                            cls.logger.info(
                                message=f"Received response from {url}: {response.status}"
                            )

                        # Return the JSON response
                        return await response.json()

            # Run the asynchronous __put__ function
            return asyncio.run(
                __put__(
                    log=log,
                    url=url,
                    **kwargs,
                )
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            cls.logger.error(message=f"Caught an exception while attempting to send 'PUT' request to URL: '{url}': {e}")

            # Re-raise the exception to the caller
            raise e
