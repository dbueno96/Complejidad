import tkinter as tk
from ui.application import Application
from utils.constants import CONST_APP_TITLE





    

root = tk.Tk()
root.title(CONST_APP_TITLE)
app = Application(master=root)

app.mainloop()