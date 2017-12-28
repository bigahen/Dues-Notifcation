import wx


class GUI(wx.Frame):
    def __init__(self, parent, title):
        super(GUI, self).__init__(parent, title=title,
                                      size=(600, 400))

        self.init_ui()
        self.Centre()
        self.SetMinSize(size=(600, 400))
        self.Show()

    # Initialize the UI
    def init_ui(self):
        panel = wx.Panel(self)

        # Get system font
        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)

        # Set up the menubar
        """menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)"""

        # Main vertical sizer box
        vertical_sizer_box = wx.BoxSizer(wx.VERTICAL)

        # Adds Enter Message dialog
        label_hbox = wx.BoxSizer(wx.HORIZONTAL)
        label_stext = wx.StaticText(panel, label='Enter Message:')
        label_stext.SetFont(font)
        label_hbox.Add(label_stext)
        vertical_sizer_box.Add(label_hbox, flag=wx.LEFT | wx.TOP, border=5)

        # Adds text box to enter dialog
        message_hbox = wx.BoxSizer(wx.HORIZONTAL)
        message_textctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        message_hbox.Add(message_textctrl, proportion=1, flag=wx.EXPAND)
        vertical_sizer_box.Add(message_hbox, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.EXPAND | wx.TOP,
                               border=5)

        # Add gap between box and buttons
        vertical_sizer_box.Add((-1, 10))

        # Add buttons and field for recipients file
        buttons_hbox = wx.BoxSizer(wx.HORIZONTAL)
        recipients_tc = wx.TextCtrl(panel, size=(150, 22))
        buttons_hbox.Add(recipients_tc, proportion=0, flag=wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, border=5)
        select_file_button = wx.Button(panel, label='Select File', size=(70, 30))
        buttons_hbox.Add(select_file_button)
        buttons_hbox.Add((0, 10), 1, flag=wx.EXPAND)
        tags_button = wx.Button(panel, label='Tags', size=(50, 30))
        buttons_hbox.Add(tags_button, flag=wx.RIGHT, border=5)
        send_message_button = wx.Button(panel, label='Send Message', size=(100, 30))
        buttons_hbox.Add(send_message_button, flag=wx.LEFT | wx.BOTTOM | wx.ALIGN_RIGHT, border=0)
        vertical_sizer_box.Add(buttons_hbox, flag=wx.RIGHT | wx.EXPAND, border=10)

        # Add gap a bottom of screen
        vertical_sizer_box.Add((-1, 10))

        panel.SetSizer(vertical_sizer_box)


if __name__ == '__main__':
    app = wx.App()
    GUI(None, title='PDT Notification System')
    app.MainLoop()
