""" This library supports the development of GUI applications using Python's tkinter. """

# importing tkinter module
import tkinter as tk

import _baseWindow

__all__ = [

]

class window:
    """make a window"""

    ### class variable ###
    __is_firstWindow : bool = True

    def __init__(self, title:str, width:int, height=int, x:int=0, y:int=0):
        if window.__is_firstWindow == True:
            self.window = _baseWindow.mainWindow(title, width, height, x, y)
            window.__is_firstWindow = False
        else:
            self.window = _baseWindow.subWindow(title, width, height, x, y)
            window.__is_firstWindow = False