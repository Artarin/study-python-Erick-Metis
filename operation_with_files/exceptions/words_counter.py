"""this program search and counting quontity of simple word in text.file"""
pre_path = "books_for_analysis//"
books = ["Életbölcseség.txt",
         "Chambers's.txt",
         "Crash Beam by John Barrett.txt" 
         ]
for book in books:
    print (book +':')
    with open (pre_path+book, 'r', encoding='utf-8') as f:
        text = f.read()
        print (("count 'the...':") + str(text.lower().count('the')))
        print (("count 'the':") + str(text.lower().count('the ')))