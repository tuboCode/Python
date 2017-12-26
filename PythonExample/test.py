#coding=utf-8

import wx

class Example(wx.Frame):
    def __init__(self, title):
        super(Example, self).__init__(None, title=title,size=(250, 150))
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Center()
        self.Show()

    def OnPaint(self, e):
        dc = wx.PaintDC(self)
                
        dc.DrawLines(((20, 60), (100, 60), (100, 10), (20, 10),(20, 60)))

if __name__=="__main__":
    app = wx.App()
    Example('Shapes')
    app.MainLoop()

