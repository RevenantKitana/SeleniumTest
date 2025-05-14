import os
import random

def save_account(user_data):
    with open("data/account.txt", "a", encoding="utf-8") as f:
        f.write(f"{user_data['username']}|{user_data['password']}\n")

def load_random_account():
    try:
        with open("data/account.txt", "r", encoding="utf-8") as f:
            # Read and filter valid lines
            lines = [line.strip() for line in f.readlines() if line.strip() and line.count("|") == 1]
            if not lines:
                return None
            
            # Select a random valid line
            account = random.choice(lines).split("|")
            if len(account) != 2:
                return None
                
            # Strip whitespace from fields
            username, password = [field.strip() for field in account]
            if not username or not password:
                return None
                
            return {
                "username": username,
                "password": password
            }
            
    except FileNotFoundError:
        return None
    except (IOError, UnicodeDecodeError):
        return None