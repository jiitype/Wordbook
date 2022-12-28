from tkinter import messagebox
import tkinter as tk
import random as rd
import csv


class Application(tk.Frame):
  def __init__(self, master):
    super().__init__(master)
    self.pack()

    self.master.geometry("500x300")
    self.master.title("単語帳アプリ")

    self.word()
    self.setVar()
    self.widgets()

  def widgets(self):
    self.frame1 = tk.Frame(self.master, bd=2, relief="ridge")
    self.frame1.pack(fill="x")

    self.button1 = tk.Button(self.frame1, text="使い方", command=self.howtouse)
    self.button1.pack(side="left")

    self.button2 = tk.Button(self.frame1, text="終了", command=quit)
    self.button2.pack(side="right")

    self.text = tk.StringVar()
    self.text.set(self.wordlist[self.num][0])

    self.label1 = tk.Label(self.master, textvariable=self.text, font=("",28))
    self.label1.pack(pady=25)

    self.frame2 = tk.Frame(self.master)
    self.frame2.pack(fill="x")

    self.canvas = tk.Canvas(self.frame2, bg="white", width=100, height=100)
    self.canvas.pack(side="left", padx=20)

    self.choices()

    self.button3 = tk.Button(self.master, text="判定", command=self.judge)
    self.button3.place(x=190, y=245)

    self.button4 = tk.Button(self.master, text="次へ", command=self.next)
    self.button4.place(x=270, y=245)

    self.text2 = tk.StringVar()
    self.text2.set("")
    
    self.label2 = tk.Label(self.master, textvariable=self.text2, fg="red", font=("",10))
    self.label2.place(x=330, y=248)
    
  def howtouse(self):
    messagebox.showinfo("使い方","正しい答えを選んで判定ボタンを押してください。\n正解すると次の単語へ進めます。")

  def setVar(self):
    self.num = rd.randint(0, len(self.wordlist) - 1)

    self.rdo_check = tk.IntVar()
    self.rdo_check.set(0)

    self.judgenum = 0

  def word(self):
    try:
      f = open("word.csv", "r", encoding = "utf-8-sig")
      self.wordlist = list(csv.reader(f))
      f.close()
    
    except:
      f = open("word.csv", "r")
      self.wordlist = list(csv.reader(f))
      f.close()

  def choices(self):
    rdnum = rd.randint(0, 3)
    self.ans = self.wordlist[self.num][1]
    self.wanum = []
    fontSize = 13
    posx = 190

    while len(self.wanum) <= 4:
      n = rd.randint(0, len(self.wordlist) - 1)
      if n == self.num or n in self.wanum:
        continue
      else:
        self.wanum.append(n)

    for i in range(4):
      if i == 0:
        if i == rdnum:
          self.rdo1 = tk.Radiobutton(self.frame2, value=0, variable=self.rdo_check, text=self.ans, font=("",fontSize))
          self.rdo1.place(x=posx, y=0)
        else:
          self.rdo1 = tk.Radiobutton(self.frame2, value=0, variable=self.rdo_check, text=self.wordlist[self.wanum[i]][1], font=("",fontSize))
          self.rdo1.place(x=posx, y=0)
      
      if i == 1:
        if i == rdnum:
          self.rdo2 = tk.Radiobutton(self.frame2, value=1, variable=self.rdo_check, text=self.ans, font=("",fontSize))
          self.rdo2.place(x=posx, y=25)
        else:
          self.rdo2 = tk.Radiobutton(self.frame2, value=1, variable=self.rdo_check, text=self.wordlist[self.wanum[i]][1], font=("",fontSize))
          self.rdo2.place(x=posx, y=25)
      
      if i == 2:
        if i == rdnum:
          self.rdo3 = tk.Radiobutton(self.frame2, value=2, variable=self.rdo_check, text=self.ans, font=("",fontSize))
          self.rdo3.place(x=posx, y=50)
        else:
          self.rdo3 = tk.Radiobutton(self.frame2, value=2, variable=self.rdo_check, text=self.wordlist[self.wanum[i]][1], font=("",fontSize))
          self.rdo3.place(x=posx, y=50)

      if i == 3:
        if i == rdnum:
          self.rdo4 = tk.Radiobutton(self.frame2, value=3, variable=self.rdo_check, text=self.ans, font=("",fontSize))
          self.rdo4.place(x=posx, y=75)
        else:
          self.rdo4 = tk.Radiobutton(self.frame2, value=3, variable=self.rdo_check, text=self.wordlist[self.wanum[i]][1], font=("",fontSize))
          self.rdo4.place(x=posx, y=75)

  def quit(self):
    self.master.destroy()

  def judge(self):
    checked_num = self.rdo_check.get()
    choices_list = [self.rdo1["text"], self.rdo2["text"], self.rdo3["text"], self.rdo4["text"]]

    if choices_list[checked_num] == self.ans:
      self.draw_maru()
      self.judgenum = 1

    else:
      self.draw_batsu()
      self.judgenum = 2
  
  def draw_maru(self):
    self.canvas.delete("batsu1")
    self.canvas.delete("batsu2")

    self.canvas.create_oval(20, 20, 85, 85, outline="red", width=7, tag="maru")

  def draw_batsu(self):
    self.canvas.delete("maru")

    self.canvas.create_line(20, 20, 85, 85, fill="blue", width=7, tag="batsu1")
    self.canvas.create_line(20, 85, 85, 20, fill="blue", width=7, tag="batsu2")

  def choices_destroy(self):
    self.rdo1.destroy()
    self.rdo2.destroy()
    self.rdo3.destroy()
    self.rdo4.destroy()

  def next(self):
    if self.judgenum == 1:
      self.num = rd.randint(0, len(self.wordlist) - 1)

      self.text.set(self.wordlist[self.num][0])

      self.text2.set("")

      self.choices_destroy()
      self.choices()

      self.canvas.delete("maru")

      self.judgenum = 0
    
    elif self.judgenum == 2:
      self.text2.set("正しい答えを選んでください")

    else:
      self.text2.set("判定ボタンを押してください")


def main():
  win = tk.Tk()
  app = Application(master = win)
  app.mainloop()


if __name__ == "__main__":
  main()
