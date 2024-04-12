import inspect
import logging

class LogGenerator():
    @staticmethod
    def logger():
        name=inspect.stack()[1][3]
        logger=logging.getLogger(name)
        log_file=logging.FileHandler("C:\\Users\\lenovo\\PycharmProjects\\OrangeHRM_project\\logs\\hrm.log")
        log_format=logging.Formatter("%(asctime)s:%(name)s: %(levelname)s:%(lineno)s:%(funcName)s:%(message)s")
        log_file.setFormatter(log_format)
        logger.addHandler(log_file)
        logger.setLevel(logging.INFO)
        return logger

