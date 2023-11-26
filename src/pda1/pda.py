from stack import *

""" 
Define ADT PDA atau PDA Class using OOP Concept
Using concept Nondeterministic PDA by final state
"""

class PDA:
  # Constructor atau Prosedur CreatePDA
  # Init by default
  # Coba bikin override pakai: input .txt file, input manual by tuples
  def __init__(self):
    """ Declare tuples with 6 elements, containing
    1. Set of States
    2. Set of Input Symbols
    3. Set of Stack Symbols
    4. Set of production rules (current state, read symbol, pop from stack, next state, push to stack)
    5. Starting state ("q0" by default)
    6. Starting stack ("Z0" by default)
    7. Set of Accepting States (only {"F"} by default)
    8. [Optinal] 2 Mode: E by empty stack and F by accepting states
    9. Stack to track
    ++ Mode: Translate to CFG, then to CNF, check use Left Derivations (Too Complex, Difficult, and NGULIII T-T)
    Stack, and production rules in form of Dictionary
    """
    # Make Configuration instead: CurrentState, RemainingInput, Stack
    self.States = set("q0", "qf") # First element as starting state
    self.InputSymbols = set()     # Input string to read symbol by symbol, as remaining input tracker
    self.StackSymbols = set("Z0") # First element as starting state
    self.ProductionRules = set()
    self.FinalStates = set("qf")
    # self.AcceptanceMode = "FinalState" or "EmptyStack"
    self.CurrentConfiguration = set("q0", "<html></html>", Stack())

  # Fungsi untuk cek konfigurasi HTML (by Instance Definition or ID)
  def readInput(self, input):
    pass
  
  # Fungsi untuk cek HTML, mengembalikan true jika .html sudah sesuai
  def acceptInput(self, input):
    pass
  
  # Fungsi untuk menyalin PDA ???
  def copy(self):
    pass
  
  # Prosedur untuk parse/read file ke InputSymbols
  def readFile(filename):
    pass
  
  # Prosedur handling by exceptions to validate config (?) to parsed PDA files
  def validate(self):
    pass
  
  # Gtw buat apa, barangkali penting
  def hasEpsilonTransition(self, config):
    pass
  
  # Prosedur untuk mengubah config dengan langkah berdasarkan production
  def replaceStackTop(conf, production):
    pass

  # Fungsi return true, jika mencapai final state
  # That's why by final state is simpler to implement
  # Dipanggil hanya ketika remaining HTML is empty string ""
  def hasAccepted(conf):
    pass
  
  # NPDA methods
  # Handle to raise error when failed (symbol invalid)
  def validateTransitionSymbol(self):
    pass
  
  # Fungsi untuk mengembalikan nilai transisi sesuai aturan produksi yang diberikan
  def getTransition(self):
    pass
  
  # Fungsi untuk mengembalikan next config sesuai transisi yang sudah diproduksi di atas
  def getNextConfiguration(self):
    pass
  
  # Prosedur untuk membaca input dan memprosesnya (ID* atau |-*)
  def readInputStepWise(self):
    pass