from tkinter import *
import datetime
from get_crypto_price import get_btc_inr, get_doge_inr, get_eth_inr

root = Tk()
root.title('Crypto Price Tracker')
root.geometry(f'200x200+{root.winfo_screenwidth()-200}+0')    #'w+h+x+y'
root.configure(bg='black')

time = Label(root)
time.configure(foreground='white', background='black')
time.pack()

btc = Label(root)
btc.configure(background='black')
btc.pack()

eth = Label(root)
eth.configure(background='black')
eth.pack()

doge = Label(root)
doge.configure(background='black')
doge.pack()


def clock():
    text = datetime.datetime.now().strftime("Time: %H:%M:%S")
    time.config(text=text)
    root.after(1000, clock)

def btc_crypto_price_show():
    price = get_btc_inr()
    text = f"BTC-INR - Rs. {price}"
    print(text)
    btc.config(text=text)
    btc.configure(foreground='white')
    root.after(15000)

def eth_crypto_price_show():
    price = get_eth_inr()
    text = f"ETH-INR - Rs. {price}"
    print(text)
    eth.config(text=text)
    eth.configure(foreground='white')
    root.after(15000)

def doge_crypto_price_show():
    price = get_doge_inr()
    text = f"DOGE-INR - Rs. {price}"
    print(text)
    doge.config(text=text)
    doge.configure(foreground='white')
    root.after(15000)

# run first time
clock()
btc_crypto_price_show()
eth_crypto_price_show()
doge_crypto_price_show()

root.mainloop()