import inspect
import json
import logging
import os
from time import sleep
from config.common_variables import user_file, sys_config_file


def getLogger():
    '''
    Logger utilities
    :return:
    '''
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    filehandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s : %(levelname)s \t\t: %(name)s \t\t: %(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)  # filehandler object
    logger.setLevel(logging.INFO)
    return logger


def get_home_directory():
    '''
    Get home directory path of project
    :return: home directory path as string
    '''
    return os.getcwd()


def get_download_directory():
    '''
    Get download directory path of project
    :return: download directory path as string
    '''
    return get_home_directory() + "/config/download/"


def load_system_config_to_json():
    '''
    Load system_config file
    :return: return system_config as json
    '''
    with open(get_home_directory() + "/config/" + sys_config_file) as json_file:
        data = json.load(json_file)
    return data


def load_user_file_to_json():
    '''
    Load user file to json
    :return: return users as json
    '''
    with open(get_home_directory() + "/config/" + user_file) as json_file:
        data = json.load(json_file)
    return data


def get_totp(secret):
    '''
    Get totp 6 digit code for secret key
    :param secret: secret key to generate totp
    :return: 6 digit totp as string
    '''
    import pyotp
    sleep(35)
    totp = pyotp.TOTP(secret)
    totp = totp.now()
    return totp
