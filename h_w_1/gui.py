import tkinter as tk
from tkinter import scrolledtext

class GUI:
    def __init__(self, hostname, command_handler):
        self.hostname = hostname
        self.command_handler = command_handler
        self.window = tk.Tk()
        self.window.title(f"{hostname} Shell Emulator")

        self.text_area = scrolledtext.ScrolledText(self.window, width=80, height=20)
        self.text_area.pack()

        self.entry = tk.Entry(self.window, width=80)
        self.entry.pack()
        self.entry.bind('<Return>', self.execute_command)

    def execute_command(self, event):
        command = self.entry.get()
        self.text_area.insert(tk.END, f"{self.hostname}: {command}\n")
        self.entry.delete(0, tk.END)

        try:
            if command.startswith("ls"):
                output = self.command_handler.ls()
                self.text_area.insert(tk.END, "\n".join(output) + "\n")
            elif command.startswith("cd"):
                _, dir_name = command.split()
                self.command_handler.cd(dir_name)
            elif command.startswith("rmdir"):
                _, dir_name = command.split()
                self.command_handler.rmdir(dir_name)
            elif command.startswith("rm"):
                _, file_name = command.split()
                self.command_handler.rm(file_name)
            elif command == "exit":
                self.command_handler.exit()
            else:
                self.text_area.insert(tk.END, "Unknown command\n")
        except Exception as e:
            self.text_area.insert(tk.END, str(e) + "\n")

    def run(self):
        self.window.mainloop()
