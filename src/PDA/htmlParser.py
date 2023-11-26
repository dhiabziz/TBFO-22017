from html.parser import HTMLParser
from html.entities import name2codepoint
from re import search

tokenTag = {
    "html" : '1',
    "head" : '2',
    "body" : '3',
    "title" : '4',
    "script" : '5',
    "link" : '6',
    "h1" : '7',
    "h2" : '8',
    "h3" : '9',
    "h4" : 'a',
    "h5" : 'b',
    "h6" : 'c',
    "p" : 'd',
    "br" : 'e',
    "em" : 'f',
    "b" : 'g',
    "abbr" : 'h',
    "strong" : 'i',
    "small" : 'j',
    "hr" : 'k',
    "div" : 'l',
    "a" : 'm',
    "img" : 'n',
    "button" : 'o',
    "form" : 'p',
    "input" : 'q',
    "table" : 'r',
    "tr" : 's',
    "th" : 't',
    "td" : 'u',
}

tokenAttribut = {
    "id" : 'A',
    "class" : 'B',
    "style" : 'C',
    "rel" : 'D',
    "href" : 'E',
    "src" : 'F',
    "alt" : 'G',
    "type" : 'H',
    "action" : 'I',
    "method" : 'J'
}

tokenNilaiAttribut = {
    "submit" : 'K',
    "reset" : 'L',
    "button" : 'M',
    "GET" : 'N',
    "POST" : 'O',
    "text" : 'P',
    "password" : 'Q',
    "email" : 'R',
    "number" : 'S',
    "checkbox" : 'T'
}

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.Myrawdata = ""

    def handle_starttag(self, tag, attrs):
        if (tag in tokenTag):
            self.Myrawdata += tokenTag[tag.strip()]
        else: # Tidak ada di Dict Token
            self.Myrawdata += "!"
        
        for attr in attrs:
            if (attr[0] in tokenAttribut): # cek apakah attribute ada di dict
                # Add Token Attribute
                self.Myrawdata += "*"+tokenAttribut[attr[0].strip()]

                # Add Attribute Value Token if exists {attr}=".*" or {attr}='.*'
                if (search(f'{attr[0]}(\s)*=(\s)*("(.*)"|\'(.*)\')', self.get_starttag_text())):
                    self.Myrawdata += '='

                if (attr[0] == "type" or attr[0] == "method"): # Kalau type atau method, value harus dicek PDA
                    if (attr[1] in tokenNilaiAttribut): # Cek apakah value ada di dict
                        self.Myrawdata += tokenNilaiAttribut[attr[1]]
                    else: # token arbitrary value
                        self.Myrawdata += '!'
            else: # token arbitrary attribute
                self.Myrawdata += "*!"

    def handle_endtag(self, tag):
        if (tag in tokenTag): # Add token endtag
            self.Myrawdata += '/' + tokenTag[tag.strip()]
        else: # Token arbritary 
            self.Myrawdata += "/!"

    def handle_data(self, data):
        if(data.strip() != ""):
            self.Myrawdata += "+"

    def handle_comment(self, data):
        self.Myrawdata += ""