import pyodbc
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
from PIL import ImageTk, Image
    
connection_to_db = pyodbc.connect(
    r'Driver={SQL Server};Server=THINKPAD\SQLEXPRESS;Database=Shop;Trusted_Connection=yes;')
cursor = connection_to_db.cursor()

def Exit():
    jk=messagebox.askokcancel("Выйти из приложения","Хотите выйти из приложения?")
    if jk == True:
        tk.destroy()
    else:
        pass


def Exit_order():
    jk=messagebox.askokcancel("Выйти из приложения","Хотите выйти из приложения?")
    if jk == True:
        tk.destroy()
    else:
        pass


def Exit_window(window,act):
    jd=messagebox.askokcancel('закрыть окно','Закрыть окно?',parent=window)
    if jd == True:
        interf.entryconfig(act,state='active')
        window.destroy()
    else:
        pass


def Ok_payment(s, re):
    jk=messagebox.showinfo("Успешная оплата","Оплата покупки прошла успешно")
    s.delete(*s.get_children())
    
    n = name.get()
    e = add.get()
    r = card1.get()
    q = card2.get()
    u = card3.get()
       
   
    
    with connection_to_db.cursor() as cursor:
        r1 = f"UPDATE Users SET user_name = '{n}' WHERE id_user = '{re}'"
        r2 = f"UPDATE Users SET adress = '{e}' WHERE id_user = '{re}'"
        r3 = f"UPDATE Users SET card = '{r}' WHERE id_user = '{re}'"
        r4 = f"UPDATE Users SET date_card = '{q}' WHERE id_user = '{re}'"
        r5 = f"UPDATE Users SET pin = '{u}' WHERE id_user = '{re}'"
        
        cursor.execute(r1)
        cursor.execute(r2)
        cursor.execute(r3)
        cursor.execute(r4)
        cursor.execute(r5)
        connection_to_db.commit()
    
    


def payment(y, ddd):

    tkpay = Toplevel(tk)
    tkpay.title("Оплата")
    tkpay.geometry("300x400+300+200")
    interf.entryconfig(2,state='disabled')
    tkpay.protocol( "WM_DELETE_WINDOW",lambda window=tkpay, act = 1: Exit_window(window,act))

    pay = Label(tkpay, text = 'Оплата покупки')
    pay.pack()

    global name, add, card1, card2, card3
    
    name1 = Label(tkpay, text = 'введите имя покупателя: ')
    name1.pack()
    
    name = StringVar()
    name_entry = Entry(tkpay, textvariable=name)
    name_entry.pack()

    adress = Label(tkpay, text = 'введите адрес доставки: ')
    adress.pack()

    add = StringVar()
    add_entry = Entry(tkpay, textvariable=add)
    add_entry.pack()

    card = Label(tkpay, text = 'укажите номер карты: ')
    card.pack()

    card1 = StringVar()
    card1_entry = Entry(tkpay, textvariable=card1)
    card1_entry.pack()

    card22 = Label(tkpay, text = 'укажите срок действия карты: ')
    card22.pack()

    card2 = StringVar()
    card2_entry = Entry(tkpay, textvariable=card2)
    card2_entry.pack()

    card3 = Label(tkpay, text = 'укажите Pin код карты: ')
    card3.pack()

    card3 = StringVar()
    card3_entry = Entry(tkpay, textvariable=card3)
    card3_entry.pack()

    Button_entry = Button(tkpay, text="Подтвердить оплату", command = lambda re = ddd, s = y:Ok_payment(s, re))
    Button_entry.place(relx=0.25, rely=0.6, relwidth=0.5, relheight=0.20)
    
   

    
