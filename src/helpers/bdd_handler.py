from sqlalchemy import create_engine
from sqlalchemy import text
from src.helpers.logging_helper import logHelper


class DBHandler:
    """
    A class to handle database connections and queries.

    Attributes:
    -----------
    db_type : str
        The type of database to connect to. Can be "oracle" or "mssql".
    host : str
        The hostname or IP address of the database server.
    port : str
        The port number to use for the database connection.
    user : str
        The username to use for the database connection.
    password : str
        The password to use for the database connection.
    database : str
        The name of the database to connect to (only used for MSSQL).
    engine : sqlalchemy.engine.Engine
        The SQLAlchemy engine object used for the database connection.
    connection : sqlalchemy.engine.Connection
        The SQLAlchemy connection object used for the database connection.
    """

    def __init__(
        self, db_type, host, port, user, password, database, service_name=None
    ):
        self.db_type = db_type
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.engine = None
        self.connection = None
        self.service_name = None
        if db_type == "oracle":
            self.service_name = service_name
        self.logger = logHelper().get_logger(__name__)


    def connect(self):
        """
        Connects to the database using the provided credentials.
        """
        if self.db_type == "oracle":
            try:
                self.logger.info(
                    f"Conectando a la base de datos {self.host} con los parámetros: {self.user}, {self.password}, {self.host}, {self.port}, {self.service_name}"
                )
                self.engine = create_engine(
                    f"oracle+oracledb://{self.user}:{self.password}@{self.host}:{self.port}/?service_name={self.service_name}"
                )
            except Exception as e:
                self.logger.error(f"Error al conectar a la base de datos: {e}")
                self.logger.info(
                    f"Reintentando conectar a la base de datos {self.host}"
                )
                self.engine = create_engine(
                    f"oracle+oracledb://{self.user}:{self.password}@{self.host}:{self.port}/?service_name={self.service_name}",
                    pool_timeout=60,
                    pool_recycle=600,
                )

        elif self.db_type == "mssql":
            try:
                self.logger.info(f"Conectando a la base de datos {self.host}...")
                self.engine = create_engine(
                    f"mssql+pymssql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
                )
            except Exception as e:
                self.logger.error(f"Error al conectar a la base de datos: {e}")
                self.logger.info(
                    f"Reintentando conectar a la base de datos {self.host}..."
                )
                self.engine = create_engine(
                    f"mssql+pymssql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
                )
        self.connection = self.engine.connect()

    def execute_query_and_return_values(self, query):
        """
        Executes the provided SQL query and returns the results.

        Parameters:
        -----------
        query : str
            The SQL query to execute.

        Returns:
        --------
        list of tuples
            The results of the query as a list of tuples.
        """
        try:
            self.logger.info(f"Ejecutando query: {query}")
            result = self.connection.execute(text(query))
            result_as_dict = result.mappings().all()
            return result_as_dict
        except Exception as e:
            self.logger.error(f"Error al ejecutar query: {e}")

    def execute_statement_and_commit(self, query):
        """
        Executes the provided SQL query

        Parameters:
        -----------
        query : str
            The SQL query to execute.

        """
        try:
            self.logger.info(f"Ejecutando query: {query}")
            self.connection.execute(text(query))
            #check if query has commit string
            if "COMMIT" in query:
                self.logger.info("Query contains commit statement")
            else:
                self.logger.info("Query does not contain commit statement")
                self.logger.info("committing transaction...")
                self.connection.commit()
        except Exception as e:
            self.logger.error(f"Error al ejecutar query: {e}")

    def commit(self):
        """
        Commits the current transaction to the database.
        """
        self.logger.info("Committing transaction...")
        try:
            self.connection.commit()
        except Exception as e:
            self.logger.error(f"Error al hacer commit: {e}")

    def close(self):
        """
        Closes the database connection.
        """
        self.logger.info("Cerrando conexión a la base de datos...")
        self.connection.close()
