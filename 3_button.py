#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Simple window - Just a simple window
# Copyright (c) 2016 Jorge Maldonado Ventura
#
# This file is part of Simple window
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='Título original')
        self.label = Gtk.Label('asdasd')
        self.button = Gtk.Button()
        self.button.add(self.label)
        self.button.connect('clicked', self.button_clicked)
        self.add(self.button)

    def button_clicked(self, widget):
        print('Me has pulsado.')

if __name__ == '__main__':
    win = Window()
    win.connect('delete-event', Gtk.main_quit)
    win.show_all()
    Gtk.main()