def udochki():
    tk1 = Toplevel(tk)
    tk1.title("Удочки")
    tk1.geometry("700x300+300+200")
    interf.entryconfig(2,state='disabled')
    tk1.protocol( "WM_DELETE_WINDOW",lambda window=tk1,act=2: Exit_window(window,act))


    
    framek = Frame(tk1,width=300,height=150,bg='gray')#создание рамок
    framet = Frame(tk1, width=300, height=150, bg='sky blue')
    framek.place(relx=0, rely=0, relwidth=1, relheight=0.5)#расположение рамок
    framet.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

    cursor.execute("""SELECT dbo.products.id_product, dbo.products.name, dbo.products.price, dbo.products.ammount
FROM   dbo.categories INNER JOIN
             dbo.Products_category ON dbo.categories.id_category = dbo.Products_category.id_category INNER JOIN
             dbo.products ON dbo.Products_category.id_product = dbo.products.id_product
WHERE (dbo.categories.id_category = 1)""")  # выбираем  данные из таблицы
    row = cursor.fetchall()  # выбираем количество строк
    # работаем с таблицей
    heads = ['id', 'названние', 'цена (руб.)', 'количество']  # создаем названия столбцов
    table = ttk.Treeview(framek, show='headings')  # создание таблицы
    table['columns'] = heads  # присваеваем столбцы в таблицу
    table['displaycolumns']=['названние', 'цена (руб.)', 'количество']
    style = ttk.Style()
    
    style.theme_use("alt")#cтили
    style.map("Treeview")

    # работаем со столбцами
    for y in heads:
        table.heading(y, text=y, anchor=CENTER)
        table.column(y, anchor=CENTER)
    # работаем с данными
    for i in row:
        table.insert('', END, values=(" ".join(i)))
    

    table.pack(expand=YES, fill=BOTH)#отрисовка таблиц


    Button_entry = Button(tk1, text="добавить в заказ", command = lambda table = table: order(table))
    Button_entry.place(relx=0.25, rely=0.5, relwidth=0.30, relheight=0.40)





def katushki():
    tk2 = Toplevel(tk)
    tk2.title("Катушки")
    tk2.geometry("700x300+300+200")
    interf.entryconfig(3,state='disabled')
    tk2.protocol("WM_DELETE_WINDOW", lambda window=tk2,act=3:Exit_window(window,act))


    framek = Frame(tk2,width=300,height=150,bg='gray')#создание рамок
    framet = Frame(tk2, width=300, height=150, bg='sky blue')
    framek.place(relx=0, rely=0, relwidth=1, relheight=0.5)#расположение рамок
    framet.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

    cursor.execute("""SELECT dbo.products.id_product, dbo.products.name, dbo.products.price, dbo.products.ammount
FROM   dbo.categories INNER JOIN
             dbo.Products_category ON dbo.categories.id_category = dbo.Products_category.id_category INNER JOIN
             dbo.products ON dbo.Products_category.id_product = dbo.products.id_product
WHERE (dbo.categories.id_category = 2)""")  # выбираем  данные из таблицы
    row = cursor.fetchall()  # выбираем количество строк
    # работаем с таблицей
    heads = ['id', 'названние', 'цена (руб.)', 'количество']  # создаем названия столбцов
    table = ttk.Treeview(framek, show='headings')  # создание таблицы
    table['columns'] = heads  # присваеваем столбцы в таблицу
    table['displaycolumns']=['названние', 'цена (руб.)', 'количество']
    style = ttk.Style()
    
    style.theme_use("alt")#cтили
    style.map("Treeview")

    # работаем со столбцами
    for y in heads:
        table.heading(y, text=y, anchor=CENTER)
        table.column(y, anchor=CENTER)
    # работаем с данными
    for i in row:
        table.insert('', END, values=(" ".join(i)))
    
    table.pack(expand=YES, fill=BOTH)#отрисовка таблиц

    Button_entry = Button(tk2, text="добавить в заказ", command = lambda table = table: order(table))
    Button_entry.place(relx=0.25, rely=0.5, relwidth=0.30, relheight=0.40)


def warning():
        jk=messagebox.askokcancel("Корзина","Хотите добавить этот продукт в корзину?")
        if jk == True:
            
            pass
            
        else:
            pass
        
