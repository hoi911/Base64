import tkinter

window = tkinter.Tk()

window.title("First Program")
window.geometry("400x400+100+100")
window.resizable(False, False)

label = tkinter.Label(window, text="Hello", width="10", height="5", fg="red", relief="solid")
label.pack()

window.mainloop()