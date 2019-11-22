from tkinter import *
d={}
l=[]

def add(a,b,c,v):
    if [a,b,c,d] not in l:
        l.append([a,b,c,v])
    d.update({a:b})
    di.set(d)
    print(d)
    print(l)

def upd(a,b,c,v):
    if a in d:
        d[a]=b
        for i in l:
                if a in i:
                    l.remove(i)
                else:
                    print('Value Not Found')
                    
    l.append([a,b,c,v])
    print(d)
    print(l)
    
def dele(a):
    if a in d:
            del d[a]
    else:
            print('Key Not Found')
    for i in l:
        if a in i:
            l.remove(i)
            print(d)
            print(l)
        else:
                print('Value Not Found')

def csvtime():
    import csv
    csvData = l
    with open('book2.csv', 'a',newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(csvData)
    csvFile.close()

def graph():
    import pandas as pd
    import matplotlib.pyplot as plt
    book = pd.read_csv('book2.csv')
    print(book.head(30))
    print()
    print('Total Number of books: ',book.shape[0])
    plt.subplots_adjust(top=0.968,bottom=0.317,left=0.052,right=0.977,hspace=0.2,wspace=0.2)
    pd.Series(book['Category']).value_counts().plot(kind='bar')
    plt.show()

def graph2():
    import pandas as pd
    import matplotlib.pyplot as plt
    book = pd.read_csv('book2.csv')
    print(book.head(30))
    print()
    print('Total Number of books: ',book.shape[0])
    #plt.figure(figsize=(10,10))
    plt.subplots_adjust(top=0.968,bottom=0.344,left=0.073,right=0.977,hspace=0.2,wspace=0.2)
    pd.Series(book['Author']).value_counts().plot(kind='bar')
    plt.show()
    
w=Tk()
w.title('Library Database')
a=StringVar()
b=StringVar()
c=StringVar()

l1=Label(w,text='Library Books PESU EC Campus',width=50,font=("Courier New",18,'bold')).grid(row=0,columnspan=5)
di=StringVar()

e1 = Entry(w,textvariable=a)
e2 = Entry(w,textvariable=b)
e3c = Entry(w,textvariable=c)
e3d = Entry(w,textvariable=d)

e3 = Entry(w)
e4 = Entry(w)
e4c = Entry(w)
e4d = Entry(w)
e5 = Entry(w)

l3=Label(w,text='ISBN',width=30).grid(row=1,column=0)
l4=Label(w,text='Name',width=30).grid(row=1,column=1)
l5=Label(w,text='Author',width=30).grid(row=1,column=2)
l6=Label(w,text='Category',width=30).grid(row=1,column=3)

e1.grid(row=2,column=0)
e2.grid(row=2,column=1)
e3c.grid(row=2,column=2)
e3d.grid(row=2,column=3)

e3.grid(row=3,column=0)
e4.grid(row=3,column=1)
e4c.grid(row=3,column=2)
e4d.grid(row=3,column=3)

e5.grid(row=4,column=0)


b1=Button(w,text='Add',width=10,command= lambda : add(e1.get(),e2.get(),e3c.get(),e3d.get())).grid(row=2,column=4)
b3=Button(w,text='Update',width=10,command= lambda: upd(e3.get(),e4.get(),e4c.get(),e4d.get())).grid(row=3,column=4)
b2=Button(w,text='Delete',width=10,command= lambda: dele(e5.get())).grid(row=4,column=1)

b4=Button(w,text='Update CSV',width=10,command= lambda: csvtime()).grid(row=4,column=4)
b5=Button(w,text='Graph for Category',width=20,command= lambda: graph()).grid(row=4,column=3)
b6=Button(w,text='Graph for Authors',width=20,command= lambda: graph2()).grid(row=4,column=2)


l2=Label(w,textvar=di,width=30).grid(row=5,columnspan=5)

#b3=Button(w,text='Display',width=10,command= setText(str(d))).grid(row=3,column=2)


w.mainloop()
