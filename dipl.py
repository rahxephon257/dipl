import tkinter as tk
from tkinter import *
import re
from tkinter import ttk

from constants.font import TIMES_NEW_ROMAN_MAIN, TIMES_NEW_ROMAN_BOLD, BUTTON_FONT
from constants.text import GROUP_LESSONS, BODY_STRONG, STRETCH, PERSTRAIN, CROSSFIT, GYM, SAUNA, SUNBURN, YOGA, THAI


def is_valid(newval):                                     #проверка ввода номера
    return re.match("^\+\d{0,11}$", newval) is not None


def check_password(password):                          #проверка пороля
    digits = '1234567890'
    upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_letters = 'abcdefghijklmnopqrstuvwxyz'
    symbols = '!@#$%^&*()-+'
    acceptable = digits+upper_letters+lower_letters+symbols

    passwd = set(password)
    if any(char not in acceptable for char in passwd):
        print('Ошибка. Запрещенный спецсимвол')
    else:
        recommendations = []
        if len(password) < 12:
            recommendations.append(f'увеличить число символов - {12-len(password)}')
        for what, message in ((digits,        'цифру'),
                              (symbols,       'спецсимвол'),
                              (upper_letters, 'заглавную букву'),
                              (lower_letters, 'строчную букву')):
            if all(char not in what for char in passwd):
                recommendations.append(f'добавить 1 {message}')

        if recommendations:
            print("Слабый пароль. Рекомендации:", ", ".join(recommendations))
        else:
            print('Сильный пароль.')


def rega():                                          #регистрация
    window1 = Tk()
    window1.title('Регестрация!')
    window1.geometry('700x600')
    window1.config(bg='#363636')
    window1.resizable(False, False)
    label = Label(window1, text="Логин(телефон):",
                  font=("Times new roman", 15), bg="#363636", fg="#D3D3D3")
    label.place(x=100, y=200)
    check = (window1.register(is_valid), "%P")
    phone_entry = ttk.Entry(window1, validate="key", validatecommand=check, width=40)
    phone_entry.place(x=270, y=205)
    label = Label(window1, text="Придумайте\nПороль:",
                  font=("Times new roman", 15), bg="#363636", fg="#D3D3D3")
    label.place(x=100, y=250)
    check2 = (window1.register(check_password), "%P")
    pass_entry = ttk.Entry(window1, validate="key", validatecommand=check2, width=40, show="*")
    pass_entry.place(x=270, y=267)
    btn = Button(window1, text='Назад', font=BUTTON_FONT, bg="#D3D3D3", fg="black", command=window1.destroy)
    btn.place(x=70, y=500)
    btn = Button(window1, text='Создать', font=BUTTON_FONT, bg="#D3D3D3", fg="black", command=completion_registration)
    btn.place(x=520, y=500)


def warrning1():                                             #ошибка занят телефон
    window2 = tk.Tk()
    window2.title('Ошибка!')
    window2.geometry('600x500')
    window2.config(bg='#363636')
    window2.resizable(False, False)
    label = Label(window2, text="Данный логин(телефон) уже занят,\n используйте другой логин(телефон)",
                  font=("Times new roman", 15), bg="#363636", fg="red")
    label.pack(expand=1)
    btn = Button(window2, text='Повторить', font=BUTTON_FONT, bg="blue", fg="white", command=rega)
    btn.place(x=250, y=450)


def enter(test_mode=False):                                      #Вход в приложение
    window3 = tk.Tk()
    window3.title('Вход в приложение!')
    window3.geometry('700x580')
    window3.config(bg='#363636')
    window3.resizable(False, False)
    label = Label(window3, text="Логин(телефон):",
                  font=("Times new roman", 15), bg="#363636", fg="#FFFAFA")
    label.place(x=100, y=200)
    check = (window3.register(is_valid), "%P")
    phone_entry = ttk.Entry(window3, validate="key", validatecommand=check, width=40)
    phone_entry.place(x=270, y=205)
    label = Label(window3, text="Придумайте\nПороль:",
                  font=("Times new roman", 15), bg="#363636", fg="#FFFAFA")
    label.place(x=100, y=250)
    check2 = (window3.register(check_password), "%P")
    pass_entry = ttk.Entry(window3, validate="key", validatecommand=check2, width=40, show="*")
    pass_entry.place(x=270, y=267)
    btn = Button(window3, text='Назад', font=BUTTON_FONT, bg="#D3D3D3", fg="#000000", command=window3.destroy)
    btn.place(x=70, y=500)
    btn = Button(window3, text='Войти', font=BUTTON_FONT, bg="#D3D3D3", fg="#000000", command=personal_account)#, command=warrning2)
    btn.place(x=520, y=500)
    if test_mode:
        window3.mainloop()