def order(table):
    
    warning()
    tk3 = Toplevel(tk)
    tk3.title("Заказ")
    tk3.geometry("400x300+300+200")
    tk3.protocol("WM_DELETE_WINDOW", lambda window=tk3,act=5: Exit_window(window,act))
    tk3.overrideredirect(True)
    tv = ttk.Treeview(tk3, columns=(1, 2), show='headings', height=8)
    
    tv.heading(1, text="Наименование")
    tv.heading(2, text="Стоимость (руб.)")
    tv.pack()

    
    
    with connection_to_db.cursor() as cursor:
        ii = f"select top (1) cast((SELECT TOP (1) CAST(id_order AS int) AS Expr1 FROM dbo.Order2 ORDER BY Expr1 DESC)AS nvarchar)from order2 order by id_order desc"#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        cursor.execute(ii)
        
        s = cursor.fetchall()
        
        #print(s)
        y = ''
        for ppp in s:
            #y = str, y)
            y =' '.join(ppp)
            y = int(y) + 1
            #print(y)

        
        
        

    
        cursor.execute(f"""SELECT TOP (100) PERCENT dbo.Order2.name_produts, dbo.Order2.price, dbo.Order2.id_user, dbo.Order2.id_order
FROM   dbo.Order2 INNER JOIN
             dbo.Users ON dbo.Order2.id_user = dbo.Users.id_user
where Order2.id_user = (select top (1) cast((SELECT TOP (1) CAST(id_user AS int) AS Expr1 FROM Users 
ORDER BY Expr1 DESC)AS nchar)from Users order by id_user desc)
ORDER BY dbo.Order2.id_user DESC """)
        uu = cursor.fetchall()

   
    

    for i in uu:
        tv.insert('', END, values=(" ".join(i)))
        
    t = table.selection()[0]#берем адрес выбранной строки
    uu = table.item(t)#берем все выделенные данные
    a, e, p = uu['values'][0:3]
    

    tv.insert('',END,values=(e, p))

    
    
   
    with connection_to_db.cursor() as cursor:
        r = (f"INSERT INTO Order2(id_order, id_user, id_product, name_produts, price) values ('{y}', '{yy}', '{a}', '{e}', '{p}')")
        cursor.execute(r)
        connection_to_db.commit()
        
    
    total = sum(int(tv.set(item,2)) for item in tv.get_children())
    
    print(total)
            

        
   
        
    
 
   
    tt = Label(tk3, text = total)
    pr = Label(tk3, text = "Итог: ")
    tt.place(relx=0.55, rely=0.6)
    pr.place(relx=0.45, rely=0.6)
    
    
    Button_entry = Button(tk3, text="оплатить", command = lambda ddd = yy, y = tv: payment(y, ddd))
    Button_entry.place(relx=0.25, rely=0.7, relwidth=0.5, relheight=0.2)

    

def items():
    tk4 = Toplevel(tk)
    tk4.title("Снаряжение")
    tk4.geometry("700x300+300+200")
    interf.entryconfig(4,state='disabled')
    tk4.protocol("WM_DELETE_WINDOW", lambda window=tk4,act=4: Exit_window(window,act))


    framek = Frame(tk4,width=300,height=150,bg='gray')#создание рамок
    framet = Frame(tk4, width=300, height=150, bg='sky blue')
    framek.place(relx=0, rely=0, relwidth=1, relheight=0.5)#расположение рамок
    framet.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

    cursor.execute("""SELECT dbo.products.id_product, dbo.products.name, dbo.products.price, dbo.products.ammount
FROM   dbo.categories INNER JOIN
             dbo.Products_category ON dbo.categories.id_category = dbo.Products_category.id_category INNER JOIN
             dbo.products ON dbo.Products_category.id_product = dbo.products.id_product
WHERE (dbo.categories.id_category = 4)""")  # выбираем  данные из таблицы
    row = cursor.fetchall()  # выбираем количество строк
    # работаем с таблицей
    heads = ['id', 'названние', 'цена (руб.)', 'количество']  # создаем названия столбцов
    table = ttk.Treeview(framek, show='headings')  # создание таблицы
    table['columns'] = heads  # присваеваем столбцы в таблицу
    table['displaycolumns']=['названние', 'цена (руб.)', 'количество']
    style = ttk.Style()
    
    style.theme_use("alt")#cтили
    style.map("Treeview")

    # работаем со столбцами
    for y in heads:
        table.heading(y, text=y, anchor=CENTER)
        table.column(y, anchor=CENTER)
    # работаем с данными
    for i in row:
        table.insert('', END, values=(" ".join(i)))

    table.pack(expand=YES, fill=BOTH)#отрисовка таблиц


    Button_entry = Button(tk4, text="добавить в заказ", command = lambda table = table: order(table))
    Button_entry.place(relx=0.25, rely=0.5, relwidth=0.30, relheight=0.40)

   

