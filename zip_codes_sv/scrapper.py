from enum import Enum

import requests
from bs4 import BeautifulSoup


class Departament(Enum):
    ahuchapan = "ah"
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
    
class Scrapper:
    __url:str
    soup:object

    def __init__(self,departament:Departament):


    def url_definition(self,dep:str) -> str:

        self.__url = self.__url.format(dep)

    def souping(self) -> object:
        """
        Returns a soup object after pass through try-catch to valididate url source is up
        """
        try:
            request_object = requests.get(self.__url)
        except requests.exceptions.ConnectionError as e:
            print(f"It's wouldn't continue 'cause url is wrong")
        else:
            soup_object = BeautifulSoup(request_object.text,"html.parser")
            self.soup = soup_object

    def zip_codes() -> dict[str]:
        pass

    def summary() -> str:
        pass

