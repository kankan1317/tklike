"""windowクラスの基底クラス"""

import tkinter as tk

class mainWindow:
    def __init__(self, title:str, width:int, height:int, x:int=0, y:int=0):
        self.master = tk.Tk()

        self.master.title(title)
        self.master.geometry(f"{width}x{height}+{x}+{y}")


class subWindow:
    def __init__(self, title:str, width:int, height:int, x:int=0, y:int=0):
        self.master = tk.Toplevel()

        self.master.title(title)
        self.master.geometry(f"{width}x{height}+{x}+{y}")