import os
from dotenv import load_dotenv

BASEDIR = os.path.abspath(os.path.dirname(__name__))
load_dotenv(os.path.join(BASEDIR, 'conf/.env'))

message_delay = 1

BOT_TOKEN = os.getenv('BOTTOKEN')
BOT_ID = ""
