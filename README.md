# Rhythmbox Osdlyrics Plugin

This is a simple plugin that helps you to toggle lyrics display through toolbar button. 
It calls osdlyrics to display lyrics, so _osdlyrics is required_.

## Introduction

This plugin will create a toolbar button, like this:

![Toolbar Button](http://liberize.u.qiniudn.com/rhythmbox-osdlyrics-plugin.jpg)

You can toggle lyrics display by clicking it.

Besides, it will remember your lyrics state (on/off) every time you quit rhythmbox.

## Install

First install osdlyrics if you haven't installed it yet.

You can download the package from [official site](https://code.google.com/p/osd-lyrics/), or you can add a ppa `ppa:osd-lyrics/ppa` if you are using ubuntu.

Then use `git clone` to download or simply download as zip file.

Just copy this directory to `~/.local/share/rhythmbox/plugins/` (if not exist, make one).

Finally open rhythmbox, enable it in plugin manager dialog.

_PS: you may want to disable the original lyrics plugin as well._

## Contact

* @liberize: <https://github.com/liberize>
* Blog Page: <http://liberize.me/>
* Email: <liberize@gmail.com>
