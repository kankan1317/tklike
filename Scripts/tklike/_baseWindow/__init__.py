"""windowクラスの基底クラス"""

import tkinter as tk

class mainWindow:
    def __init__(self, title:str, width:int, height:int):
        self.master = tk.Tk()

        self.master.title(title)
        self.master.geometry(f"{width}x{height}")


class subWindow:
    def __init__(self, title:str, width:int, height:int):
        self.master = tk.Toplevel()

        self.master.title(title)
        self.master.geometry(f"{width}x{height}")