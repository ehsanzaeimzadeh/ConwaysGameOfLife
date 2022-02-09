from tkinter import *
import time
# Created by @EhsanZaeimzadeh <ehsan@pigmentory.app>
__author__ = "Ehsan Zaeimzadeh"
__email__ = "ehsan@pigmentory.app"
class GoL():
   #----------
   def __init__(self, aliveList):
      self.m = Tk()
      self.m.wm_title("GoL - Game of Life")
      self.L = 500 # Length
      self.O = 10 # Offset
      self.B = {} # Blocks, or cells
      self.c = Canvas(self.m, width = self.L+self.O, height = self.L+self.O)
      self.c.bind("<Button-1>", self.click)
      self.c.pack()
      self.b = Button(self.m, text = "Evolve!", command = self.start)
      self.b.pack()
     
      for c in range(0, self.L+self.O, self.O):
         for r in range(0, self.L+self.O, self.O):
            if c == 0 or r == 0 or c == self.L or r == self.L:
               self.B["C"+str(c)+"R"+str(r)] = self.c.create_rectangle(c, r, c+self.O, r+self.O, fill = "black")
            else:
               self.B["C"+str(c)+"R"+str(r)] = self.c.create_rectangle(c, r, c+self.O, r+self.O, fill = "white")
      self.turnOn(aliveList)
      mainloop()
   #----------   
   def click(self, event):
      k = "C"+str(int(event.x/10)*10)+"R"+str(int(event.y/10)*10)
      if self.alive(k):
         self.turnOff([k])
      else:
         self.turnOn([k])
        
   #----------
   def start(self):
      dead = []
      alive = []
      for c in range(self.O, self.L, self.O):
         for r in range(self.O, self.L, self.O):
            k = "C"+str(c)+"R"+str(r)
            nrOfAlive = 0
            for i in self.findN(k):
               if self.alive(i):
                  nrOfAlive += 1
                  
            if self.alive(k):
               if nrOfAlive < 2 or nrOfAlive > 3:
                  dead.append(k)
               else:
                  alive.append(k)
            else:
               if nrOfAlive == 3:
                  alive.append(k)
      self.turnOff(dead)
      self.turnOn(alive)    
   #----------
   def alive(self, k):
      if "re" in self.c.itemcget(self.B[k], "fill"):
         return True
      else:
         return False
   #----------
   def turnOn(self, al):
      for l in al:
         self.c.itemconfig(self.B[l], fill="red")
   #----------
   def turnOff(self, dl):
      for l in dl:
         self.c.itemconfig(self.B[l], fill="white")
   #----------
   def findN(self, k):
      c = int(k.split("R")[0][1:])
      r = int(k.split("R")[1])
      return(["C"+str(c-self.O)+"R"+str(r-self.O),
              "C"+str(c-self.O)+"R"+str(r),
              "C"+str(c-self.O)+"R"+str(r+self.O),
              "C"+str(c)+"R"+str(r-self.O),
              "C"+str(c)+"R"+str(r+self.O),
              "C"+str(c+self.O)+"R"+str(r-self.O),
              "C"+str(c+self.O)+"R"+str(r),
              "C"+str(c+self.O)+"R"+str(r+self.O)])
#----------
l1 = ["C200R250", "C210R250", "C220R250", "C230R250", "C240R250", "C250R250", "C260R250", "C270R250", "C280R250", "C290R250"]
l2 = ["C250R230", "C250R270", "C230R230", "C230R240", "C230R250", "C230R260", "C230R270", "C270R230", "C270R240", "C270R250", "C270R260", "C270R270"]
g = GoL(l2)