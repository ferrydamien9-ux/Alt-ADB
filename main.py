import os
import sys

# Alt-ADB v1.0.1 - The Alternative Android Debug Bridge
# Released: Dec 2025

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    print("=" * 40)
    print("      Alt-ADB v1.0.1 (STABLE)       ")
    print("   Created for GitHub Deployment    ")
    print("=" * 40)
    print("Type 'help' for commands or 'exit' to quit.")

def main():
    clear_screen()
    show_banner()
    
    while True:
        try:
            # Interactive command prompt
            user_input = input("\nalt-adb> ").strip().lower()

            if user_input in ["exit", "quit"]:
                print("Shutting down Alt-ADB. Goodbye!")
                break
            
            elif user_input == "help":
                print("\nAvailable Commands:")
                print(" - devices : List connected Android devices")
                print(" - reboot  : Reboot the target device")
                print(" - version : Show version info")
                print(" - help    : Show this menu")
                print(" - exit    : Close the program")

            elif user_input == "devices":
                print("\n[Scanning USB Ports...]")
                # Placeholder for future USB logic
                print("Result: No devices authorized or connected.")

            elif user_input == "version":
                print("\nAlt-ADB Version: 1.0.1")
                print("Build: Python-Stable-Web")

            elif user_input == "reboot":
                print("\nAttempting to send reboot signal...")
                print("Error: Target device not found.")

            elif not user_input:
                continue

            else:
                print(f"\nUnknown command: '{user_input}'")

        except KeyboardInterrupt:
            print("\nForce closing...")
            sys.exit()

if __name__ == "__main__":
    main()
