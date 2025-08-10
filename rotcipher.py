#!/usr/bin/env python3
"""
Interactive ROT Cipher Tool
A terminal-based cipher tool supporting customizable ROT encryption/decryption
Author: SPLO1T
"""

import os
import sys
import time
from datetime import datetime

# ANSI color codes for terminal output
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_ascii_art():
    """Display cool ASCII art for ROT CIPHER"""
    art = f"""
{Colors.CYAN}{Colors.BOLD}
    ██████╗  ██████╗ ████████╗     ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗ 
    ██╔══██╗██╔═══██╗╚══██╔══╝    ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗
    ██████╔╝██║   ██║   ██║       ██║     ██║██████╔╝███████║█████╗  ██████╔╝
    ██╔══██╗██║   ██║   ██║       ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
    ██║  ██║╚██████╔╝   ██║       ╚██████╗██║██║     ██║  ██║███████╗██║  ██║
    ╚═╝  ╚═╝ ╚═════╝    ╚═╝        ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
{Colors.END}
{Colors.YELLOW}                         🔐 ROT CIPHER TOOL v1.0 by SPLO1T 🔐{Colors.END}
{Colors.WHITE}{"="*80}{Colors.END}
"""
    print(art)

def typewriter_effect(text, delay=0.05):
    """Create a typewriter effect for text"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_animation(message="Loading", duration=2):
    """Display a loading animation with dots"""
    print(f"{Colors.YELLOW}", end="")
    for i in range(duration * 4):
        dots = "." * ((i % 4) + 1)
        sys.stdout.write(f"\r{message}{dots}   ")
        sys.stdout.flush()
        time.sleep(0.25)
    print(f"{Colors.END}")

def rot_cipher(text, shift, decode=False):
    """
    Apply ROT cipher to text with given shift value
    Args:
        text (str): Text to encode/decode
        shift (int): ROT shift value (1-25)
        decode (bool): If True, reverse the shift for decoding
    Returns:
        str: Encoded/decoded text
    """
    if decode:
        shift = -shift
    
    result = []
    for char in text:
        if char.isalpha():
            # Determine if uppercase or lowercase
            is_upper = char.isupper()
            char = char.lower()
            
            # Apply ROT cipher
            shifted = ord(char) - ord('a')
            shifted = (shifted + shift) % 26
            new_char = chr(shifted + ord('a'))
            
            # Preserve original case
            if is_upper:
                new_char = new_char.upper()
            
            result.append(new_char)
        else:
            # Non-alphabetic characters remain unchanged
            result.append(char)
    
    return ''.join(result)

def save_to_log(operation, original_text, result_text, rot_value):
    """Save operation to log file"""
    try:
        with open('rot_cipher_history.txt', 'a', encoding='utf-8') as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] {operation} (ROT{rot_value})\n")
            f.write(f"Original: {original_text}\n")
            f.write(f"Result:   {result_text}\n")
            f.write("-" * 50 + "\n")
        return True
    except Exception as e:
        print(f"{Colors.RED}Error saving to log: {e}{Colors.END}")
        return False

def display_menu(rot_value):
    """Display the main menu"""
    print(f"\n{Colors.BLUE}{Colors.BOLD}MAIN MENU{Colors.END}")
    print(f"{Colors.WHITE}{'='*40}{Colors.END}")
    print(f"{Colors.GREEN}[1]{Colors.END} Encode Text")
    print(f"{Colors.CYAN}[2]{Colors.END} Decode Text")
    print(f"{Colors.YELLOW}[3]{Colors.END} Change ROT Value (Current: {Colors.BOLD}{rot_value}{Colors.END})")
    print(f"{Colors.MAGENTA}[4]{Colors.END} View History")
    print(f"{Colors.RED}[5]{Colors.END} Exit")
    print(f"{Colors.WHITE}{'='*40}{Colors.END}")

def encode_text(rot_value):
    """Handle text encoding"""
    print(f"\n{Colors.GREEN}{Colors.BOLD}🔒 ENCODE MODE (ROT{rot_value}){Colors.END}")
    print(f"{Colors.WHITE}{'-'*40}{Colors.END}")
    
    text = input(f"{Colors.WHITE}Enter text to encode: {Colors.END}")
    if not text.strip():
        print(f"{Colors.RED}Error: Please enter some text to encode.{Colors.END}")
        return
    
    encoded = rot_cipher(text, rot_value)
    
    print(f"\n{Colors.YELLOW}Original:{Colors.END} {text}")
    print(f"{Colors.GREEN}{Colors.BOLD}Encoded: {encoded}{Colors.END}")
    
    # Save to log
    if save_to_log("ENCODE", text, encoded, rot_value):
        print(f"{Colors.CYAN}✓ Saved to rot_cipher_history.txt{Colors.END}")

def decode_text(rot_value):
    """Handle text decoding"""
    print(f"\n{Colors.CYAN}{Colors.BOLD}🔓 DECODE MODE (ROT{rot_value}){Colors.END}")
    print(f"{Colors.WHITE}{'-'*40}{Colors.END}")
    
    text = input(f"{Colors.WHITE}Enter text to decode: {Colors.END}")
    if not text.strip():
        print(f"{Colors.RED}Error: Please enter some text to decode.{Colors.END}")
        return
    
    decoded = rot_cipher(text, rot_value, decode=True)
    
    print(f"\n{Colors.YELLOW}Original:{Colors.END} {text}")
    print(f"{Colors.CYAN}{Colors.BOLD}Decoded: {decoded}{Colors.END}")
    
    # Save to log
    if save_to_log("DECODE", text, decoded, rot_value):
        print(f"{Colors.CYAN}✓ Saved to rot_cipher_history.txt{Colors.END}")

def change_rot_value(current_rot):
    """Handle changing the ROT value"""
    print(f"\n{Colors.YELLOW}{Colors.BOLD}⚙️  CHANGE ROT VALUE{Colors.END}")
    print(f"{Colors.WHITE}{'-'*40}{Colors.END}")
    print(f"Current ROT value: {Colors.BOLD}{current_rot}{Colors.END}")
    print(f"{Colors.WHITE}Valid range: 1-25{Colors.END}")
    
    try:
        new_rot = int(input(f"{Colors.WHITE}Enter new ROT value: {Colors.END}"))
        if 1 <= new_rot <= 25:
            print(f"{Colors.GREEN}✓ ROT value changed to {new_rot}{Colors.END}")
            return new_rot
        else:
            print(f"{Colors.RED}Error: ROT value must be between 1 and 25.{Colors.END}")
            return current_rot
    except ValueError:
        print(f"{Colors.RED}Error: Please enter a valid number.{Colors.END}")
        return current_rot

def view_history():
    """Display the last few entries from the history file"""
    print(f"\n{Colors.MAGENTA}{Colors.BOLD}📜 RECENT HISTORY{Colors.END}")
    print(f"{Colors.WHITE}{'-'*40}{Colors.END}")
    
    try:
        if not os.path.exists('rot_cipher_history.txt'):
            print(f"{Colors.YELLOW}No history file found. Encode or decode something first!{Colors.END}")
            return
        
        with open('rot_cipher_history.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        if not lines:
            print(f"{Colors.YELLOW}History file is empty.{Colors.END}")
            return
        
        # Display last 10 operations
        print(f"{Colors.WHITE}Showing last entries:{Colors.END}\n")
        
        # Group lines by operations (every 4 lines is one operation)
        operations = []
        current_op = []
        for line in lines:
            if line.strip() == "-" * 50:
                if current_op:
                    operations.append(current_op)
                    current_op = []
            else:
                current_op.append(line.strip())
        
        # Show last 5 operations
        for op in operations[-5:]:
            for line in op:
                if line.startswith('['):
                    print(f"{Colors.CYAN}{line}{Colors.END}")
                elif line.startswith('Original:'):
                    print(f"{Colors.YELLOW}{line}{Colors.END}")
                elif line.startswith('Result:'):
                    print(f"{Colors.GREEN}{line}{Colors.END}")
            print()
            
    except Exception as e:
        print(f"{Colors.RED}Error reading history: {e}{Colors.END}")

def startup_sequence():
    """Handle the startup sequence with animations"""
    clear_screen()
    print_ascii_art()
    
    typewriter_effect(f"{Colors.WHITE}Welcome to the ROT Cipher Tool!{Colors.END}", 0.03)
    loading_animation("Initializing cipher engine", 1)
    
    print(f"{Colors.GREEN}✓ Ready to encrypt and decrypt!{Colors.END}")
    time.sleep(1)

def main():
    """Main program loop"""
    rot_value = 13  # Default ROT13
    
    # Startup sequence
    startup_sequence()
    
    while True:
        try:
            clear_screen()
            print_ascii_art()
            display_menu(rot_value)
            
            choice = input(f"\n{Colors.WHITE}Choose an option (1-5): {Colors.END}").strip()
            
            if choice == '1':
                encode_text(rot_value)
            elif choice == '2':
                decode_text(rot_value)
            elif choice == '3':
                rot_value = change_rot_value(rot_value)
            elif choice == '4':
                view_history()
            elif choice == '5':
                print(f"\n{Colors.YELLOW}Thanks for using ROT Cipher Tool!{Colors.END}")
                typewriter_effect(f"{Colors.CYAN}Goodbye! 👋{Colors.END}", 0.05)
                break
            else:
                print(f"{Colors.RED}Invalid choice. Please select 1-5.{Colors.END}")
            
            if choice in ['1', '2', '3', '4']:
                input(f"\n{Colors.WHITE}Press Enter to continue...{Colors.END}")
                
        except KeyboardInterrupt:
            print(f"\n\n{Colors.YELLOW}Program interrupted by user.{Colors.END}")
            print(f"{Colors.CYAN}Goodbye! 👋{Colors.END}")
            break
        except Exception as e:
            print(f"{Colors.RED}An unexpected error occurred: {e}{Colors.END}")
            input(f"{Colors.WHITE}Press Enter to continue...{Colors.END}")

if __name__ == "__main__":
    main()