## DEV BY freez (bwzv) // github: https://github.com/freez000/Python-Auto-Clicker
import customtkinter
from pynput.mouse import Button, Controller
import time
import threading
import keyboard

root = customtkinter.CTk()
root.geometry("500x300")
root.title("Simple AutoClicker in Python -- By freez (bwzv)")

mouse = Controller()
check_var = customtkinter.StringVar(value="off")
check_var_k = customtkinter.StringVar(value="off")


def toggle_check_var():
    if check_var.get() == "on":
        check_var.set("off")
    else:
        check_var.set("on")

def toggle_check_var_k():
    if check_var_k.get() == "on":
        check_var_k.set("off")
    else:
        check_var_k.set("on")

#keyboard.add_hotkey("f4", toggle_check_var)
#keyboard.add_hotkey("f3", toggle_check_var_k)

is_running = False
is_running_k = False  

#----------------| Function Auto Clicker |----------------#
def auto_clicker_left_click():
    global is_running

    is_running = True

    while check_var.get() == "on" and is_running:
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(1 / int(slide_bar_CPS.get())) 

    is_running = False  

def auto_clicker_right_click():
    global is_running

    is_running = True

    while check_var.get() == "on" and is_running:
        mouse.press(Button.right)
        mouse.release(Button.right)
        time.sleep(1 / int(slide_bar_CPS.get()))

    is_running = False
#---------------------------------------------------------#
###########################################################
#--------------| Function Keyboard Clicker |---------------#
def set_key_choice():
    global key_choice
    key_choice = get_key.get()

def Keyboard_auto_clicker():
    global is_running_k

    key_choice = get_key.get()

    is_running_k = True

    while check_var_k.get() == "on" and is_running_k:
        keyboard.press_and_release(key_choice)
        time.sleep(1 / int(slide_bar_KPS.get()))
        if check_var_k.get() == "off":
            break
    
    is_running_k = False
#---------------------------------------------------------#
###########################################################
#-------------------| Global Callback |-------------------#
def mouse_callback(choice=None):
    global is_running
    value_slider = int(slide_bar_CPS.get())
    label_CPS.configure(text=f"CPS: {value_slider}")
    
    if choice is None:
        choice = rolle_menu_var.get()
    
    if check_var.get() == "on" and not is_running and rolle_menu.get() == "Left Click":
        time.sleep(0.2)
        threading.Thread(target=auto_clicker_left_click, daemon=True).start()
    elif check_var.get() == "on" and not is_running and rolle_menu.get() == "Right Click":
        time.sleep(0.2)
        threading.Thread(target=auto_clicker_right_click, daemon=True).start()
    elif check_var.get() == "off":
        is_running = False

def Keyboard_callback(value_slider_=None):
    global is_running_k

    value_slider = int(slide_bar_KPS.get())
    label_KSP.configure(text=f"Keyboard click/s: {value_slider}")

    if check_var_k.get() == "on":
        if not is_running_k:
            time.sleep(0.2)
            threading.Thread(target=Keyboard_auto_clicker, daemon=True).start()
        else:
            pass
    elif check_var_k.get() == "off":
        is_running_k = False

def Settings_callback():
    mouse_set = Settings_var_mouse.get()
    Keyboard_set = Settings_var_Keyboard.get()

    keyboard.add_hotkey(f"{mouse_set}", toggle_check_var)
    keyboard.add_hotkey(f"{Keyboard_set}", toggle_check_var_k)
#---------------------------------------------------------#
###########################################################
#-----------------------| Tab View |----------------------#
tabview = customtkinter.CTkTabview(master=root)

tabview.add("Auto Clicker")
tabview.add("Keyboard Clicker")
tabview.add("Settings")
tabview.set("Auto Clicker")

tabview.pack()
#---------------------------------------------------------#
###########################################################
#-----------------| Auto Clicker Window |-----------------#
rolle_menu_var = customtkinter.StringVar(value="Left Click")
rolle_menu = customtkinter.CTkOptionMenu(
    master=tabview.tab("Auto Clicker"),
    values=["Left Click", "Right Click"],
    command=mouse_callback,
    variable=rolle_menu_var
)
rolle_menu.pack(pady=10)

