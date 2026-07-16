import os
from dotenv import load_dotenv
load_dotenv()
PHONE_NUMBER=os.getenv("PHONE_NUMBER")
INVALID_PHONE_NUMBER=os.getenv("INVALID_PHONE_NUMBER")
FIRST_NAME=os.getenv("FIRST_NAME")
LAST_NAME = os.getenv("LAST_NAME")
EMAIL_ADDRESS=os.getenv("EMAIL_ADDRESS")
NEW_PHONE_NUMBER=os.getenv("NEW_PHONE_NUMBER")
BASE_URL=os.getenv("BASE_URL")
ASSIGNING_INSTITUTION=os.getenv("ASSIGNING_INSTITUTION")
ORG=os.getenv("ORG")
