import abc
from random import randint
from typing import List

import requests
from bing_image_urls import bing_image_urls
from serpapi import GoogleSearch


class Image(abc.ABC):
    """Abstract class for image search engines."""

    def __init__(self, endpoint: str):
        self.departament = self.__switcher(endpoint)

    def __switcher(self, endpoint: str):
        """
        Connect endpoints used for zipcode module
        with departaments names for image search.
        """
        switch = {
            "ah": "ahuchapan",
            "so": "sonsonate",
            "sa": "santa ana",
            "ca": "cabañas",
            "ch": "chalatenango",
            "cu": "cuscatlan",
            "li": "la libertad",
            "pa": "la paz",
            "ss": "san salvador",
            "sv": "san vicente",
            "mo": "morazan",
            "sm": "san miguel",
            "us": "usulutan",
            "un": "la union",
        }
        return switch.get(endpoint, "Invalid value")

    @property
    @abc.abstractclassmethod
    def images(cls) -> List[str]:
        """Return a list of images urls."""


class ImageBing(Image):
    """Class to get images urls from Bing engine."""

    def __init__(self, endpoint: str):
        super().__init__(endpoint)

    @property
    def images(self) -> List[str]:
        """Return a list of images urls"""
        links: List[str] = bing_image_urls(
            query=f"El Salvador {self.departament}",
            page_counter=randint(0, 10),
            limit=30,
        )
        return links


class ImageAzure(Image):
    """Class to get images urls from OFICIAL Bing engine"""

    def __init__(self, endpoint: str, key: str, endpoint_key: str):
        super().__init__(endpoint)
        self.__KEY: str = key
        self.__ENDPOINT: str = endpoint_key
        self.__HEADERS: str = {"Ocp-Apim-Subscription-Key": self.__KEY}

    @property
    def images(self) -> List[str]:
        """Return a list of images urls"""
        params = {
            "q": f"El Salvador {self.departament}",
            "count": 100,
            "safeSearch": "Moderate",
        }

        response: object = requests.get(
            self.__ENDPOINT, headers=self.__HEADERS, params=params
        )
        images: List[str] = response.json()["value"]
        links: List[str] = [image["contentUrl"] for image in images]
        return links


class ImageGoogle(Image):
    """Class to get images urls from Google engine."""

    def __init__(self, endpoint: str, key: str):
        super().__init__(endpoint)
        self.__KEY: str = key

    @property
    def images(self) -> List[str]:
        """Return a list of images urls"""
        params = {
            "q": f"El Salvador {self.departament}",
            "gl": "us",
            "hl": "en",
            "tbm": "isch",
            "ijn": "0",
            "api_key": self.__KEY,
        }

        response: object = GoogleSearch(params)
        links: List[str] = response.get_dict()["images_results"]
        return links
