# -*- coding: utf-8 -*-

import xbmcgui, xbmcaddon

SCRIPT_ID = 'script.panelbug'
SCRIPT_DIR = xbmcaddon.Addon(SCRIPT_ID).getAddonInfo('path')

class BuggyWindow(xbmcgui.WindowXML):
  def __init__(self, *args, **kwargs):
    xbmcgui.WindowXML.__init__(self)

  def onInit(self):
    self.panel = self.getControl(200)
    for i in range(10):
      self.panel.addItem(str(i))

  def onClick(self, controlId):
    if controlId == 200:
      print self.getControl(controlId).getSelectedItem()

if __name__ == '__main__':
  win = BuggyWindow('panel_bug.xml', SCRIPT_DIR)
  win.doModal()
  del win
