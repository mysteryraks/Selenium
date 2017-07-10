import logging
import inspect

def customLogger(logLevel):

    #Gets the name of the class/method from where this method is called.
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    #By default log everything
    logger.setLevel(logging.DEBUG)

    #Define file handler
    fileHandler = logging.FileHandler("{0}.log".format(loggerName), mode='a')
    fileHandler.setLevel(logLevel)

    #Defining the format
    formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s: %(message)s ',
                                  datefmt='%m%d%Y %H%M%S')

    #set the formatter and then finally set the logger
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger

