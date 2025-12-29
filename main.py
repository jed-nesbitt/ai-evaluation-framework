import tkinter as tk
from tkinter import messagebox

# Set up root window
root = tk.Tk()
root.title("AI Evaluation Framework")
root.geometry("1280x720")  # Wider window

# Style settings
FONT = ("Helvetica", 30)
BUTTON_STYLE = {"font": FONT, "width": 25, "height": 3, "padx": 10, "pady": 10}

def add_restart_button():
    restart_btn = tk.Button(root, text="Restart", font=("Helvetica", 14), command=start_screen)
    restart_btn.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)  # Bottom-right corner with margin
    
def start_screen():
    clear_screen()
    label = tk.Label(root, text="Is the output specific and verifiable?", font=FONT)
    label.pack(pady=20)
    tk.Button(root, text="Yes", command=screen_2, **BUTTON_STYLE).pack(pady=10)
    tk.Button(root, text="No", command=lambda: show_message("Reprompt ask for sources or clasrification", start_screen), **BUTTON_STYLE).pack(pady=10)

def screen_2():
    clear_screen()
    label = tk.Label(root, text="Does the output cite credible sources?", font=FONT)
    label.pack(pady=20)
    tk.Button(root, text="Yes", command=screen_3, **BUTTON_STYLE).pack(pady=10)
    tk.Button(root, text="No", command=lambda: show_message("Possible misinformation or hallucination. Investigate claims manually.", screen_3), **BUTTON_STYLE).pack(pady=10)
    add_restart_button()

def screen_3():
    clear_screen()
    label = tk.Label(root, text="Can you cross-check the information with trusted sources?", font=FONT)
    label.pack(pady=20)
    tk.Button(root, text="Yes", command=lambda: show_message_good("Validate Claims",screen_4), **BUTTON_STYLE).pack(pady=10)
    tk.Button(root, text="No", command=lambda: show_message("Output may not be reliable", screen_4), **BUTTON_STYLE).pack(pady=10)
    add_restart_button()
    
def screen_4():
    clear_screen()
    label = tk.Label(root, text="Is there internal logic and consistency in the output?", font=FONT)
    label.pack(pady=20)
    tk.Button(root, text="Yes", command=screen_5, **BUTTON_STYLE).pack(pady=10)
    tk.Button(root, text="No", command=lambda: show_message("Check for contradictions, ask AI to re-express or correct. Start again if necessary.", screen_5), **BUTTON_STYLE).pack(pady=10)
    add_restart_button()

def screen_5():
    clear_screen()
    label = tk.Label(root, text="Does the output cover major counterarguments or uncertainties?", font=FONT)
    label.pack(pady=20)
    tk.Button(root, text="Yes", command=screen_6, **BUTTON_STYLE).pack(pady=10)
    tk.Button(root, text="No", command=lambda: show_message("Potential Bias. Start again if necessary", screen_5), **BUTTON_STYLE).pack(pady=10)
    add_restart_button()

def screen_6():
    clear_screen()
    label = tk.Label(root, text="Does the output oversimplify the issue?", font=FONT)
    label.pack(pady=20)
    tk.Button(root, text="Yes", command=lambda: show_message("Ask for nuanc to dive deeper", screen_7), **BUTTON_STYLE).pack(pady=10)
    tk.Button(root, text="No", command=screen_7, **BUTTON_STYLE).pack(pady=10)
    add_restart_button()

def screen_7():
    clear_screen()
    label = tk.Label(root, text="Could the AI be mirroring online bias?", font=FONT)
    label.pack(pady=20)
    tk.Button(root, text="Yes", command=lambda: show_message("Be Skeptical, AI could be reflecting training data and not the truth", screen_8), **BUTTON_STYLE).pack(pady=10)
    tk.Button(root, text="No", command=lambda: show_message_good("More likely to be balanced",screen_8 ), **BUTTON_STYLE).pack(pady=10)
    add_restart_button()

def screen_8():
    clear_screen()
    label = tk.Label(root, text="Thank you, please press restart or reset the page to start again", font=FONT)
    label.pack(pady=100)
    add_restart_button()
    
def show_message(message, retry_func):
    messagebox.showinfo("Be Careful", message)
    retry_func()
    
def show_message_good(message, retry_func):
    messagebox.showinfo("Good", message)
    retry_func()

def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

start_screen()
root.mainloop()
