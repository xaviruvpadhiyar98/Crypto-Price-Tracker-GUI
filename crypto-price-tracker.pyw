from tkinter import *
from datetime import datetime
from get_latest_crypto_prices import get_latest_crypto_with_percentage
import ctypes

myappid = u'dhruv_padhiyar_crypto_price_tracker_v01' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

root = Tk()
root.title("Crypto Price Tracker")
root.geometry(f"200x200+{root.winfo_screenwidth()-200}+0")  #'w+h+x+y'
root.configure(bg="black")
root.attributes('-topmost',True)
root.iconbitmap('readme_assets/favicon.ico')

time = Label(root)
time.configure(foreground="white", background="black", font=('Arial', 14))
time.pack()

crypto_prices = Label(root)
crypto_prices.configure(background="black")
crypto_prices.pack()


def clock():
    text = datetime.now().strftime("Time: %H:%M:%S")
    time.config(text=text)
    root.after(1000, clock)

def show_crypto_price():
    text = ""
    for k, v in get_latest_crypto_with_percentage().items():
        text += f"{k} - Rs. {round(v['quoteResponse']['result'][0]['regularMarketPrice'], 3)} ({round(v['quoteResponse']['result'][0]['regularMarketChangePercent'],2)}%)\n"

    crypto_prices.config(text=text)
    if v["quoteResponse"]["result"][0]["regularMarketChangePercent"] > 0:
        crypto_prices.configure(foreground="green")
    else:
        crypto_prices.configure(foreground="red")
    root.after(30000, show_crypto_price)


clock()
show_crypto_price()

root.mainloop()
