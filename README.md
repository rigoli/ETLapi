# ETLapi
# Scraper de Noticias de Cointelegraph

Este proyecto incluye una clase `Scraper` en Python que utiliza Selenium para recopilar noticias de [Cointelegraph](https://cointelegraph.com/). Puedes utilizar esta clase para recopilar las últimas noticias basadas en una etiqueta específica, así como para obtener el contenido completo de una noticia específica.

## Instalación

Antes de poder usar este proyecto, debes asegurarte de tener Python y Selenium instalados en tu entorno de desarrollo. Puedes instalar Selenium con pip utilizando el siguiente comando:

```
pip install selenium
```

Además, debes tener el [ChromeDriver](https://sites.google.com/chromium.org/driver/) instalado y en tu PATH.

## Uso

Para utilizar la clase `Scraper`, debes importarla en tu archivo de Python. Aquí hay un ejemplo de cómo hacerlo:

```python
from scraper import Scraper
```

Luego, puedes crear una nueva instancia de Scraper, proporcionando la etiqueta para la cual deseas recopilar noticias:

```python
my_scraper = Scraper('bitcoin')
```

Con tu instancia de `Scraper`, puedes recopilar noticias y obtener el contenido de las noticias. Aquí hay un ejemplo de cómo hacerlo:

```python
# Recopilar noticias
news = my_scraper.get_news(10)
print(news)

# Obtener el contenido de una noticia
content = my_scraper.get_news_single(news[0]['urlId'])
print(content)
```

En este ejemplo, recopilamos 10 noticias para la etiqueta 'bitcoin' y luego obtenemos y mostramos el contenido de la primera noticia.


## Métodos

La clase `Scraper` tiene dos métodos principales que puedes utilizar:

- `get_news(num_news)`: Recopila `num_news` noticias para la etiqueta proporcionada cuando se creó la instancia de `Scraper`. Las noticias se devuelven como una lista de diccionarios, con cada diccionario que contiene información sobre una noticia (incluyendo su `urlId` que puede usarse para obtener su contenido).

- `get_news_single(urlId)`: Obtiene y devuelve el contenido completo de la noticia con el `urlId` proporcionado.


## Contribuir

Si encuentras algún problema con este proyecto o tienes alguna sugerencia de mejora, no dudes en abrir un Issue o un Pull Request.


## Licencia

Este proyecto está bajo la licencia MIT.
