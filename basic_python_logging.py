#!/usr/bin/python

import logging
import os
import sys

def configure_logger(log_file):
    """Accepts a fully-qualified filename to the log file.

    Logs at DEBUG to file and at WARNING to stdout.

    Returns a fully-configured logger object.
    """
    logger = logging.getLogger('ProgramName')
    log_formatter = logging.Formatter(
        "%(name)s: %(asctime)s - %(levelname)s: %(message)s")
    file_handler = logging.FileHandler(
        log_file)
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(log_formatter)
    stream_handler.setLevel(logging.WARNING)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger

if __name__ == "__main__":
    LOG = configure_logger('logfile.txt')
    LOG.debug('This is debug level')
    LOG.info('This is info level')
    LOG.warning('This is warning level')
    LOG.error('This is error level')   
    LOG.critical('This is critical level')
