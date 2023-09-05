from data_py.gui.main_window import Mywindow

def main():
    app = QApplication(sys.argv)
    window = Mywindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()