import sys

from colorama import Fore, Style

# Make sure that the user is running Python 3.8 or higher
if sys.version_info < (3, 8):
    exit("Python 3.8 or higher is required to run this art piece >:O!")

# ASCII logo, uses Colorama for coloring the logo.
logo = f"""
{Fore.RED}~~~~~~{Fore.LIGHTRED_EX}~~~~~~{Fore.YELLOW}~~~~~~{Fore.GREEN}~~~~~~{Fore.BLUE}~~~~~~{Fore.MAGENTA}~~~~~~
{Fore.RED}~~~~~~{Fore.LIGHTRED_EX}~~~~~~{Fore.YELLOW}~~~~~~{Fore.GREEN}~~~~~~{Fore.BLUE}~~~~~~{Fore.MAGENTA}~~~~~~
{Fore.RED}~~~~~~{Fore.LIGHTRED_EX}~~~~~~{Fore.YELLOW}~~~~~~{Fore.GREEN}~~~~~~{Fore.BLUE}~~~~~~{Fore.MAGENTA}~~~~~~
{Fore.RED}~~~~~~{Fore.LIGHTRED_EX}~~~~~~{Fore.YELLOW}~~~~~~{Fore.GREEN}~~~~~~{Fore.BLUE}~~~~~~{Fore.MAGENTA}~~~~~~
{Fore.RED}~~~~~~{Fore.LIGHTRED_EX}~~~~~~{Fore.YELLOW}~~~~~~{Fore.GREEN}~~~~~~{Fore.BLUE}~~~~~~{Fore.MAGENTA}~~~~~~
{Fore.RED}~~~~~~{Fore.LIGHTRED_EX}~~~~~~{Fore.YELLOW}~~~~~~{Fore.GREEN}~~~~~~{Fore.BLUE}~~~~~~{Fore.MAGENTA}~~~~~~{Fore.RESET}
"""
