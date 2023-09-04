import PySimpleGUI as sg
from pathlib import Path

sg.set_options(font = "Calibri 18",button_element_size = (6,3))
sg.theme("DarkPurple1")

menu_layout = [
    ['File',['Open','Save','---',"Exit"]],
    ['Tools',['Word Count']],
]
layout = [
    [sg.Menu(menu_layout)],
    [sg.Text('text edit',key = "-title-")],
    [sg.Multiline(no_scrollbar =True,size = (40,30),key = "-tb-")]
]

window = sg.Window("Text Editor",layout)
while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Word Count":
        fulltext = values['-tb-']
        ot = fulltext.replace("\n","").split(" ")
        ot = [i for i in ot if i]
        word_count = len(ot)
        char_count = len("".join(ot))
        sg.popup(f"Word Count = {word_count}\nCharacter Count = {char_count}",title = "wordcount",)
        #print("test")
    
    if event == "Open":
        file_path = sg.popup_get_file("open",no_window = True)
        if file_path:
            file = Path(file_path)
            window["-tb-"].update(file.read_text())
            file_path = file_path.split("/")
            window["-title-"].update(file_path[-1])
            #print(file.read_text())
    if event == "Save":
        file_path = sg.popup_get_file("Save as",no_window = True,save_as =True) +".txt"
        file = Path(file_path)
        file.write_text(values['-tb-'])
        window["-title-"].update(file_path[-1:])
            
        
window.close()