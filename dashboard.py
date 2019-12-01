#!/usr/bin/python3
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Monitor(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Monitor Resources")
        self.box = Gtk.Box(spacing=6)
        self.set_default_size(640,480)
        menuBar = Gtk.MenuBar()
        file    = Gtk.MenuItem("File")
        menuBar.append(file)
        
        #Add Submenu
        openMenu = Gtk.Menu()
        open = Gtk.ImageMenuItem("Open")
        openMenu.append(open)
        file.set_submenu(openMenu)
        open.connect("clicked", self.on_file_clicked)

        #Add Menu Bar to window
        vbox = Gtk.VBox(False, 2)
        vbox.pack_start(menuBar, False, False, 0)
        self.add(vbox)
  
    def on_file_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a file", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

app = Monitor()
app.connect("destroy", Gtk.main_quit)
app.show_all()
Gtk.main()
