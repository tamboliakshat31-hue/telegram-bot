import os
from dotenv import load_dotenv

load_dotenv()

# Bot Configuration
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID", "")
PAYMENT_LOG_CHANNEL = int(os.getenv("PAYMENT_LOG_CHANNEL", "-1003853425883"))
EXCLUSIVE_CONTENT_CHANNEL = int(os.getenv("EXCLUSIVE_CONTENT_CHANNEL", "-1003897009577"))

# Payment Gateway Configuration
MERCHANT_ID = os.getenv("MERCHANT_ID", "HuUfFh33921066625955")
UPI_ID = os.getenv("UPI_ID", "paytm.s1mjler@pty")
AUTO_SELECT_AMOUNT = os.getenv("AUTO_SELECT_AMOUNT", "true").lower() == "true"
AUTO_VERIFY = os.getenv("AUTO_VERIFY", "true").lower() == "true"

# Payment Timeout Configuration
PAYMENT_TIMEOUT_MINUTES = int(os.getenv("PAYMENT_TIMEOUT_MINUTES", "20"))
PAYMENT_TIMEOUT_SECONDS = PAYMENT_TIMEOUT_MINUTES * 60  # 1200 seconds

# Database Configuration (Optional)
DATABASE_URL = os.getenv("DATABASE_URL", "")

# Payment Gateway (Optional)
PAYMENT_API_KEY = os.getenv("PAYMENT_API_KEY", "")
PAYMENT_SECRET = os.getenv("PAYMENT_SECRET", "")

# Features
ENABLE_FORWARDING = True
ENABLE_CHANNEL_PREVIEW = True
ENABLE_ANALYTICS = True
ENABLE_PAYMENT_LOGGING = True
ENABLE_EXCLUSIVE_ACCESS = True
ENABLE_UPI_PAYMENTS = True
ENABLE_PAYMENT_TIMEOUT = True
