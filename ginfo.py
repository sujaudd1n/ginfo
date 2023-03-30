import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import requests


class Ginfo_window(Gtk.Window):
    def __init__(self):
        super().__init__(title="Ginfo")


window = Ginfo_window()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
