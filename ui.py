import modules.selUI.selUI as selui
import modules.ANSIcolour as ansi
import os

def repoSel():
    menu=selui.SelectionMenu.create(os.listdir("./repos"), ansi.Bold.RED+"select mod-config"+ansi.RESET, selui.SelectionMenu.defaultOptions)
    print(menu.refresh())