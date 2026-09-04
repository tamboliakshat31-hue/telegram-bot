# Telegram Bot - Exclusive Content Bot

A feature-rich Telegram bot with subscription plans, exclusive content management, and premium features.

## Features

✨ **Exclusive Content Management**
- Handpicked content delivery
- No repeats, no second chances
- Limited time offers
- Reserved for premium members

💰 **Flexible Subscription Plans**
- 1 Day - ₹49
- 7 Days - ₹149
- 30 Days - ₹399
- Lifetime - ₹599

📱 **Bot Features**
- Menu system with inline buttons
- Payment confirmation
- Channel preview
- Exclusive member access
- Forwarding enabled
- User-friendly interface

## Installation

### Prerequisites
- Python 3.8+
- Telegram Bot Token (from @BotFather)

### Setup Steps

1. **Clone the repository**
```bash
git clone https://github.com/tamboliakshat31-hue/telegram-bot.git
cd telegram-bot
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure bot token**
```bash
cp .env.example .env
# Edit .env and add your BOT_TOKEN from @BotFather
```

5. **Run the bot**
```bash
python main.py
```

## Getting Your Bot Token

1. Open Telegram and search for **@BotFather**
2. Send `/start` command
3. Send `/newbot` to create a new bot
4. Follow the prompts and get your bot token
5. Add the token to your `.env` file

## Usage

### User Commands
- `/start` - Start the bot and see welcome message
- Click **Menu** - Access main menu
- Click **SUBSCRIPTION PLANS** - View pricing
- Select a plan - Choose subscription duration
- **CONFIRM PAYMENT** - Complete purchase

### Admin Commands (Optional)
- Manage users and subscriptions
- Send broadcast messages
- View analytics
- Manage exclusive content

## File Structure

```
telegram-bot/
├── main.py              # Main bot script with handlers
├── config.py            # Configuration settings
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variables template
├── .env                 # Your actual environment variables (create this)
└── README.md           # This file
```

## Subscription Plans

| Plan | Duration | Price |
|------|----------|-------|
| 🎁 Basic | 1 Day | ₹49 |
| 💎 Premium | 7 Days | ₹149 |
| 🔥 Pro | 30 Days | ₹399 |
| 👑 Ultimate | Lifetime | ₹599 |

### What's Included
✅ Exclusive handpicked content  
✅ Regular uploads  
✅ No repeats policy  
✅ Limited time access  
✅ Private community  
✅ Forwarding enabled  

## Features Explained

### Menu System
The bot provides an intuitive menu with the following options:
- **📋 Menu** - Main navigation
- **📎 Attach** - Attach files
- **⏰ History** - View message history
- **🎤 Voice** - Voice message support

### Subscription Flow
1. User selects a plan
2. Views subscription details
3. Confirms payment
4. Gets instant access to exclusive content
5. Can cancel anytime

## Configuration Options

Edit `config.py` to customize:
- Enable/disable forwarding
- Toggle channel preview
- Enable analytics
- Adjust feature settings

## Database Integration (Optional)

To add user tracking and subscription management:
```python
# Add database connection string to .env
DATABASE_URL=postgresql://user:password@localhost/telegram_bot
```

## Payment Integration (Optional)

To enable real payments, integrate with:
- Razorpay
- PayPal
- Stripe
- Or any other payment gateway

## Deployment

### Local Deployment
```bash
python main.py
```

### Cloud Deployment (Heroku, AWS, etc.)
1. Add Procfile:
```
worker: python main.py
```

2. Deploy using your platform's CLI

### Docker Deployment
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

## Troubleshooting

### Bot not responding
- Check if bot token is correct in `.env`
- Ensure bot is running: `python main.py`
- Check internet connection

### Payment not working
- Verify payment gateway credentials
- Check API keys in `.env`
- Review payment gateway logs

### Subscription not activating
- Ensure user ID is correct
- Check database connection
- Verify subscription plan exists

## Support

For issues or feature requests, please open an issue on GitHub.

## License

This project is open source and available under the MIT License.

## Author

Created by: tamboliakshat31-hue

---

**Made with ❤️ for exclusive content sharing**
