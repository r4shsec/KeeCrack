# KeeCrack - KeePassXC Database Brute Forcer
KeePassXC is a safe way to store your login credentials. However, just because its a "safe" way to store your login credentials, doesn't mean you should use a weak database password to store your login credentials. 

Using a weak password may result in attackers having access to your login credentials. I made this script as a **proof of concept and for awareness**. 

## How?
- Your database file might be leaked to others if you run malware on your pc. 
- Your database file might be leaked to others if you send it to others.

## Social
[Github - @r4shsec](https://github.com/r4shsec)

[YouTube - @r4shsec](https://youtube.com/@r4shsec)

## Usage
1. Move your KeePassXC database to the "ImportedDatabase" folder
2. Move any existing wordlists to the "list" folder
### Installation
```console
git clone 
cd KeeCrack
pip install -r requirements.txt
python app.py
```

## Modes

1. Using a wordlist
> This uses a wordlist to sort through all the passwords till one is a match.
2. Brute Force
> Goes through 128 random passwords to determine the correct password to unlock the database. 
