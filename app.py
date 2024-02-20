import os, time, shutil, itertools, string
from colorama import Fore, Style
from pykeepass import PyKeePass

clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')

def BreakKeePass(database_path:str, database_password:str):
    try:
        kp = PyKeePass(database_path, password=database_password)
        print(f"{Fore.GREEN}Cracked - {Style.BRIGHT}{database_password}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}{e} - {Style.BRIGHT}{database_password}{Style.RESET_ALL}")

def BruteForce(charset, maxlength):
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
        for i in range(1, maxlength + 1)))

class Crack:
    def __init__(self, database_path:str):
        self.database_path = database_path
    def wordlists(self, wordlist_path:str):
        with open(wordlist_path,'r') as f:
            passwords = f.read().splitlines()
        print(f"{Fore.YELLOW}Loaded {Style.BRIGHT}{len(passwords)} passwords{Style.RESET_ALL}")
        threads = []
        for password in passwords:
            BreakKeePass(self.database_path, password)
    def brute_force(self):
        for attempt in BruteForce(string.ascii_lowercase+string.ascii_uppercase+string.digits, 10):
            BreakKeePass(self.database_path, attempt)


if __name__ == '__main__':
    clear()
    print(f"""
{Fore. LIGHTGREEN_EX}
 ██ ▄█▀▓█████ ▓█████  ▄████▄   ██▀███   ▄▄▄       ▄████▄   ██ ▄█▀
 ██▄█▒ ▓█   ▀ ▓█   ▀ ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ 
▓███▄░ ▒███   ▒███   ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ 
▓██ █▄ ▒▓█  ▄ ▒▓█  ▄ ▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ 
▒██▒ █▄░▒████▒░▒████▒▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
▒ ▒▒ ▓▒░░ ▒░ ░░░ ▒░ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
░ ░▒ ▒░ ░ ░  ░ ░ ░  ░  ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
░ ░░ ░    ░      ░   ░          ░░   ░   ░   ▒   ░        ░ ░░ ░ 
░  ░      ░  ░   ░  ░░ ░         ░           ░  ░░ ░      ░  ░   
                     ░                           ░               
{Fore.GREEN}KeeCrack is an open sourced tool made by {Style.BRIGHT}@r4shsec{Style.RESET_ALL+Fore.GREEN} to crack the KeepassXC passwords.{Fore.RESET}
{Fore.GREEN}Move the {Style.BRIGHT}.kdbx{Style.RESET_ALL+Fore.GREEN} file to {Style.BRIGHT}ImportedDatabases{Style.RESET_ALL+Fore.GREEN} to start{Fore.RESET}
                     """)
    files = []
    db_files = os.listdir('ImportedDatabases')
    for db in db_files:
        if db.endswith('.kdbx'):
            files.append(db)
    print(f"\n{Fore.BLUE}[ SELECT ]\n{Fore.RESET}")
    amount = 0
    for file in files:
        amount += 1
        print(f"{Fore.GREEN}[{amount}] {Style.BRIGHT}{file}{Style.RESET_ALL}")
    select = int(input(f"\n{Fore.BLUE}SELECT > "))
    if select > amount:
        print(f"{Fore.RED}Invalid Option!{Fore.RESET}")
    else:
        database_file = f"ImportedDatabases/{files[select-1]}"
        print(f"{Fore.BLUE}SELECTED {Style.BRIGHT}{database_file}{Style.RESET_ALL}")
        KeePassXCCrack = Crack(database_file)
        print(f"\n{Fore.BLUE}[ SELECT ]\n{Fore.RESET}")
        print(f"{Fore.GREEN}[1] {Style.BRIGHT}Brute Force{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[2] {Style.BRIGHT}Wordlists{Style.RESET_ALL}")
        bruteforce_option = int(input(f"\n{Fore.BLUE}SELECT > "))
        if bruteforce_option == 2:
            wordlists = os.listdir('list')
            print(f"{Fore.BLUE}[ SELECT ]\n{Fore.RESET}")
            wordlist_list = []
            for wordlist in wordlists:
                if wordlist.endswith('.txt'):
                    wordlist_list.append(wordlist)
            zamount = 0
            for file in wordlist_list:
                zamount += 1
                print(f"{Fore.GREEN}[{zamount}] {Style.BRIGHT}{file}{Style.RESET_ALL}")
            wordlist_file = int(input(f"\n{Fore.BLUE}SELECT > "))
            selected_wordlist_file = f"list/{wordlist_list[wordlist_file-1]}"
            print(f"{Fore.BLUE}SELECTED {Style.BRIGHT}{selected_wordlist_file}{Style.RESET_ALL}")
            print(f"\n{Fore.GREEN}Starting Crack...{Fore.RESET}")
            KeePassXCCrack.wordlists(selected_wordlist_file)
        elif bruteforce_option == 1:
            KeePassXCCrack.brute_force()