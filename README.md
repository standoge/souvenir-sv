
# Zip codes El Salvador
This Python package scrapes [this web](https://www.listasal.info/articulos/codigo-postal-el-salvador.shtml) to get zip codes by municipality. It uses Requests with BeautifulSoup to extract that information, which is returned as a dict or JSON.

## Install 🛠️

This package is in **PIP**, so you can install it as a dependency:

```python
pip install zipcode-sv
```
## How to use 🪐

```python
from zipcode.department import Department, Endpoint
```

You have to import `Department`, which is the main class for scraping the zip codes. `Endpoint` is an Enum with El Salvador's departments to select from which one you want to get their municipalities with their zip codes.

```python
# returns endpoint to extract data in web source
my_department = Endpoint.san_salvador.value 
# scrapes web source to get municipalities with its zip codes     
san_salvador_zipcodes = Department(my_department)
# returs a dict with municipalities and its zip codes
san_salvador_zipcodes.zip_codes                  
```

You must expect a dictionary like this.

```python
{ "Aguilares":"01122",
	"Apopa":"01123",
	"Ayutuxtepeque":"01121",
	"Delgado":"01118",
	"Cuscatancingo":"01119",
	"El Paisnal":"01124",
	"Guazapa":"01125",
	"Ilopango":"01117",
	"Mejicanos":"01120",
	"Nejapa":"01126",
	"Panchimalco":"01127",
	"Rosario de Mora":"01128",
	"San Marcos":"01115",
	"San Martín":"01129",
	"San Salvador":"01101",
	"Santiago Texacuangos":"01130",
	"Santo Tomás":"01131",
	"Soyapango":"01116",
	"Tonacatepeque":"01132",
	" ":" ",
	"Summary":"San Salvador es un departamento fundado en 1525 ubicado en la Zona Central de El Salvador. Posee 3 distritos y 19 municipios."
}
```
