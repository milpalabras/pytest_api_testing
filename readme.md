# API Testing Con Python, Requests and Pytest

Este proyecto es un ejemplo de como realizar pruebas de API con Python, Requests y Pytest.

### Pre-requisitos 📋
debes tener instalado lo siguiente:
 * python 3.11 - 👉 [Python](https://www.python.org/) - Sitio Oficial
 * invoke - 👉 [Invoke](http://www.pyinvoke.org/) - Sitio Oficial
 * java V8 o superior- 👉 [Java](https://www.java.com/es/download/) - Sitio Oficial

### Dependencias 📋

 * Selenium - 👉 [Selenium](https://www.selenium.dev/) - Sitio Oficial
 * requests - 👉 [Requests Library](https://requests.readthedocs.io/en/latest/)
 * pytest - [Pytest Library](https://docs.pytest.org/en/latest/)
 * assertpy - [Assertpy Library](https://github.com/assertpy/assertpy)
 * cerberus - [Cerberus Library](https://docs.python-cerberus.org/)
 * poetry - [Poetry Library](https://python-poetry.org/docs/)




## Instalación 🔧

1. Instalar Python 3.11.0 desde [Python](https://www.python.org/downloads/)

2. Instalar Invoke:

    ```bash
    pip install invoke
    ```

3. Clonar el repositorio e ingresar a la carpeta del proyecto:

    ```bash
    git clone https://github.com/milpalabras/pytest_api_testing.git
    cd pytest_api_testing
    ```
4. iniciar la tarea setup:

    ```bash
    invoke setup
    ```
4. Crear un archivo `.env` en la raíz del proyecto con las siguientes variables:

    ```env
    BASE_URI =     
    LOGIN = 
    LOGIN_EMAIL = 
    LOGIN_DNI = 
    PASSWORD = 
    LOGIN2 = 
    LOGIN_EMAIL2 = 
    LOGIN_DNI2 = 
    PASSWORD2 = 

    #bbd stuff
    SQL_SERVER =
    SQL_USER = 
    SQL_PASSWORD = 
    SQL_DATABASE = 
    SQL_PORT = 

    ORACLE_SERVER = 
    ORACLE_USER = 
    ORACLE_PASSWORD = 
    ORACLE_DATABASE = 
    ORACLE_PORT = 
    SERVICE_NAME = 

    #gmail stuff
    GMAIL_USER = 
    GMAIL_PASSWORD = 
    IMAP_SERVER = 

    ```

5. Ejecutar los casos de prueba:

    ```bash
    poetry run pytest
    ```

6. para ejecutar el reporte de allure:

    ```bash
    invoke generate-report
    ```



️
