import requests
from requests import Response
from requests.exceptions import RequestException
from requests import Session

class ScannerAPI:
    __slots__ = ("base_url", "endpoint", "headers", "_session")
    def __init__(self, base_url: str, endpoint: str, headers: dict[str, str] | None = None):
        self.base_url: str = base_url
        self.endpoint: str = endpoint
        self.headers: dict[str, str] | None = headers
        
        self._session: Session = Session()
        self._session.headers.update(headers or {})
    
    def __repr__(self) -> str:
        data: dict[str, str | None] = {
            "base_url": self.base_url,
            "endpoint": self.endpoint,
            "headers": self.headers # pyright: ignore[reportAssignmentType]
        }
        return f"ScannerAPI({data!r})"
    
    def __request(self, method: str, body: dict | None = None, params: dict | None = None) -> Response | None:
        try:
            response = self._session.request(
                method,
                f"{self.base_url}{self.endpoint}",
                json=body,
                params=params,
                timeout=5
            )
            return response
        except RequestException:
            return None

    def get(self, params: dict | None = None) -> dict | None:
        response = self.__request("GET", params=params)
        if response and response.status_code == 200:
            return response.json()
        return None

    def post(self, body: dict) -> dict | None:
        response = self.__request("POST", body=body)
        if response and response.status_code == 201:
            return response.json()
        return None
    
    def put(self, body: dict) -> dict | None:
        response = self.__request("PUT", body=body)
        if response and response.status_code == 200:
            return response.json()
        return None
    
    def delete(self) -> bool: # pyright: ignore[reportReturnType]
        response = self.__request("DELETE")
        if response is not None and response.status_code == 200:
            return True
        return False

    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        self._session.close()