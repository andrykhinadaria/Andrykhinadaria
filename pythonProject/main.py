from tkinter import *

root = Tk()
root.title("Опрос")
root.geometry("720x800")




btn = Button(text="Посмотреть результаты",          # текст кнопки
             background="#555",     # фоновый цвет кнопки
             foreground="#ccc",     # цвет текста
             padx="20",             # отступ от границ до содержимого по горизонтали
             pady="8",              # отступ от границ до содержимого по вертикали
             font="16")              # высота шрифта
btn.pack(side=BOTTOM, padx=0, pady=50)
label1 = Label(text="Какой язык программирования вам больше всего нравится ?")
label1.pack(side=TOP,padx=0,pady=10)
Possible_answer = IntVar()

python_checkbutton = Radiobutton(text="Java",variable=Possible_answer, value=1, padx=15, pady=10)
python_checkbutton.pack(side=TOP,padx=0,pady=10)
python_checkbutton = Radiobutton(text="Python",variable=Possible_answer, value=2, padx=15, pady=10)
python_checkbutton.pack(side=TOP,padx=0,pady=10)

label1 = Label(text="Какой язык программирования вам больше всего нравится ?")
label1.pack(side=TOP,padx=0,pady=10)
answer = IntVar()

python_checkbutton = Radiobutton(text="Java",variable=answer, value=3, padx=15, pady=10)
python_checkbutton.pack(side=TOP,padx=0,pady=10)
python_checkbutton = Radiobutton(text="Python",variable=answer, value=4, padx=15, pady=10)
python_checkbutton.pack(side=TOP,padx=0,pady=10)






root.mainloop()