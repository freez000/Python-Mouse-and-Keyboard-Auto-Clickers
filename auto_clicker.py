import customtkinter
from pynput.mouse import Button, Controller
import time
import threading

root = customtkinter.CTk()
root.geometry("500x300")
root.title("Simple AutoClicker in Python -- By freez (bwzv)")

mouse = Controller()
chek_var = customtkinter.StringVar(value="off")
is_running = False 

def auto_clicker():
    global is_running
    is_running = True
    while chek_var.get() == "on" and is_running:
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(1 / int(slide_bar_CPS.get()))  
    is_running = False 

def callback(choice=None):
    global is_running
    value_slider = int(slide_bar_CPS.get())
    label_CPS.configure(text=f"CPS: {value_slider}")
    
    if choice is None:
        choice = rolle_menu_var.get()
    
    if chek_var.get() == "on" and not is_running:
        time.sleep(1)
        threading.Thread(target=auto_clicker, daemon=True).start()
    
    elif chek_var.get() == "off":
        is_running = False 

rolle_menu_var = customtkinter.StringVar(value="Left Click")
rolle_menu = customtkinter.CTkOptionMenu(
    master=root,
    values=["Left Click", "Right Click"],
    command=callback,
    variable=rolle_menu_var
)
rolle_menu.pack(pady=10)

slide_bar_CPS = customtkinter.CTkSlider(
    master=root,
    from_=1,
    to=50,
    number_of_steps=49,
    command=callback
)
slide_bar_CPS.pack(pady=10)

label_CPS = customtkinter.CTkLabel(master=root, text=f"CPS: 25")
label_CPS.pack(pady=2)

chekbox_autoclick = customtkinter.CTkCheckBox(
    master=root,
    text="Activate Auto Clicker",
    command=callback,
    variable=chek_var,
    onvalue="on",
    offvalue="off"
)
chekbox_autoclick.pack(pady=10)

root.mainloop()
