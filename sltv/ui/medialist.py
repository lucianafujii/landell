# -*- coding: utf-8 -*-
# Copyright (C) 2010 Holoscópio Tecnologia
# Author: Luciana Fujii Pontello <luciana@holoscopio.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import gobject
import gtk
from sltv.settings import UI_DIR

class MediaListUI:
    def __init__(self, ui, media_list):
        self.interface = gtk.Builder()
        self.interface.add_from_file(UI_DIR + "/medialist.ui")
        self.dialog = self.interface.get_object("medialist_dialog")
        self.dialog.set_transient_for(ui.main_window)
        add_button = self.interface.get_object("add_button")
        self.edit_button = self.interface.get_object("edit_button")
        self.remove_button = self.interface.get_object("remove_button")
        close_button = self.interface.get_object("close_button")

        self.media_list = media_list
        self.media_list_treeview = self.interface.get_object(
                "medialist_treeview"
        )
        self.media_list_treeview.set_model(self.media_list.get_store())
        cell = gtk.CellRendererText()
        column =  gtk.TreeViewColumn('Items', cell, text=0)
        self.media_list_treeview.append_column(column)

        selection = self.media_list_treeview.get_selection()
        selection.set_mode(gtk.SELECTION_BROWSE)
        selection.connect("changed", self.on_treeview_changed)

        self.block_buttons(selection)

        add_button.connect("clicked", self.on_add_item)
        self.edit_button.connect("clicked", self.on_edit_item)
        self.remove_button.connect("clicked", self.on_remove_item)
        close_button.connect("clicked", self.close_dialog)
        self.dialog.connect("delete_event", self.close_dialog)

    def block_buttons(self, selection):
        (model, iter) = selection.get_selected()
        if iter == None or model == None:
            self.remove_button.set_sensitive(False)
            self.edit_button.set_sensitive(False)
        else:
            self.remove_button.set_sensitive(True)
            self.edit_button.set_sensitive(True)

    def on_treeview_changed(self, selection):
        self.block_buttons(selection)

    def show_window(self):
        self.dialog.show_all()
        self.dialog.run()

    def close_dialog(self, widget, data= None):
        self.dialog.hide_all()

    def on_add_item(self, button):
        self.edit_item.set_media_item(None)
        self.edit_item.show_window()

    def on_edit_item(self, button):
        (model, iter) = self.media_list_treeview.get_selection().get_selected()
        if iter != None and model != None:
            name = model.get_value(iter, 0)
            media_item = self.media_list.get_item(name)
            self.edit_item.set_media_item(media_item)
            self.edit_item.show_window()

    def on_remove_item(self, button):
        (model, iter) = self.media_list_treeview.get_selection().get_selected()
        if iter != None and model != None:
            name = model.get_value(iter, 0)
            self.media_list.remove_item(name)
            self.media_list.save()