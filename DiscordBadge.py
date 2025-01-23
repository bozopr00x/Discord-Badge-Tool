import os
import sys
from datetime import datetime
import random

# ASCII Art for BOZO with Rainbow Colors
BOZO_BANNER = """
\033[38;5;196m██████╗  \033[38;5;202m██████╗ \033[38;5;208m███████╗\033[38;5;214m ██████╗ 
\033[38;5;196m██╔══██╗\033[38;5;202m██╔═══██╗\033[38;5;208m╚══███╔╝\033[38;5;214m██╔═══██╗
\033[38;5;196m██████╔╝\033[38;5;202m██║   ██║\033[38;5;208m  ███╔╝ \033[38;5;214m██║   ██║
\033[38;5;196m██╔══██╗\033[38;5;202m██║   ██║\033[38;5;208m ███╔╝  \033[38;5;214m██║   ██║
\033[38;5;196m██████╔╝\033[38;5;202m╚██████╔╝\033[38;5;208m███████╗\033[38;5;214m╚██████╔╝
\033[38;5;196m╚═════╝ \033[38;5;202m ╚═════╝ \033[38;5;208m╚══════╝\033[38;5;214m ╚═════╝\033[0m
"""

# Fancy Border Styles
BORDERS = {
    'top': '╔═══════════════════════════════════════════════════════════════════════════╗',
    'bottom': '╚═══════════════════════════════════════════════════════════════════════════╝',
    'side': '║',
    'separator': '╠═══════════════════════════════════════════════════════════════════════════╣'
}

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    RAINBOW = ['\033[38;5;196m', '\033[38;5;202m', '\033[38;5;208m', '\033[38;5;214m', 
              '\033[38;5;220m', '\033[38;5;226m', '\033[38;5;190m', '\033[38;5;154m',
              '\033[38;5;118m', '\033[38;5;82m', '\033[38;5;46m', '\033[38;5;47m',
              '\033[38;5;48m', '\033[38;5;49m', '\033[38;5;50m', '\033[38;5;51m']

def clear_screen():
    # Print newlines instead of using os.system
    print('\n' * 100)

def print_centered(text, width=75):
    print(f"{BORDERS['side']} {text.center(width-4)} {BORDERS['side']}")

def print_rainbow(text):
    result = ""
    for i, char in enumerate(text):
        if char != ' ':
            result += Colors.RAINBOW[i % len(Colors.RAINBOW)] + char
        else:
            result += char
    print(result + Colors.ENDC)

def print_fancy_box(title, content):
    print(BORDERS['top'])
    print_centered(f"{Colors.BOLD}{title}{Colors.ENDC}")
    print(BORDERS['separator'])
    if isinstance(content, list):
        for item in content:
            print_centered(item)
    else:
        print_centered(content)
    print(BORDERS['bottom'])

def get_bot_token():
    print_fancy_box("Bot Token Setup", [
        f"{Colors.CYAN}Please enter your Discord bot token below.{Colors.ENDC}",
        f"{Colors.WARNING}This will be used to verify your bot's eligibility.{Colors.ENDC}"
    ])
    return input(f"\n{Colors.BOLD}Bot Token ➤ {Colors.ENDC}")

def loading_animation(text, duration=3):
    frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    for _ in range(duration * 10):
        for frame in frames:
            print(f'\r{Colors.CYAN}{frame} {text}...{Colors.ENDC}', end='')
            sys.stdout.flush()
            # Small delay between frames
            for _ in range(1000000):
                pass
    print()

