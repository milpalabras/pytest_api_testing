import os
import pytest
import selenium.webdriver
from src.helpers.logging_helper import logHelper
from src.helpers.email_helper import EmailHelper
from src.helpers.bdd_handler import DBHandler
from config import (
    ORACLE_SERVER,
    ORACLE_PORT,
    ORACLE_USER,
    ORACLE_PASSWORD,
    ORACLE_DATABASE,
    SERVICE_NAME,
    SQL_SERVER,
    SQL_PORT,
    SQL_USER,
    SQL_PASSWORD,
    SQL_DATABASE,
    LOGIN,
    PASSWORD,
)


@pytest.fixture(scope="session")
def Customer_api_cliente():
    """
    Fixture para el cliente de la API de Customer
    """
    logger = logHelper().get_logger(__name__)
    logger.info(f"\n{'-'*40}SETUP DEL CLIENTE{'-'*80}\n")
    yield 
    logger.info(f"\n{'-'*40}TEARDOWN DEL CLIENTE{'-'*80}\n")
    

@pytest.fixture(scope="module", autouse=True)
def test_log_limits():
    logger = logHelper().get_logger(__name__)
    pytest_name = os.path.basename(
        os.environ.get("PYTEST_CURRENT_TEST").split("::")[0].strip(".py")
    )
    logger.info(f"\n{'-'*40}INICIO DE TEST SUITE- {pytest_name}{'-'*80}\n")

    yield
    logger.info(f"\n{'-'*40}FIN DE TEST SUITE- {pytest_name}{'-'*80}\n")


test = None
status_tag = None
line = None
duration = None
exception = None
result = None


@pytest.fixture(scope="function", autouse=True)
def test_log(request, pytestconfig):
    logger = logHelper().get_logger(__name__)
    logger.info("Inicio Test '{}'".format(request.node.name))    
    def fin():
        logger.info("Fin Test '{}' \n".format(request.node.name))

    request.addfinalizer(fin)
    yield
    global test, status_tag, line, duration, exception, duration_raw, result

    logger.info(f"NOMBRE DEL TEST: {test}")
    logger.info(f"STATUS_TAG: {status_tag}")
    logger.info(f"LINE: {line}")
    logger.info(f"DURATION: {duration}")
    logger.info(f"EXCEPTION: {exception}")
    logger.info(f"RESULT: {result}")
    test = None
    status_tag = None
    line = None
    duration = None
    exception = None
    duration_raw = None
    result = None


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    global test, status_tag, line, duration, exception, duration_raw, result
    report = yield
    result = report.get_result()

    if result.when == "call":
        (filename, line, name) = item.location
        test = item.nodeid
        status_tag = result.outcome
        line = line
        duration_raw = call.duration
        duration = round(duration_raw, 2)
        exception = call.excinfo


@pytest.fixture
def chromebrowser():
    options = selenium.webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")
    driver = selenium.webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def firefoxbrowser():
    driver = selenium.webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def db_handler_oracle():
    logger = logHelper().get_logger(__name__)
    logger.info(f"\n{'-'*40}SETUP CONEXIÓN DE LA BASE DE DATOS{'-'*80}\n")
    MAX_RETRIES = 5
    db_handler = DBHandler(
        "oracle",
        ORACLE_SERVER,
        ORACLE_PORT,
        ORACLE_USER,
        ORACLE_PASSWORD,
        ORACLE_DATABASE,
        SERVICE_NAME,
    )
    for _ in range(MAX_RETRIES):
        try:
            db_handler.connect()
            break
        except Exception as e:
            logger = logHelper().get_logger(__name__)
            logger.error(f"Error al conectar a la base de datos: {e}, reintento nro {_+1} de {MAX_RETRIES}")
            continue

    yield db_handler
    logger.info(f"\n{'-'*40}TEARDOWN DE LA BASE DE DATOS{'-'*80}\n")
    db_handler.close()

@pytest.fixture(scope="session")
def db_handler_mssql():
    db_handler = DBHandler(
        "mssql", SQL_SERVER, SQL_PORT, SQL_USER, SQL_PASSWORD, SQL_DATABASE
    )
    db_handler.connect()
    yield db_handler
    db_handler.close()


@pytest.fixture(scope="session")
def email_helper():
    email_helper = EmailHelper()
    yield email_helper
    #email_helper.delete_email_from_sender("sender@mail.com")
