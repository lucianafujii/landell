# -*- coding: utf-8 -*-
# Copyright (C) 2010 Holoscópio Tecnologia
# Author: Thadeu Lima de Souza Cascardo <cascardo@holoscopio.com>
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

import gi
from gi.repository import GObject

class MediaItem(GObject.GObject):
    def __init__(self, name, factory):
        GObject.GObject.__init__(self)
        self.name = name
        self.factory = factory
        self.config = {}
    def set_parent(self, parent):
        self.parent = parent
    def get_config(self):
        return self.config
    def set_config(self, config):
        self.config = config
    def create(self):
        media_item = self.factory.create()
        media_item.config(self.config)
        return media_item
    def get_factory(self):
        return self.factory