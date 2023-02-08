import modules.selUI.selUI as selui
import modules.selUI.unikey as unikey
import modules.ANSIcolour as ansi
import shared
import os


def repoSel():
    while True:
        os.system(shared.system.cmd.clear)
        menu=selui.SelectionMenu.create(os.listdir("./repos"), ansi.Bold.RED+"select mod-config"+ansi.RESET, selui.SelectionMenu.defaultOptions)
        print(menu.refresh())
        
        inp=unikey.getch()