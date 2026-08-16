# Fishy Telegram Bot 🐟

A simple Telegram bot with 100 fishy messages.

## Commands

- `/start` - Say hello
- `/fish` - Send a random fishy message

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Add your bot token

Edit `.env`:

```env
BOT_TOKEN=your_telegram_bot_token_here
```

Get the token from Telegram's BotFather.

### 3. Run

```bash
python bot.py
```

## Files

```text
fishy_telegram_bot/
├── bot.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

The 100 messages are stored directly in `bot.py`.

## Security

Never commit your real `.env` file or bot token to GitHub.