def warrning2():                                   #ошибка входа, не верный пароль
    window5 = tk.Tk()
    window5.title('Ошибка!')
    window5.geometry('600x500')
    window5.config(bg='#363636')
    window5.resizable(False, False)
    label = Label(window5, text="У вас введен неверно\nпороль или логин",
                  font=("Times new roman", 20), bg="#363636", fg="red")
    label.pack(expand=1)
    btn = Button(window5, text='Повторить', font=BUTTON_FONT, bg="blue", fg="white", command=window5.destroy)
    btn.place(x=250, y=430)


def completion_registration():                               #Завершение регистрации
    window4 = tk.Tk()
    window4.title('Завершение регистрации!')
    window4.geometry('580x600')
    window4.config(bg='#363636')
    window4.resizable(False, False)
    label = Label(window4, text="Фамилия:",
                  font=("Times new roman", 15), bg="#363636", fg="#D3D3D3")
    label.place(x=100, y=100)
    entry_lastname = Entry(window4, width=40)               #21312213333333333331111111111111
    entry_lastname.place(x=250, y=100)
    label = Label(window4, text="Имя:",
                  font=("Times new roman", 15), bg="#363636", fg="#D3D3D3")
    label.place(x=100, y=160)
    entry_firstname = Entry(window4, width=40)
    entry_firstname.place(x=250, y=160)
    label = Label(window4, text="Отчество:",
                  font=("Times new roman", 15), bg="#363636", fg="#D3D3D3")
    label.place(x=100, y=220)
    entry_middlename = Entry(window4, width=40)
    entry_middlename.place(x=250, y=220)
    label = Label(window4, text="Email:",
                  font=("Times new roman", 15), bg="#363636", fg="#D3D3D3")
    label.place(x=100, y=280)
    entry_date = Entry(window4, width=40)
    entry_date.place(x=250, y=340)
    entry_email = Entry(window4, width=40)
    entry_email.place(x=250, y=280)
    label = Label(window4, text="Возвраст:",
                  font=("Times new roman", 15), bg="#363636", fg="#D3D3D3")
    label.place(x=100, y=340)
    combo = ttk.Combobox(window4)
    combo['values'] = ("Мужской", "Женский")
    combo.place(x=250, y=400)
    label = Label(window4, text="Пол:",
                  font=("Times new roman", 15), bg="#363636", fg="#D3D3D3")
    label.place(x=100, y=400)
    btn = Button(window4, text='Завершить', font=BUTTON_FONT, bg="#D3D3D3", fg="black", command=personal_account)
    btn.place(x=260, y=480)


def personal_account():                                      #личный аккаунт
    window6 = tk.Tk()
    window6.title('Личный кабинет!')
    window6.geometry('900x650')
    window6.config(bg='#363636')
    window6.resizable(False, False)

    message = StringVar()

    btn = Button(window6, text='Наши\nинструктора', font=BUTTON_FONT, bg="#D3D3D3", fg="black", command=instroock)
    btn.place(x=70, y=100)
    btn = Button(window6, text='Расписание\nгрупповых занятий', font=BUTTON_FONT, bg="#D3D3D3", fg="black", command=schedule)
    btn.place(x=70, y=220)
    btn = Button(window6, text='Рассписание\n персональных занятий', font=BUTTON_FONT, bg="#D3D3D3", fg="black", command=schedule)
    btn.place(x=70, y=340)
    btn = Button(window6, text='Услуги фитнес\n клуба', font=BUTTON_FONT, bg="#D3D3D3", fg="black", command=services)
    btn.place(x=70, y=460)
    label = Label(window6, text="Персональные даанные",
                  font=("Times new roman", 15), bg="#363636", fg="#D3D3D3")
    label.place(x=550, y=55)
    label = Label(window6, text="Фамилия, Имя,\nОтчество",
                  font=("Times new roman", 15), bg="#363636", fg="#D3D3D3")
    label.place(x=350, y=100)
    label = Label(window6, text="Телефон",
                  font=("Times new roman", 15), bg="#363636", fg="#D3D3D3")
    label.place(x=375, y=230)
    entry_phone = Entry(window6, width=50)
    entry_phone.place(x=540, y=230)
    label = Label(window6, text="Email",
                  font=("Times new roman", 15), bg="#363636", fg="#D3D3D3")
    label.place(x=380, y=350)
    entry_email = Entry(window6, width=50)
    entry_email.place(x=540, y=350)
    label = Label(window6, text="Возвраст",
                  font=("Times new roman", 15), bg="#363636", fg="#D3D3D3")
    label.place(x=376, y=470)
    entry_email = Entry(window6, width=50)
    entry_email.place(x=540, y=470)

    btn = Button(window6, text='Изменить', font=BUTTON_FONT, bg="#D3D3D3", fg="black")
    btn.place(x=700, y=590)


