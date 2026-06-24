import os

API_ID    = os.environ.get("API_ID", "30723612")
API_HASH  = os.environ.get("API_HASH", "9ca08fc02acd2f9fbbcc73787bcb1a46")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8993371083:AAENopIEV3PzKOVea0UP8gu2Co73W_dPc8") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
