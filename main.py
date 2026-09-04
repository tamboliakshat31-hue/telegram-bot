import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Replace with your bot token
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

# Subscription plans
PLANS = {
    "1_day": {"price": "₹49", "duration": "1 DAY", "emoji": "🎁"},
    "7_days": {"price": "₹149", "duration": "7 DAYS", "emoji": "💎"},
    "30_days": {"price": "₹399", "duration": "30 DAYS", "emoji": "🔥"},
    "lifetime": {"price": "₹599", "duration": "LIFETIME", "emoji": "👑"}
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    
    # Create main menu keyboard
    keyboard = [
        [InlineKeyboardButton("📋 Menu", callback_data="menu")],
        [InlineKeyboardButton("📎 Attach", callback_data="attach")],
        [InlineKeyboardButton("⏰ History", callback_data="history")],
        [InlineKeyboardButton("🎤 Voice", callback_data="voice")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_text = (
        f"🎉 Welcome {user.first_name}!\n\n"
        "✨ EXCLUSIVE CONTENT ✨\n"
        "• HANDPICKED CONTENT\n"
        "• REGULAR UPLOADS\n"
        "• EXCLUSIVE MATERIAL\n"
        "• LIMITED ACCESS\n\n"
        "🔒 GET PREMIUM NOW!"
    )
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show the main menu."""
    keyboard = [
        [InlineKeyboardButton("🎁 CHANNEL PREVIEW", callback_data="preview")],
        [InlineKeyboardButton("💰 SUBSCRIPTION PLANS", callback_data="plans")],
        [InlineKeyboardButton("📱 HOW TO GET", callback_data="how_to")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.callback_query.edit_message_text(
        text="📚 MAIN MENU\n\nChoose an option:",
        reply_markup=reply_markup
    )

async def show_plans(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show subscription plans."""
    query = update.callback_query
    await query.answer()
    
    plans_text = "💎 SUBSCRIPTION PLANS 💎\n\n"
    plans_text += "⭐ EXCLUSIVE HANDPICKED MAAL 🩸\n"
    plans_text += "⭐ RESERVED FOR THE FEW 🕷️\n"
    plans_text += "⭐ NO REPEATS • NO SECOND CHANCES 💀\n"
    plans_text += "⭐ LIMITED TIME ONLY ⏳\n\n"
    
    keyboard = []
    for plan_key, plan_data in PLANS.items():
        button_text = f"{plan_data['emoji']} {plan_data['duration']} • {plan_data['price']}"
        keyboard.append([InlineKeyboardButton(button_text, callback_data=f"subscribe_{plan_key}")])
    
    keyboard.append([InlineKeyboardButton("⬅️ Back", callback_data="menu")])
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        text=plans_text,
        reply_markup=reply_markup
    )

async def handle_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle subscription selection."""
    query = update.callback_query
    plan_key = query.data.replace("subscribe_", "")
    
    if plan_key in PLANS:
        plan = PLANS[plan_key]
        await query.answer(f"You selected {plan['duration']} - {plan['price']}")
        
        keyboard = [
            [InlineKeyboardButton("✅ CONFIRM PAYMENT", callback_data=f"payment_{plan_key}")],
            [InlineKeyboardButton("⬅️ Back", callback_data="plans")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        message = (
            f"✨ SUBSCRIPTION DETAILS ✨\n\n"
            f"Plan: {plan['duration']}\n"
            f"Price: {plan['price']}\n"
            f"Status: ACTIVE\n\n"
            f"🔒 CLICK HERE TO CLAIM"
        )
        
        await query.edit_message_text(
            text=message,
            reply_markup=reply_markup
        )

async def handle_payment(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle payment confirmation."""
    query = update.callback_query
    plan_key = query.data.replace("payment_", "")
    
    if plan_key in PLANS:
        plan = PLANS[plan_key]
        await query.answer()
        
        message = (
            f"✅ PAYMENT CONFIRMED!\n\n"
            f"Plan: {plan['duration']}\n"
            f"Amount: {plan['price']}\n\n"
            f"🎉 Welcome to our EXCLUSIVE community!\n"
            f"🚀 Access granted • Forwarding: ON ✅\n"
            f"📱 Check your messages for exclusive content"
        )
        
        keyboard = [[InlineKeyboardButton("📱 Back to Menu", callback_data="menu")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            text=message,
            reply_markup=reply_markup
        )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle button presses."""
    query = update.callback_query
    await query.answer()
    
    if query.data == "menu":
        await menu(update, context)
    elif query.data == "plans":
        await show_plans(update, context)
    elif query.data == "preview":
        message = "🎬 CHANNEL PREVIEW\n\n⭐ EXCLUSIVE HANDPICKED CONTENT\n⭐ REGULAR UPLOADS\n⭐ EXCLUSIVE MAAL 👿\n⭐ LIMITED ACCESS\n\n✨ RESERVED FOR THE FEW ✨"
        keyboard = [[InlineKeyboardButton("⬅️ Back", callback_data="menu")]]
        await query.edit_message_text(text=message, reply_markup=InlineKeyboardMarkup(keyboard))
    elif query.data == "how_to":
        message = "📱 HOW TO GET ACCESS:\n\n1️⃣ Choose a subscription plan\n2️⃣ Click CONFIRM PAYMENT\n3️⃣ Complete payment\n4️⃣ Get instant access to exclusive content!\n\n⏳ LIMITED TIME OFFER - GET IN BEFORE IT'S GONE!"
        keyboard = [[InlineKeyboardButton("⬅️ Back", callback_data="menu")]]
        await query.edit_message_text(text=message, reply_markup=InlineKeyboardMarkup(keyboard))

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log the error and send a telegram message to notify the developer."""
    logger.error(msg="Exception while handling an update:", exc_info=context.error)

def main() -> None:
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    # log all errors
    application.add_error_handler(error_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling()

if __name__ == '__main__':
    main()
