import sys
from app.core.helpers.UI import UI


ui = UI()


def exit_program():
    ui.warn("Program exited...")
    sys.exit()