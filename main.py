import subprocess

class AltADBLogic:
    def check_connection(self):
        """Checks if a device is actually connected via ADB."""
        try:
            result = subprocess.check_output(["adb", "devices"]).decode("utf-8")
            devices = [line for line in result.split('\n') if line.strip() and "List" not in line]
            return len(devices) > 0
        except Exception:
            return False

    def run_command(self, cmd):
        """Generic runner for ADB commands with error handling."""
        if not self.check_connection():
            return "Error: No device found. Check Wireless Debugging."
        try:
            # Using 'shell=True' can be risky, but for local ADB tools it's often necessary
            process = subprocess.Popen(f"adb {cmd}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process.communicate()
            return out.decode("utf-8") if out else err.decode("utf-8")
        except Exception as e:
            return str(e)
