import os
from dotenv import load_dotenv

load_dotenv()

# Bot Configuration
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID", "")

# Database Configuration (Optional)
DATABASE_URL = os.getenv("DATABASE_URL", "")

# Payment Gateway (Optional)
PAYMENT_API_KEY = os.getenv("PAYMENT_API_KEY", "")
PAYMENT_SECRET = os.getenv("PAYMENT_SECRET", "")

# Features
ENABLE_FORWARDING = True
ENABLE_CHANNEL_PREVIEW = True
ENABLE_ANALYTICS = True
