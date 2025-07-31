import tkinter as tk
from tkinter import filedialog import messagebox
import zipfile
import os
import schedule
import threading
import time
from datetime import datetime

# Globals
scheduled = False
scheduler_thread = None
folder_path = ""
interval_minutes = 10

def zip_folder(folder_path, output_zip):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, start=folder_path)
                zipf.write(full_path, arcname)

def do_zip():
    if not os.path.isdir(folder_path):
        print("Folder path is invalid.")
        return
    output_name = f"{os.path.basename(folder_path)}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    output_path = os.path.join(os.path.dirname(folder_path), output_name)
    try:
        zip_folder(folder_path, output_path)
        print(f"[{datetime.now()}] Zipped to {output_path}")
    except Exception as e:
        print("Error:", e)

def browse_folder():
    global folder_path
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry_folder.delete(0, tk.END)
        entry_folder.insert(0, folder_path)

def start_schedule():
    global scheduled, scheduler_thread, interval_minutes, folder_path
    folder_path = entry_folder.get()
    try:
        interval_minutes = int(entry_interval.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Interval must be an integer.")
        return

    if not os.path.isdir(folder_path):
        messagebox.showerror("Error", "Please select a valid folder.")
        return

    schedule.clear()
    schedule.every(interval_minutes).minutes.do(do_zip)
    scheduled = True
    lbl_status.config(text=f"Scheduled every {interval_minutes} min")

    def run_schedule():
        while scheduled:
            schedule.run_pending()
            time.sleep(1)

    scheduler_thread = threading.Thread(target=run_schedule, daemon=True)
    scheduler_thread.start()

def stop_schedule():
    global scheduled
    scheduled = False
    schedule.clear()
    lbl_status.config(text="Schedule stopped")

# GUI Setup
root = tk.Tk()
root.title("Scheduled Folder Zipper")
root.geometry("450x250")
root.resizable(False, False)

tk.Label(root, text="Folder to Zip:", font=("Arial", 12)).pack(pady=5)
entry_folder = tk.Entry(root, width=50)
entry_folder.pack()
tk.Button(root, text="Browse", command=browse_folder).pack(pady=5)

tk.Label(root, text="Interval (minutes):", font=("Arial", 12)).pack()
entry_interval = tk.Entry(root, width=10)
entry_interval.insert(0, "10")
entry_interval.pack()

tk.Button(root, text="Start Scheduler", bg="green", fg="white", command=start_schedule).pack(pady=5)
tk.Button(root, text="Stop Scheduler", bg="red", fg="white", command=stop_schedule).pack(pady=5)

lbl_status = tk.Label(root, text="Schedule not started", fg="blue")
lbl_status.pack(pady=10)

root.mainloop()
