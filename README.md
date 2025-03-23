# OpenAI Responses API Telegram Bot

A Telegram bot that leverages OpenAI's latest Responses API to provide intelligent conversations with real-time web search capabilities. The bot intelligently decides when to use its pre-trained knowledge and when to search the web for up-to-date information.

## Features

- Integration with OpenAI's latest Responses API
- Smart web search capability (bot decides when to use web search)
- Immediate feedback with 🔍 indicator when performing web searches
- Maintains conversation context between messages
- Real-time typing indicators for better user experience
- Efficient response handling with proper error management

## Technical Details

- Uses OpenAI's `gpt-4o-mini` model
- Implements tool-choice auto-selection for intelligent web search decisions
- Handles response streaming and tool calls efficiently
- Maintains conversation context using response IDs

## Setup

1. Clone the repository:
```bash
git clone https://github.com/esakrissa/responses-api-telegram.git
cd responses-api-telegram
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
2. Send any question or message
3. The bot will:
   - Use its pre-trained knowledge for general questions
   - Automatically search the web when up-to-date information is needed
   - Show a 🔍 indicator when performing web searches
   - Maintain context for natural conversation flow

## Example Interactions

- General knowledge questions (uses pre-trained knowledge)
- Current events questions (triggers web search)
- Technical questions about recent developments (triggers web search)
- Follow-up questions (maintains context)

## Requirements

- Python 3.11+
- OpenAI API access with Responses API enabled
- Telegram Bot Token
- See `requirements.txt` for complete Python package dependencies 