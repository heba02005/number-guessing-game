import random
import tkinter as tk

# عدد المحاولات لكل مستوى
LEVELS = {'سهل': 10, 'متوسط': 7, 'صعب': 5}

FONT = ('Segoe UI', 14)
BIG = ('Segoe UI', 20, 'bold')


class GuessGame:
    def __init__(self, root):
        self.root = root
        root.title('لعبة تخمين الأرقام')
        root.geometry('460x520')
        root.configure(bg='#f4f1ea')

        tk.Label(root, text='🎯 لعبة تخمين الأرقام', font=BIG,
                 bg='#f4f1ea').pack(pady=(20, 5))
        tk.Label(root, text='أنا فكرت في رقم من 1 لـ 100.. تقدر تخمّنه؟',
                 font=FONT, bg='#f4f1ea').pack(pady=5)

        # اختيار المستوى
        self.level = tk.StringVar(value='متوسط')
        frame = tk.Frame(root, bg='#f4f1ea')
        frame.pack(pady=10)
        for name, tries in LEVELS.items():
            tk.Radiobutton(frame, text=f'{name} ({tries})',
                           variable=self.level, value=name, font=FONT,
                           bg='#f4f1ea').pack(side='left', padx=8)

        tk.Button(root, text='ابدأ لعبة جديدة', font=FONT, bg='#2e7d32',
                  fg='white', command=self.start_game).pack(pady=8)

        # معلومات اللعبة
        self.range_label = tk.Label(root, text='', font=FONT, bg='#f4f1ea')
        self.range_label.pack(pady=(15, 2))
        self.attempts_label = tk.Label(root, text='', font=FONT, bg='#f4f1ea')
        self.attempts_label.pack(pady=2)

        # خانة التخمين
        self.entry = tk.Entry(root, font=BIG, width=6, justify='center')
        self.entry.pack(pady=12)
        self.entry.bind('<Return>', lambda e: self.make_guess())

        self.guess_btn = tk.Button(root, text='خمّن', font=FONT, bg='#1565c0',
                                   fg='white', command=self.make_guess,
                                   state='disabled')
        self.guess_btn.pack(pady=5)

        # الرسالة
        self.message = tk.Label(root, text='اختار المستوى واضغط ابدأ',
                                font=('Segoe UI', 15, 'bold'), bg='#f4f1ea',
                                wraplength=420)
        self.message.pack(pady=20)

    def start_game(self):
        self.low = 1
        self.high = 100
        self.count = 0
        self.max_attempts = LEVELS[self.level.get()]
        self.number = random.randint(self.low, self.high)
        self.guess_btn.config(state='normal')
        self.entry.config(state='normal')
        self.entry.delete(0, tk.END)
        self.entry.focus()
        self.update_info()
        self.show('اللعبة بدأت! اكتب تخمينك 👇', '#333333')

    def update_info(self):
        self.range_label.config(
            text=f'الرقم بين {self.low} و {self.high}')
        left = self.max_attempts - self.count
        self.attempts_label.config(text=f'المحاولات المتبقية: {left}')

    def show(self, text, color):
        self.message.config(text=text, fg=color)

    def end_game(self):
        self.guess_btn.config(state='disabled')
        self.entry.config(state='disabled')

    def make_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            self.show('اكتب رقم صحيح من فضلك', '#c62828')
            return

        # خارج المدى أو متجرّب قبل كده: مش بيتحسب محاولة
        if guess < self.low or guess > self.high:
            self.show(f'اكتب رقم بين {self.low} و {self.high}', '#c62828')
            return

        self.count += 1
        self.entry.delete(0, tk.END)

        if guess == self.number:
            self.show(f'🎉 مبروك! خمّنت الرقم {self.number} '
                      f'في {self.count} محاولات', '#2e7d32')
            self.end_game()
            self.update_info()
            return

        if self.count >= self.max_attempts:
            self.show(f'😢 خلصت المحاولات.. الرقم كان {self.number}',
                      '#c62828')
            self.end_game()
            self.update_info()
            return

        if guess < self.number:
            self.low = guess + 1
            self.show('⬆️ الرقم أكبر من كده', '#e65100')
        else:
            self.high = guess - 1
            self.show('⬇️ الرقم أصغر من كده', '#e65100')
        self.update_info()


root = tk.Tk()
GuessGame(root)
root.mainloop()