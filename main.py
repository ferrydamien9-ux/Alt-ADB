import adbutils
import sys
from pprint import pprint

def get_device_manager():
    """Initializes the ADB client."""
    try:
        return adbutils.AdbClient(host="127.0.0.1", port=5037)
    except Exception as e:
        print(f"Error: Could not connect to ADB server. Is it running?\n{e}")
        sys.exit(1)

def list_connected_devices(adb):
    """Prints a clean list of connected devices with UX in mind."""
    devices = adb.device_list()
    
    if not devices:
        print(" [!] No devices found. Please connect a device and enable USB Debugging.")
        return []

    print(f" [+] Found {len(devices)} device(s):")
    print("-" * 40)
    for i, dev in enumerate(devices, 1):
        # Fetching model info for better UX than just a serial number
        model = dev.prop.model if dev.prop.model else "Unknown Model"
        print(f"{i}. [{dev.serial}] - {model}")
    print("-" * 40)
    return devices

def main():
    print("--- Alt-ADB Management Tool ---")
    adb = get_device_manager()
    devices = list_connected_devices(adb)

    if devices:
        # Example: Perform an action on the first device found
        target_device = devices[0]
        print(f"Selected: {target_device.serial}")
        
        # Uncomment the line below to take a screenshot as a test
        # target_device.screenshot().save("debug_screen.png")
        # print("Task Complete: Screenshot saved.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting Alt-ADB...")
        sys.exit(0)
        
