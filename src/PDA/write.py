file1 = open("html.txt", "a")  # append mode
for i in range(ord('c'), ord('s')):
    file1.write('3 ' + chr(i) + ' 3 ' + chr(i) + ' ' + chr(i) + '3\n')
file1.close()