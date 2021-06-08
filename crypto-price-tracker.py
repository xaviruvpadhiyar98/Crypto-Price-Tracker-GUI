from tkinter import *
import datetime
from get_crypto_price import get_ticker_prices

root = Tk()
root.title('Crypto Price Tracker')
root.geometry(f'200x200+{root.winfo_screenwidth()-200}+0')    #'w+h+x+y'
root.configure(bg='black')

time = Label(root)
time.configure(foreground='white', background='black')
time.pack()

crypto_prices = Label(root)
crypto_prices.configure(background='black')
crypto_prices.pack()

def clock():
    text = datetime.datetime.now().strftime("Time: %H:%M:%S")
    time.config(text=text)
    root.after(1000, clock)

def show_crypto_price():
    text = ''
    for k,v in get_ticker_prices().items():
        text += f"{k} - Rs. {round(v, 3)}\n"

    crypto_prices.config(text=text)
    crypto_prices.configure(foreground='white')
    root.after(30000, show_crypto_price)


clock()
show_crypto_price()

root.mainloop()