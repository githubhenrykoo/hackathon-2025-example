#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram import Update
from telegram.ext import ContextTypes

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a pong message when the command /ping is issued."""
    await update.message.reply_text('Pong!')

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Placeholder for a weather command."""
    # In a real bot, you would call a weather API here
    await update.message.reply_text('Weather feature is coming soon!')
