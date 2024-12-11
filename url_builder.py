from typing import *
from pydantic import BaseModel


class URLBuilder(BaseModel):
    """
    A utility class for constructing URLs by appending endpoints to a base URL.

    Attributes:
        base_url (str): The base URL used as the starting point for building other URLs.
        temp_base_url (Optional[str]): A temporary URL used for building URLs with query parameters.
        temp_urls (Optional[List[str]]): A list of temporary URLs used for building URLs with query parameters.
    """

    class Config:
        arbitrary_types_allowed: bool = True

    base_url: str
    temp_base_url: Optional[str] = None

    temp_urls: Optional[List[str]] = []

    def add_query_params(
        self,
        url: str,
        **kwargs,
    ) -> str:
        """
        Adds query parameters to a given URL.

        Args:
            url (str): The URL to which query parameters will be added.
            **kwargs: Arbitrary keyword arguments to be included as query parameters.

        Returns:
            str: The URL with added query parameters.
        """
        query_params: str = "&".join(f"{key}={value}" for key, value, in kwargs.items())

        if query_params:
            return f"{url}?{query_params}"
        return url

    def build_url(
        self,
        endpoint: str,
        **kwargs,
    ) -> str:
        """
        Constructs a generic API URL by appending the given endpoint to the base URL.

        This method creates a temporary URL by appending the endpoint to the base URL,
        and then adds query parameters if provided. It also appends the constructed URL
        to a list of temporary URLs.

        Args:
            endpoint (str): The endpoint to append.
            **kwargs: Optional query parameters.

        Returns:
            str: The constructed URL.
        """
        self._temp_base_url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"

        if not self.temp_urls:
            self.temp_urls = [self._temp_base_url]

        self.temp_urls.append(self._temp_base_url)

        return self.add_query_params(
            url=self._temp_base_url,
            **kwargs,
        )
