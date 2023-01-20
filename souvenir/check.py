import httpx
import re

from random import randint


def parameters(query: str):
    json_args = {
        "q": query,
        "first": randint(2, 9),
        "count": randint(2, 40),
        "adlt": False,
        "qft": "",
    }

    return json_args


def main():

    URL = "https://www.bing.com/images/async"

    response = httpx.get(URL, params=parameters("Usulutan"))
    links = re.findall(r"murl&quot;:&quot;(.*?)&quot;", response.text)

    print(links)


if __name__ == "__main__":
    main()
