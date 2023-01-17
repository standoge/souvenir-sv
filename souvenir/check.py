import httpx
import re

from random import randint
from souvenir.zipcode import Endpoint


# municipalitites/municipio?departament=dep
def main():

    URL = "https://www.bing.com/images/async"

    DEP = Endpoint.chalatenango.value
    AH = "Chalatenango San Isidro"
    parameters = {
        "q": AH,
        "first": randint(2, 9),
        "count": randint(20, 40),
        "adlt": False,
        "qft": "",
    }

    response = httpx.get(URL, params=parameters)
    links = re.findall(r"murl&quot;:&quot;(.*?)&quot;", response.text)

    print(links)


if __name__ == "__main__":
    main()
