import PySimpleGUI as sg 
from time import time
def create_wind():
    sg.theme("DarkPurple1")
    sg.set_options(font = "Calibri 14",button_element_size = (6,3))
    layout = [
        [sg.Push()],[sg.Text("x",pad = 0,enable_events = True)],
        [sg.VPush()],
        [sg.Push()],[sg.Text('000',font = "young 50",key="-t-")],[sg.Push()],
        [sg.Push()],[sg.Button('start',border_width =0,key = "-s-"),sg.Button('lap',border_width =0,key = "-l-",visible = False)],[sg.Push()],
        [sg.Column([[]],key ="-ls-")],
        [sg.VPush()],


    ]
    return sg.Window('stopwatch',layout,auto_size_text=18,size = (300,600),no_titlebar = True,element_justification = "centre")
window = create_wind()
    
st = 0
i=0
active = False
while True:
    event,values = window.read(timeout =10)

    if event == 'x':
        break
    if event == '-s-':
        if active:
            active = False
            window["-s-"].update('reset')
            window['-l-'].update(visible = False)
        else:
            if st>0:
                window.close()
                window = create_wind()
                st =0
            else:

                #print("bla bla")
                st = time()
                active = True
                window["-s-"].update('stop')
                window['-l-'].update(visible = True)
    if active:
        
        et = round(time()-st,1)
        window["-t-"].update(et)
        #print(et)
    
    if event == "-l-":
        i=i+1
        #window.resize()
        window.extend_layout(window["-ls-"],[[sg.Text(i),sg.VSeparator(),sg.Text(et)]])

window.close()