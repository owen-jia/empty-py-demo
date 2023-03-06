import tkinter

root = tkinter.Tk()
root.title("tkinter 测试")
root.geometry("300x500")

b = 0


def add_one():
    global b
    if b == 9:
        b = 0
    else:
        b += 1
    print(b)
    show_entry(b)


a = tkinter.Button(root, text="累加", command=add_one)
a.pack()
a.place(x='100', y='50')


def clean_entry():
    c.delete(0)


d = tkinter.Button(root, text="清除", command=clean_entry)
d.pack()
d.place(x='150', y='50')

c = tkinter.Entry(root, bd=5)
c.pack()
c.place(x='70', y='100')

e = tkinter.Label(root, text="测试demo")
e.place(x='110', y='150')


def show_entry(m='0'):
    return c.insert(0, m)


if __name__ == '__main__':
    print('process start...')
    root.mainloop()
