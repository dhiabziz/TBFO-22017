tokenTag = {
    '1': 'html', 
    '2': 'head', 
    '3': 'body', 
    '4': 'title', 
    '5': 'script', 
    '6': 'link', 
    '7': 'h1', 
    '8': 'h2', 
    '9': 'h3', 
    'a': 'h4', 
    'b': 'h5', 
    'c': 'h6', 
    'd': 'p', 
    'e': 'br', 
    'f': 'em', 
    'g': 'b', 
    'h': 'abbr', 
    'i': 'strong', 
    'j': 'small', 
    'k': 'hr', 
    'l': 'div', 
    'm': 'a', 
    'n': 'img', 
    'o': 'button', 
    'p': 'form', 
    'q': 'input', 
    'r': 'table', 
    's': 'tr', 
    't': 'th', 
    'u': 'td'
}

tokenAttribut = {
    'A': 'id', 
    'B': 'class', 
    'C': 'style', 
    'D': 'rel', 
    'E': 'href', 
    'F': 'src', 
    'G': 'alt', 
    'H': 'type', 
    'I': 'action', 
    'J': 'method'
}

tokenNilaiAttribut = {
    'K': 'submit', 
    'L': 'reset', 
    'M': 'button', 
    'N': 'GET', 
    'O': 'POST', 
    'P': 'text', 
    'Q': 'password', 
    'R': 'email', 
    'S': 'number', 
    'T': 'checkbox'
}

new1 = {}
new2 = {}
new3 = {}
for key,val in tokenAttribut.items():
    new1[val] = key
for key,val in tokenNilaiAttribut.items():
    new2[val] = key
for key,val in tokenTag.items():
    new3[val] = key

print(new1)
print()
print(new2)
print()
print(new3)