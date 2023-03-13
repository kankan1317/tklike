""" This library supports the development of GUI applications using Python's tkinter. """

# importing tkinter module
import tkinter as tk

__all__ = [

]

class window:
    """make a window"""

    ### class variable ###
    __is_firstWindow : bool = True

    def __init__(self, title:str, width=None, height=None): ...