from tkinter import ttk
from tkinter import messagebox
from tkinter import *

# 将任意2~16进制字符串转换成10进制
def x_to_num(num,x):
    num_dict = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,
                "a":10,"b":11,"c":12,"d":13,"e":14,"f":15}
    i = 0
    res = 0
    while len(num) > 0:
        temp = num[-1]
        if temp in num_dict:
            temp = num_dict[temp]
        else:
            temp = int(temp)
        num = num[0:-1]
        res += temp * x**i
        i+=1
    return res


# 把10进制数转换成任意2~16进制字符串
def num_to_x_str(num,x):
    res = []
    res_str = ""
    num_dict = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    if x>=2 and x<=16:
        while num>0:
            if num%x<10:
                res.append(num%x)
            else:
                res.append(num_dict[num%x])
            num //= x
        res.reverse()
    else:
        return None
    for i in res:
        res_str += str(i)
    return res_str

# 按钮点击事件
def test_to():
    num_dict = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,
                "a":10,"b":11,"c":12,"d":13,"e":14,"f":15}
    entryStartText = entryStart.get()
    if entryStartText == "":
        messagebox.showwarning("警告","请输入要转换的数字")
    else:
        com1Text = com1.get()
        if len(com1Text) == 3:
            x1 = int(com1Text[0])
        elif len(com1Text) == 4:
            x1 = int(com1Text[0:2])
        com2Text = com2.get()
        if len(com2Text) == 3:
            x2 = int(com2Text[0])
        elif len(com2Text) == 4:
            x2 = int(com2Text[0:2])
        for i in entryStartText:
            if i in num_dict:
                temp = num_dict[i]
            else:
                temp = int(i)
            if temp >= x1:
                messagebox.showwarning("警告","输入的不是"+str(x1)+"进制数字")
                break
        else:
            entryEndText = num_to_x_str( x_to_num(entryStartText,x1),x2 )
            #print(entryEndText)
            entryEnd.delete(0,"end")
            entryEnd.insert("end",entryEndText)

top = Tk()
top.title("进制转换器")
top.geometry("400x600")

label1 = Label(top,text="万能进制转换器",font=("楷体",30))
label1.pack(pady=50)

frame1 = Frame(top)
frame2 = Frame(top)

entryStart = Entry(frame1, bd = 5, width=20, font=("楷体",20), fg = "red")
entryEnd = Entry(frame2, bd = 5, width=20, font=("楷体",20), fg = "red")
values = [str(i)+"进制" for i in range(2,17)]
com1 = ttk.Combobox(
            master=frame1,  # 父容器
            height=10,  # 高度,下拉显示的条目数量
            width=6,  # 宽度
            state='readonly',  # 设置状态 normal(可选可输入)、readonly(只可选)、 disabled
            cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
            font=('', 15),  # 字体
            textvariable=StringVar(),  # 通过StringVar设置可改变的值
            values=values,  # 设置下拉框的选项
            )
com2 = ttk.Combobox(
            master=frame2,  # 父容器
            height=10,  # 高度,下拉显示的条目数量
            width=6,  # 宽度
            state='readonly',  # 设置状态 normal(可选可输入)、readonly(只可选)、 disabled
            cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
            font=('', 15),  # 字体
            # text = "2进制",
            textvariable=StringVar(),  # 通过StringVar设置可改变的值
            values=values,  # 设置下拉框的选项
            )
entryStart.pack(side=LEFT)
com1.pack(side=RIGHT)
frame1.pack(pady=50)

entryEnd.pack(side=LEFT)
com2.pack(side=RIGHT)
frame2.pack(pady=50)

# 设置下拉框默认值
com1.current(8)
com2.current(0)

button1 = Button(top, text="转换",font=("楷体",20), command=test_to)
button1.pack(pady=50)

top.mainloop()
