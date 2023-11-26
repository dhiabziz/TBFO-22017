""" 
Define ADT Stack, but using List as Stack instead
Define (Explicit) Stack Class using OOP concept
"""

class Stack:
  # Constructor atau Prosedur CreateStack
  def __init__(self):
    # Using list as main attribute, but limited to methods will be used
    # Stack limit = infinite/limitless (assumed)
    self.Stack = []
    self.Length = 0
  
  # Representasi string dari Stack untuk print
  def __str__(self):
    PrintStack = ""
    for i in range(len(self.Stack), 0, -1):
      PrintStack += self.Stack[i] + "|"
    return PrintStack

  # Fungsi yang mengembalikan panjang/tinggi Stack
  def getLength(self):
    return self.Length # atau len(self.Stack)

  # Fungsi untuk cek apakah Stack kosong 
  def isEmpty(self):
    return self.Length == 0  # atau size(self) == 0
  
  # Prosedur push
  def push(self, data):
    # data berupa Stack string tags
    self.Stack.append(data)
    self.Length += 1
  
  # Prosedur pop
  def pop(self):
    # handle kasus Stack kosong, jika kosong return None, jika tidak return top value
    if not (self.Length == 0): # atau pakai isEmpty()
      return self.Stack.pop()
    else:
      return None
  
  # Fungsi yang mengembalikan nilai Top dari Stack
  def top(self):
    return self.Stack[-1]
