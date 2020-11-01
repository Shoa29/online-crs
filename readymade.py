import tkinter as tk
from tkinter import ttk


class PlaceholderEntry(ttk.Entry):
    def __init__(self, container, placeholder, *args, **kwargs):
        super().__init__(container, *args, style = "Placeholder.TEntry", **kwargs)
        self.placeholder = placeholder
        self.insert("0", self.placeholder)
        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)
    def _clear_placeholder(self, e):
        if self["style"] == "Placeholder.TEntry":
            self.delete("0", "end")
            self["style"] = "TEntry"
    def _add_placeholder(self,e):
        if not self.get():
            self.insert("0", self.placeholder)
            self["style"] = "Placeholder.TEntry"

root = tk.Tk()
style = ttk.Style(root)

style.configure("Placeholder.TEntry", foreground="#d5d5d5")

entry = PlaceholderEntry(root, "Sample placeholder")
entry.pack()

root.mainloop()