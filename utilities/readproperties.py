import configparser
import os

config = configparser.RawConfigParser()
fileName = os.path.abspath(
    os.curdir) + '/configurations/config.ini'

config.read(filenames=fileName)  # this is path for the MacOS. The path changes for other OS.


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('commonInfo', 'baseURL')
        return url

    @staticmethod
    def getPassword():
        psw = config.get('commonInfo','password')
        return psw