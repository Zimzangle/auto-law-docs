from PyQt5.QtWidgets import QApplication
from data_py.gui.main_window import Mywindow
import traceback
import sys
import os

try:
    os.system('pip install -r data_py/requirements.txt')
    def main():
        app = QApplication(sys.argv)
        window = Mywindow(current_directory)
        window.show()
        sys.exit(app.exec_())

    if __name__ == "__main__":
        current_directory = os.getcwd()
        main()

except Exception as e:
    with open('error_log.txt', 'w') as log_file:
        log_file.write(traceback.format_exc())