import abc
from random import randint
from typing import Dict, List

from bing_image_urls import bing_image_urls
from requests_cache import CachedSession
from serpapi import GoogleSearch


class Image(abc.ABC):
    """Abstract class for image search engines."""

    def __init__(self, endpoint: str):
        self.query = endpoint
        self.time = 604800

    @property
    @abc.abstractclassmethod
    def images(cls) -> List[str]:
        """Return a list of images urls."""


class ImageBingLimited(Image):
    """Class to get images urls from Bing engine."""

    def __init__(self, endpoint: str):
        super().__init__(endpoint)
        self.cache = CachedSession(
            cache_name=".cache/BingLimited", expire_after=self.time
        )

    @property
    def images(self) -> List[str]:
        """Return a list of images urls"""
        links: List[str] = bing_image_urls(
            query=f"El Salvador {self.query}",
            page_counter=randint(0, 10),
            limit=30,
        )
        return links


class ImageBing(Image):
    """Class to get images urls from OFICIAL Bing engine"""

    def __init__(self, endpoint: str, key: str, endpoint_key: str):
        super().__init__(endpoint)
        self.cache = CachedSession(cache_name=".cache/Bing", expire_after=self.time)
        self.__KEY: str = key
        self.__ENDPOINT: str = endpoint_key
        self.__HEADERS: str = {"Ocp-Apim-Subscription-Key": self.__KEY}

    @property
    def images(self) -> List[str]:
        """Return a list of images urls"""
        params = {
            "q": f"El Salvador {self.query}",
            "count": 100,
            "safeSearch": "Moderate",
        }

        response: object = self.cache.get(
            self.__ENDPOINT, headers=self.__HEADERS, params=params
        )
        images: List[Dict[str]] = response.json()["value"]
        links: List[Dict[str]] = [image["contentUrl"] for image in images]
        return links


class ImageGoogle(Image):
    """Class to get images urls from Google engine."""

    def __init__(self, endpoint: str, key: str):
        super().__init__(endpoint)
        self.__KEY: str = key
        self.cache = CachedSession(cache_name=".cache/Google", expire_after=self.time)

    @property
    def images(self) -> List[str]:
        """Return a list of images urls"""
        params = {
            "q": f"El Salvador {self.query}",
            "gl": "us",
            "hl": "en",
            "tbm": "isch",
            "ijn": "0",
            "api_key": self.__KEY,
        }

        response: object = GoogleSearch(params)
        links: List[str] = response.get_dict()["images_results"]
        return links
