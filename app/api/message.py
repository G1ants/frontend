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

def send_message(input: MessageRequest) -> Optional[MessageResponse]:
    try:
        response = requests.post(f"{BASE_URL}/{SERVICE_ENDPOINT}", json=input.model_dump())    
        response.raise_for_status()
        message_response = MessageResponse.model_validate(response.json())
        return message_response
    except TypeError as e:
        log.error(f"Failed to parse the resposne for message {input.message}from server: {e}")
        return None
    except requests.RequestException as e:
        log.error(f"Failed to fetch response for message {input.message} from server: {e}")
        return None
    except Exception as e:
        log.error(f"Unknown error for message{input.message} occurred: {e}")
        return None
