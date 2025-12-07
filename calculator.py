import tkinter as tk

# Colors
dark_bg = '#2E2E2E'
dark_button = '#4A4A4A'
light_fg = '#FFFFFF'
light_bg = '#FFFFFF'
light_button = '#F0F0F0'
dark_fg = '#000000'

# Mode
mode = 'dark'

def apply_theme():
    global mode
    if mode == 'dark':
        bg = dark_bg
        btn_bg = dark_button
        fg = light_fg
    else:
        bg = light_bg
        btn_bg = light_button
        fg = dark_fg
    
    window.configure(bg=bg)
    layar.configure(bg=bg, fg=fg, insertbackground=fg)
    frame.configure(bg=bg)
    for btn in buttons:
        btn.configure(bg=btn_bg, fg=fg)
    btn_clear.configure(bg=btn_bg, fg=fg)
    btn_toggle.configure(bg=btn_bg, fg=fg)

def toggle_mode():
    global mode
    mode = 'light' if mode == 'dark' else 'dark'
    apply_theme()

def bttn(button):
    current = layar.get()
    layar.delete(0, tk.END)
    layar.insert(0, current + button)

def hitung():
    try:
        hasil = str(eval(layar.get()))
        layar.delete(0, tk.END)
        layar.insert(0, hasil)
    except:
        layar.delete(0,tk.END)
        layar.insert(0, "Error")

def clear():
    layar.delete(0, tk.END)

window = tk.Tk()
window.title("Kalkulator Sederhana by Gavel")
window.geometry("300x400")

window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)

layar = tk.Entry(window, font=("Monaco", 20), borderwidth=5, relief="ridge", justify="right")
layar.pack(fill="both", padx=10, pady=10)

frame = tk.Frame(window)
frame.pack()

button_list = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "=","0",".","+"
]

for r in range(4):
    frame.rowconfigure(r, weight=1)
for c in range(4):
    frame.columnconfigure(c, weight=1)

row = 0
col = 0
buttons = []

for t in button_list:
    action= (lambda x=t: bttn(x)) if t != "=" else hitung
    btn = tk.Button(frame, text=t, width=5, height=2, font=("Monaco", 18), command=action)
    btn.grid(row=row, column=col, padx=5, pady=5)
    buttons.append(btn)

    col+= 1
    if col == 4:
        row += 1
        col = 0

btn_clear = tk.Button(window, text="CLEAR", width=20, height=2, font=("Monaco", 14), command=clear)
btn_clear.pack(pady=10)

btn_toggle = tk.Button(window, text="Toggle Mode", width=20, height=2, font=("Monaco", 14), command=toggle_mode)
btn_toggle.pack(pady=10)

apply_theme()

window.mainloop()
