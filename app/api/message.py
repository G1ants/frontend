from typing import Optional
import requests
from dotenv import load_dotenv

import os

import logging

from models.message import MessageRequest, MessageResponse 
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


load_dotenv()
BASE_URL = os.getenv('BACKEND_URL')
SERVICE_ENDPOINT = "message"

def send_message():
    print('test')
