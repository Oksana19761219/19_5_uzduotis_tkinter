from tkinter import Tk, NW, Button, PhotoImage, StringVar, messagebox

langas = Tk()
langas.geometry("470x520")
langas.configure(bg="#808080")

simbolis = StringVar("")
simbolis.set("x")


def zaisti_dar_karta(iliustracija_o, iliustracija_x, o_laimejo, x_laimejo):
    zaideju_pasirinkimai["x"] = []
    zaideju_pasirinkimai["o"] = []
    for indeksas in range(1, 10):
        mygtukai[indeksas]["image"] = iliustracija_nieko
        mygtukai[indeksas].configure(command=lambda nr=indeksas: zaisti(nr,
                                                                        iliustracija_o,
                                                                        iliustracija_x,
                                                                        o_laimejo,
                                                                        x_laimejo))


def tikrinti_laimejima(zaidejo_pasirinkimai, iliustracija_laimejimas):
    for laimejimas in laimejimai:
        if laimejimas.issubset(zaidejo_pasirinkimai):
            for indeksas in list(laimejimas):
                mygtukai[indeksas]["image"] = iliustracija_laimejimas
            return True
    return False


def ar_lygiosios():
    pasirinkimai = zaideju_pasirinkimai["x"] + zaideju_pasirinkimai["o"]
    if sorted(pasirinkimai) == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        messagebox.showinfo('Pabaiga', 'lygiosios')


def pasirinkti_simboli(zaidejo_simbolis, iliustracija_o, iliustracija_x, o_laimejo, x_laimejo):
    if zaidejo_simbolis == "x":
        iliustracija = iliustracija_x
        iliustracija_laimejo = x_laimejo
        simbolis.set("o")
    else:
        iliustracija = iliustracija_o
        iliustracija_laimejo = o_laimejo
        simbolis.set("x")
    return iliustracija, iliustracija_laimejo


def zaisti(nr, iliustracija_o, iliustracija_x, o_laimejo, x_laimejo):
    if nr not in zaideju_pasirinkimai["x"] and nr not in zaideju_pasirinkimai["o"]:
        zaidejo_simbolis = simbolis.get()
        zaideju_pasirinkimai[zaidejo_simbolis].append(nr)
        iliustracija, iliustracija_laimejo = pasirinkti_simboli(zaidejo_simbolis,
                                                                iliustracija_o,
                                                                iliustracija_x,
                                                                o_laimejo,
                                                                x_laimejo)
        mygtukai[nr]["image"] = iliustracija
        laimejimas = tikrinti_laimejima(zaideju_pasirinkimai[zaidejo_simbolis], iliustracija_laimejo)
        if laimejimas:
            for indeksas in range(1, 10):
                mygtukai[indeksas].configure(command='')
        else:
            ar_lygiosios()


iliustracija_nieko = PhotoImage(file="nieko.png")
iliustracija_o = PhotoImage(file="O.png")
iliustracija_x = PhotoImage(file="X.png")
o_laimejo = PhotoImage(file="O_laimejo.png")
x_laimejo = PhotoImage(file="X_laimejo.png")
zaideju_pasirinkimai = {"x": [], "o": []}
laimejimai = [{1, 2, 3},
              {4, 5, 6},
              {7, 8, 9},
              {1, 4, 7},
              {2, 5, 8},
              {3, 6, 9},
              {1, 5, 9},
              {3, 5, 7}]

mygtukas_1 = Button(langas, command=lambda nr=1: zaisti(nr, iliustracija_o, iliustracija_x, o_laimejo, x_laimejo))
mygtukas_2 = Button(langas, command=lambda nr=2: zaisti(nr, iliustracija_o, iliustracija_x, o_laimejo, x_laimejo))
mygtukas_3 = Button(langas, command=lambda nr=3: zaisti(nr, iliustracija_o, iliustracija_x, o_laimejo, x_laimejo))
mygtukas_4 = Button(langas, command=lambda nr=4: zaisti(nr, iliustracija_o, iliustracija_x, o_laimejo, x_laimejo))
mygtukas_5 = Button(langas, command=lambda nr=5: zaisti(nr, iliustracija_o, iliustracija_x, o_laimejo, x_laimejo))
mygtukas_6 = Button(langas, command=lambda nr=6: zaisti(nr, iliustracija_o, iliustracija_x, o_laimejo, x_laimejo))
mygtukas_7 = Button(langas, command=lambda nr=7: zaisti(nr, iliustracija_o, iliustracija_x, o_laimejo, x_laimejo))
mygtukas_8 = Button(langas, command=lambda nr=8: zaisti(nr, iliustracija_o, iliustracija_x, o_laimejo, x_laimejo))
mygtukas_9 = Button(langas, command=lambda nr=9: zaisti(nr, iliustracija_o, iliustracija_x, o_laimejo, x_laimejo))

mygtukai = {1: mygtukas_1,
            2: mygtukas_2,
            3: mygtukas_3,
            4: mygtukas_4,
            5: mygtukas_5,
            6: mygtukas_6,
            7: mygtukas_7,
            8: mygtukas_8,
            9: mygtukas_9}

mygtukas_1.config(image=iliustracija_nieko, width="110", height="110")
mygtukas_2.config(image=iliustracija_nieko, width="110", height="110")
mygtukas_3.config(image=iliustracija_nieko, width="110", height="110")
mygtukas_4.config(image=iliustracija_nieko, width="110", height="110")
mygtukas_5.config(image=iliustracija_nieko, width="110", height="110")
mygtukas_6.config(image=iliustracija_nieko, width="110", height="110")
mygtukas_7.config(image=iliustracija_nieko, width="110", height="110")
mygtukas_8.config(image=iliustracija_nieko, width="110", height="110")
mygtukas_9.config(image=iliustracija_nieko, width="110", height="110")

mygtukas_1.place(x=50, y=40, anchor=NW)
mygtukas_2.place(x=180, y=40, anchor=NW)
mygtukas_3.place(x=310, y=40, anchor=NW)
mygtukas_4.place(x=50, y=170, anchor=NW)
mygtukas_5.place(x=180, y=170, anchor=NW)
mygtukas_6.place(x=310, y=170, anchor=NW)
mygtukas_7.place(x=50, y=300, anchor=NW)
mygtukas_8.place(x=180, y=300, anchor=NW)
mygtukas_9.place(x=310, y=300, anchor=NW)

mygtukas_10 = Button(langas, text="Žaisti dar kartą",
                     command=lambda: zaisti_dar_karta(iliustracija_o,
                                                      iliustracija_x,
                                                      o_laimejo,
                                                      x_laimejo))
mygtukas_10.config(background='#990000', width="52", height="2")
mygtukas_10.place(x=50, y=450, anchor=NW)

langas.mainloop()
