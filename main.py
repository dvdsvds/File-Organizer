import customtkinter as ctk
from tkinter import filedialog, messagebox
import threading

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "core", "build", "Release"))

import fileorganizer  

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class FileOrganizerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("File Organizer")
        self.geometry("700x500")
        self.resizable(False, False)

        self.path_var = ctk.StringVar()
        self.path_entry = ctk.CTkEntry(self, width=535, textvariable=self.path_var, placeholder_text="폴더 경로를 선택하세요")
        self.path_entry.place(x=115, y=60)

        self.select_btn = ctk.CTkButton(self, text="폴더 선택", command=self.choose_folder, width=40)
        self.select_btn.place(x=50, y=60)

        self.run_btn = ctk.CTkButton(self, text="정리 시작", command=self.start_organize, width=600, height=40)
        self.run_btn.place(x=50, y=120)

        self.log_box = ctk.CTkTextbox(self, width=600, height=250)
        self.log_box.place(x=50, y=180)
        self.log_box.insert("end", "File Organizer Ready!\n")

        self.footer = ctk.CTkLabel(self, text="Made by dvdsvds", text_color="gray")
        self.footer.place(relx=0.5, rely=0.95, anchor="center")

    def choose_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.path_var.set(folder)

    def start_organize(self):
        folder = self.path_var.get()
        if not folder or not os.path.isdir(folder):
            messagebox.showwarning("경고", "유효한 폴더를 선택하세요!")
            return
        self.append_log(f"-> {folder}\n")
        threading.Thread(target=self.run_organize, args=(folder,), daemon=True).start()

    def run_organize(self, folder):
        try:
            fileorganizer.organize(folder)
            self.append_log("!\n")
        except Exception as e:
            self.append_log(f"오류 발생: {e}\n")

    def append_log(self, text):
        self.log_box.insert("end", text)
        self.log_box.see("end")

if __name__ == "__main__":
    app = FileOrganizerApp()
    app.mainloop()