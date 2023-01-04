import abc

from bing_image_urls import bing_image_urls
from serpapi import GoogleSearch


class Image(abc.ABC):
    def __init__(self, endpoint: str):
        self.departament = self.__switcher(endpoint)

    @staticmethod
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
    def images(self):
        """Return a list of images urls."""


class ImageBing(Image):
    def __init__(self, endpoint: str):
        super().__init__(endpoint)

    @property
    def images(self):
        """Return a list of images urls from Bing engine."""
        return bing_image_urls(f"El Salvador departamento {self.departament}", limit=30)


class ImageGoogle(Image):
    def __init__(self, endpoint: str, key: str):
        super().__init__(endpoint)
        self.__key: str = key

    @property
    def images(self):
        """Return a list of images urls from Google engine."""
        params = {
            "q": f"El Salvador departamento {self.departament}",
            "gl": "us",
            "hl": "en",
            "tbm": "isch",
            "ijn": "0",
            "api_key": self.__key,
        }

        search = GoogleSearch(params)
        results = search.get_dict()["images_results"]
        return results