def instroock():                                        #Наши иструктора
    window15 = tk.Tk()
    window15.title('Наши инструктора')
    window15.geometry('1000x700')
    window15.rowconfigure(index=0, weight=1)
    window15.columnconfigure(index=0, weight=1)
    window15.resizable(False, False)
    heads = ['ФИО', 'Опыт работы', 'Специализация', 'Образование']
    people = [('Криворучко Александр', 'Более 5 лет', 'Персональный тренер.Подбор питания. Силовые '
                                                      'тренировки силы и сухой мышечной массы.'
                                                      'Кростфит, тренировки направленные на коррекцию'
                                                      'тела и увеличение выносливости и сжигания жира.'
                                                      'ЛФК тренировки. Направленные на восстановления'
                                                      'спортсмена. Подготовка к более серьезным силовым'
                                                      'нагрузкам.',                                        'Выпускник МГАФК'),
              ('Иванова Марина', 'Более 7 лет',       'Аэробика, степ-аэробика, силовой и функциональный'
                                                      'тренинг, стрейчинг, суставная гимнастика, зумба.',  'Выпускница ООО "СтартФит", Диплом по специализации: Инструктор-универсал групповых'
                                                                                                           'программ, фитнес аэробики. Сертифицированный инструктор по миофасциальному релизу.'),
              ('Самсонов Максим', 'Более 3 лет',      'Аэробика, степ-аэробика, силовой и функциональный'
                                                      'тренинг, стрейчинг, суставная гимнастика, зумба.',  'МГАФК (бывш.МОГИФК) 19 Факультет физической культуры Кафедра теории и методики'
                                                                                                           'физического воспитания'),
              ('Иванов Виталий', 'Более 10 лет ',     'Составление тренировочных программ. Коррекция веса'
                                                      'и фигуры. Функциональный тренинг, повышение '
                                                      'мышечной массы. Составление плана питания.',        'Мастер спорта по taekwon-do ITF Выпускник КГУФКСТ Закончил курсы школы фитнеса и'
                                                                                                           'бодибилдинга Варвары Медведевой'),
              ('Полина Ульянова', 'Более 6 лет',      'Инструктор Йоги. Дыхательные практики и практику '
                                                      'асан. Силовыеи гибкостные упражнения.',             'Иструктор-методист по адаптивной физической культуре.'),
              ('Никита Козлов', 'Более 12 лет',        'Единоборства, бокс Многократный чемпион Москвы.'
                                                      'Призер кубка России среди мужчин 2010г. Чемпион'
                                                      'Спартакиады России среди молодежи 2010г. Призер'
                                                      'международного турнира RUSSIA OPEN 2012.',          'Выпускник Московского Института Физической Культуры и Спорта 2012г.')]

    table = ttk.Treeview(window15, show='headings')
    table['columns'] = heads

    for header in heads:
        table.heading(header, text=header, anchor='w')

    for row in people:
        table.insert('', 0, values=row)

    scroll_pane =ttk.Scrollbar(window15, command=table.yview)
    table.configure(yscrollcommand=scroll_pane.set)
    scroll_pane.pack(side=tk.RIGHT, fill=tk.Y)
    table.pack(expand=tk.YES, fill=tk.BOTH)


def schedule():                                       #расписание
    pass

def services():                                          #Предлагаемые услуги
    window14 = tk.Tk()
    window14.title('Личный кабинет!')
    window14.geometry('855x650')
    window14.config(bg='#363636')
    window14.resizable(False, False)
    label = Label(window14, text="Услуги",
                  font=("Times new roman", 15), bg="#363636", fg="#FFFAFA")
    label.pack(side=TOP, pady=50)
    label = Label(window14, text="Спортивная фигура располагает к вам людей, а безупречное здоровье\n позволяет жить полной и активной жизнью!"
                                "Настало время прислушаться\n к собственному организму, привести в порядок мышцы, избавиться от\n лишнего"
                                " веса,стать стройным, подтянутым, а главное – здоровым.",
                  font=("Times new roman", 15), bg="#363636", fg="#FFFAFA")
    label.place(x=110, y=100)
    btn = Button(window14, width=11, height=2, text='Групповые\nзанятия', font=BUTTON_FONT, bg="#D3D3D3", fg="black", command=group_lessons)
    btn.place(x=130, y=240)
    btn = Button(window14, width=11, height=2, text='Персональный\nтренинг', font=BUTTON_FONT, bg="#D3D3D3", fg="black", command=personal_training)
    btn.place(x=360, y=240)
    btn = Button(window14, width=11, height=2, text='Кросфит', font=BUTTON_FONT, bg="#D3D3D3", fg="black", command=crossfit)
    btn.place(x=590, y=240)
    btn = Button(window14, width=11, height=2, text='Тренажерный\nзал', font=BUTTON_FONT, bg="#D3D3D3", fg="black", command=gym)
    btn.place(x=130, y=350)
    btn = Button(window14, width=11, height=2, text='Сауна', font=BUTTON_FONT, bg="#D3D3D3", fg="black", command=sauna)
    btn.place(x=360, y=350)
    btn = Button(window14, width=11, height=2, text='Йога', font=BUTTON_FONT, bg="#D3D3D3", fg="black", command=yoga)
    btn.place(x=590, y=350)
    btn = Button(window14, width=11, height=2, text='Единоборства', font=BUTTON_FONT, bg="#D3D3D3", fg="black", command=martial)
    btn.place(x=130, y=460)
    btn = Button(window14, width=11, height=2, text='Студия\nзагара', font=BUTTON_FONT, bg="#D3D3D3", fg="black", command=sunburn)
    btn.place(x=360, y=460)
    btn = Button(window14, width=11, height=2, text='Тайский\nбокс', font=BUTTON_FONT, bg="#D3D3D3", fg="black", command=thai_box)
    btn.place(x=590, y=460)
    btn = Button(window14, text='Вернуться', font=BUTTON_FONT, bg="#D3D3D3", fg="black", command=window14.destroy)
    btn.pack(side=BOTTOM, pady=35)


def group_lessons():
    window7 = tk.Tk()
    window7.title('Групповые занятия!')
    window7.geometry('865x600')
    window7.config(bg='#363636')
    window7.resizable(False, False)
    main_frame = Frame(window7, bg='#363636')
    main_frame.pack(fill=BOTH, expand=1)

    canvas = Canvas(main_frame, bg='#363636')
    canvas.pack(side=LEFT, fill=BOTH, expand=1)
    #
    scroll_bar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
    scroll_bar.pack(side=RIGHT, fill=Y)
    #
    canvas.configure(yscrollcommand=scroll_bar.set,)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    working_frame = Frame(canvas, bg='#363636')
    working_frame.pack(fill=BOTH, anchor='nw')

    canvas.create_window((0, 0), window=working_frame, anchor='nw')

    group_label = Label(working_frame,  text="Групповые занятия", font=TIMES_NEW_ROMAN_BOLD, fg="#D3D3D3", bg='#363636')
    group_label.pack(anchor=NW, pady=3, padx=20)

    group_text = Label(working_frame, justify=LEFT, text=GROUP_LESSONS, font=TIMES_NEW_ROMAN_MAIN, fg="#D3D3D3", bg='#363636')
    group_text.pack(anchor=NW, pady=10, padx=20)

    force_label = Label(working_frame, text="Силовая программа", font=TIMES_NEW_ROMAN_BOLD, fg="#D3D3D3", bg='#363636')
    force_label.pack(anchor=NW, pady=3, padx=20)

    force_text = Label(working_frame, justify=LEFT, text=BODY_STRONG, font=TIMES_NEW_ROMAN_MAIN, fg="#D3D3D3", bg='#363636')
    force_text.pack(anchor=NW, pady=10, padx=20)

    stretch_label = Label(working_frame, text="Растяжка", font=TIMES_NEW_ROMAN_BOLD, fg="#D3D3D3", bg='#363636')
    stretch_label.pack(anchor=NW, pady=3, padx=20)

    stretch_text = Label(working_frame, justify=LEFT, text=STRETCH, font=TIMES_NEW_ROMAN_MAIN, fg="#D3D3D3", bg='#363636')
    stretch_text.pack(anchor=NW, pady=10, padx=20)

    return_btn = Button(working_frame, text='Вернуться', font=BUTTON_FONT, bg="#D3D3D3", fg="black", command=window7.destroy)
    return_btn.pack(anchor=S, pady=15)




def personal_training():
    window8 = tk.Tk()
    window8.title('Персональный тренинг!')
    window8.geometry('650x390')
    window8.config(bg='#363636')
    window8.resizable(False, False)
    label = Label(window8, text="Персональный тренинг",
                  font=TIMES_NEW_ROMAN_BOLD, bg="#363636", fg="#D3D3D3")
    label.place(x=20, y=30)
    perstrain_label = Label(window8, justify=LEFT, text=PERSTRAIN, font=TIMES_NEW_ROMAN_MAIN, fg="#D3D3D3", bg='#363636')
    perstrain_label.place(x=20, y=80)
    btn = Button(window8, text='Вернуться', font=BUTTON_FONT, bg="#D3D3D3", fg="black",
                 command=window8.destroy)
    btn.pack(side=BOTTOM, pady=20)

def crossfit():
    window9 = tk.Tk()
    window9.title('Кростфит!')
    window9.geometry('650x435')
    window9.config(bg='#363636')
    window9.resizable(False, False)
    label = Label(window9, text="Кростфит",
                  font=TIMES_NEW_ROMAN_BOLD, bg="#363636", fg="#D3D3D3")
    label.place(x=20, y=30)
    crossfit_text = Label(window9, justify=LEFT, text=CROSSFIT, font=TIMES_NEW_ROMAN_MAIN, fg="#D3D3D3", bg='#363636')
    crossfit_text.place(x=20, y=80)
    btn = Button(window9, text='Вернуться', font=BUTTON_FONT, bg="#D3D3D3", fg="black",
                 command=window9.destroy)
    btn.pack(side=BOTTOM, pady=20)



def gym():
    window10 = tk.Tk()
    window10.title('Тренажерный зал!')
    window10.geometry('650x370')
    window10.config(bg='#363636')
    window10.resizable(False, False)
    label = Label(window10, text="Тренажерный зал",
                  font=TIMES_NEW_ROMAN_BOLD, bg="#363636", fg="#D3D3D3")
    label.place(x=20, y=30)
    gym_text = Label(window10, justify=LEFT, text=GYM, font=TIMES_NEW_ROMAN_MAIN, fg="#D3D3D3", bg='#363636')
    gym_text.place(x=20, y=80)
    btn = Button(window10, text='Вернуться', font=BUTTON_FONT, bg="#D3D3D3", fg="black",
                 command=window10.destroy)
    btn.pack(side=BOTTOM, pady=20)


def sauna():
    window11 = tk.Tk()
    window11.title('Сауна!')
    window11.geometry('650x370')
    window11.config(bg='#363636')
    window11.resizable(False, False)
    label = Label(window11, text="Сауна",
                  font=TIMES_NEW_ROMAN_BOLD, bg="#363636", fg="#D3D3D3")
    label.place(x=20, y=30)
    sauna_text = Label(window11, justify=LEFT, text=SAUNA, font=TIMES_NEW_ROMAN_MAIN, fg="#D3D3D3", bg='#363636')
    sauna_text.place(x=20, y=80)
    btn = Button(window11, text='Вернуться', font=BUTTON_FONT, bg="#D3D3D3", fg="black",
                 command=window11.destroy)
    btn.pack(side=BOTTOM, pady=20)


def yoga():
    window16 = tk.Tk()
    window16.title('Йога')
    window16.geometry('865x600')
    window16.config(bg='#363636')
    window16.resizable(False, False)
    main_frame = Frame(window16, bg='#363636')
    main_frame.pack(fill=BOTH, expand=1)

    canvas = Canvas(main_frame, bg='#363636')
    canvas.pack(side=LEFT, fill=BOTH, expand=1)
    #
    scroll_bar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
    scroll_bar.pack(side=RIGHT, fill=Y)
    #
    canvas.configure(yscrollcommand=scroll_bar.set, )
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    working_frame = Frame(canvas, bg='#363636')
    working_frame.pack(fill=BOTH, anchor='nw')

    canvas.create_window((0, 0), window=working_frame, anchor='nw')

    label = Label(working_frame, text="Йога",
                  font=TIMES_NEW_ROMAN_BOLD, bg="#363636", fg="#D3D3D3")
    label.pack(anchor=NW, pady=10, padx=20)
    yoga_text = Label(working_frame, justify=LEFT, text=YOGA, font=TIMES_NEW_ROMAN_MAIN, fg="#D3D3D3", bg='#363636')
    yoga_text.pack(anchor=NW, pady=10, padx=20)
    btn = Button(working_frame, text='Вернуться', font=BUTTON_FONT, bg="#D3D3D3", fg="black",
                 command=window16.destroy)
    btn.pack(side=BOTTOM, pady=20)



def thai_box():
    window18 = tk.Tk()
    window18.title('Тайский бокс')
    window18.geometry('865x600')
    window18.config(bg='#363636')
    window18.resizable(False, False)
    main_frame = Frame(window18, bg='#363636')
    main_frame.pack(fill=BOTH, expand=1)

    canvas = Canvas(main_frame, bg='#363636')
    canvas.pack(side=LEFT, fill=BOTH, expand=1)
    #
    scroll_bar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
    scroll_bar.pack(side=RIGHT, fill=Y)
    #
    canvas.configure(yscrollcommand=scroll_bar.set, )
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    working_frame = Frame(canvas, bg='#363636')
    working_frame.pack(fill=BOTH, anchor='nw')

    canvas.create_window((0, 0), window=working_frame, anchor='nw')

    label = Label(working_frame, text="Тайский бокс",
                  font=TIMES_NEW_ROMAN_BOLD, bg="#363636", fg="#D3D3D3")
    label.pack(anchor=NW, pady=10, padx=20)
    thai_text = Label(working_frame, justify=LEFT, text=THAI, font=TIMES_NEW_ROMAN_MAIN, fg="#D3D3D3", bg='#363636')
    thai_text.pack(anchor=NW, pady=10, padx=20)
    btn = Button(working_frame, text='Вернуться', font=BUTTON_FONT, bg="#D3D3D3", fg="black",
                 command=window18.destroy)
    btn.pack(side=BOTTOM, pady=20)


def martial():
    window13 = tk.Tk()
    window13.title('Единоборства')
    window13.geometry('650x500')
    window13.config(bg='#363636')
    window13.resizable(False, False)
    main_frame = Frame(window13, bg='#363636')
    main_frame.pack(fill=BOTH, expand=1)

    canvas = Canvas(main_frame, bg='#363636')
    canvas.pack(side=LEFT, fill=BOTH, expand=1)
    #
    scroll_bar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
    scroll_bar.pack(side=RIGHT, fill=Y)
    #
    canvas.configure(yscrollcommand=scroll_bar.set, )
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    working_frame = Frame(canvas, bg='#363636')
    working_frame.pack(fill=BOTH, anchor='nw')

    canvas.create_window((0, 0), window=working_frame, anchor='nw')

    label = Label(working_frame, text="Единоборства",
                  font=TIMES_NEW_ROMAN_BOLD, bg="#363636", fg="#D3D3D3")
    label.pack(anchor=NW, pady=10, padx=20)
    label = Label(working_frame, justify=LEFT,
                  text="Каждый родитель желает, чтобы его ребенок рос здоровым и достойным человеком.\nИменно с этими целями,"
                       "принимается решение — отдать свое чадо заниматься боевыми\nискусствами. Клуб  предлагает выбрать "
                       "одно из боевых искусств для вашего ребенка:",
                  font=TIMES_NEW_ROMAN_MAIN, bg="#363636", fg="#D3D3D3")
    label.pack(anchor=NW, pady=10, padx=20)
    label = Label(working_frame, justify=LEFT,
                  text="Бокс",
                  font=TIMES_NEW_ROMAN_BOLD, bg="#363636", fg="#D3D3D3")
    label.pack(anchor=NW, pady=10, padx=20)
    label = Label(working_frame, justify=LEFT,
                  text="Контактная борьба, где противники наносят друг другу удары в специальных перчатках.\n"
                       "Запрещены удары ногами, локтями, головой, всевозможные броски и захваты. Бокс\nразвивает"
                       "координацию, реакцию и маневрирование. Бокс годится для активных детей,\nстремящихся к"
                       "самоутверждению. Но учтите, что это очень травмоопасный спорт.\nТравмы головы в боксе не редкость.",
                  font=TIMES_NEW_ROMAN_MAIN, bg="#363636", fg="#D3D3D3")
    label.pack(anchor=NW, pady=10, padx=20)
    label = Label(working_frame, justify=LEFT,
                  text="Тхэквондо",
                  font=TIMES_NEW_ROMAN_BOLD, bg="#363636", fg="#D3D3D3")
    label.pack(anchor=NW, pady=10, padx=20)
    label = Label(working_frame, justify=LEFT,
                  text="Боевое искусство родом из Кореи. 70% техники строится на выполнении ударов, в том\nчисле ногами,"
                       "прыжков и блоков. В тхэквондо следует отдавать подвижных и выно-\nсливых детей. Они получат хорошую"
                       "растяжку, разовьют мускулатуру, поработают над\nкоординацией.",
                  font=TIMES_NEW_ROMAN_MAIN, bg="#363636", fg="#D3D3D3")
    label.pack(anchor=NW, pady=10, padx=20)
    label = Label(working_frame, justify=LEFT,
                  text="Самбо",
                  font=TIMES_NEW_ROMAN_BOLD, bg="#363636", fg="#D3D3D3")
    label.pack(anchor=NW, pady=10, padx=20)
    label = Label(working_frame, justify=LEFT,
                  text="Российский вид борьбы, напоминающий восточное дзюдо. Его суть — это «самооборона\n без оружия». В"
                       "самбо, в отличие от дзюдо, запрещается наносить удушающие приемы,\n а болевые наоборот разрешены.",
                  font=TIMES_NEW_ROMAN_MAIN, bg="#363636", fg="#D3D3D3")
    label.pack(anchor=NW, pady=10, padx=20)
    btn = Button(working_frame, text='Вернуться', font=BUTTON_FONT, bg="#D3D3D3", fg="black",
                 command=window13.destroy)
    btn.pack(anchor=S, pady=15)


def sunburn():
    window14 = tk.Tk()
    window14.title('Студия загара!')
    window14.geometry('650x500')
    window14.config(bg='#363636')
    window14.resizable(False, False)
    label = Label(window14, text="Студия загара",
                  font=TIMES_NEW_ROMAN_BOLD, bg="#363636", fg="#D3D3D3")
    label.place(x=20, y=30)
    sunburn_text = Label(window14, justify=LEFT, text=SUNBURN, font=TIMES_NEW_ROMAN_MAIN, fg="#D3D3D3", bg='#363636')
    sunburn_text.place(x=20, y=80)
    btn = Button(window14, text='Вернуться', font=BUTTON_FONT, bg="#D3D3D3", fg="black",
                 command=window14.destroy)
    btn.pack(side=BOTTOM, pady=20)

window = tk.Tk()
window.title('Здравствуйте!')
window.geometry('700x430')
window.config(bg='#363636')
window. resizable(False, False)
lbl = Label(window, text="Приветствуем вас в нашем фитнес приложении! \nУ вас уже есть учетная запись?",
            font=("Times new roman", 15), bg="#363636", fg="#FFFAFA")
lbl.place(x=150, y=150)
btn = Button(window, text='Регестрация', font=BUTTON_FONT, bg="#D3D3D3", fg="black", command=rega)
btn.place(x=30, y=345)
btn = Button(window, text='Войти', font=BUTTON_FONT, bg="#D3D3D3", fg="black", command=enter)
btn.place(x=600, y=345)
window.mainloop()


if __name__ == '__main__':
    enter(test_mode=True)





