import logging

log_format = '%(asctime)s - %(levelname)s - %(funcName)s - %(message)s'

formatter = logging.Formatter(log_format)

def setup_logger(logger_name='my_log', log_file='my_log.log', level=logging.DEBUG, log_format = formatter):
    ''' 
    
    ----------------------------------------------------------
    You can create multiple logger by use this function.
    pass the argument as it required
    ----------------------------------------------------------
    Source code: --
    -----------------------------------------------------------------------------------------------------------
    def setup_logger(logger_name='my_log', log_file='my_log.log', level=logging.DEBUG, log_format = formatter):
        handler = logging.FileHandler(log_file)  #adding log file to file handler
        handler.setFormatter(log_format)         # setting the format for the logger

        logger = logging.getLogger(logger_name)  #creating the main logger
        logger.setLevel(level)                   #setting the logger lavel
        logger.addHandler(handler)               # adding the logger to file handler

        return logger                           #returning the logger
    ------------------------------------------------------------------------------------------------------------
    by Default the logger level is set on DEBUG, change it in the time of creating logger when creating instance.

    ----------------------------------------------------------
    e.g.
    -----------------------------------------------------------------
    # log_1 = setup_logger(logger_name = 'log1', log_file='log1.log')
    # log_2 = setup_logger('log2', 'log2.log')

    # #givving the msg
    # log_1.info('This is from log1 logger')
    # log_2.info('This is from log2 logger')
    -----------------------------------------------------------------
    '''
    handler = logging.FileHandler(log_file)  #adding log file to file handler
    handler.setFormatter(log_format)         # setting the format for the logger

    logger = logging.getLogger(logger_name)  #creating the main logger
    logger.setLevel(level)                   #setting the logger lavel
    logger.addHandler(handler)               # adding the logger to file handler

    return logger                           #returning the logger


# log_1 = setup_logger(logger_name = 'log1', log_file='log1.log')
# log_2 = setup_logger('log2', 'log2.log')

# #givving the msg
# log_1.info('THis is from log1')
# log_2.info('thia ia from log2')