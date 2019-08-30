import tkinter as tk
import pandas as pd
import os
import PIL.ImageTk
import PIL.Image
import cv2 as cv
from tkinter import ttk

# dataframe index τις φυλες και καθε στηλη θα είναι η ιδιότητα του μάλλον θελει 2 και να παιζω με 0 1


Titles = ['French Script MT', 30]
M_Font = ['Helvetica', 13]

main_db = pd.DataFrame(index=['Goblin', 'Raisen', 'Human', 'Hyirus'],
                       columns=['tribe_one', 'tribe_two', 'class_one', 'class_two', 'class_three'])

tribe_db = pd.DataFrame(columns=['Goblin', 'Raisen', 'Human', 'Hyirus'],
                        index=['tribe_one', 'tribe_two'])

tribe_db.loc['tribe_one', 'Goblin'] = 'Urhara'
tribe_db.loc['tribe_two', 'Goblin'] = 'Ortisclad'
tribe_db.loc['tribe_one', 'Raisen'] = 'Rotten'
tribe_db.loc['tribe_two', 'Raisen'] = 'Clarimoss'
tribe_db.loc['tribe_one', 'Human'] = 'Nazi'
tribe_db.loc['tribe_two', 'Human'] = 'Anarchist'
tribe_db.loc['tribe_one', 'Hyirus'] = 'Oram'
tribe_db.loc['tribe_two', 'Hyirus'] = 'Slen'

classes_db = pd.DataFrame(columns=['race', 'class_one', 'class_two', 'class_three'],
                          index=['Urhara', 'Ortisclad', 'Rotten', 'Clarimoss', 'Nazi', 'Anarchist', 'Oram', 'Slen'])

classes_db.loc['Urhara', 'race'] = 'Goblin'
classes_db.loc['Urhara', 'class_one'] = 'Warlock'   # ok
classes_db.loc['Urhara', 'class_two'] = 'Berserker' # ok
classes_db.loc['Urhara', 'class_three'] = 'Thief'   # ok

classes_db.loc['Ortisclad', 'race'] = 'Goblin'
classes_db.loc['Ortisclad', 'class_one'] = 'Warrior'    # ok
classes_db.loc['Ortisclad', 'class_two'] = 'Mage'   # ok
classes_db.loc['Ortisclad', 'class_three'] = 'Shaman'   # ok

classes_db.loc['Rotten', 'race'] = 'Raisen'
classes_db.loc['Rotten', 'class_one'] = 'Necromancer'   # ok
classes_db.loc['Rotten', 'class_two'] = 'Bone Crusher'  # ok
classes_db.loc['Rotten', 'class_three'] = 'Shadow Shifter'  # ok

classes_db.loc['Clarimoss', 'race'] = 'Raisen'
classes_db.loc['Clarimoss', 'class_one'] = 'Reanimator'     # ok
classes_db.loc['Clarimoss', 'class_two'] = 'Fallen Knight'  # ok
classes_db.loc['Clarimoss', 'class_three'] = 'Blood Caster'     # ok

classes_db.loc['Nazi', 'race'] = 'Human'
classes_db.loc['Nazi', 'class_one'] = 'Sharp Shooter'    # ok
classes_db.loc['Nazi', 'class_two'] = 'Gunsmith'    # ok
classes_db.loc['Nazi', 'class_three'] = 'Medic'

classes_db.loc['Anarchist', 'race'] = 'Human'
classes_db.loc['Anarchist', 'class_one'] = 'Pyromaniac'
classes_db.loc['Anarchist', 'class_two'] = 'Bruiser'
classes_db.loc['Anarchist', 'class_three'] = 'Hacker'

classes_db.loc['Oram', 'race'] = 'Hyirus'
classes_db.loc['Oram', 'class_one'] = 'Hero'
classes_db.loc['Oram', 'class_two'] = 'Slave'
classes_db.loc['Oram', 'class_three'] = 'Noble' # ok

classes_db.loc['Slen', 'race'] = 'Hyirus'
classes_db.loc['Slen', 'class_one'] = 'Priest'  # ok
classes_db.loc['Slen', 'class_two'] = 'Nature Manipulator'
classes_db.loc['Slen', 'class_three'] = 'Dark Artist'


