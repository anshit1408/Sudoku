from Tkinter import*
import tkMessageBox
import random
rt=Tk()
rt.title('!!Welcome!!')
v=IntVar()
w=OptionMenu(rt,v,2,3,4)
w.grid(row=2,column=0)
s=v.get()*v.get()
def info():
    tkMessageBox.showinfo('!!Welcome!!','Name:Anshit Hayaran\nE.No.:151239\nBatch:B1\nP.No.:9454535787\nEmail id:anshithayaran14@gmail.com')
def fun(d):
    if d==0:
        tkMessageBox.showerror('!!OOPS!!','`YOU NEED TO SELECT THE DEGREE FIRST`\n <PLEASE RUN THE GAME AGAIN>') 
    s=d*d
    rt.destroy()
    root=Tk()
    root.title('SUDOKU')
    def dest():
        if tkMessageBox.askokcancel('EXIT','Are you sure?'):
            root.destroy()
    c=[[0 for i in range(17)]for j in range(17)]
    e=[[0 for i in range(17)]for j in range(17)]
    b=[[0 for i in range(17)]for j in range(17)]
    a=[0 for i in range(17)]
    t=[1]
    i=1
    while i<s+1:
        j=1
        while j<s+1:
            r=random.randint(1,s)
            if a[r]<s:
                c[i][j]=r
                a[r]+=1
                j+=1
        i+=1
    i=1
    while i<s:
        t.insert(i,i+d)
        i+=d
    i=1
    while i<s+1:
        j=1
        while j<s+1:
            r=random.randint(1,s)
            if i in t:
                if j in t:
                    for k in range(1,d+1):
                        for l in range(1,d+1):
                            for m in range(0,d): 
                                a[m*d+k]=c[j+m][i+k-1]
                    k=1
                    while k<s+1:
                        l=k+1
                        while l<s+1:
                            if a[k]==a[l]:
                                a[l]='*'
                            l+=1
                        k+=1
                    k=1
                    while k<s+1:
                        k+=1
                    for k in range(1,d+1):
                        for l in range(1,d+1):
                            for m in range(0,d):
                                c[j+m][i+k-1]=a[d*m+k]
            for k in range(0,j):
                if c[i][k]==c[i][j]:
                    c[i][j]='*'
            for k in range(0,i):
                if c[k][j]==c[i][j]:
                    c[i][j]='*'
            j+=1
        i+=1
    def hint():
        for i in range(1,s+1):
            for j in range(1,s+1):
                print c[i][j],
            print
        print
    for i in range(1,s+1):
        for j in range(1,s+1):
            e[i][j]=Entry(root,width=4,bg='grey')
            e[i][j].grid(row=i,column=j)
            r=random.randint(1,s)
            ra=random.randint(1,9)
            if ra<6:
                if c[i][j]!='*':
                    e[i][j]=Entry(root,width=4,bg='blue')
                    e[i][j].grid(row=i,column=j)
                    e[i][j].insert(0,c[i][j])
            else: 
                e[i][j]=StringVar()
                e[i][j]=Entry(root,width=4,bg='grey')
                e[i][j].grid(row=i,column=j)
    def nxt():
        for i in range(1,s+1):
            for j in range(1,s+1):
                e[i][j]=Entry(root,width=4,bg='grey')
                e[i][j].grid(row=i,column=j)
                r=random.randint(1,s)
                ra=random.randint(1,9)
                if ra<6:
                    if c[i][j]!='*':
                        e[i][j]=Entry(root,width=4,bg='blue')
                        e[i][j].grid(row=i,column=j)
                        e[i][j].insert(0,c[i][j])
                else: 
                    e[i][j]=StringVar()
                    e[i][j]=Entry(root,width=4,bg='grey')
                    e[i][j].grid(row=i,column=j)
    def check():
        i=1
        while i<s+1:
            j=1
            while j<s+1:
                b[i][j]=e[i][j].get(),
                j+=1
            i+=1
        i=1
        while i<s+1:
            j=1
            while j<s+1:
                if i in t:
                    if j in t:
                        for k in range(1,d+1):
                            for l in range(1,d+1):
                                for m in range(0,d): 
                                    a[m*d+k]=b[j+m][i+k-1]
                        k=1
                        while k<s+1:
                            l=k+1
                            while l<s+1:
                                if a[k]==a[l]:
                                    a[l]='*'
                                l+=1
                            k+=1
                        k=1
                        while k<s+1:
                            k+=1
                        for k in range(1,d+1):
                            for l in range(1,d+1):
                                for m in range(0,d):
                                    b[j+m][i+k-1]=a[d*m+k]          
                for k in range(0,j):
                    if b[i][k]==b[i][j]:
                        b[i][j]='*'
                for k in range(0,i):
                    if b[k][j]==b[i][j]:
                        b[i][j]='*'
                j+=1
            i+=1
        i=1
        def win():
            tkMessageBox.showinfo('!!CONGRATS!!','!YOU WON THE GAME!\n THANK YOU FOR PLAYING THIS GAME : )')
        def loss():
            tkMessageBox.showerror('!!OH NO!!','!YOU WERE NOT ABLE TO COMPLETE THE GAME!\n TRY AGAIN IF U LIKE IT :(') 
        flag=0
        while i<s+1:
            j=1
            while j<s+1:
                if b[i][j]!='*':
                    e[i][j].delete(0,END)
                    e[i][j].insert(0,b[i][j])
                else:
                    e[i][j]=Entry(root,width=4,bg='red')
                    e[i][j].grid(row=i,column=j)
                    e[i][j].delete(0,END)
                    e[i][j].insert(0,b[i][j])
                    flag=1
                j+=1
            i+=1
        if flag==0:
                win()
        elif flag==1:
                loss()
    if d==2:
        Button(root,text='Info',command=info,cursor='trek').grid(row=5,column=2,columnspan=2,sticky=N+E+W+S)
        Button(root,text='Exit',command=dest,bg='red',cursor='pirate').grid(row=7,column=1,columnspan=4,sticky=N+E+W+S)
        Button(root,text='Next',command=nxt,font='Arial 7',cursor='right_side').grid(row=5,column=4,columnspan=1,sticky=N+E+W+S)
        Button(root,text='Hint',command=hint,font='Arial 7',cursor='target').grid(row=5,column=1,columnspan=1,sticky=N+E+W+S)
        Button(root,text='Check',command=check,bg='green',cursor='pencil').grid(row=6,column=1,columnspan=4,sticky=N+E+W+S)
    elif d==3:
        Button(root,text='Info',command=info,cursor='trek').grid(row=10,column=4,columnspan=3,sticky=N+E+W+S)
        Button(root,text='Exit',command=dest,bg='red',cursor='pirate').grid(row=12,column=1,columnspan=9,sticky=N+E+W+S)
        Button(root,text='Next',command=nxt,cursor='right_side').grid(row=10,column=7,columnspan=3,sticky=N+E+W+S)
        Button(root,text='Hint',command=hint,cursor='target').grid(row=10,column=1,columnspan=3,sticky=N+E+W+S)
        Button(root,text='Check',command=check,bg='green',cursor='pencil').grid(row=11,column=1,columnspan=9,sticky=N+E+W+S)
    elif d==4:
        Button(root,text='Info',command=info,cursor='trek').grid(row=17,column=6,columnspan=6,sticky=N+E+W+S)
        Button(root,text='Exit',command=dest,bg='red',cursor='pirate').grid(row=19,column=1,columnspan=16,sticky=N+E+W+S)
        Button(root,text='Next',command=nxt,cursor='right_side').grid(row=17,column=12,columnspan=5,sticky=N+E+W+S)
        Button(root,text='Hint',command=hint,cursor='target').grid(row=17,column=1,columnspan=5,sticky=N+E+W+S)
        Button(root,text='Check',command=check,bg='green',cursor='pencil').grid(row=18,column=1,columnspan=16,sticky=N+E+W+S)
    root.mainloop()
Label(rt,text='Choose the level & click on game',bg='grey').grid(row=0,column=0,sticky=N+E+W+S)
def start():
    Button(root,command=fun).grid()
    rt.destroy()
p=PhotoImage(file='images.gif')
Button(rt,image=p,command=lambda:fun(v.get())).grid(row=1,column=0)
rt.mainloop()
