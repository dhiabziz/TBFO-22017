# TBFO-22017
Tugas Pemrograman  
IF2124 Teori Bahasa Formal dan Otomata 
HTML Checker dengan Pushdown Automata (PDA)

Cara Pemakaian:

Pindah ke Directory PDA.

Pengecekan dengan Spek Bonus:

    "python mainBonus.py html.txt (FileHTML).txt"
    
Pengecekan tanpa Spek Bonus:

    "python main.py html.txt (FileHTML).txt"


STRUKTUR file config:

Q P F # total states

a # input word symbols

Z Y # stack symbols

Q # starting state

Z # starting stack

F # accepting states

Q a Z Q YZ # list of productions (current state, read from word, take from stack, next state, add to stack)

Q a Y Q YY

Q e Z P Z

Q e Y P Y 

P a Z P e 

P a Y P e

P e Z F e
