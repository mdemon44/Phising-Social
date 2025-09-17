#!/usr/bin/env python3
"""
EMONSEC Security Tools Suite
Password Generator and Email Generator
"""

import random
import string
import argparse
import sys
import os
from time import sleep

class Color:
    """ANSI color codes for terminal output"""
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    """Display the application banner with colorful ASCII art"""
    clear_screen()
    # Multi-colored ASCII Art Banner with rainbow colors
    rainbow_colors = [Color.RED, Color.YELLOW, Color.GREEN, Color.CYAN, Color.BLUE, Color.PURPLE]
    
    banner_lines = [
        "        __  _______       _____   ___    ___________ ________  __    ______",
        "       /  |/  / __ \     /  _/ | / / |  / /  _/ ___//  _/ __ )/ /   / ____/",
        "      / /|_/ / /_/ /     / //  |/ /| | / // / \__ \ / // __  / /   / __/   ",
        "     / /  / / _, _/    _/ // /|  / | |/ // / ___/ // // /_/ / /___/ /___   ",
        "    /_/  /_/_/ |_(_)  /___/_/ |_/  |___/___//____/___/_____/_____/_____/   "
    ]
    
    # Print each line with a different rainbow color
    for i, line in enumerate(banner_lines):
        color = rainbow_colors[i % len(rainbow_colors)]
        print(f"{color}{Color.BOLD}{line}{Color.END}")
    
    print(f"{Color.BLUE}{Color.BOLD}                                                                           {Color.END}")
    print(f"{Color.PURPLE}{'='*60}{Color.END}")
    print(f"{Color.CYAN}{'EMONSEC SECURITY TOOLS SUITE':^60}{Color.END}")
    print(f"{Color.GREEN}{'Made by pentadex':^60}{Color.END}")
    print(f"{Color.PURPLE}{'='*60}{Color.END}\n")

def display_help():
    """Display help information"""
    display_banner()
    print(f"{Color.BOLD}HELP SECTION{Color.END}")
    
    print(f"{Color.GREEN}Password Generator Commands:{Color.END}")
    print("  - Option 1: Normal password (8 chars, letters and numbers)")
    print("  - Option 2: Medium password (12 chars, letters, numbers, basic symbols)")
    print("  - Option 3: High security password (16 chars, letters, numbers, all symbols)")
    print("  - Option 4: Custom password (choose your own parameters)")
    print("  - Option 5: Back to main menu")
    print()
    
    print(f"{Color.CYAN}Email Generator Commands:{Color.END}")
    print("  - Option 1: Name-based email generation")
    print("  - Option 2: Random email generation")
    print("  - Option 3: Back to main menu")
    print()
    
    print(f"{Color.YELLOW}Main Menu Commands:{Color.END}")
    print("  - Option 1: Password Generator")
    print("  - Option 2: Email Generator")
    print("  - Option 3: Help")
    print("  - Option 4: Exit")
    print()
    
    print(f"{Color.BLUE}General Usage:{Color.END}")
    print("  - Use number keys to navigate menus")
    print("  - Follow on-screen instructions")
    print("  - All generated content is displayed and can be copied")
    print()
    
    input(f"{Color.BLUE}Press Enter to return to main menu...{Color.END}")

def generate_password(strength="medium", length=None, use_upper=True, 
                     use_lower=True, use_digits=True, use_special=True):
    """
    Generate a password based on specified criteria
    
    Args:
        strength (str): Password strength (normal, medium, high)
        length (int): Custom password length
        use_upper (bool): Include uppercase letters
        use_lower (bool): Include lowercase letters
        use_digits (bool): Include digits
        use_special (bool): Include special characters
    
    Returns:
        str: Generated password
    """
    # Set default parameters based on strength
    if strength == "normal":
        default_length = 8
        charset = string.ascii_letters + string.digits
    elif strength == "medium":
        default_length = 12
        charset = string.ascii_letters + string.digits + "!@#$%&*"
    elif strength == "high":
        default_length = 16
        charset = string.ascii_letters + string.digits + string.punctuation
    else:  # Custom
        default_length = 12
        charset = ""
        if use_upper:
            charset += string.ascii_uppercase
        if use_lower:
            charset += string.ascii_lowercase
        if use_digits:
            charset += string.digits
        if use_special:
            charset += string.punctuation
    
    # Use custom length if provided
    if length is None:
        length = default_length
    else:
        # Validate length
        length = max(4, min(120, length))
    
    # Ensure charset is not empty
    if not charset:
        charset = string.ascii_letters + string.digits
    
    # Generate password
    password = ''.join(random.choice(charset) for _ in range(length))
    return password

def generate_email(mode, first_name=None, last_name=None):
    """
    Generate email addresses
    
    Args:
        mode (str): 'name' for name-based, 'random' for random
        first_name (str): First name for name-based generation
        last_name (str): Last name for name-based generation
    
    Returns:
        list: Generated email addresses
    """
    domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "icloud.com"]
    
    if mode == "name" and first_name and last_name:
        # Generate name-based emails
        first = first_name.lower()
        last = last_name.lower()
        
        patterns = [
            f"{first}.{last}",
            f"{first}{last}",
            f"{first}_{last}",
            f"{first[0]}.{last}",
            f"{first[0]}{last}",
            f"{first}.{last[0]}",
            f"{first}{last[0]}",
            f"{first[0]}{last[0]}"
        ]
        
        emails = [f"{pattern}@{random.choice(domains)}" for pattern in patterns]
        return emails
    
    else:
        # Generate random emails
        emails = []
        for _ in range(5):
            username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(6, 12)))
            domain = random.choice(domains)
            emails.append(f"{username}@{domain}")
        
        return emails

