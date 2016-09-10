# -*- coding: UTF-8 -*-

from ninja_ide.core import plugin


class bbb(plugin.Plugin):
    def initialize(self):
        # Init your plugin
        pass

    def finish(self):
        # Shutdown your plugin
        pass

    def get_preferences_widget(self):
        # Return a widget for customize your plugin
        pass
