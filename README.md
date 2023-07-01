# API DSG24 RGL
# Scraper de Noticias de Cointelegraph

Este proyecto incluye una clase `Scraper` en Python que utiliza Selenium para recopilar noticias de [Cointelegraph](https://cointelegraph.com/). Puedes utilizar esta clase para recopilar las últimas noticias basadas en una etiqueta específica, así como para obtener el contenido completo de una noticia específica.

## Instalación

Antes de poder usar este proyecto, debes asegurarte de tener Python y Selenium instalados en tu entorno de desarrollo. Puedes instalar Selenium con pip utilizando el siguiente comando:

```
pip install selenium
```

Además, debes tener el [ChromeDriver](https://sites.google.com/chromium.org/driver/) instalado y en tu PATH.

## Instancia

La aplicación está creada usando Flask y se ejecuta en localhost en el puerto 8000.

## Endpoints

1. `'/'`: Devuelve un mensaje de bienvenida y una lista de los puntos finales disponibles.

   Ejemplo de uso: `http://localhost:8000/`

2. `'/news/\<keyword>/\<nNews>'`: Devuelve las últimas `nNews` noticias para la `keyword` dada. Este punto final acepta tanto solicitudes POST como GET.

   Ejemplo de uso: `http://localhost:8000/news/bitcoin/10`

3. `'/singlenews'`: Devuelve el contenido de una noticia dada por `urlId`, que se pasa como parámetro GET.

   Ejemplo de uso: `http://localhost:8000/singlenews?urlId=/news/2023-07-01/bitcoin-price-dips-below-35k`

\## Manejo de errores

Cualquier error generado al obtener noticias se maneja internamente y se devuelve un mensaje de error al cliente.

## Métodos

La clase `ScraperCointelegraph` tiene dos métodos principales que puedes utilizar:

- `get_news(num_news)`: Recopila `num_news` noticias para la etiqueta proporcionada cuando se creó la instancia de `Scraper`. Las noticias se devuelven como una lista de diccionarios, con cada diccionario que contiene información sobre una noticia (incluyendo su `urlId` que puede usarse para obtener su contenido).

- `get_news_single(urlId)`: Obtiene y devuelve el contenido completo de la noticia con el `urlId` proporcionado.


## Contribuir

Si encuentras algún problema con este proyecto o tienes alguna sugerencia de mejora, no dudes en abrir un Issue o un Pull Request.


## Licencia

Este proyecto está bajo la licencia MIT.
