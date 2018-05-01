import backend
from tkinter import *


def get_selected_row(event):
    global selected_tuple, index
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)

def add_command():
    link_text = t3.get("1.0",'end-1c')
    link_url = t4.get("1.0",'end-1c')
    list1.insert(END, (link_text,link_url))

def delete_command():
    list1.delete(index)

def finish_command():
    progress_text = t1.get("1.0",'end-1c')
    thoughts_text = t2.get("1.0",'end-1c')
    if len(progress_text) > 0 and len(thoughts_text) > 0:
        backend.add_day_progress_thoughts(progress_text,thoughts_text)
    all_items = list1.get(0, END)
    link_names=[x[0] for x in all_items]
    links=[x[1] for x in all_items]    
    if len(links) > 0:
        backend.add_links(link_names,links)
    window.destroy()

window = Tk()

window.wm_title('Log editor')

l1 = Label(window, text='Today\'s progress:')
l1.grid(row=0,column=0)
l2 = Label(window, text='Thoughts:')
l2.grid(row=1,column=0)
l3 = Label(window, text='Link text:')
l3.grid(row=2,column=0)
l4 = Label(window, text='Link URL:')
l4.grid(row=3,column=0)
l5 = Label(window, text='Links:')
l5.grid(row=4,column=0)


t1 = Text(window, height=7, width=50)
t1.grid(row=0,column=1)
t2 = Text(window, height=7, width=50)
t2.grid(row=1,column=1)
t3 = Text(window, height=1, width=50)
t3.grid(row=2,column=1)
t4 = Text(window, height=1, width=50)
t4.grid(row=3,column=1)


list1 = Listbox(window, height = 7, width = 70)
list1.grid(row=4, column=1, rowspan = 3)
sb1 = Scrollbar(window)
sb1.grid(row = 4, column = 2, rowspan = 3)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text = "Add link",height = 2, width = 20, command = add_command)
b1.grid(row = 5, column = 0)
b2 = Button(window, text = "Remove selected link",height = 2, width = 20, command = delete_command)
b2.grid(row = 6, column = 0)
b3 = Button(window, text = "Finish",height = 2, width = 20, command= finish_command)
b3.grid(row = 7, column = 1)

window.mainloop()
