#!/usr/bin/env python
# -*- coding: utf-8 -*-

def format_message(message: str) -> str:
    """Format a message for better display."""
    return message.strip()

def validate_input(text: str) -> bool:
    """Simple validation function for user input."""
    return bool(text and text.strip())