def password_generator_menu():
    """Password generator menu"""
    while True:
        display_banner()
        print(f"{Color.BOLD}PASSWORD GENERATOR{Color.END}")
        print(f"{Color.GREEN}1. Normal (8 chars, letters and numbers){Color.END}")
        print(f"{Color.CYAN}2. Medium (12 chars, letters, numbers, basic symbols){Color.END}")
        print(f"{Color.YELLOW}3. High (16 chars, letters, numbers, all symbols){Color.END}")
        print(f"{Color.BLUE}4. Custom (choose your own parameters){Color.END}")
        print(f"{Color.RED}5. Back to main menu{Color.END}")
        
        choice = input(f"\n{Color.PURPLE}Select an option (1-5): {Color.END}").strip()
        
        if choice == "1":
            password = generate_password("normal")
            display_result("Generated Password", password)
        
        elif choice == "2":
            password = generate_password("medium")
            display_result("Generated Password", password)
        
        elif choice == "3":
            password = generate_password("high")
            display_result("Generated Password", password)
        
        elif choice == "4":
            custom_password_menu()
        
        elif choice == "5":
            break
        
        else:
            print(f"{Color.RED}Invalid option!{Color.END}")
            sleep(1)

def custom_password_menu():
    """Custom password generator menu"""
    display_banner()
    print(f"{Color.BOLD}CUSTOM PASSWORD GENERATOR{Color.END}")
    
    try:
        length = int(input(f"{Color.GREEN}Password length (4-120): {Color.END}").strip() or "12")
        length = max(4, min(120, length))
        
        use_upper = input(f"{Color.CYAN}Include uppercase letters? (y/n): {Color.END}").strip().lower() != 'n'
        use_lower = input(f"{Color.YELLOW}Include lowercase letters? (y/n): {Color.END}").strip().lower() != 'n'
        use_digits = input(f"{Color.BLUE}Include digits? (y/n): {Color.END}").strip().lower() != 'n'
        use_special = input(f"{Color.PURPLE}Include special characters? (y/n): {Color.END}").strip().lower() != 'n'
        
        password = generate_password("custom", length, use_upper, use_lower, use_digits, use_special)
        display_result("Generated Password", password)
    
    except ValueError:
        print(f"{Color.RED}Invalid length! Using default.{Color.END}")
        sleep(1)

def email_generator_menu():
    """Email generator menu"""
    while True:
        display_banner()
        print(f"{Color.BOLD}EMAIL GENERATOR{Color.END}")
        print(f"{Color.GREEN}1. Name-based email generation{Color.END}")
        print(f"{Color.CYAN}2. Random email generation{Color.END}")
        print(f"{Color.RED}3. Back to main menu{Color.END}")
        
        choice = input(f"\n{Color.PURPLE}Select an option (1-3): {Color.END}").strip()
        
        if choice == "1":
            display_banner()
            print(f"{Color.BOLD}NAME-BASED EMAIL GENERATION{Color.END}")
            first_name = input(f"{Color.GREEN}Enter first name: {Color.END}").strip()
            last_name = input(f"{Color.CYAN}Enter last name: {Color.END}").strip()
            
            if first_name and last_name:
                emails = generate_email("name", first_name, last_name)
                display_result("Generated Emails", "\n".join(emails))
            else:
                print(f"{Color.RED}Please provide both first and last name!{Color.END}")
                sleep(1)
        
        elif choice == "2":
            emails = generate_email("random")
            display_result("Generated Emails", "\n".join(emails))
        
        elif choice == "3":
            break
        
        else:
            print(f"{Color.RED}Invalid option!{Color.END}")
            sleep(1)

def display_result(title, content):
    """Display generated result"""
    display_banner()
    print(f"{Color.GREEN}{Color.BOLD}{title}{Color.END}")
    print(f"{Color.CYAN}{content}{Color.END}")
    print(f"\n{Color.YELLOW}{'='*60}{Color.END}")
    
    input(f"\n{Color.BLUE}Press Enter to continue...{Color.END}")

def main():
    """Main application function"""
    # Display banner immediately when starting
    display_banner()
    
    while True:
        print(f"{Color.BOLD}MAIN MENU{Color.END}")
        print(f"{Color.GREEN}1. Password Generator{Color.END}")
        print(f"{Color.CYAN}2. Email Generator{Color.END}")
        print(f"{Color.YELLOW}3. Help{Color.END}")
        print(f"{Color.RED}4. Exit{Color.END}")
        
        choice = input(f"\n{Color.PURPLE}Select an option (1-4): {Color.END}").strip()
        
        if choice == "1":
            password_generator_menu()
        
        elif choice == "2":
            email_generator_menu()
        
        elif choice == "3":
            display_help()
        
        elif choice == "4":
            print(f"\n{Color.GREEN}Thank you for using EMONSEC Security Tools!{Color.END}")
            break
        
        else:
            print(f"{Color.RED}Invalid option!{Color.END}")
            sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Color.GREEN}Program terminated by user.{Color.END}")
        sys.exit(0)