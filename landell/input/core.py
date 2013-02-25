# -*- coding: utf-8 -*-
# Copyright (C) 2010 Holoscopio Tecnologia
# Author: Marcelo Jorge Vieira <metal@holoscopio.com>
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
gi.require_version("Gst", "1.0")
from gi.repository import Gst

INPUT_TYPE_AUDIO = 1
INPUT_TYPE_VIDEO = 2

class Input(Gst.Bin):

    def __init__(self, type):
        Gst.Bin.__init__(self)
        self.type = type
        if (type & INPUT_TYPE_AUDIO):
            self.audio_pad = Gst.GhostPad.new_no_target("audio_pad", Gst.PadDirection.SRC)
            self.add_pad(self.audio_pad)
        if (type & INPUT_TYPE_VIDEO):
            self.video_pad = Gst.GhostPad.new_no_target("video_pad", Gst.PadDirection.SRC)
            self.add_pad(self.video_pad)

    def get_type(self):
        return self.type

    def does_audio(self):
        return self.type & INPUT_TYPE_AUDIO

    def does_video(self):
        return self.type & INPUT_TYPE_VIDEO
