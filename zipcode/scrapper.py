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
    __url:str = "https://www.listasal.info/municipios/{}.shtml"
    soup:object

    def __init__(self,departament:Departament):
        self.url_definition(departament)
        self.souping()


    def url_definition(self,dep:str) -> str:
        """Concat base ulr with departament endpoint"""
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

    def summary(self) -> str:
        """Returns a summary of municipalities and extra info about them"""
          

    def zip_codes(self,soup) -> dict[str]:
        """Returns a dict with all zip codes and their respective municipalities"""
        municipalities = dict()

        tuples = soup.find("table",attrs={"class":"datatable"}).find_all("tr")
        
        l = len(tuples)
        for i in range(1,l):
            
            munname = tuples[i].find("td").text
            municipalities[munname] = tuples[i].find_all("td")[3].text    
        
        municipalities['Summary'] = get_summary(soup) 
        return municipalitiespass


