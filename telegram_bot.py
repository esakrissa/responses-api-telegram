import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from openai import OpenAI
import asyncio

# Load environment variables
load_dotenv()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# System message for the assistant
SYSTEM_MESSAGE = """You are a helpful assistant in a Telegram chat. 
You provide clear, concise, and helpful responses to user queries.
You can search the web to provide up-to-date information.
Always cite your sources when you use web search results.
You maintain a friendly and professional tone."""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    # Initialize conversation memory
    context.chat_data['last_response_id'] = None
    await update.message.reply_text(
        'Hi! I\'m your AI assistant with web search capability. Feel free to ask me anything!'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text(
        'You can chat with me naturally. I can search the web to provide up-to-date information!'
    )

async def show_typing(context: ContextTypes.DEFAULT_TYPE, chat_id: int) -> None:
    """Show typing animation while processing."""
    while True:
        await context.bot.send_chat_action(chat_id=chat_id, action="typing")
        await asyncio.sleep(4.5)  # Telegram typing status lasts 5 seconds, so we refresh it every 4.5 seconds

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle incoming messages and respond using OpenAI with web search."""
    chat_id = update.effective_chat.id
    
    try:
        # Start typing animation
        typing_task = asyncio.create_task(show_typing(context, chat_id))
        
        # Get the user's message
        user_message = update.message.text
        
        # Create response with web search tool available but not forced
        response = client.responses.create(
            model="gpt-4o-mini",
            input=[
                {
                    "role": "system",
                    "content": [
                        {"type": "input_text", "text": SYSTEM_MESSAGE}
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "input_text", "text": user_message}
                    ]
                }
            ],
            tools=[
                {"type": "web_search"}
            ],
            tool_choice="auto",  # Let the model decide when to use tools
            temperature=0.7,
            previous_response_id=context.chat_data.get('last_response_id')  # Include previous conversation context
        )
        
        # Store the response ID for context
        context.chat_data['last_response_id'] = response.id
        
        # Check if web search is being used
        if response.output:
            for item in response.output:
                if item.type == "web_search_call":
                    await update.message.reply_text("🔍 Searching the web for information...")
                    break
        
        # Process and send the final response
        if response.output:
            for message in response.output:
                if message.type == "message" and message.content:
                    for content in message.content:
                        if content.type == "output_text":
                            await update.message.reply_text(content.text)
        
        # Cancel typing animation
        typing_task.cancel()
        
    except Exception as e:
        logger.error(f"Error processing message: {e}")
        await update.message.reply_text(
            "I apologize, but I encountered an error processing your message. Please try again."
        )
        # Cancel typing animation in case of error
        if 'typing_task' in locals():
            typing_task.cancel()

def main() -> None:
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(os.getenv('TELEGRAM_BOT_TOKEN')).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main() 