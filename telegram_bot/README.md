# Basic Telegram Bot

A simple Telegram bot built with Python and the python-telegram-bot library.

## Features

- `/start` - Start the bot
- `/help` - Show available commands
- `/ping` - Check if the bot is alive
- `/weather` - Get weather information (placeholder for future implementation)
- Echo functionality - The bot will echo back any message you send

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- A Telegram account
- A Telegram Bot Token (obtained from [@BotFather](https://t.me/BotFather))

### Installation

1. Clone this repository:
   ```
   git clone <repository-url>
   cd telegram_bot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file based on the provided `.env.example`:
   ```
   cp .env.example .env
   ```

4. Edit the `.env` file and add your Telegram Bot Token:
   ```
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   ```

### Running the Bot

Run the bot with the following command:
```
python bot.py
```

## Project Structure

```
telegram_bot/
├── bot.py                  # Main bot script
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variables template
├── README.md               # This file
├── handlers/               # Command handlers
│   ├── __init__.py
│   └── basic_handlers.py   # Basic command handlers
└── utils/                  # Utility functions
    ├── __init__.py
    └── helpers.py          # Helper functions
```

## Extending the Bot

To add new commands:

1. Create a new handler function in `handlers/basic_handlers.py` or create a new handler file
2. Import the handler in `bot.py`
3. Register the handler with `application.add_handler(CommandHandler("command_name", handler_function))`
4. Update the help text in the `help_command` function

## License

[MIT](LICENSE)
