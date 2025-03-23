# AI Telegram Bot with Web Search

A Telegram bot powered by OpenAI's GPT-4o-mini model with web search capabilities. The bot can answer questions using its pre-trained knowledge and search the web for up-to-date information when needed.

## Features

- Natural language conversation with GPT-4o-mini
- Real-time web search capability
- Immediate feedback when searching the web
- Conversation memory to maintain context
- Typing indicators for better UX

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-telegram-bot.git
cd ai-telegram-bot
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Create a `.env` file with your API keys:
```
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
OPENAI_API_KEY=your_openai_api_key
```

4. Run the bot:
```bash
python telegram_bot.py
```

## Usage

1. Start a chat with your bot on Telegram
2. Send `/start` to initialize the conversation
3. Ask any question - the bot will:
   - Use its knowledge to answer simple questions
   - Search the web for current information when needed
   - Show a 🔍 indicator when performing web searches

## Requirements

See `requirements.txt` for the complete list of dependencies. 