slide_bar_CPS = customtkinter.CTkSlider(
    master=tabview.tab("Auto Clicker"),
    from_=1,
    to=50,
    number_of_steps=49,
    command=mouse_callback
)
slide_bar_CPS.pack(pady=10)

label_CPS = customtkinter.CTkLabel(master=tabview.tab("Auto Clicker"), text=f"CPS: 25")
label_CPS.pack(pady=2)

checkbox_autoclick = customtkinter.CTkCheckBox(
    master=tabview.tab("Auto Clicker"),
    text="Activate Auto Clicker (Default: F4)",
    command=mouse_callback,
    variable=check_var,
    onvalue="on",
    offvalue="off"
)
checkbox_autoclick.pack(pady=10)
#---------------------------------------------------------#
###########################################################
#---------------| Keyboard Clicker Window |----------------#
texte_input_key = customtkinter.CTkLabel(master=tabview.tab("Keyboard Clicker"), text="Enter your key (Juste enter one key)")

get_key = customtkinter.StringVar(value="e") 

input_key = customtkinter.CTkEntry(
    master=tabview.tab("Keyboard Clicker"), 
    placeholder_text="...", 
    width=25, 
    textvariable=get_key)

button_apply_Keyboard = customtkinter.CTkButton(master=tabview.tab("Keyboard Clicker"), text="Apply the key", command=set_key_choice)

texte_input_key.pack()
input_key.pack(pady=5)
button_apply_Keyboard.pack(pady=5)


slide_bar_KPS = customtkinter.CTkSlider(
    master=tabview.tab("Keyboard Clicker"),
    from_=1,
    to=50,
    number_of_steps=49,
    command=Keyboard_callback
)
slide_bar_KPS.pack(pady=2)

label_KSP = customtkinter.CTkLabel(master=tabview.tab("Keyboard Clicker"), text=f"Keyboard click/s: 25")
label_KSP.pack()

checkbox_Keyboardclicker = customtkinter.CTkCheckBox(
    master=tabview.tab("Keyboard Clicker"),
    text="Activate Keyboard AutoClicker (Default: F3)",
    onvalue="on",
    offvalue="off",
    command=Keyboard_callback,
    variable=check_var_k

)
checkbox_Keyboardclicker.pack(pady=2)
###########################################################
#-----------------------| Settings |----------------------#
label_Settings = customtkinter.CTkLabel(
    master=tabview.tab("Settings"),
    text="Settings",

)
label_Settings.pack()

label_mouse_settings = customtkinter.CTkLabel(master=tabview.tab("Settings"), text="Select your key for Mouse auto clicker:",)
Settings_var_mouse = customtkinter.StringVar(value="f4") # To change default value (f4) for activate/deactivate Mouse Auto clicker
Settings_start_key_mouse = customtkinter.CTkEntry(
    master=tabview.tab("Settings"),
    textvariable=Settings_var_mouse
)
label_mouse_settings.pack()
Settings_start_key_mouse.pack(pady=5)

label_Keyboard_settings = customtkinter.CTkLabel(master=tabview.tab("Settings"), text="Select your key for Keyboard auto clicker:",)
Settings_var_Keyboard = customtkinter.StringVar(value="f3") # To change default value (f3) for activate/deactivate Keyboard auto clicker
Settings_start_key_Keyboard = customtkinter.CTkEntry(
    master=tabview.tab("Settings"),
    textvariable=Settings_var_Keyboard
)
label_Keyboard_settings.pack()
Settings_start_key_Keyboard.pack(pady=5)

button_apply_settings = customtkinter.CTkButton(master=tabview.tab("Settings"), text="Apply Settings", command=Settings_callback)
button_apply_settings.pack(pady=2)

keyboard.add_hotkey(f"{Settings_start_key_mouse.get()}", toggle_check_var)
keyboard.add_hotkey(f"{Settings_start_key_Keyboard.get()}", toggle_check_var_k)

root.mainloop()

