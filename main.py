import requests
from bs4 import BeautifulSoup
from tkinter import *

def my_fonk():
    x_degisken = start()
    print("x degiskeni=" + x_degisken)

def start():
    number = spinbox.get()
    print(number)
    y_degisken = my_list[int(number)]
    text.delete("1.0", END)
    text.insert(END, y_degisken)
    return y_degisken

def spinbox_selected():
    print(spinbox.get())


url = "https://news.ycombinator.com"
my_list = []
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("a", href=True)

    for link in links:
        href = link['href']
        if href.startswith(('http:', 'https:')):
            my_list.append(href)
else:
    print("Sayfa getirilemedi. HTTP Kodu:", response.status_code)


window = Tk()
window.title("Hacker News")
window.minsize(width=600 , height=600)

label = Label(text ="Kaçıncı habere gitmek istediğinizi seçin(1-30)")
label.config(bg = "orange",fg = "black",padx = 10, pady=10)
label.pack()

spacer1 = Label(text="")
spacer1.pack()

spinbox = Spinbox(from_= 1, to=32, command =spinbox_selected, width=41)
spinbox.pack()

spacer2 = Label(text="")
spacer2.pack()

button = Button(text="buton")
button.config(padx=10, pady=10,command= start, width= 33,bg="orange",fg = "black")
button.pack()

spacer3 = Label(text="")
spacer3.pack()

text = Text()
text.config(width=32, height=10)
text.pack()

window.mainloop()