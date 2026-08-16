import os
import random
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN is not set. Put it in your .env file.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello 👋 I'm a fishy little Telegram bot. 🐟"
    )

async def fish(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(FISHY_MESSAGES))

FISHY_MESSAGES = ['Hello 👋', 'Hey there 🐟', "What's swimming on?", 'You look fishy today.', 'Something smells suspicious... 🐠', 'Caught you lurking.', 'Stay fishy.', 'The fish council has noticed you.', 'Why are you staring at me?', 'Blub blub.', 'This message is 100% fish-approved.', 'Suspicious activity detected.', 'You have entered the fish zone.', 'A fish told me about you.', 'Keep calm and swim.', 'Who let you into the aquarium?', 'Definitely not a normal message.', 'Fish.exe is running.', 'Your vibes are slightly aquatic.', 'The ocean knows.', 'I have questions. Fish has answers.', 'This seems... fishy.', 'Permission to swim?', 'Current status: suspicious.', 'You have been observed by a goldfish.', 'The salmon are judging you.', 'Nice username, fish.', 'Do not trust the penguins.', 'A wild fish appeared!', 'Blub detected.', 'Your message passed the fish test.', 'The aquarium doors are locked.', 'Something is bubbling.', 'Fish intelligence online.', 'Report to the nearest pond.', 'You smell like secrets.', 'The tuna committee is meeting.', 'Please remain aquatic.', 'Warning: excessive fishiness.', 'A suspicious carp has entered the chat.', 'No thoughts, only bubbles.', 'Swimming through the chat...', 'This bot has seen things.', 'The fish know what you did.', 'Definitely a normal Telegram bot.', 'You have been fin-tagged.', 'The sea has accepted your request.', 'Bubble protocol activated.', "I would explain, but I'm a fish.", 'Your aquatic clearance is pending.', 'Incoming fish.', 'Outgoing fish.', 'The shrimp are monitoring this conversation.', 'Something moved in the tank.', 'That was not a normal bubble.', 'Fish mode: ON.', 'The ocean is calling.', 'You are now 3% more suspicious.', 'Carp diem.', 'Cod you please behave?', 'This chat needs more water.', 'A fish has entered the premises.', 'The reef has opinions.', 'No refunds after entering the aquarium.', 'Please hold while I consult a fish.', 'The fish hotline is busy.', 'Your request has been forwarded to the sardines.', 'A mysterious fin appeared.', 'Aquatic authentication successful.', 'You passed the vibe check, fish edition.', 'This conversation is getting salty.', 'The ocean approves.', 'Fish detected nearby.', 'Something is definitely swimming here.', 'Your message has bubbles.', 'Deep thoughts, shallow water.', 'The plankton have been notified.', 'Do not feed the bot.', 'Bot.exe smells like seaweed.', 'A suspicious dolphin is watching.', 'The crab committee disagrees.', 'This is your official fish warning.', 'You have been promoted to fish.', "Congratulations, you're aquatic now.", 'Swimming privileges granted.', 'The sea has receipts.', 'Your fish license expires never.', 'The bubbles are listening.', 'Please insert one fish.', 'Fish required to continue.', '404: Normal behavior not found.', 'This bot runs on water and questionable decisions.', 'The aquarium server is alive.', 'Someone tell the octopus.', 'Eight arms, zero explanations.', 'Fish facts unavailable.', 'The reef is loading...', 'Your aquatic session has started.', 'Have a suspiciously nice day. 🐟']

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("fish", fish))

    print("Fishy bot is swimming...")
    app.run_polling()

if __name__ == "__main__":
    main()
