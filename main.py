import PySimpleGUI as sg

def main():
    CANCEL_TEXT = "キャンセル"
    OK_TEXT = "OK"

    # color theme
    sg.theme("Default1")

    # components
    layout =    [
                    [sg.Text("１行目")],
                    [sg.Text("２行目、文字入力"), sg.InputText(key = "SetValueKey")],
                    [sg.Text("３行目、ファイルブラウズ"), sg.InputText(), sg.FileBrowse("ファイルを選択", key = "FileBrouseKey")],
                    [sg.Text("４行目、コンボボックス"), sg.Combo(("アイテムA", "アイテムB"), default_value = "アイテムA", key = "ComboBoxKey", size = (10, 1))],
                    [sg.Button(OK_TEXT), sg.Button(CANCEL_TEXT)]
                ]
    
    # create win
    window = sg.Window("サンプルプログラム", layout)

    # processing loop
    cnt = 0
    while True:
        # wait until detecting action
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            print("window closed")
            break
        elif event == CANCEL_TEXT:
            print("cancel button pushed")
            break
        elif event == OK_TEXT:
            print("ok button pushed")
            print("set value is {}".format(values["SetValueKey"]))
            print("file brouse is {}".format(values["FileBrouseKey"]))
            print("combo box is {}".format(values["ComboBoxKey"]))
        elif event == "FileBrouseKey":
            print("file brouse set")
        elif event == "ComboBoxKey":
            print("combo box set")
    
    # after loop
    window.close()

if __name__ == "__main__":
    main()
    print("Done.")