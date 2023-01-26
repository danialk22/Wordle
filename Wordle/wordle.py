from random import randint
import tkinter as tk


global word
# word = "HELLO"
# word.replace()
window = tk.Tk()
window.title("Definetly not Wordle")
window.configure(bg="black")

file = open("Wordle/Wordle Database.txt", "r")

words = []

for word in file.readlines():
    words.append(word[:5])
#print(word)




def getbg(g, w):
    bg=["","","","",""]
    done = []
    for i in range(0,5):
        if g[i] == w[i]:
            bg[i] = "green"
            w = w.replace(w[i]," ",1)
            #done.append(g[i])
    #print(w)
    for i in range(0,5):
        if g[i] in w and bg[i] == "":
            bg[i] = "yellow"
            w = w.replace(g[i]," ",1)
            #done.append(g[i])
    

        elif bg[i] == "":
            bg[i] = "grey"
    #print(w)

    return bg


def reset(event):
    # label.destroy()
    # frame.destroy()
    #global mainframe
    mainframe.destroy()
    window.quit()


def enter(event):
    global i
    global word
    colors=[]
    guess = entry.get()
    if len(guess) == 5 and guess in words:
        entry.delete(0,tk.END)
        guess = guess.upper()
        colors = getbg(guess, word)
        j=0
        for c in guess:
            arr[i].configure(text=c, bg=colors[j], fg="black")
            i+=1
            j+=1

    if colors == ["green", "green", "green", "green", "green"]:
        end = tk.Label(
            text="CONGRATS!!",
            fg="green",
            bg="black",
            width=38,
            height=5,
            master=mainframe
        )
        end.pack()
        #label.configure(text="CONGRATS!!", fg="green")
        entry.destroy()
        

    elif (i==30):
        end = tk.Label(
            text="The word was " + word,
            fg="red",
            bg="black",
            width=38,
            height=5,
            master=mainframe
        )
        end.pack()
        #label.configure(text="The word was " + word)
        entry.destroy()


if __name__ == "__main__":  
    while True:
        ind = randint(0,len(words))

        word = words[ind]
        word = word.upper()
        #word = "CHAFE"

        mainframe = tk.Frame(bg="black")
        
        frame = tk.Frame(bg="black",master=mainframe)


        label = tk.Label(
            text="W  O  R  D  L  E",
            fg="white",
            bg="black",
            width=38,
            height=5,
            master=mainframe
        )
        entry = tk.Entry(fg="black", bg="grey", width=38,master=frame)

        arr=[]
        global i
        i=0
        for r in range(0,6):
            txtframe = tk.Frame(bg="black", master=frame)
            txtframe.rowconfigure([0,1], minsize=10)
            txtframe.columnconfigure([0,1,2,3,4,5,6,7,8], minsize=10)
            for c in range(0,9,2):
                s = tk.Label(
                    text=" ",
                    bg="grey",
                    fg="black",
                    height=2,
                    width=2,
                    master=txtframe
                )
                s.grid(row=0, column=c)
                arr.append(s)
            txtframe.pack()

        label.pack()
        frame.pack()
        entry.pack()
        mainframe.pack()

        entry.bind("<Return>", enter)
        window.bind("<space>", reset)
        window.bind("<Escape>", quit)

        tk.mainloop()






