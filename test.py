import tkinter as tk
import tkinter as ttk
import requests
from bs4 import BeautifulSoup

win = tk.Tk()
win.title("Tracker")
win.geometry("220x300+100+100")

# lable creation
lable = ttk.Label(win, text='Stock name:')
lable.grid(row=0, column=0, sticky=tk.W)

#    lable1 = ttk.Label(win, text='Second')
#   lable1.grid(row=1, column=0, sticky=tk.W)
# entry box creation
stock_name = ttk.StringVar()
entrybox_lab = ttk.Entry(win, width=16, textvariable=stock_name)
entrybox_lab.focus()
entrybox_lab.grid(row=0, column=1)

lable1 = ttk.Label(win, text='Stock Price:')
lable1.grid(row=3, column=0, sticky=tk.W)

res = ttk.Label(win, text="")
res.grid(row=3, column=1)


def action():
    global latest_price
    name = stock_name.get()
    # print(name)
    ##print("Working.....")
    ##name = "TATASTEEL"
    url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=' + str(name)
    # print(url)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
    response = requests.get(url, headers=headers)
    response
    # print("Working .....")

    soup = BeautifulSoup(response.text, 'html.parser')
    # print("Parsing Done .....")
    data_array = soup.find(id='responseDiv').getText().strip().split(":")
    type(data_array)
    # print(data_array)
    for item in data_array:
        if 'lastPrice' in item:
            index = data_array.index(item) + 1
            print("Index -> " + str(index))
            latest_price = data_array[index].split('"')[1]
            # print(latest_price)
            res.config(text=latest_price)


entrybox_lab.delete(0, tk.END)
btn = ttk.Button(win, text="SEARCH", command=action)
btn.grid(row=1, column=1)

cal1 = ttk.Label(win, text='Old Price:')
cal1.grid(row=4, column=0, sticky=tk.W)

old = ttk.StringVar()
cal2 = ttk.Entry(win, width=16, textvariable=old)
cal2.grid(row=4, column=1)

cal3 = ttk.Label(win, text='Numbers:')
cal3.grid(row=5, column=0, sticky=tk.W)

num = ttk.StringVar()
cal4 = ttk.Entry(win, width=16, textvariable=num)
cal4.grid(row=5, column=1)

profit = ttk.Label(win, text='Profit')
profit.grid(row=7, column=0, sticky=tk.W)

res1 = ttk.Label(win, text="")
res1.grid(row=7, column=1)

profitp = ttk.Label(win, text='Profit Percent')
profitp.grid(row=8, column=0, sticky=tk.W)

res2 = ttk.Label(win, text="")
res2.grid(row=8, column=1)


def calculate():
    o_price = old.get()
    number = num.get()
    n = int(number)
    op = float(o_price)
    latest=float(latest_price)
    lp=(latest-op)*n
    per=((latest-op)/op)*100
    lp1 = '{:.2f}'.format(lp)
    per1='{:.2f}'.format(per)
    res1.config(text=lp1)
    res2.config(text=per1)


btn1 = ttk.Button(win, text="Calculate", command=calculate)
btn1.grid(row=6, column=1)

win.mainloop()
