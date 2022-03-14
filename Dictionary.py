from tkinter import *
from PyDictionary import PyDictionary
import tkinter.ttk as ttk 
from ttkthemes import ThemedStyle
import comm

dic = PyDictionary()

#Fulscreen mode


#Geometry
root = Tk()
#root.attributes("-zoomed", True)
root.attributes('-alpha',0.85)
root.geometry("1920x1080")
root.config(bg="#8FECFE")
root.title("Szótár")

#Theme
style=ThemedStyle(root)
style.set_theme('black')

#submit command style 
s = ttk.Style()
s.configure('my.TButton', font=("Helvetica",20),foreground='#8FECFE',anchor='center')

#ScrollBar
#scrollbar=Scrollbar(root)
#scrollbar.pack(side=RIGHT,fill=Y)

#Screen functions
def RenderAngolSzotar():

	global root
	root.bind('<Return>', lambda x: dict())

	#forget old packs
	titleStart.place_forget()
	canvas.pack_forget()
	titlesc2.pack_forget()
	framesc2.pack_forget()
	wordsc2.pack_forget()
	frame2sc2.pack_forget()
	valasz.pack_forget()
	correct.pack_forget()
	searchButtonsc2.pack_forget()

	#new packs
	title.pack()
	frame.pack(pady=25)
	word.pack(pady=15)
	frame2.pack(pady=25)
	meaning.pack(pady=15)
	frame3.pack(pady=25)
	synonym.pack(pady=15)
	frame4.pack(pady=25)
	antonym.pack(pady=15)
	searchButton.pack()

def RenderMagyarSzotar():
	global root
	root.bind('<Return>', lambda x: isCorrect())

	#forget old packs
	titleStart.place_forget()
	canvas.pack_forget()
	title.pack_forget()
	frame.pack_forget()
	word.pack_forget()
	frame2.pack_forget()
	meaning.pack_forget()
	frame3.pack_forget()
	synonym.pack_forget()
	frame4.pack_forget()
	antonym.pack_forget()
	searchButton.pack_forget()


	#New packs
	titlesc2.pack()
	framesc2.pack(pady=15)
	wordsc2.pack(pady=15)
	frame2sc2.pack(pady=15)
	valasz.pack(side=LEFT)
	correct.pack(pady=15)
	searchButtonsc2.pack(pady=15)

def szepit(valamias):
	szep2=valamias[0]

	for i in valamias:
		if i!=szep2:
			szep2= szep2+i+", "	

	return szep2[:-2]+"."



def szepit2(valamias):
	szep2=""
	for i in valamias:
		szep2=szep2+i+": "
		for j in valamias[i]:
			szep2=szep2+j+", "
		szep2=szep2[:-2]+'.\n'

	return szep2


#Dictionary functions
def dict():
	valami=dic.synonym(word.get())
	valami2=dic.antonym(word.get())
	valami3=dic.meaning(word.get())#['Noun']

	if not valami:
		szep="Nem létezik szinonima."
	else:
		szep=szepit(valami)

	if not valami2:
		szep2="Nem létezik ellentét."
	else:
		szep2=szepit(valami2)

	if not valami3:
		szep3="Nincs találat."
	else:
		szep3=szepit2(valami3)		


	synonym.config(text=szep)
	antonym.config(text=szep2)
	meaning.config(text=szep3)

def isCorrect():
	s=wordsc2.get()
	ret=comm.helyesiras(s)
	correct.config(text=ret)

	if ret.find('ismeretlen')==-1:
		frame2sc2.config(highlightbackground="green",highlightcolor="green",highlightthickness=2,bg="#ccffcc")
		valasz.config(bg="#ccffcc")
		correct.config(bg="#ccffcc")

	else:
		frame2sc2.config(highlightbackground="red",highlightcolor="red",highlightthickness=2,bg="#ffcccc")
		valasz.config(bg="#ffcccc")
		correct.config(bg="#ffcccc")


#Menubar
menubar=Menu(root)

#Angol
angol=Menu(menubar,tearoff=0)

menubar.add_cascade(label="Szótárak",menu=angol)
angol.add_command(label="Angol Szótár",command=RenderAngolSzotar)
angol.add_command(label="Magyar Szótár",command=RenderMagyarSzotar)

#Photo/ STARTSCREEN
W=1920
H=1080#
canvas = Canvas(root, height=1100, width=900,bg="#8FECFE",highlightthickness=0)
image = PhotoImage(file="startimage.png")
canvas.create_image(W/4, H/2, anchor="center", image=image)

titleStart=Label(root, text="Szótárak",font=("Maghrib",70),bg="#8FECFE")
titleStart.place(relx = 0.5,
                   rely = 0.25,
                   anchor = 'center')

canvas.pack()



#-----------------------------------------English Dictionary---------------------------------------------------

#TitleFrame
title=Label(root,bg="#8FECFE",text="Angol Szótár", font=("Maghrib",45))

#Frame1
frame = Frame(root,bg="#8FECFE")
Label(frame, text="Írd be a szót: ",font=("Maghrib",30),bg="#8FECFE").pack(side=LEFT)

word = ttk.Entry(frame,font=("Helvetica 15 bold"))


#Frame 2
frame2 = Frame(root,bg="#8FECFE")

Label(frame2,text="Jelentés: ",font=("Maghrib",30),bg="#8FECFE").pack(side=LEFT)
meaning = Label(frame2,text="",font=("Helvetica 15 "),wraplength=1200,bg="#8FECFE")


#Frame 3
frame3 = Frame(root, bg="#8FECFE")

Label(frame3,text="Szinonima: ",font=("Maghrib",30),bg="#8FECFE").pack(side=LEFT)
synonym = Label(frame3,text="",font=("Helvetica 15 "),bg="#8FECFE",wraplength=1200)

#Frame 4
frame4 = Frame(root,bg="#8FECFE",borderwidth=10)

Label(frame4,text="Ellentét: ",font=("Maghrib",30),bg="#8FECFE").pack(side=LEFT)
antonym = Label(frame4,text="",font=("Helvetica 15 "),bg="#8FECFE",wraplength=1200)

#submit button
searchButton=ttk.Button(root,text="Keres",command=dict,style='my.TButton')



#---------------------------------------------Magyar Szotar---------------------------------------------------

#TitleFrame
titlesc2=Label(root,bg="#8FECFE",text="Magyar Szótár", font=("Maghrib",45))

#Frame1
framesc2 = Frame(root,bg="#8FECFE")
Label(framesc2, text="Írd be a szót: ",font=("Maghrib",30),bg="#8FECFE").pack(side=LEFT)

wordsc2 = ttk.Entry(framesc2,font=("Helvetica 15 bold"),width=50)

#Frame2
frame2sc2=Frame(root,bg="#8FECFE")

valasz=Label(frame2sc2,text="Helyes-e? ",font=("Maghrib",30),bg="#8FECFE")
correct =Label(frame2sc2,text="",font=("Helvetica 15 "),wraplength=1200,bg="#8FECFE")


#submit button
searchButtonsc2=ttk.Button(root,text="Keres",command=isCorrect,style='my.TButton')

root.config(menu=menubar)
#scrollbar.config(command=synonym.yview)
root.mainloop()