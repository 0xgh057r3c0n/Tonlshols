import os
import sys

def print_banner():
    print("  _______          _       _           _        ")
    print(" |__   __|        | |     | |         | |       ")
    print("    | | ___  _ __ | | ___ | |__   ___ | | ___   ")
    print("    | |/ _ \| '_ \| |/ __|| '_ \ / _ \| |/ __|  ")
    print("    | | (_) | | | | |\__ \| | | | (_) | |\__ \  ")
    print("    |_|\___/|_| |_|_||___/(_)_|_|\___/|_||___/  ")
    print("                                                ")
    print("  Port Forwarding Tool using Serveo.net         ")
    print("  Author: G4UR4V007                             ")
    print("  Version: 1.0                                 ")

def get_user_input():
    print("Select the protocol to forward:")
    print("1. TCP")
    print("2. HTTP")
    choice = input("Enter your choice (1/2): ")
    if choice == "1":
        protocol = "tcp"
    elif choice == "2":
        protocol = "http"
    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)

    port = input("Enter the local port to forward: ")

    return protocol, port

def create_tunnel(protocol, port):
    if protocol == "tcp":
        os.system(f"ssh -R 4444:localhost:{port} serveo.net")
    elif protocol == "http":
        os.system(f"ssh -R 80:localhost:{port} serveo.net")

def main():
    print_banner()
    protocol, local_port = get_user_input()
    create_tunnel(protocol, local_port)

if __name__ == "__main__":
    main()
    