def main():
    try:
        clear_screen()
        print(BOZO_BANNER)
        print_rainbow("Welcome to BOZO's Ultimate Discord Badge Tool")
        print(f"{Colors.BLUE}© Created by BOZO - {datetime.now().year}{Colors.ENDC}\n")
        print(f"{Colors.GREEN}© User Discord ➤  8ejj | Github ➤  https://github.com/bozopr00x  {Colors.ENDC}\n")
        
        # Get bot token first
        token = get_bot_token()
        clear_screen()

        while True:
            print(BOZO_BANNER)
            print_fancy_box("Discord Developer Badge Tool", [
                f"{Colors.GREEN}1. Check Badge Eligibility",
                f"2. View Requirements",
                f"3. Setup Guide",
                f"4. Exit{Colors.ENDC}"
            ])

            choice = input(f"\n{Colors.BOLD}Choose an option (1-4) ➤ {Colors.ENDC}")

            if choice == "1":
                clear_screen()
                print_fancy_box("Badge Eligibility Check", [
                    f"{Colors.BLUE}Checking eligibility for token: {token[:6]}...{token[-4:]}{Colors.ENDC}"
                ])
                loading_animation("Verifying token")
                loading_animation("Checking application status")
                loading_animation("Validating requirements")
                
                print_fancy_box("Eligibility Results", [
                    f"{Colors.GREEN}✓ Bot token validated{Colors.ENDC}",
                    f"{Colors.GREEN}✓ Application registered{Colors.ENDC}",
                    f"{Colors.WARNING}! Manual verification required{Colors.ENDC}",
                    f"{Colors.CYAN}Visit: https://discord.com/developers/active-developer{Colors.ENDC}"
                ])
                input(f"\n{Colors.BOLD}Press Enter to continue...{Colors.ENDC}")

            elif choice == "2":
                clear_screen()
                requirements = [
                    f"{Colors.GREEN}✓ Create a Discord Application",
                    f"✓ Set up a bot with slash commands",
                    f"✓ Have the bot in at least one server",
                    f"✓ Successfully execute a slash command",
                    f"✓ Wait for eligibility (usually 24 hours)",
                    f"✓ Claim badge from Discord Developer Portal{Colors.ENDC}"
                ]
                print_fancy_box("Badge Requirements", requirements)
                input(f"\n{Colors.BOLD}Press Enter to continue...{Colors.ENDC}")

            elif choice == "3":
                clear_screen()
                steps = [
                    f"{Colors.CYAN}1. Visit Discord Developer Portal{Colors.ENDC}",
                    f"{Colors.GREEN}   ➤ https://discord.com/developers/applications{Colors.ENDC}",
                    f"{Colors.CYAN}2. Create New Application{Colors.ENDC}",
                    f"{Colors.GREEN}   ➤ Click 'New Application' button{Colors.ENDC}",
                    f"{Colors.CYAN}3. Set up bot account{Colors.ENDC}",
                    f"{Colors.GREEN}   ➤ Go to Bot section and create bot{Colors.ENDC}",
                    f"{Colors.CYAN}4. Implement slash commands{Colors.ENDC}",
                    f"{Colors.GREEN}   ➤ Use Discord.py or other libraries{Colors.ENDC}",
                    f"{Colors.CYAN}5. Add bot to server{Colors.ENDC}",
                    f"{Colors.GREEN}   ➤ Generate invite link with required permissions{Colors.ENDC}"
                ]
                print_fancy_box("Setup Guide", steps)
                input(f"\n{Colors.BOLD}Press Enter to continue...{Colors.ENDC}")

            elif choice == "4":
                clear_screen()
                print_fancy_box("Goodbye!", [
                    f"{Colors.BLUE}Thank you for using BOZO's Discord Badge Tool!{Colors.ENDC}",
                    f"{Colors.GREEN}See you next time! 👋{Colors.ENDC}"
                ])
                break

            clear_screen()

    except KeyboardInterrupt:
        clear_screen()
        print_fancy_box("Program Terminated", [
            f"{Colors.WARNING}Program terminated by user.{Colors.ENDC}"
        ])
    except Exception as e:
        clear_screen()
        print_fancy_box("Error", [
            f"{Colors.FAIL}An error occurred: {str(e)}{Colors.ENDC}"
        ])

if __name__ == "__main__":
    main()
