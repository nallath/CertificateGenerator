__author__ = 'jaime'

import wx

class MainGUI(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MainGUI, self).__init__(*args, **kwargs)
        self.initGUI()

    def initGUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnQuit, fitem)

        self.SetSize((300, 200))
        self.SetTitle('Certificate Generator')
        self.Centre()
        self.Show(True)

    def OnQuit(self, e):
        self.Close()