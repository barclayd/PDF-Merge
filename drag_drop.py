import tkinter


class DragDropListbox(tkinter.Listbox):
    def __init__(self, master, list, **kw):
        kw['selectmode'] = tkinter.SINGLE
        tkinter.Listbox.__init__(self, master, kw)
        self.bind('<Button-1>', self.set_current)
        self.bind('<B1-Motion>', self.change_selection)
        self.current_index = None
        self.list = list

    def set_current(self, event):
        self.current_index = self.nearest(event.y)

    def change_selection(self, event):
        i = self.nearest(event.y)
        if i < self.current_index:
            x = self.get(i)
            pdf_index = self.curselection()[0]
            pdf = self.list[pdf_index]
            self.delete(i)
            self.list.pop(pdf_index)
            self.insert(i+1, x)
            self.list.insert(pdf_index-1, pdf)
            self.current_index = i
        elif i > self.current_index:
            x = self.get(i)
            pdf_index = self.curselection()[0]
            pdf = self.list[pdf_index]
            self.delete(i)
            self.list.pop(pdf_index)
            self.insert(i-1, x)
            self.list.insert(pdf_index+1, pdf)
            self.current_index = i
