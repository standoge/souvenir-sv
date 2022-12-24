from typing import Dict
from enum import Enum

import requests
from bs4 import BeautifulSoup


class Endpoint(Enum):
    ahuachapan = "ah"
    sonsonate = "so"
    santa_ana = "sa"
    cabanas = "ca"
    chalatenango = "ch"
    cuscatlan = "cu"
    la_libertad = "li"
    la_paz = "pa"
    san_salvador = "ss"
    san_vicente = "sv"
    morazan = "mo"
    san_miguel = "sm"
    usulutan = "us"
    la_union = "un"


class Department:
    __url: str = "https://www.listasal.info/municipios/{}.shtml"
    __soup: object
    sumamry: str
    zip_codes: Dict[str, str]

    def __init__(self, departament: Endpoint) -> None:
        self.url_definition(departament)
        self.souping()

    def url_definition(self, dep: str) -> None:
        """Concat base ulr with departament endpoint"""
        self.__url = self.__url.format(dep)

    def souping(self) -> None:
        """
        Return a soup object after pass through try-catch to valididate
        if url source is up
        """
        try:
            request_object = requests.get(self.__url)
        except requests.exceptions.ConnectionError as e:
            print(f"It's wouldn't continue 'cause url is wrong {e}")
        else:
            soup_object = BeautifulSoup(request_object.text, "html.parser")
            self.__soup = soup_object

    @property
    def summary(self) -> str:
        """Return a summary of municipalities and extra info about them"""
        summary = self.__soup.find("div", attrs={"class": "articulo"})
        return summary.p.text

    @property
    def zip_codes(self) -> Dict[str, str]:
        """Return a dict with all zip codes and their respective municipalities"""
        municipalities = {}

        tuples = self.__soup.find("table", attrs={"class": "datatable"}).find_all("tr")

        municipalities_count = len(tuples)
        for i in range(1, municipalities_count):

            munname = tuples[i].find("td").text
            municipalities[munname] = tuples[i].find_all("td")[3].text

        municipalities["Summary"] = self.summary
        return municipalities
