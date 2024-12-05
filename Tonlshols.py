import os
import sys

# Define color codes globally
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
RESET = "\033[0m"

def print_banner():
    print(f"{BLUE}  _______          _       _           _        {RESET}")
    print(f"{BLUE} |__   __|        | |     | |         | |       {RESET}")
    print(f"{GREEN}    | | ___  _ __ | | ___ | |__   ___ | | ___   {RESET}")
    print(f"{GREEN}    | |/ _ \| '_ \| |/ __|| '_ \ / _ \| |/ __|  {RESET}")
    print(f"{YELLOW}    | | (_) | | | | |\__ \| | | | (_) | |\__ \  {RESET}")
    print(f"{YELLOW}    |_|\___/|_| |_|_||___/(_)_|_|\___/|_||___/  {RESET}")
    print(f"{RESET}                                                ")
    print(f"{RED}  Port Forwarding Tool using Serveo.net         {RESET}")
    print(f"{RED}  Author: G4UR4V007                             {RESET}")
    print(f"{RED}  Version: 1.0                                 {RESET}")

def get_user_input():
    print(f"{GREEN}Select the protocol to forward:{RESET}")
    print(f"{YELLOW}1. TCP{RESET}")
    print(f"{YELLOW}2. HTTP{RESET}")
    choice = input(f"{RED}Enter your choice (1/2): {RESET}")
    if choice == "1":
        protocol = "tcp"
    elif choice == "2":
        protocol = "http"
    else:
        print(f"{RED}Invalid choice. Exiting.{RESET}")
        sys.exit(1)

    port = input(f"{RED}Enter the local port to forward: {RESET}")

    return protocol, port

def create_tunnel(protocol, port):
    if protocol == "tcp":
        print(f"{GREEN}Creating TCP tunnel...{RESET}")
        os.system(f"ssh -R 4444:localhost:{port} serveo.net")
    elif protocol == "http":
        print(f"{GREEN}Creating HTTP tunnel...{RESET}")
        os.system(f"ssh -R 80:localhost:{port} serveo.net")

def main():
    print_banner()
    protocol, local_port = get_user_input()
    create_tunnel(protocol, local_port)

if __name__ == "__main__":
    main()
