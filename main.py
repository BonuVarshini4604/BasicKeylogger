
import tkinter as tk
from tkinter import messagebox
from pathlib import Path

from logger_utils import (
    validate_sample,
    append_record,
    read_log,
    delete_log as remove_log_file,
)

LOG_FILE = Path(__file__).with_name("test_log.txt")

BG = "#0B1220"
PANEL = "#142238"
INPUT_BG = "#0A1728"
TEXT = "#E7EEF8"
MUTED = "#9AABC2"
TEAL = "#43D9B5"
RED = "#FF6B79"
BLUE = "#4B8DFF"
BORDER = "#263B56"

session_active = False


def make_button(parent, label, command, color=TEAL, foreground=BG):
    return tk.Button(
        parent,
        text=label,
        command=command,
        bg=color,
        fg=foreground,
        activebackground=color,
        activeforeground=foreground,
        relief="flat",
        bd=0,
        padx=13,
        pady=10,
        cursor="hand2",
        font=("Segoe UI", 9, "bold"),
    )


def start_session():
    global session_active
    session_active = True

    text_box.config(state="normal")
    status_label.config(text="● ACTIVE", fg=TEAL)
    start_button.config(state="disabled")
    stop_button.config(state="normal")
    save_button.config(state="normal")
    activity_label.config(text="Session started. Enter sample text.")


def stop_session():
    global session_active
    session_active = False

    text_box.config(state="disabled")
    status_label.config(text="● STOPPED", fg=RED)
    start_button.config(state="normal")
    stop_button.config(state="disabled")
    save_button.config(state="disabled")
    activity_label.config(text="Session stopped. Input is disabled.")


def save_record():
    if not session_active:
        messagebox.showwarning(
            "Session stopped", "Click Start before saving."
        )
        return

    sample = text_box.get("1.0", "end-1c")

    if not validate_sample(sample):
        messagebox.showwarning(
            "Empty input", "Enter sample text before saving."
        )
        return

    try:
        append_record(LOG_FILE, sample)
        activity_label.config(text="Test record saved successfully.")
        messagebox.showinfo("Success", "Your test record was saved.")
        text_box.delete("1.0", "end")
    except (OSError, ValueError) as error:
        messagebox.showerror("Save error", str(error))


def view_log():
    try:
        content = read_log(LOG_FILE)

        viewer = tk.Toplevel(root)
        viewer.title("Session History")
        viewer.geometry("580x380")
        viewer.configure(bg=BG)

        tk.Label(
            viewer,
            text="SAVED TEST RECORDS",
            bg=BG,
            fg=TEAL,
            font=("Segoe UI", 14, "bold"),
        ).pack(anchor="w", padx=18, pady=(18, 8))

        output = tk.Text(
            viewer,
            bg=INPUT_BG,
            fg=TEXT,
            insertbackground=TEXT,
            selectbackground=BLUE,
            font=("Consolas", 10),
            wrap="word",
            relief="flat",
            padx=12,
            pady=12,
        )
        output.pack(fill="both", expand=True, padx=18, pady=(0, 18))
        output.insert("1.0", content or "No saved records yet.")
        output.config(state="disabled")

    except OSError as error:
        messagebox.showerror("Read error", str(error))


def delete_saved_log():
    if not messagebox.askyesno(
        "Confirm deletion",
        "Delete all saved demonstration records?",
    ):
        return

    try:
        remove_log_file(LOG_FILE)
        activity_label.config(text="Saved records deleted.")
        messagebox.showinfo("Deleted", "The test log has been deleted.")
    except OSError as error:
        messagebox.showerror("Delete error", str(error))


def clear_input():
    if session_active:
        text_box.delete("1.0", "end")
        activity_label.config(text="Test input cleared.")


def close_app():
    stop_session()
    root.destroy()


# Main window
root = tk.Tk()
root.title("Keyboard Event Lab | Cybersecurity")
root.geometry("760x650")
root.minsize(650, 590)
root.configure(bg=BG)

