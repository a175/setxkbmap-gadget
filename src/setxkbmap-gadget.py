#!/usr/bin/env python
import pygtk,gtk
pygtk.require('2.0')
import os,sys

class SetxkbmapButtonConfigData:
    def __init__(self):
        self.layout=[]
        self.option=[]


        self.add_layout("JP","-model jp106 -layout jp")
        self.add_layout("US","-model pc -layout us")
        self.add_layout("DE","-model pc -layout de")
        self.add_layout("FR","-model pc -layout fr")
        self.add_layout("Dvorak","-model pc -layout us -variant dvorak")
        self.add_layout("Left handed Dvrak","-model pc -layout us -variant dvorak-l")
        self.add_layout("Right handed Dvrak","-model pc -layout us -variant dvorak-r")

        self.add_option("Clear all oprions","-option")
        self.add_option(None,None)
        self.add_option("CapsLock  -> Ctrl","-option ctrl:nocaps")
        self.add_option("CapsLock <-> Ctrl","-option ctrl:swapcaps")


    def add_layout(self,label,code,position=-1):
        if position < 0:
            position = len(self.layout)+position+1
        self.layout.insert(position,(label,code))
    def add_option(self,label,code,position=-1):
        if position < 0:
            position = len(self.option)+position+1
        self.option.insert(position,(label,code))        
    
class SetxkbmapButtonArea:
    def __init__(self,config):
        if config:
            self.config=config
        else:
            self.config=SetxkbmapButtonConfigData()
        hbox = gtk.HBox()
        frame=gtk.Frame()
        frame.set_label("Layout and Model")
        vbbox = gtk.VButtonBox()
        vbbox.set_layout(gtk.BUTTONBOX_START)
        for (label, arg) in self.config.layout:
            if label:
                button = gtk.Button(label=label)
                button.connect('clicked', self.on_click_option_button,arg)
                vbbox.add(button)
            else:
                vbbox.add(gtk.HSeparator())
        frame.add(vbbox)
        hbox.add(frame)
        
        frame=gtk.Frame()
        frame.set_label("Option")
        vbbox = gtk.VButtonBox()
        vbbox.set_layout(gtk.BUTTONBOX_START)
        for (label, arg) in self.config.option:
            if label:
                button = gtk.Button(label=label)
                button.connect('clicked', self.on_click_option_button,arg)
                vbbox.add(button)
            else:
                vbbox.add(gtk.HSeparator())
        frame.add(vbbox)
        hbox.add(frame)
        hbox.show_all()
        self.hbox=hbox
    def get_hbox(self):
        return self.hbox
    def on_click_layout_button(self,widget,arg):
        self.exec_setxkbmap(arg)
    def on_click_option_button(self,widget,arg):
        self.exec_setxkbmap(arg)
    def exec_setxkbmap(self,arg):
        command="setxkbmap "+arg
        print command
        os.system(command)

class SetxkbmapButtonMain:
    def __init__(self,title,width,height,config):
        if width <0:
            width = -width
        if height <= 0:
            height=width
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_default_size(width,height)
        self.window.set_title(title)
        self.window.connect("destroy", lambda w: gtk.main_quit())
        area = SetxkbmapButtonArea(config)
        self.window.add(area.get_hbox())
        self.window.show()

def main():
    window_width=10
    window_height=0
    window_title="Click to change keyboard layout"
    argv= sys.argv[:]
    config=SetxkbmapButtonConfigData()
    while argv!= []:
        arg=argv.pop(0)
        if arg=="-width":
            window_width=int(argv.pop(0))
        elif arg=="-height":
            window_height=int(argv.pop(0))
        elif arg=="-window-title":
            window_title=argv.pop(0)
        elif arg=="-layout":
            label=argv.pop(0)
            command=argv.pop(0)
            config.add_layout(label,command,0)
        elif arg=="-option":
            label=argv.pop(0)
            command=argv.pop(0)
            config.add_option(label,command,0)
    SetxkbmapButtonMain(window_title,window_width,window_height,config)
    gtk.main()

if __name__ == "__main__":
    main()