def praise_abort():
    quit()


def pop(tlt, msg):
    popup = tk.Tk()
    popup.wm_title(tlt)
    l1 = tk.Label(popup, text=msg)
    l1.pack()
    b1 = tk.Button(popup, text='Οκ', command=lambda: popup.destroy())
    b1.pack()
    popup.geometry('300x50')
    popup.mainloop()


class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, 'Delivious - D&D®')
        s = ttk.Style()
        s.theme_use('clam')
        container = ttk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        menu_bar = tk.Menu(container)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label='Σχετικά με το DBridger®',
                              command=lambda: pop('Περι Delivious®', 'Προγραμματιστής Γκάτζιαρης Παντελής'))
        file_menu.add_command(label='Έξοδος', command=lambda: praise_abort())
        menu_bar.add_cascade(label='File', menu=file_menu)
        tk.Tk.config(self, menu=menu_bar)
        self.frames = {}

        for F in (Login, CharSheet):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(Login)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Login(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        lab = ttk.Label(self, text='Welcome to Delivious traveler', font=Titles)
        lab2 = ttk.Label(self, text='Enter your name, sir :', font=M_Font)
        nam = ttk.Entry(self)
        lab3 = ttk.Label(self, text='And our secret will be?', font=M_Font)
        pwd = ttk.Entry(self, show='!')
        lab4 = ttk.Label(self, text='Login or Sign Up, It\'s up to you!', font=M_Font)
        btn_container = ttk.Frame(self)

        btn = ttk.Button(btn_container, text='Sign Up!', command=lambda: controller.show_frame(CharSheet))
        btn2 = ttk.Button(btn_container, text='Login', command=lambda: print('yay'))
        lab.pack()
        lab2.pack(padx='10', pady='3')
        nam.pack(padx='10', pady='3')
        lab3.pack(padx='10', pady='3')
        pwd.pack(padx='10', pady='3')
        lab4.pack(padx='10', pady='3')
        btn_container.pack(side='top', padx='10', pady='3')
        btn.pack(side='left', padx='10', pady='3')
        btn2.pack(side='left', padx='10', pady='3')


class CharSheet(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        tribes = []
        classes = []
        default_title = 'What are you?'

        def _clear_all(*args):
            tribe_opt.set('')
            prof_opt.set('')
            wms.config(text=default_title)

        def _update_tribe(*args):
            prof_opt.set('')
            tribes = []
            tribex = list(tribe_db[:][race_opt.get()])
            for line in tribex:
                tribes.append(line)
            tribe_opt.set(tribes[0])
            tribe_opt.config(values=list(tribes))

        def _update_classes(*args):
            classes = []
            classx = list(classes_db.loc[tribe_opt.get()])
            for line in classx:
                classes.append(line)
            del classes[0]
            prof_opt.config(values=list(classes))
            # Goblin
            if prof_opt.get() == 'Berserker':
                _img_selector('Photos\\Goblin\\goblin_berserker.jpg',
                              'Tribe Lores\\Goblin.txt')
            elif prof_opt.get() == 'Mage':
                _img_selector('Photos\\Goblin\\goblin_mage.jpg',
                              'Tribe Lores\\Goblin.txt')
            elif prof_opt.get() == 'Shaman':
                _img_selector('Photos\\Goblin\\goblin_shaman.jpg', 'Tribe Lores\\Goblin.txt')
            elif prof_opt.get() == 'Thief':
                _img_selector('Photos\\Goblin\\goblin_thief.jpg', 'Tribe Lores\\Goblin.txt')
            elif prof_opt.get() == 'Warlock':
                _img_selector('Photos\\Goblin\\goblin_warlock.jpg', 'Tribe Lores\\Goblin.txt')
            elif prof_opt.get() == 'Warrior':
                _img_selector('Photos\\Goblin\\goblin_warrior.jpg', 'Tribe Lores\\Goblin.txt')

            # Human
            elif prof_opt.get() == 'Gunsmith':
                _img_selector('Photos\\Human\\human_gunsmith.jpg', 'Tribe Lores\\Human.txt')
            elif prof_opt.get() == 'Sharp Shooter':
                _img_selector('Photos\\Human\\human_sharp.jpg', 'Tribe Lores\\Human.txt')

            # Hyirus
            elif prof_opt.get() == 'Noble':
                _img_selector('Photos\\Hyirus\\hyirus_noble.jpg', 'Tribe Lores\\Hyirus.txt')
            elif prof_opt.get() == 'Priest':
                _img_selector('Photos\\Hyirus\\hyirus_priest.jpg', 'Tribe Lores\\Hyirus.txt')

            # Raisen
            elif prof_opt.get() == 'Blood Caster':
                _img_selector('Photos\\Raisen\\raisen_blood.jpg', 'Tribe Lores\\Raisen.txt')
            elif prof_opt.get() == 'Bone Crusher':
                _img_selector('Photos\\Raisen\\raisen_bone.jpg', 'Tribe Lores\\Raisen.txt')
            elif prof_opt.get() == 'Fallen Knight':
                _img_selector('Photos\\Raisen\\raisen_fallen.jpg', 'Tribe Lores\\Raisen.txt')
            elif prof_opt.get() == 'Necromancer':
                _img_selector('Photos\\Raisen\\raisen_necro.jpg', 'Tribe Lores\\Raisen.txt')
            elif prof_opt.get() == 'Reanimator':
                _img_selector('Photos\\Raisen\\raisen_reanim.jpg', 'Tribe Lores\\Raisen.txt')
            elif prof_opt.get() == 'Shadow Shifter':
                _img_selector('Photos\\Raisen\\raisen_shadow.jpg', 'Tribe Lores\\Raisen.txt')

        wms = ttk.Label(self, text='What are you?', font=Titles)
        race_window = ttk.Frame(self)
        race_lab = ttk.Label(race_window, text='Race:', font=M_Font)
        race_opt = ttk.Combobox(race_window, values=list(main_db.index), postcommand=_clear_all)
        race_opt.set('Human')
        tribe_lab = ttk.Label(race_window, text='Tribe:', font=M_Font)
        tribe_opt = ttk.Combobox(race_window, values=list(tribes), postcommand=_update_tribe)
        prof_lab = ttk.Label(race_window, text='Class:', font=M_Font)
        prof_opt = ttk.Combobox(race_window, values=list(classes), postcommand=_update_classes)
        prof_opt.bind('<<ComboboxSelected>>', _update_classes)
        race_window.pack(anchor='nw', side='left', padx='10', pady='10')
        btn = ttk.Button(race_window, text='Stat\'s Dealer',
                         command=lambda: (print(race_opt.get(), tribe_opt.get(), prof_opt.get()),
                                          race_window.destroy(),
                                          wms.config(text='Choose Your Traits Wisely')))
        wms.pack()
        race_lab.pack()
        race_opt.pack()
        tribe_lab.pack()
        tribe_opt.pack()
        prof_lab.pack()
        prof_opt.pack()
        btn.pack(padx='10', pady='3')
        hero_container = ttk.Frame(self)
        canvas = ttk.Label(hero_container)
        hero_text = tk.Text(hero_container, font=M_Font)

        def _img_selector(path, path_txt):

            wms.config(text=prof_opt.get())
            cv_img = cv.imread(path)
            cv_img = cv.cvtColor(cv_img, cv.COLOR_BGR2RGB)
            cv_img = PIL.Image.fromarray(cv_img)
            new_img = cv_img.resize((300, 300))
            new_img.save(path + "_resized.jpg", "JPEG", optimize=True)
            new_img = PIL.ImageTk.PhotoImage(new_img)
            canvas.config(image=new_img)
            canvas.image = new_img
            with open(path_txt, 'r') as f:
                hero_text.insert('insert', f.read())
            hero_text.pack(side='left')
            hero_text.config(width=35, height=20, state='disabled')

        hero_container.pack()
        canvas.pack()


app = Main()
app.geometry('800x600')
app.mainloop()
