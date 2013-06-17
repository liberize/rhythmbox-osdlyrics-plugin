#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import os
from gi.repository import Gtk, GObject, Peas
from ConfigParser import ConfigParser

ui_str = """
<ui>
  <toolbar name="ToolBar">
    <toolitem name="ShowLyrics" action="ShowLyrics"/>
    <separator/>
  </toolbar>
</ui>
"""
cur_path = os.path.dirname(os.path.realpath(__file__))
conf_file = cur_path + '/config'
config = ConfigParser()
lyrics_on = True

class ShowLyricsPlugin(GObject.Object, Peas.Activatable):
	__gtype_name__ = 'ShowLyricsPlugin'

	object = GObject.property (type = GObject.Object)

	def __init__(self):
		GObject.Object.__init__(self)
		self.window = None
			
	def do_activate(self):
		global config, lyrics_on
		
		data = dict()
		shell = self.object
		manager = shell.props.ui_manager
		
		config.read(conf_file)
		lyrics_on = config.getboolean('Lyrics', 'Show')
		if lyrics_on:
			os.system('[ ! -n "`pgrep osdlyrics`" ] && osdlyrics&')
			label = "关闭歌词"
		else:
			label = "显示歌词"

		data['action_group'] = Gtk.ActionGroup(name='ShowLyricsPluginActions')
		action = Gtk.Action(	name = 'ShowLyrics',
					label = label,
		                    	tooltip = "显示/关闭歌词",
		                    	stock_id = Gtk.STOCK_EDIT
		                    )
		action.connect('activate', self.show_lyrics, shell)
		data['action_group'].add_action(action)
				
		manager.insert_action_group(data['action_group'], 0)
		data['ui_id'] = manager.add_ui_from_string(ui_str)
		manager.ensure_update()

		shell.data = data
		
		print "Plugin Activated."
	
	def do_deactivate(self):
		global config, lyrics_on
		
		shell = self.object
		data = shell.data

		manager = shell.props.ui_manager
		manager.remove_ui(data['ui_id'])
		manager.remove_action_group(data['action_group'])
		manager.ensure_update()

		shell.data = None
		
		if self.window is not None:
			self.window.destroy()
		
		config.set('Lyrics', 'Show', str(lyrics_on))
		config.write(open(conf_file, 'w'))
		os.system('[ -n "`pgrep osdlyrics`" ] && killall osdlyrics')

		print "Plugin Deactivated."

	def show_lyrics(self, action, shell):
		global lyrics_on
						
		if lyrics_on:
			os.system('[ -n "`pgrep osdlyrics`" ] && killall osdlyrics')
			action.set_label("显示歌词")
			lyrics_on = False
		else:
			os.system('[ ! -n "`pgrep osdlyrics`" ] && osdlyrics&')
			action.set_label("关闭歌词")
			lyrics_on = True
		
		manager = shell.props.ui_manager
		manager.ensure_update()
