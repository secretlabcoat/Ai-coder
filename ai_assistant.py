"""
Ai-coder - Simple AI Assistant
Just run: python ai_assistant.py
"""

import json
import os
import time
from datetime import datetime
from pathlib import Path

class AiCoder:
    def __init__(self):
        self.memory_file = "memory.json"
        self.messages = self.load_memory()
        print("🤖 Ai-coder is ready!")
        print("Type 'exit' to quit")
        print("Type 'new' for new chat")
        print("Type 'help' for commands")

    def load_memory(self):
        if Path(self.memory_file).exists():
            with open(self.memory_file, 'r') as f:
                return json.load(f)
        return []

    def save_memory(self):
        with open(self.memory_file, 'w') as f:
            json.dump(self.messages, f, indent=2)

    def add_message(self, role, content):
        self.messages.append({
            "role": role,
            "content": content,
            "time": datetime.now().isoformat()
        })
        self.save_memory()

    def chat(self, message):
        self.add_message("user", message)
        response = f"I received: {message}"
        self.add_message("assistant", response)
        return response

    def run(self):
        while True:
            user_input = input("\nYou: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Goodbye!")
                break
            elif user_input.lower() == 'new':
                self.messages = []
                print("New chat started!")
                continue
            elif user_input.lower() == 'help':
                print("\nCommands:")
                print("  exit/quit - Exit the program")
                print("  new - Start new chat")
                print("  help - Show this help")
                print("  (anything else) - Chat with AI")
                continue

            response = self.chat(user_input)
            print(f"\nAi-coder: {response}")

if __name__ == "__main__":
    ai = AiCoder()
    ai.run()