# Header
header = tk.Frame(root, bg=BG)
header.pack(fill="x", padx=28, pady=(24, 16))

tk.Label(
    header,
    text="◈  CYBER LAB",
    bg=BG,
    fg=TEAL,
    font=("Segoe UI", 10, "bold"),
).pack(anchor="w")

tk.Label(
    header,
    text="Keyboard Event Lab",
    bg=BG,
    fg=TEXT,
    font=("Segoe UI", 25, "bold"),
).pack(anchor="w", pady=(8, 3))

tk.Label(
    header,
    text="Consent-based input logging demonstration",
    bg=BG,
    fg=MUTED,
    font=("Segoe UI", 10),
).pack(anchor="w")

# Main panel
panel = tk.Frame(
    root, bg=PANEL, highlightbackground=BORDER, highlightthickness=1
)
panel.pack(fill="both", expand=True, padx=28, pady=5)

status_row = tk.Frame(panel, bg=PANEL)
status_row.pack(fill="x", padx=20, pady=(20, 8))

tk.Label(
    status_row,
    text="SESSION STATUS",
    bg=PANEL,
    fg=MUTED,
    font=("Segoe UI", 9, "bold"),
).pack(side="left")

status_label = tk.Label(
    status_row,
    text="● STOPPED",
    bg=PANEL,
    fg=RED,
    font=("Segoe UI", 10, "bold"),
)
status_label.pack(side="right")

tk.Label(
    panel,
    text="TEST INPUT",
    bg=PANEL,
    fg=TEXT,
    font=("Segoe UI", 10, "bold"),
).pack(anchor="w", padx=20, pady=(12, 7))

text_box = tk.Text(
    panel,
    height=9,
    bg=INPUT_BG,
    fg=TEXT,
    insertbackground=TEAL,
    selectbackground=BLUE,
    font=("Consolas", 11),
    wrap="word",
    relief="flat",
    padx=12,
    pady=12,
    state="disabled",
)
text_box.pack(fill="both", expand=True, padx=20, pady=(0, 12))

tk.Label(
    panel,
    text="Only text entered in this field can be recorded.",
    bg=PANEL,
    fg=MUTED,
    font=("Segoe UI", 9),
).pack(anchor="w", padx=20, pady=(0, 12))

# Session controls
controls = tk.Frame(panel, bg=PANEL)
controls.pack(fill="x", padx=16, pady=5)

start_button = make_button(
    controls, "▶  Start", start_session, color=TEAL
)
start_button.pack(side="left", padx=4)

stop_button = make_button(
    controls, "■  Stop", stop_session, color=RED
)
stop_button.pack(side="left", padx=4)
stop_button.config(state="disabled")

save_button = make_button(
    controls, "Save Record", save_record, color=BLUE, foreground="white"
)
save_button.pack(side="left", padx=4)
save_button.config(state="disabled")

# Utility controls
utilities = tk.Frame(panel, bg=PANEL)
utilities.pack(fill="x", padx=16, pady=(8, 12))

make_button(
    utilities, "Clear Input", clear_input,
    color="#31445F", foreground=TEXT
).pack(side="left", padx=4)

make_button(
    utilities, "View Log", view_log,
    color="#31445F", foreground=TEXT
).pack(side="left", padx=4)

make_button(
    utilities, "Delete Log", delete_saved_log,
    color="#66313D", foreground="white"
).pack(side="left", padx=4)

# Footer
activity_label = tk.Label(
    root,
    text="Ready. Start a session to begin your demonstration.",
    bg=BG,
    fg=MUTED,
    font=("Segoe UI", 9),
    anchor="w",
)
activity_label.pack(fill="x", padx=30, pady=(12, 4))

tk.Label(
    root,
    text="PRIVACY FIRST  •  LOCAL DEMO  •  NO SYSTEM-WIDE MONITORING",
    bg=BG,
    fg=TEAL,
    font=("Segoe UI", 8, "bold"),
).pack(pady=(4, 18))

root.protocol("WM_DELETE_WINDOW", close_app)
root.mainloop()
