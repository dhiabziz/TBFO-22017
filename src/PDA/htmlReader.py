import htmlParser
import os

def readHTML(path):
    if(os.path.isfile(path)):
        try:
            with open(path, 'r') as file:
                data = file.read()
        except IOError as e:
            print("File tidak berhasil dibuka!")
            exit()
    else:
        print(path, "Tidak ditemukan! Cek nama file")
        exit()
    
    parser = htmlParser.MyHTMLParser()
    parser.feed(data)
    
    return parser.Myrawdata



    