def bait():
    tk5 = Toplevel(tk)
    tk5.title("Приманки")
    tk5.geometry("700x300+300+200")
    interf.entryconfig(1,state='disabled')
    tk5.protocol("WM_DELETE_WINDOW", lambda window=tk5,act=1: Exit_window(window,act))

    frame_bait1 = Frame(tk5,width=300,height=150,bg='gray')#создание рамок
    frame_bait2 = Frame(tk5, width=300, height=150, bg='sky blue')
    frame_bait1.place(relx=0, rely=0, relwidth=1, relheight=0.5)#расположение рамок
    frame_bait2.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

   
    cursor.execute("""SELECT dbo.products.id_product, dbo.products.name, dbo.products.price, dbo.products.ammount
FROM   dbo.categories INNER JOIN
             dbo.Products_category ON dbo.categories.id_category = dbo.Products_category.id_category INNER JOIN
             dbo.products ON dbo.Products_category.id_product = dbo.products.id_product
WHERE (dbo.categories.id_category = 3)""")  # выбираем  данные из таблицы
    row = cursor.fetchall()  # выбираем количество строк
    
    # работаем с таблицей
    heads = ['id', 'названние', 'цена (руб.)', 'количество']  # создаем названия столбцов
    table = ttk.Treeview(frame_bait1, show='headings')  # создание таблицы
    table['columns'] = heads  # присваиваем столбцы в таблицу
    table['displaycolumns']=['названние', 'цена (руб.)', 'количество']
    style = ttk.Style()
    
    style.theme_use("alt")#cтили
    style.map("Treeview")

    # работаем со столбцами
    for y in heads:
        table.heading(y, text=y, anchor=CENTER)
        table.column(y, anchor=CENTER)
    # работаем с данными
    for i in row:
        table.insert('', END, values=(" ".join(i)))
    

    Button_entry = Button(frame_bait2, text="добавить в заказ", command = lambda table = table: order(table))
    Button_entry.place(relx=0.25, rely=0.5, relwidth=0.30, relheight=0.40)
    
    table.pack(expand=YES, fill=BOTH)#отрисовка таблиц

    return table

   
    

#===============================создание главного окна==============================
tk = Tk()
tk.title('Магазин "FisherPro"')  # название окна
tk.geometry('800x350+250+150')  # Размер окна
tk.protocol("WM_DELETE_WINDOW",Exit)

interf = Menu()

sysmenu=Menu()

interf.add_command(label="Приманки",command=bait)
interf.add_command(label="Удочки",command=udochki)
interf.add_command(label="Катушки", command=katushki)
interf.add_command(label="Снаряжение",command=items)
interf.add_separator()

interf.add_command(label="Выход",command=Exit)



#path = PhotoImage(file = "C:\\Users\\Andrey\\OneDrive\\Desktop\\curs\\fish_main10.png")
#mLabel = Label(tk, image = path)
#mLabel.place(x = 0, y = 0, relwidth = 1, relheight = 1)

with connection_to_db.cursor() as cursor:
    iii = f"select top (1) cast((SELECT TOP (1) CAST(id_user AS int) AS Expr1 FROM dbo.Users ORDER BY Expr1 DESC)AS nvarchar)from Users order by id_user desc"#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    cursor.execute(iii)
    ss = cursor.fetchall()
    yy = ''
    for pppp in ss:
        yy +=' '.join(pppp)
        yy = int(yy) + 1
        g = f" INSERT INTO Users (id_user) values('{yy}')"
        cursor.execute(g)
        connection_to_db.commit()



#====================================главное меню==========================================
sysmenu.add_cascade(label="Классы товаров", menu=interf)

tk.config(menu=sysmenu)#вывод всех меню

tk.mainloop()#вывод окна

    
