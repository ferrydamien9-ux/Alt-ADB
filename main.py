import os
import sys
import subprocess

# Alt-ADB v1.5.0 - The "Bridge" Update
# Released: Jan 2026

def show_banner():
    print("=" * 45)
    print("      Alt-ADB v1.5.0 - BRIDGE UPDATE      ")
    print("   Full Command Execution Enabled (BETA)  ")
    print("=" * 45)

def run_adb(command):
    """Internal function to bridge Alt-ADB to the system ADB"""
    try:
        # This attempts to run the command through the system's PATH
        result = subprocess.run(['adb'] + command.split(), capture_output=True, text=True)
        if result.returncode == 0:
            print(result.stdout)
        else:
            print(f"ADB Error: {result.stderr}")
    except FileNotFoundError:
        print("Error: 'adb.exe' not found in system PATH.")
        print("Please install Android Platform Tools to use Bridge Mode.")

def main():
    show_banner()
    
    while True:
        try:
            user_input = input("\nalt-adb v1.5.0> ").strip()

            if user_input.lower() in ["exit", "quit"]:
                break
            
            elif user_input.lower() == "help":
                print("\nv1.5.0 Commands:")
                print(" - devices   : Show connected hardware")
                print(" - shell     : Enter device bash shell")
                print(" - logcat    : View real-time device logs")
                print(" - install   : Install an .apk (Usage: install app.apk)")
                print(" - exit      : Close Alt-ADB")

            # BRIDGE LOGIC: Directly passing commands to the bridge
            elif user_input.lower() == "devices":
                run_adb("devices")
            
            elif user_input.lower() == "shell":
                print("Entering remote shell... (Type 'exit' to return to Alt-ADB)")
                os.system("adb shell")

            elif user_input.lower().startswith("install "):
                apk_path = user_input.split(" ")[1]
                run_adb(f"install {apk_path}")

            elif not user_input:
                continue

            else:
                # If it's an unknown command, try passing it directly to ADB
                print(f"Forwarding '{user_input}' to system bridge...")
                run_adb(user_input)

        except KeyboardInterrupt:
            print("\nSession Terminated.")
            sys.exit()

if __name__ == "__main__":
    main()
