from tkinter import *
from datetime import datetime
from get_ticker_price import get_ticker_price
from ctypes import windll
from read_tickers import read_tickers
from concurrent.futures import ThreadPoolExecutor, as_completed

myappid = "dhruv_padhiyar_crypto_price_tracker_v01"  # arbitrary string
windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

root = Tk()
root.title("Crypto Price Tracker")
root.geometry(f"200x200+{root.winfo_screenwidth()-200}+0")  #'w+h+x+y'
root.configure(bg="black")
root.attributes("-topmost", True)
root.iconbitmap("readme_assets/favicon.ico")

time = Label(root, foreground="white", background="black", font=("Arial", 14))
time.pack()


def clock():
    text = datetime.now().strftime("Time: %H:%M:%S")
    time.config(text=text)
    root.after(1000, clock)


tickers = read_tickers()
crypto_labels = {
    ticker: Label(root, background="black", text=ticker, foreground="white")
    for ticker in tickers
}


def show_ticker_price():
    with ThreadPoolExecutor(max_workers=10) as e:
        future_to_url = {
            e.submit(get_ticker_price, ticker): ticker for ticker in tickers
        }
        for future in as_completed(future_to_url):
            data = future.result()
            ticker = data["quoteResponse"]["result"][0]["symbol"]
            regularMarketPrice = round(
                data["quoteResponse"]["result"][0]["regularMarketPrice"], 2
            )
            regularMarketChangePercent = round(
                data["quoteResponse"]["result"][0]["regularMarketChangePercent"], 2
            )
            crypto_labels[ticker].pack()
            if regularMarketChangePercent > 0:
                background = "green"
            else:
                background = "red"

            crypto_labels[ticker].config(
                text=f"{ticker} Rs. {regularMarketPrice} {regularMarketChangePercent}%",
                background=background,
            )

    root.after(10000, show_ticker_price)


clock()
show_ticker_price()

root.mainloop()
