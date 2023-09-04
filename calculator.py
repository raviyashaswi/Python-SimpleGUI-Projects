import PySimpleGUI as sg
def win_fun(theme):
    sg.theme("them")
    sg.set_options(font = "Calibri 14",button_element_size= (6,3))
    bs = (6,3)
    layout = [
    [sg.Text("C",
    enable_events=True,
    justification= 'right',
    expand_x=True,
    expand_y=True,
    size=(20,3),
    right_click_menu = theme_list,
    key ='-txt-',
    )
    ],
    [sg.Button("Clr",size = bs),sg.Button("(",size = bs),sg.Button(")",size = bs),sg.Button("=",size = bs)],
    [sg.Button("7",size = bs),sg.Button("8",size = bs),sg.Button("9",size = bs),sg.Button("*",size = bs)],
    [sg.Button("4",size = bs),sg.Button("5",size = bs),sg.Button("6",size = bs),sg.Button("-",size = bs)],
    [sg.Button("1",size = bs),sg.Button("2",size = bs),sg.Button("3",size = bs),sg.Button("+",size = bs)],
    [sg.Button("0",expand_x=True),sg.Button(".",size = bs),sg.Button("/",size = bs)],
    ]
    return sg.Window("calculator",layout)
theme_list = ['menu',['dark','LightGrey1','DarkGray8','Random']]
win = win_fun("dark")
number = []
while True:
    event,values = win.read()
    if event == sg.WIN_CLOSED:
        break
    if event in theme_list[1]:
        win.close()
        win = win_fun(event)

    
    if event in ['1','2','3','4','5','6','7','8','9','0','.']:
        number.append(event)
        string = "".join(number)
        win['-txt-'].update(string)
    if event in ['%','*','-','+','/','(',')']:
        if event == '(':
            number.append("*")
        number.append(event)
        string = "".join(number)
        win['-txt-'].update(string)
    if event == '=':
        print(string)
        x = eval(string)
        win['-txt-'].update(x)
        number.clear()
        number.append(str(x))
    if event == "Clr":
        number.pop()
        
        string = "".join(number)
        win['-txt-'].update(string)
win.close()