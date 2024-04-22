import logging
import time
import os

TRACE = 15

logging.addLevelName(TRACE, "TRACE")


class logHelper:
    def __init__(self):
        pass

    def get_logger(self, filename, mode="a"):
        logger = logging.getLogger(filename)
        if not logger.handlers:
            handlerName = os.path.basename(
                os.environ.get("PYTEST_CURRENT_TEST").split("::")[0].strip(".py")
            )
            worker_id = os.environ.get("PYTEST_XDIST_WORKER") or "main"
            handler = logging.FileHandler(
                f"{handlerName}-{worker_id}_{time.strftime('%d_%m_%Y')}.log"
            )
            handler.setLevel(logging.DEBUG)
            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.DEBUG)
            self.logger = logger
        return logger
