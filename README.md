# Prácticas Tipología y ciclo de vida de los datos
En este repositoriose encuentran las diferentes entregas de prácticas de la Asignatura Tipología y ciclo de vida de los datos del Master universitario de Ciencia de Datos de la Universitat Oberta de Catalunya

Nombres de los integrantes del grupo:
  - Miguel Ciriano Martín
  - Pedro Antonio Pérez Pérez

Descriptivo de los archivos:
  - Scraper_ayudas_general.py: Archivo que contiene el código Python necesario para extraer la información sobre ayudas generales para empresas publicadas por el Estado o las diferentes autonomías
  - Convocatorias.csv: El archivo resultante de la ejecución de Scraper_ayudas_general.py con la información de las ayudas
  - scraper.ipynb: Archivo que contiene el código Python necesario para extraer todas las instancias de ayudas entregadas en un rango de tiempo.
  - Ayudas_entregadas.csv: Archivo resultante de la ejecución de scraper.ipynb con todas las instancias de ayudas entregadas a empresas

Cómo usar los archivos de código del repositorio:
  - Scraper_ayudas_general: Contiene un campo parametrizable, "num_paginas". Como la información se ofrece paginada en el sitio web, podemos ajustar la cantidad de páginas que avanzaremos para extraer información. Cada página contiene 10 elementos por lo que extraeremos 10 * num_paginas como cantidad de resultados final. En este caso hemos decidido utilizar la información más reciente para mantener la representatividad futura también y nos hemos decidido por num_paginas = 50.

  - scraper.ipynb: Contiene dos campos parametrizables principales, "start_page" y "end_page". Con estos dos campos seleccionaremos la página inicial y la final sobre las que iterar en nuestra búsqueda de información.

DOI: 10.5281/zenodo.14060197
