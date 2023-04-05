import tkinter as tk 
from tkinter import ttk


class todo:

    def __init__(self, root):
        self.root=root
        self.root.title("to do list app")
        self.root.geometry("720x480+400+200")
        self.root.resizable(False, False)
        self.label=tk.Label(self.root,bg="purple",fg="black",font="Times 35 bold",text="WHAT WE GONNA DO TODAY!")
        self.label.pack(side=tk.TOP)
        self.tasks=tk.Label(self.root,bg="purple",fg="black",font="Times 20 bold",text="tasks to do")
        self.tasks.place(x="40",y="100")
        self.main_text = tk.Listbox(self.root, height="20",width="30",font="Times 20 bold")
        self.main_text.place(x="250",y="100")
        self.entry=tk.Entry(self.root,font="Times 15 bold" ,width="20")
        self.entry.place(x="40",y="150")
        self.button=tk.Button(self.root,font="Times 15 bold",bg="purple",text="add",command=self.add)
        self.button.place(x="40",y="190")
        self.delete_button=tk.Button(self.root,font="Times 15 bold",bg="purple",text="delete last",command=self.delete_last)
        self.delete_button.place(x="100",y="190")
        


    def add(self):
        content=self.entry.get() 
        self.main_text.insert(tk.END,content)
        with open("tasks.txt", "w") as file:
            file.write(content)
            self.entry.delete(0, tk.END)

    def delete_last(self):
        self.main_text.delete(tk.END)
        
def main():
    root=tk.Tk()
    ui=todo(root)
    root.mainloop()

if __name__ == '__main__':
    main()
