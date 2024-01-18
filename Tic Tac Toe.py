# NEED EDITING IN check() function emerging as a tail of restart() function

from PySimpleGUI import *
import os

try:
    def resource_path(relative_path):
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
    logo_game=resource_path("Assets/logo_tictactoe.png")
    Window("Window Title",[[Image(logo_game)]],transparent_color=theme_background_color(),no_titlebar=True,
           keep_on_top=True).read(timeout=5000,close=True)
    def ext_1(string):
        lyt=[[Text(string,font=("Helvetica",15))],[Button("Exit",button_color="red")]]
        wnd=Window("Exit",lyt,element_justification="c")
        event,values=wnd.read()
        wnd.close()
        exit()
    def executer():
        for root,dirs,file in os.walk("/home/user/"):
            for i in file:
                if i=="Tic Tac Toe.exe":
                    pass
    def restart():
        global k,cpass,zpass,zero,cross,freeze
        k=cpass=zpass=0
        zero=cross=freeze=[]
        theme("HotDogStand")
        lt=[[Text("Replay ?",font=("Helvetica",32),text_color="black")],
            [Button("Yes",font=("Helvetica",32),button_color=("black","green2"))]+
            [Button("Exit",font=("Helvetica",32),button_color=("black","yellow"))]]
        wn=Window("Replay ?",lt,no_titlebar=True,element_justification="c")
        event,values=wn.read()
        if event=="Exit":
            exit()
        else:
            wn.close()
            window.close()
            executer()
            exec(open("Tic Tac Toe.py").read())
    def check():
        cpass=0
        zpass=0
        if 1 in cross:
            if 2 in cross:
                if 3 in cross:
                    cpass+=1
        if 1 in cross:
            if 5 in cross:
                if 9 in cross:
                    cpass+=1
        if 3 in cross:
            if 5 in cross:
                if 7 in cross:
                    cpass+=1
        if 1 in cross:
            if 4 in cross:
                if 7 in cross:
                    cpass+=1
        if 2 in cross:
            if 5 in cross:
                if 8 in cross:
                    cpass+=1
        if 3 in cross:
            if 6 in cross:
                if 9 in cross:
                    cpass+=1
        if 4 in cross:
            if 5 in cross:
                if 6 in cross:
                    cpass+=1
        if 7 in cross:
            if 8 in cross:
                if 9 in cross:
                    cpass+=1
        if 1 in zero:
            if 2 in zero:
                if 3 in zero:
                    zpass+=1
        if 1 in zero:
            if 5 in zero:
                if 9 in zero:
                    zpass+=1
        if 3 in zero:
            if 5 in zero:
                if 7 in zero:
                    zpass+=1
        if 1 in zero:
            if 4 in zero:
                if 7 in zero:
                    zpass+=1
        if 2 in zero:
            if 5 in zero:
                if 8 in zero:
                    zpass+=1
        if 3 in zero:
            if 6 in zero:
                if 9 in zero:
                    zpass+=1
        if 4 in zero:
            if 5 in zero:
                if 6 in zero:
                    zpass+=1
        if 7 in zero:
            if 8 in zero:
                if 9 in zero:
                    zpass+=1
        if cpass>zpass:
            state1=("Cross Won")
            mark1=(cpass)
            state2="Failed"
            mark2=zpass
        elif zpass>cpass:
            state1="Failed"
            mark1=cpass
            state2=("Zero Won")
            mark2=(zpass)
        else:
            state1=("Draw")
            state2=("Draw")
            mark1=cpass
            mark2=zpass
        return mark1,mark2
        restart()
    def check_no_return():
        cpass=0
        zpass=0
        if 1 in cross:
            if 2 in cross:
                if 3 in cross:
                    cpass+=1
        if 1 in cross:
            if 5 in cross:
                if 9 in cross:
                    cpass+=1
        if 3 in cross:
            if 5 in cross:
                if 7 in cross:
                    cpass+=1
        if 1 in cross:
            if 4 in cross:
                if 7 in cross:
                    cpass+=1
        if 2 in cross:
            if 5 in cross:
                if 8 in cross:
                    cpass+=1
        if 3 in cross:
            if 6 in cross:
                if 9 in cross:
                    cpass+=1
        if 4 in cross:
            if 5 in cross:
                if 6 in cross:
                    cpass+=1
        if 7 in cross:
            if 8 in cross:
                if 9 in cross:
                    cpass+=1
        if 1 in zero:
            if 2 in zero:
                if 3 in zero:
                    zpass+=1
        if 1 in zero:
            if 5 in zero:
                if 9 in zero:
                    zpass+=1
        if 3 in zero:
            if 5 in zero:
                if 7 in zero:
                    zpass+=1
        if 1 in zero:
            if 4 in zero:
                if 7 in zero:
                    zpass+=1
        if 2 in zero:
            if 5 in zero:
                if 8 in zero:
                    zpass+=1
        if 3 in zero:
            if 6 in zero:
                if 9 in zero:
                    zpass+=1
        if 4 in zero:
            if 5 in zero:
                if 6 in zero:
                    zpass+=1
        if 7 in zero:
            if 8 in zero:
                if 9 in zero:
                    zpass+=1
        if cpass>zpass:
            theme("Black")
            layout1=[[Text(name1+" Won -->",font=("Helvetica",20),text_color="green2")]+
                 [Text(str(cpass)+" Marks",font=("Helvetica",20),text_color="yellow")],
                 [Text(name2+" Failed -->",font=("Helvetica",20),text_color="red")]+
                 [Text(str(zpass)+" Marks",font=("Helvetica",20),text_color="yellow")]]
            window1=Window("Player Selection",layout1,element_justification="c",no_titlebar=True).read(timeout=5000,close=True)
        elif zpass>cpass:
            theme("Black")
            layout1=[[Text(name2+" Won -->",font=("Helvetica",20),text_color="green2")]+
                 [Text(str(zpass)+" Marks",font=("Helvetica",20),text_color="yellow")],
                 [Text(name1+" Failed -->",font=("Helvetica",20),text_color="red")]+
                 [Text(str(cpass)+" Marks",font=("Helvetica",20),text_color="yellow")]]
            window1=Window("Player Selection",layout1,element_justification="c",no_titlebar=True).read(timeout=5000,close=True)
        else:
            theme("Black")
            layout1=[[Text("Draw",font=("Helvetica",40),text_color="yellow")],
                 [Text(name1+" -> "+str(zpass)+" Marks",font=("Helvetica",20),text_color="green2")],
                 [Text(name2+" -> "+str(cpass)+" Marks",font=("Helvetica",20),text_color="green2")]]
            window1=Window("Player Selection",layout1,element_justification="c",no_titlebar=True).read(timeout=5000,close=True)
        restart()
    layout1=[[Text("Name of Cross ",font=("Helvetica",15))]+[Input(default_text="Player 1",size=(30,1))],
             [Text("Name of Zero   ",font=("Helvetica",15))]+[Input(default_text="Player 2",size=(30,1))],
             [Button("Play",size=(35,1),font=("Helvetica",15))]]
    window1=Window("Player Selection",layout1,element_justification="c")
    eve,val=window1.read()
    window1.close()
    try:
        name1=val[0]
        if name1=="":
            name1="Player 1"
        elif name1.isspace()==True:
            name1="Player 1"
        elif len(name1)==1:
            name1="Player 1"
    except:
        name1="Player 1"
    try:
        name2=val[1]
        if name2=="":
            name2="Player 2"
        elif name2.isspace()==True:
            name2="Player 2"
        elif len(name2)==1:
            name2="Player 2"
    except:
        name2="Player 2"
    theme("Reddit")
    logo_main=resource_path("Assets/logo.png")
    white=resource_path("Assets/white.png")
    layout=[[Image(logo_main)],[Button(button_color=("white"),key="1",image_filename=white,image_size=(150,150))]+
            [Button(button_color=("white"),key="2",image_filename=white,image_size=(150,150))]+
            [Button(button_color=("white"),key="3",image_filename=white,image_size=(150,150))],
            [Button(button_color=("white"),key="4",image_filename=white,image_size=(150,150))]+
            [Button(button_color=("white"),key="5",image_filename=white,image_size=(150,150))]+
            [Button(button_color=("white"),key="6",image_filename=white,image_size=(150,150))],
            [Button(button_color=("white"),key="7",image_filename=white,image_size=(150,150))]+
            [Button(button_color=("white"),key="8",image_filename=white,image_size=(150,150))]+
            [Button(button_color=("white"),key="9",image_filename=white,image_size=(150,150))],
            [Text(name1+" : 0",key="m1",text_color="black")]+[Text("|")]+[Text(name2+" : 0",key="m2",text_color="black")]]
    window=Window("Tic Tac Toe",layout,element_justification="c")
    k=0
    freeze=[]
    cross=[]
    zero=[]
    x=resource_path("Assets/x.png")
    o=resource_path("Assets/o.png")
    while True:
        event,values=window.read()
        if k%2==0:
            img=x
            stat="x"
        else:
            img=o
            stat="o"
        if event=="Quit" or event==None:
            break
        else:
            if event not in freeze:
                window.Element(event).Update(image_filename=img,image_size=(150,150))
                freeze.append(event)
                if stat=="x":
                    cross.append(int(event))
                else:
                    zero.append(int(event))
                k+=1
        mark1,mark2=check()
        if mark1>mark2:
            window.Element("m1").Update(text_color="green2")
            window.Element("m2").Update(text_color="red")
        elif mark1<mark2:
            window.Element("m2").Update(text_color="green2")
            window.Element("m1").Update(text_color="red")
        else:
            window.Element("m1").Update(text_color="blue")
            window.Element("m2").Update(text_color="blue")
        window.Element("m1").Update(name1+" : "+str(mark1))
        window.Element("m2").Update(name2+" : "+str(mark2))
        if len(cross)==5:
            check_no_return()    
except:
    theme("Reddit")
    ext_1("An Error had Occured !!!")
