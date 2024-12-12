import base64

from pydantic import BaseModel
from typing import *


class Headers(BaseModel):
    """
    A utility class for constructing HTTP headers.

    Attributes:
        headers (Dict[str, str]): A dictionary containing the headers. Defaults to an empty dictionary.
    """

    class Config:
        arbitrary_types_allowed = True

    headers: Optional[Dict[str, str]] = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    def authorization(
        self,
        bearer: str | None = None,
        password: str | None = None,
        username: str | None = None,
    ) -> None:
        """

        Add Authorization header to the headers dictionary.

        bearer (str): The bearer token to use for authorization.
        password (str): The password to use for authorization.
        username (str): The username to use for authorization.

        If both password and username are provided, the Authorization header is set to
        Basic <base64 encoded username:password>.

        If a bearer token is provided, the Authorization header is set to Bearer <bearer>.

        If neither password nor username are provided, an error is raised.

        If all three are provided, an error is raised.

        Returns:
            None
        """
        if all((bearer, password, username)):
            raise ValueError("Username and password cannot be provided with bearer.")
        elif not any(((bearer, password), username)):
            raise ValueError("Username and password or bearer must be provided.")

        if not self.headers:
            self.headers = {}

        if bearer:
            self.headers["Authorization"] = f"Bearer {bearer}"
        elif username and password:
            self.headers["Authorization"] = (
                f"Basic {base64.b64encode(f'{username}:{password}'.encode()).decode()}"
            )

    def to_dict(self) -> Dict[str, str]:
        """
        Returns a dictionary containing the headers.

        Returns:
            Dict[str, str]: A dictionary containing the headers.
        """
        if not self.headers:
            self.headers = {}

        return self.headers

    def update(
        self,
        **kwargs,
    ) -> None:
        """
        Update the headers dictionary with the given key-value pairs.

        Args:
            **kwargs: Key-value pairs to add to the headers dictionary.

        Returns:
            None
        """
        if not self.headers:
            self.headers = {}
        self.headers.update(kwargs)
