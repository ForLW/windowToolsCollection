import tkinter
import time
from tkinter import messagebox


def click_thing():
    messagebox.showinfo("信息", "点击事件")


class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.label_title = tkinter.Label(self)
        self.label_date = tkinter.Label(self)
        self.label_time = tkinter.Label(self)
        self.button1 = tkinter.Button(self)
        self.create_widgets()

    def create_widgets(self):
        self.label_title["text"] = "计时器"
        self.label_title["font"] = ("楷体", 30)
        self.label_title.pack(pady=50)
        self.label_title.pack(expand=1)

        # self.label_date["text"] = ""
        self.label_date["font"] = ("楷体", 20)
        self.label_date.pack(pady=10)
        # self.label_time["text"] = ""
        self.label_time["font"] = ("楷体", 20)
        self.label_time.pack(pady=10)

        self.button1["text"] = "开始计时"
        self.button1["font"] = ("楷体", 20)
        self.button1["command"] = click_thing
        self.button1.pack(pady=50)

        while True:
            time_now = time.localtime(time.time())
            self.label_date["text"] = "{}年{:0<2d}月{:0<2d}日".format(time_now.tm_year, time_now.tm_mon, time_now.tm_mday)
            self.label_time["text"] = "{:0>2d}:{:0>2d}:{:0>2d}".format(time_now.tm_hour, time_now.tm_min, time_now.tm_sec)
            self.label_time.update()
            time.sleep(0.1)


if __name__ == '__main__':
    root = tkinter.Tk()
    root.title("计时器")
    root.geometry("400x600")
    app = Application(root)
    app.mainloop()
