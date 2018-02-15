# https://api.cryptowat.ch/markets/gdax/ethusd/price
# {
#     "result":{"price":862.13},
#     "allowance":{"cost":991451,"remaining":7999008549}
# }

# import collections as col

import tkinter as tk
import time

def say_hi():
    pop_up = tk.Tk()
    pop_up.title = "Alert!"
    label = tk.Label(pop_up,
                     text='Hello World!!',
                     fg='blue')
    label.pack()
    button_ok = tk.Button(pop_up, text='Ok', command=pop_up.destroy)
    pop_up.mainloop()


# ================#
#     START       #
# ----------------#

window = tk.Tk()
window.title = "Tkinter Test :)"
button_yes = tk.Button(window, text='yes', command=say_hi())
button_yes.pack(side='LEFT')
button_quit = tk.Button(window, text='QUIT', command=window.destroy)
button_quit.pack(side='RIGHT')
window.mainloop()


# def get_price(label):
#     price = 894.23
#     text = "Current price: " + str(price)
#     label.config(text=text)
#
#
# window = tk.Tk()
# window.title = "Ticker Watcher"
# price = tk.Label(window)
# price.pack()
# get_price(price)
#
# button_start = tk.Button(window, text='Start', command=say_hi())
# button_yes.pack()
# button_quit = tk.Button(window, text='QUIT', command=window.destroy)
# button_quit.pack()
# window.mainloop()
