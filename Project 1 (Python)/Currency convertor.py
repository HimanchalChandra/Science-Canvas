import requests
import tkinter as tk

response = requests.get('http://apilayer.net/api/live?access_key=00e233ace670bd32eb417ca6a04424d7')
chk = response.json()
print (chk)

def do():
    input = w.get()
    fr1 = fr.get()
    to1 = to.get()
    div = chk['quotes']['USD'+fr1]
    newinput = input/div
    mult = chk['quotes']['USD'+to1]
    output = newinput*mult
    x = output
    print (x)
    tk.Label(root, text = x, bg = 'blue').grid(row=12, column=4, columnspan=4)
    return

root = tk.Tk()
root.geometry('350x350')
to = tk.StringVar()
fr = tk.StringVar()
w = tk.DoubleVar()
x = tk.DoubleVar()
tk.Radiobutton(root, text = 'USD', variable = fr, value = 'USD').grid(row = 2, column = 0)
tk.Radiobutton(root, text = 'USD',variable = to, value = 'USD').grid(row = 2, column = 4)
tk.Radiobutton(root, text = 'INR',variable = fr, value = 'INR').grid(row = 3, column = 0)
tk.Radiobutton(root, text = 'INR',variable = to, value = 'INR').grid(row = 3, column = 4)
tk.Radiobutton(root, text = 'POUNDS',variable = fr, value = 'GBP').grid(row = 4, column = 0)
tk.Radiobutton(root, text = 'POUNDS',variable = to, value = 'GBP').grid(row = 4, column = 4)
tk.Radiobutton(root, text = 'EURO',variable = fr, value = 'EUR').grid(row = 5, column = 0)
tk.Radiobutton(root, text = 'EURO',variable = to, value = 'EUR').grid(row = 5, column = 4)
tk.Radiobutton(root, text = 'YEN',variable = fr, value = 'JPY').grid(row = 6, column = 0)
tk.Radiobutton(root, text = 'YEN',variable = to, value = 'JPY').grid(row = 6, column = 4)
tk.Radiobutton(root, text = 'AUD',variable = fr, value = 'AUD').grid(row = 7, column = 0)
tk.Radiobutton(root, text = 'AUD',variable = to, value = 'AUD').grid(row = 7, column = 4)
tk.Radiobutton(root, text = 'CAD',variable = fr, value = 'CAD').grid(row = 8, column = 0)
tk.Radiobutton(root, text = 'CAD',variable = to, value = 'CAD').grid(row = 8, column = 4)
tk.Radiobutton(root, text = 'CNY',variable = fr, value = 'CNY').grid(row = 9, column = 0)
tk.Radiobutton(root, text = 'CNY',variable = to, value = 'CNY').grid(row = 9, column = 4)
tk.Radiobutton(root, text = 'CHF',variable = fr, value = 'CHF').grid(row = 10, column = 0)
tk.Radiobutton(root, text = 'CHF',variable = to, value = 'CHF').grid(row = 10, column = 4)
tk.Radiobutton(root, text = 'SGD',variable = fr, value = 'SGD').grid(row = 11, column = 0)
tk.Radiobutton(root, text = 'SGD',variable = to, value = 'SGD').grid(row = 11, column = 4)
tk.Entry(root, textvariable = w).grid(row = 12, column =0)
tk.Button(root, text = 'CONVERT', command = do).grid(row = 13, column = 2)
root.mainloop()