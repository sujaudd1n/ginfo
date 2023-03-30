import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import requests


class Ginfo_window(Gtk.Window):
    def __init__(self):
        super().__init__(title="Ginfo")

        self.query_field = Gtk.Entry()
        self.submit_btn = Gtk.Button.new_with_label("Search")
        self.submit_btn.connect("clicked", self.request_data)

        self.search_box = Gtk.Box()
        self.search_box.pack_start(self.query_field, True, True, 0)
        self.search_box.pack_start(self.submit_btn, True, True, 0)

        
        self.app = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.app.pack_start(self.search_box, True, True, 0)


        self.add(self.app)


    def request_data(self, widget):
        self.info_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        q = self.query_field.get_text()
        endpoint = f"https://api.github.com/users/{q}"
        res = requests.get(endpoint)
        if (res.status_code == 200):
            label = Gtk.Label(label="Success")
            self.info_box.pack_start(label, True, True, 0)
        else:
            label = Gtk.Label(label="Error")
            self.info_box.pack_start(label, True, True, 0)

        self.info_box.show_all()

        self.app.pack_start(self.info_box, True, True, 0)
        

window = Ginfo_window()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
