[![publish](https://github.com/standoge/souvenir-sv/actions/workflows/publish.yml/badge.svg)](https://github.com/standoge/souvenir-sv/actions/workflows/publish.yml)

# El Salvador souvenir

This Python package scrapes [this web](https://www.listasal.info/articulos/codigo-postal-el-salvador.shtml) to get zip codes by municipality. It uses `Requests` with `BeautifulSoup` to extract that information, which is then returned as a dictionary or JSON.
 ## Install 🛠️

This package can be installed with **PIP** as a dependency:

```bash
pip install souvenir-sv
```

## How to use 🪐

```python
# for department/municipalities zip-codes scraper
from souvenir.zipcode import Endpoint, Zipcode
# for department images scraper
from souvenir.image import ImageBing, ImageGoogle, ImageBingLimited
```

### Zip-codes:

```python
# return endpoint to extract data in web source
my_department:str = Endpoint.san_salvador.value

# scrapes web source to get municipalities with its zip codes
san_salvador_zipcodes:object = Zipcode(my_department)

# retur a dict with municipalities and its zip codes
san_salvador_zipcodes.zip_codes
```

You must expect a dictionary like this.

```json
{
  "Aguilares": "01122",
  "Apopa": "01123",
  "Ayutuxtepeque": "01121",
  "Delgado": "01118",
  "Cuscatancingo": "01119",
  "El Paisnal": "01124",
  "Guazapa": "01125",
  "Ilopango": "01117",
  "Mejicanos": "01120",
  "Nejapa": "01126",
  "Panchimalco": "01127",
  "Rosario de Mora": "01128",
  "San Marcos": "01115",
  "San Martín": "01129",
  "San Salvador": "01101",
  "Santiago Texacuangos": "01130",
  "Santo Tomás": "01131",
  "Soyapango": "01116",
  "Tonacatepeque": "01132",
  "Summary": "San Salvador es un departamento fundado en 1525 ubicado en la Zona Central de El Salvador. Posee 3 distritos y 19 municipios."
}
```

### Images:
You can check package's documentation from author's repositories.
[ImageBingLimited](https://github.com/ffreemt/bing-image-urls) and [ImageGoogle](https://github.com/arrrlo/Google-Images-Search). [ImageBing](https://learn.microsoft.com/en-us/bing/search-apis/bing-image-search/reference/endpoints?source=recommendations) is an implementation of the official Bing Search Web API. The latter class (ImageBing) have implement cache (1 week) so you can be more efficient with your requests.

> ImageGoogle & ImageAzure scraper requires an API Key to work, which means that you have to sign in on the author's package website to get access to the scraper. ImageBing does not need it.

```python
# here ins't not needed use Endpoint Enum
my_department = "La Paz"

# return urls from Bing engine (Limited to 30 images)
bing_images:List[str] = ImageBingLimited(my_department).images

# return urls from Google engine
google_images:List[Dict[str]] = ImageGoogle(my_department,api_key).images

# return urls from official Bing engine (Limited to 100 images)
bing_images_api:List[str] = ImageBing(my_department,api_key,endpoint)
```

> `endpoint` parameter of ImageBing is necessary to specify that images are to be searched for. To search for another resource, another endpoint must be used. Check official documentation.

----
Enjoy :bamboo:
