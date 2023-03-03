from tkinter import messagebox
import tkinter as tk
from tkinter import *
import re
from tkinter import ttk
from tkinter.ttk import Combobox


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
    window1 = tk.Tk()
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
    btn = Button(window1, text='Назад', font=("Times new roman", 16), bg="#D3D3D3", fg="black", command=window1.destroy)
    btn.place(x=70, y=500)
    btn = Button(window1, text='Создать', font=("Times new roman", 16), bg="#D3D3D3", fg="black", command=completion_registration)
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
    btn = Button(window2, text='Повторить', font=("Times new roman", 16), bg="blue", fg="white", command=rega)
    btn.place(x=250, y=450)



def enter():                                          #Вход в приложение
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
    btn = Button(window3, text='Назад', font=("Times new roman", 16), bg="#D3D3D3", fg="#000000", command=window3.destroy)
    btn.place(x=70, y=500)
    btn = Button(window3, text='Войти', font=("Times new roman", 16), bg="#D3D3D3", fg="#000000", command=personal_account)#, command=warrning2)
    btn.place(x=520, y=500)

def warrning2():                                   #ошибка входа, не верный пароль
    window5 = tk.Tk()
    window5.title('Ошибка!')
    window5.geometry('600x500')
    window5.config(bg='#363636')
    window5.resizable(False, False)
    label = Label(window5, text="У вас введен неверно\nпороль или логин",
                  font=("Times new roman", 20), bg="#363636", fg="red")
    label.pack(expand=1)
    btn = Button(window5, text='Повторить', font=("Times new roman", 16), bg="blue", fg="white", command=window5.destroy)
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
    combo = Combobox(window4)
    combo['values'] = ("Мужской", "Женский")
    combo.place(x=250, y=400)
    label = Label(window4, text="Пол:",
                  font=("Times new roman", 15), bg="#363636", fg="#D3D3D3")
    label.place(x=100, y=400)
    btn = Button(window4, text='Завершить', font=("Times new roman", 16), bg="#D3D3D3", fg="black", command=personal_account)
    btn.place(x=260, y=480)

def personal_account():                                      #личный аккаунт
    window6 = tk.Tk()
    window6.title('Личный кабинет!')
    window6.geometry('900x650')
    window6.config(bg='#363636')
    window6.resizable(False, False)

    message = StringVar()

    btn = Button(window6, text='Наши\nинструктора', font=("Times new roman", 16), bg="#D3D3D3", fg="black", command=instroock)
    btn.place(x=70, y=100)
    btn = Button(window6, text='Расписание\nгрупповых занятий', font=("Times new roman", 16), bg="#D3D3D3", fg="black", command=schedule)
    btn.place(x=70, y=220)
    btn = Button(window6, text='Рассписание\n персональных занятий', font=("Times new roman", 16), bg="#D3D3D3", fg="black", command=schedule)
    btn.place(x=70, y=340)
    btn = Button(window6, text='Услуги фитнес\n клуба', font=("Times new roman", 16), bg="#D3D3D3", fg="black", command=services)
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

    btn = Button(window6, text='Изменить', font=("Times new roman", 16), bg="#D3D3D3", fg="black")
    btn.place(x=700, y=590)

def instroock():                                        #Наши иструктора
    window15 = tk.Tk()
    window15.title('Наши инструктора')
    window15.geometry('1000x700')
    window15.rowconfigure(index=0, weight=1)
    window15.columnconfigure(index=0, weight=1)

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
              ('Никита Козлов', 'Более 12 лет',       'Единоборства, бокс Многократный чемпион Москвы.'
                                                      'Призер кубка России среди мужчин 2010г. Чемпион'
                                                      'Спартакиады России среди молодежи 2010г. Призер'
                                                      'международного турнира RUSSIA OPEN 2012.',          'Выпускник Московского Института Физической Культуры и Спорта 2012г.')]

    table = ttk.Treeview(window15, show='headings')
    table['columns'] = heads

    for header in heads:
        table.heading(header, text=header, anchor='w')
    table.column("ФИО", stretch=NO)

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
    btn = Button(window14, width=11, height=2, text='Групповые\nзанятия', font=("Times new roman", 16), bg="#D3D3D3", fg="black", command=group_lessons)
    btn.place(x=130, y=240)
    btn = Button(window14, width=11, height=2, text='Персональный\nтренинг', font=("Times new roman", 16), bg="#D3D3D3", fg="black", command=personal_training)
    btn.place(x=360, y=240)
    btn = Button(window14, width=11, height=2, text='Кросфит', font=("Times new roman", 16), bg="#D3D3D3", fg="black", command=crossfit)
    btn.place(x=590, y=240)
    btn = Button(window14, width=11, height=2, text='Тренажерный\nзал', font=("Times new roman", 16), bg="#D3D3D3", fg="black", command=gym)
    btn.place(x=130, y=350)
    btn = Button(window14, width=11, height=2, text='Сауна', font=("Times new roman", 16), bg="#D3D3D3", fg="black", command=sauna)
    btn.place(x=360, y=350)
    btn = Button(window14, width=11, height=2, text='Йога', font=("Times new roman", 16), bg="#D3D3D3", fg="black", command=yoga)
    btn.place(x=590, y=350)
    btn = Button(window14, width=11, height=2, text='Единоборства', font=("Times new roman", 16), bg="#D3D3D3", fg="black", command=martial)
    btn.place(x=130, y=460)
    btn = Button(window14, width=11, height=2, text='Студия\nзагара', font=("Times new roman", 16), bg="#D3D3D3", fg="black", command=sunburn)
    btn.place(x=360, y=460)
    btn = Button(window14, width=11, height=2, text='Тайский\nбокс', font=("Times new roman", 16), bg="#D3D3D3", fg="black", command=thai_box)
    btn.place(x=590, y=460)
    btn = Button(window14, text='Вернуться', font=("Times new roman", 16), bg="#D3D3D3", fg="black", command=window14.destroy)
    btn.pack(side=BOTTOM, pady=35)

def group_lessons():
    window7 = tk.Tk()
    window7.title('Групповые занятия!')
    window7.geometry('1210x600')
    window7.config(bg='#363636')

    table = ttk.Treeview(window7)
    scroll_pane = ttk.Scrollbar(window7, command=table.yview)
    table.configure(yscrollcommand=scroll_pane.set)
    scroll_pane.pack(side=tk.RIGHT, fill=tk.Y)
    table.pack(expand=tk.YES, fill=tk.BOTH)

    label = Label(table, text="Групповые занятия",
                  font=("Times new roman", 18, "bold"), bg="#363636", fg="#D3D3D3")
    label.place(x=20, y=30)
    label = Label(table, justify=tk.LEFT, text="Групповые программы  – различные направления фитнеса, которые проводятся в"
                                "группе под руководством тренера.Направление тренировок может быть самое разное —\nэто и йога, и аэробика,"
                                "и единоборства, и пилатес. Преимуществом групповых занятий является ритмичная музыка, под"
                                "которую интересно проводить занятия. Такой\nвид занятий помогает проникнуться общим духом,"
                                "драйвом и азартом, что сказывается на продуктивности занятия. Инновации фитнес клуба  —"
                                "это групповые\nпрограммы в режиме НОН-СТОП! Вы сможете заниматься любое удобное для Вас"
                                "время в наших аэробных залах, оснащенных всем необходимым оборудованием.",
                  font=("Times new roman", 12), bg="#363636", fg="#D3D3D3")
    label.place(x=20, y=80)
    label = Label(table, text="Силовая программа",
                  font=("Times new roman", 18, "bold"), bg="#363636", fg="#D3D3D3")
    label.place(x=20, y=190)
    label = Label(table, justify=tk.LEFT, text="BODY STRONG — силовой эффективный фитнес. Достигается укреплением мышц при помощи дополнительно"
                                "оборудования (бодибары, гантели, амортизаторы),\nи сопротивления веса тела. Супер Стронг делает"
                                "организм более выносливым физически, повышает упругость мышц и их массу. Вы так же эффективно"
                                "избавляться\nот избыточного веса, сжигая жировые отложения и удаления целлюлита. Упражнения высокой"
                                "и средней интенсивности, направлены они на проработку мышц рук,\nягодиц, пресса, спины, плечевого "
                                "пояса и бёдер. BODY LOW — (отангл. «low»- низкий и «body» — тело) – это силовая тренировка, направленная"
                                "на укрепление нижней\n части тела. Функциональные упражнения, были специально разработаны для прокачки"
                                "и укрепления мышц спины, брюшного пресса, ягодиц и ног. Данный тренинг,\nэто занятия для людей с любым"
                                "уровнем физической подготовки. SUPER STRONG — самая эффективная силоваяпрограмма. Коррекция фигуры"
                                "достигается с помощью\nукреплением мышц тела при использовании дополнительного оборудования в"
                                "аэробном зале. ТАЙБО (Tae—bo) — это сочетание элементов боевых искусств и аэробной\nнагрузки."
                                "Тайбо- упражнения под музыку включают элементы движения из таких направлений, как бокс, каратэ"
                                "и тхэквондо, смешанных с аэробными шагами и дополненных\nклассическими силовыми упражнениями ."
                                "Занятие помогают избавляться от жировых отложений и укреплять суставы и мышцы. Тайбо помогает"
                                "сделать ваше тело\nкрепким и красивым (т.к. в работу включаются и активно прорабатываются сразу"
                                "несколько мышечных групп). FITBALL (fitball, “fit”) — оздоровление, “ball” – мяч) –\nэто швейцарский"
                                "эффективный тренажер, гимнастический «чудо-мяч», Фитбол — это хорошая коррекция фигуры, формирование"
                                "осанки, отлично поднимает настроение.\nBODYSCULPT (БодиСкулпт) — силовая разновидность аэробики."
                                "Упражнения bodysculpt идеально подходят тем, кто желает укрепить мышечный корсет. БодиСкулпт не\n"
                                "знает ограничений по возрасту и по уровню физической подготовки, а так же состоянию здоровья."
                                "СТЭП (STEP) — основой СТЭП являются движения, напоминающие\nсобой шаги по лестнице. Основным"
                                "тренажером для использования упражнений это степ-платформа. Которая регулируется по высоте."
                                "SUPER PRESS– Программа\nнаправлена на развитие и укрепление корсета мышц (мышц живота и спины)"
                                "В данных занятиях используется дополнительный инвентарь — гантели, диски, бодибары,\nутяжелители,"
                                "мячи, — стэп платформа. Отдельные базовые упражнения для красивого рельефного пресса по программе"
                                "бодифитнеса. Аэромикс(AeroMix) – это занятие,\nсочетающие в себе аэробную и силовую нагрузки."
                                "Одним словом, это простая, но очень эффективная тренировка для тех, кто желает избавиться от"
                                "избыточного веса и\nукрепить мышцы тела. Аэробика оказывает положительное действие на весь"
                                "организм, нормализуются артериальное давление и деятельность вестибулярного аппарата.\nTRX—"
                                "Это универсальная функциональная тренировка с собственным весом с использованием подвесных"
                                "петель, которая позволяет не только развивать все мышечные\nгруппы, укреплять связки и сухожилия,"
                                "но получать гибкость, ловкость, силу, вестибулярный аппарат, выносливость, а так же эффективно"
                                "развивает мышцы кора\n(Мышцы стабилизаторы)!!! Тренировка TRX подходит для всех возвратных групп,"
                                "для мужчин и женщин, для людей с отклонениями в состоянии здоровья,\nтак же в этой тренировке нет"
                                "никакой осевой нагрузки на позвоночник! TABATA -Высокоинтенсивная интервальная тренировка, цель —"
                                "выполнение максимального\nколичества повторений за минимальное время. Если вы хотите быстро и эффективно"
                                "похудеть или привести мышцы в тонус, то регулярные занятия по протоколу.\nТабата являются отличным"
                                "способом для достижения поставленной цели! HITT -Высокоинтенсивная, скоростная тренировка, которая"
                                "включает в себя силовые\nупражнения с гантелями, штангой, резиновыми петлями на все группы мышц."
                                "Вас ждут такие упражнения как приседания, выпады, отжимания, жим, выпрыгивания,\nпланка и многие другие.",
                  font=("Times new roman", 12), bg="#363636", fg="#D3D3D3")
    label.place(x=20, y=240)
    label = Label(table, text="Растяжка",
                  font=("Times new roman", 18, "bold"), bg="#363636", fg="#D3D3D3")
    label.place(x=20, y=760)
    label = Label(table, justify=tk.LEFT,
                  text="ABS + STRETCH — Это силовое занятие для мышц брюшного пресса и спины в комбинации на растягивание"
                       "основных групп мышц. Программа включает в себя\nочередность интенсивных нагрузок на группы мышц"
                       "пресса и спины с подходами к упражнениям на растяжку и расслабление. FLEX — это совокупность"
                       "упражнений\nна растяжку всех групп мышц, направленный на развитие гибкости и разгрузку суставов,"
                       "улучшение эластичности мышц, восстановление мышечных групп после\nинтенсивных силовых тренировок."
                       "CALLANETIC – это разновидность гимнастика, т.е. многофункциональная система статических упражнений,"
                       "направленных на\nрастяжение и сокращение мышц и вызывающих активность глубоко расположенных"
                       "мышечных групп. STRETCHING— Растяжка мускулатуры тела. Данное занятие\nхорошо развивает"
                       "амплитуду движений, пластичность суставов. Специальные упражнения помогут улучшить дыхание,"
                       "эмоциональное настроение, а также помогут в\nборьбе со стрессом и усталостью. Улучшает гибкость,"
                       "эластичность мышц и связок, подвижность суставов. Помогает снять стресс и расслабиться,"
                       "восстановиться после\nинтенсивных нагрузок,",
                  font=("Times new roman", 12), bg="#363636", fg="#D3D3D3")
    label.place(x=20, y=810)
    btn = Button(table, text='Вернуться', font=("Times new roman", 16), bg="#D3D3D3", fg="black",
                 command=window7.destroy)
    btn.pack(side=BOTTOM, pady=20)



def personal_training():
    window8 = tk.Tk()
    window8.title('Персональный тренинг!')
    window8.geometry('650x390')
    window8.config(bg='#363636')
    window8.resizable(False, False)
    label = Label(window8, text="Персональный тренинг",
                  font=("Times new roman", 18, "bold"), bg="#363636", fg="#D3D3D3")
    label.place(x=20, y=30)
    label = Label(window8, justify=tk.LEFT,
                  text="Персональная тренировка– это занятие, которое тренер проводит лично для вас, с учетом\nваших"
                       "целей, физической формы, индивидуальных особенностей и пожеланий. Ваш\nперсональный тренер –"
                       "проводник в мир здоровья, прекрасного самочувствия и отличной\nформы!Занятие может проходить"
                       "в тренажерном зале, кардио зоне, в зале групповых\nпрограмм. Занимаясь персонально с тренером,"
                       "Вы достигнете поставленной цели за более\nкороткий срок и путём, безопасным для вашего здоровья."
                       "Длительность одной тренировки – от 60 минут. "
                       "Персональный тренинг в нашем фитнес клубе , также"
                       "полон инноваций!\nСпециально для Вас мы разработали программытренировок"
                       "и питания по следующим\n направлениям:\n"
                       "-коррекция веса\n"
                       "-набор мышечной массы\n"
                       "-тонус",
                  font=("Times new roman", 12), bg="#363636", fg="#D3D3D3")
    label.place(x=20, y=80)
    btn = Button(window8, text='Вернуться', font=("Times new roman", 16), bg="#D3D3D3", fg="black",
                 command=window8.destroy)
    btn.pack(side=BOTTOM, pady=20)

def crossfit():
    window9 = tk.Tk()
    window9.title('Кростфит!')
    window9.geometry('650x435')
    window9.config(bg='#363636')
    label = Label(window9, text="Кростфит",
                  font=("Times new roman", 18, "bold"), bg="#363636", fg="#D3D3D3")
    label.place(x=20, y=30)
    label = Label(window9, justify=tk.LEFT,
                  text="Кроссфит  — это программа упражнений на силу и выносливость,"
                       "состоящая в основном\nиз аэробных упражнений, гимнастики (упражнения"
                       "с весом собственного тела) и тяжёлой\nатлетики. CrossFit — это постоянно"
                       "варьируемые функциональные движения, выполн-\nяемыес высокой интенсивностью"
                       "в различных временных интервалах с целью повышения\nтренированности."
                       "Часовое занятие включает в себя разминку, сегмент развития навыков,\n"
                       "высокоинтенсивную тренировку, индивидуальные или групповые растяжки."
                       "В некоторых\nспортивных залах тренировке дня предшествует упражнение"
                       "на развитие силы. Зона\nКроссфита нашего клуба представлена штангами,"
                       "гантелями, гимнастическими кольцами,\nтурниками, медицинскими шарами."
                       "Кроссфит направлен на постоянно меняющиеся,\nвысокоинтенсивные,"
                       "функциональные движения, опираясь на такие дисциплины и\nупражнения"
                       "как: художественная гимнастика, тяжёлая атлетика, пауэрлифтинг,"
                       "стронгмен-\nупражнения, упражнения с весом собственного тела, аэробные"
                       "упражнения. Кроссфит\nФитнесе —это развитие сердечно-сосудистой"
                       "и дыхательной выносливости, мышечной\nвыносливости, силы, гибкости, скорости,"
                       "координации, ловкости и баланса.",
                  font=("Times new roman", 12), bg="#363636", fg="#D3D3D3")
    label.place(x=20, y=80)
    btn = Button(window9, text='Вернуться', font=("Times new roman", 16), bg="#D3D3D3", fg="black",
                 command=window9.destroy)
    btn.pack(side=BOTTOM, pady=20)



def gym():
    window10 = tk.Tk()
    window10.title('Тренажерный зал!')
    window10.geometry('650x370')
    window10.config(bg='#363636')
    window10.resizable(False, False)
    label = Label(window10, text="Тренажерный зал",
                  font=("Times new roman", 18, "bold"), bg="#363636", fg="#D3D3D3")
    label.place(x=20, y=30)
    label = Label(window10, justify=tk.LEFT,
                  text="В тренажерном зале в фитнес клубе к оборудованию мы"
                       "подошли инновационно и теперь\nон включает в себя"
                       "не только все необходимые тренажеры, но и обладает"
                       "удобной\nсистемой навигации, позволяющей всем без"
                       "исключения, даже новичкам, пользоваться\nвсем"
                       "оборудованием в высокой степени эффективности."
                       "Тренажерный зал для занятия\nфитнесом. Кардио зона"
                       "фитнеса укомплектована тренажерами AEROFIT и включает в себя:\n"
                       "-беговые дорожки\n"
                       "-эллипсоиды\n"
                       "-велотренажеры\n"
                       "-степперы",
                  font=("Times new roman", 12), bg="#363636", fg="#D3D3D3")
    label.place(x=20, y=80)
    btn = Button(window10, text='Вернуться', font=("Times new roman", 16), bg="#D3D3D3", fg="black",
                 command=window10.destroy)
    btn.pack(side=BOTTOM, pady=20)


def sauna():
    window11 = tk.Tk()
    window11.title('Сауна!')
    window11.geometry('650x370')
    window11.config(bg='#363636')
    window11.resizable(False, False)
    label = Label(window11, text="Сауна",
                  font=("Times new roman", 18, "bold"), bg="#363636", fg="#D3D3D3")
    label.place(x=20, y=30)
    label = Label(window11, justify=tk.LEFT,
                  text="Фитнес Клуб предлагает вам расслабиться и восстановиться после"
                       "тренировок посе-\nщениемсауны. Благодаря такому подходу вы сможете"
                       "избавиться от накопившихся токси-\nнов и шлаков, что сделает занятия на"
                       "тренажерах более эффективными. Наши специалисты\nпомогут вам с"
                       "выбором температуры и определением продолжительности приема сауны,\n"
                       "чтобы избежать ее вредного влияния."
                       "Посещение сауны отлично влияет на нервную\nсистему."
                       "Даже непродолжительное пребывание в парилке позволит забыть"
                       "обо всех\nневзгодах и проблемах. Поход в сауну – лучшее средство"
                       "расслабиться и избавиться от\nнегативных мыслей, повысить"
                       "настроение. Повышение скорости реакции, улучшение\nкоординации"
                       "и активизация работы сердца – такие положительные изменения"
                       " можно\nзаметить уже после первого посещения парилки.",
                  font=("Times new roman", 12), bg="#363636", fg="#D3D3D3")
    label.place(x=20, y=80)
    btn = Button(window11, text='Вернуться', font=("Times new roman", 16), bg="#D3D3D3", fg="black",
                 command=window11.destroy)
    btn.pack(side=BOTTOM, pady=20)


def yoga():
    pass

def thai_box():
    pass

def martial():
    window13 = tk.Tk()
    window13.title('Единоборства!')
    window13.geometry('650x690')
    window13.config(bg='#363636')
    label = Label(window13, text="Единоборства",
                  font=("Times new roman", 18, "bold"), bg="#363636", fg="#D3D3D3")
    label.place(x=20, y=30)
    label = Label(window13, justify=tk.LEFT,
                  text="Каждый родитель желает, чтобы его ребенок рос здоровым и достойным человеком.\nИменно с этими целями,"
                       "принимается решение — отдать свое чадо заниматься боевыми\nискусствами. Клуб  предлагает выбрать "
                       "одно из боевых искусств для вашего ребенка:",
                  font=("Times new roman", 12), bg="#363636", fg="#D3D3D3")
    label.place(x=20, y=80)
    label = Label(window13, justify=tk.LEFT,
                  text="Бокс",
                  font=("Times new roman", 18, "bold"), bg="#363636", fg="#D3D3D3")
    label.place(x=20, y=165)
    label = Label(window13, justify=tk.LEFT,
                  text="Контактная борьба, где противники наносят друг другу удары в специальных перчатках.\n"
                       "Запрещены удары ногами, локтями, головой, всевозможные броски и захваты. Бокс\nразвивает"
                       "координацию, реакцию и маневрирование. Бокс годится для активных детей,\nстремящихся к"
                       "самоутверждению. Но учтите, что это очень травмоопасный спорт.\nТравмы головы в боксе не редкость.",
                  font=("Times new roman", 12), bg="#363636", fg="#D3D3D3")
    label.place(x=20, y=215)
    label = Label(window13, justify=tk.LEFT,
                  text="Тхэквондо",
                  font=("Times new roman", 18, "bold"), bg="#363636", fg="#D3D3D3")
    label.place(x=20, y=340)
    label = Label(window13, justify=tk.LEFT,
                  text="Боевое искусство родом из Кореи. 70% техники строится на выполнении ударов, в том\nчисле ногами,"
                       "прыжков и блоков. В тхэквондо следует отдавать подвижных и выно-\nсливых детей. Они получат хорошую"
                       "растяжку, разовьют мускулатуру, поработают над\nкоординацией.",
                  font=("Times new roman", 12), bg="#363636", fg="#D3D3D3")
    label.place(x=20, y=390)
    label = Label(window13, justify=tk.LEFT,
                  text="Самбо",
                  font=("Times new roman", 18, "bold"), bg="#363636", fg="#D3D3D3")
    label.place(x=20, y=490)
    label = Label(window13, justify=tk.LEFT,
                  text="Российский вид борьбы, напоминающий восточное дзюдо. Его суть — это «самооборона\n без оружия». В"
                       "самбо, в отличие от дзюдо, запрещается наносить удушающие приемы,\n а болевые наоборот разрешены.",
                  font=("Times new roman", 12), bg="#363636", fg="#D3D3D3")
    label.place(x=20, y=540)
    btn = Button(window13, text='Вернуться', font=("Times new roman", 16), bg="#D3D3D3", fg="black",
                 command=window13.destroy)
    btn.pack(side=BOTTOM, pady=20)


def sunburn():
    window14 = tk.Tk()
    window14.title('Студия загара!')
    window14.geometry('650x500')
    window14.config(bg='#363636')
    label = Label(window14, text="Студия загара",
                  font=("Times new roman", 18, "bold"), bg="#363636", fg="#D3D3D3")
    label.place(x=20, y=30)
    label = Label(window14, justify=tk.LEFT,
                  text="Солярий, как лучи солнца, в разумных дозах не вреден, напротив,"
                       "ультрафиолет, как\nизвестно, способствует повышению иммунитета,"
                       "укреплению костей, а также защищает\nот депрессий. Кроме того,"
                       "после сеанса в солярии кожа становится эластичной, упругой,\n"
                       "красивой, также загар скрывает некоторые дефекты на коже."
                       "В короткие зимние дни нам\nне хватает солнечного света, а"
                       "без него как раз и появляются пресловутые сезонные\nдепрессии,"
                       "так что зимний загар — это непросто хорошая идея, а почти"
                       "необходимость.\nБольные суставы, варикоз, проблемная кожа,"
                       "а также псориаз — прямые показания для\nтого, чтобы посетить солярий."
                       "Искусственный загар не вреден, если вы соблюдаете все\nправила."
                       "Эндокринолог, дерматолог, гинеколог — врачи, с которыми нужно "
                       "обязательно\nпроконсультироваться. Есть ряд препаратов, которые"
                       "способствуют повышению\nсветочувствительности: болеутоляющие,"
                       "антидепрессанты, антибиотики. Часто они\nявляются причиной"
                       "аллергического приступа. Противопоказан солярий и людям, у\n"
                       "которых на теле много родинок. Еще одно противопоказание —"
                       "дерматиты, ведь в таком\nслучае, солярий еще больше пересушит кожу."
                       "Чтобы защитить ваши волосы, воспользу-\nйтесь специальной шапочкой."
                       "А грудь прикрывайте специальными защитными наклей-\nками. Все"
                       "украшения, включая контактные линзы, рекомендуется снять. Перед"
                       "походом в\nсолярий избегайте походов в сауну и пилинг-процедур, чтобы"
                       "не нарушить защитный\nслой кожи.",
                  font=("Times new roman", 12), bg="#363636", fg="#D3D3D3")
    label.place(x=20, y=80)
    btn = Button(window14, text='Вернуться', font=("Times new roman", 16), bg="#D3D3D3", fg="black",
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
btn = Button(window, text='Регестрация', font=("Times new roman", 16), bg="#D3D3D3", fg="black", command=rega)
btn.place(x=30, y=345)
btn = Button(window, text='Войти', font=("Times new roman", 16), bg="#D3D3D3", fg="black", command=enter)
btn.place(x=600, y=345)
window.mainloop()







