import subprocess
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

# Setting a dark background for the whole window
Window.clearcolor = get_color_from_hex('#0A0A0A')

class AltADB_GUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 15

        # --- HEADER ---
        self.add_widget(Label(
            text="ALT-ADB [v0.2 ALPHA]",
            font_size='28sp',
            bold=True,
            size_hint_y=None,
            height=50,
            color=get_color_from_hex('#FFFFFF')
        ))

        # --- TERMINAL OUTPUT AREA ---
        self.output_log = TextInput(
            text=">> System Ready. Awaiting ADB Command...\n",
            readonly=True,
            background_color=get_color_from_hex('#121212'),
            foreground_color=get_color_from_hex('#00FF41'), # Classic Terminal Green
            font_name='Courier', # Monospace font for alignment
            size_hint_y=0.5
        )
        self.add_widget(self.output_log)

        # --- BUTTON GRID ---
        button_layout = BoxLayout(orientation='vertical', spacing=10, size_hint_y=0.4)

        # Check Connection Button
        btn_check = Button(
            text="CHECK CONNECTED DEVICES",
            background_normal='',
            background_color=get_color_from_hex('#222222'),
            color=get_color_from_hex('#00D4FF') # Cyan text
        )
        btn_check.bind(on_release=lambda x: self.run_adb("devices"))
        button_layout.add_widget(btn_check)

        # List Packages Button
        btn_list = Button(
            text="LIST INSTALLED APPS",
            background_normal='',
            background_color=get_color_from_hex('#222222')
        )
        btn_list.bind(on_release=lambda x: self.run_adb("shell pm list packages -3")) # -3 shows user apps only
        button_layout.add_widget(btn_list)

        # Reboot Button (Danger Zone)
        btn_reboot = Button(
            text="REBOOT DEVICE",
            background_normal='',
            background_color=get_color_from_hex('#330000'), # Dark Red
            color=get_color_from_hex('#FF5555')
        )
        btn_reboot.bind(on_release=lambda x: self.run_adb("reboot"))
        button_layout.add_widget(btn_reboot)

        self.add_widget(button_layout)

    def run_adb(self, cmd):
        """Executes the ADB command and updates the terminal UI."""
        self.output_log.text += f">> adb {cmd}\n"
        
        try:
            # Running the command via subprocess
            # Note: On a real phone, 'adb' must be in the system path or LADB environment
            result = subprocess.run(
                ["adb"] + cmd.split(), 
                capture_output=True, 
                text=True, 
                timeout=5
            )
            
            if result.stdout:
                self.output_log.text += result.stdout + "\n"
            if result.stderr:
                self.output_log.text += "ERROR: " + result.stderr + "\n"
                
        except Exception as e:
            self.output_log.text += f"CRITICAL ERROR: {str(e)}\n"
            
        # Auto-scroll to bottom
        self.output_log.cursor = (0, len(self.output_log.text))

class AltADBApp(App):
    def build(self):
        self.title = "Alt-ADB"
        return AltADB_GUI()

if __name__ == '__main__':
    AltADBApp().run()
    
