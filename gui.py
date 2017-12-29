import wx


class PrimaryGUI(wx.Frame):

    def __init__(self, parent, title):
        super(PrimaryGUI, self).__init__(parent, title=title, size=(600, 400))

        # Initialize a dynamic TextCtrl field for use in buttons
        self.message_textctrl = wx.TextCtrl()

        # Initialize UI Functions
        self.init_ui()

        # Center the creen
        self.Centre()

        # Set the minimum screen size
        self.SetMinSize(size=(600, 400))

        # Make the screen vizible to the user
        self.Show()

    # Initialize the UI
    def init_ui(self):

        # Get system font
        font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        font.SetPointSize(10)

        # Set up the menubar
        menubar = wx.MenuBar()
        configuration_menu = wx.Menu()
        menubar.Append(configuration_menu, '&Configuration')
        self.SetMenuBar(menubar)

        panel = wx.Panel(self, style=wx.SIMPLE_BORDER)
        panel.SetBackgroundColour(wx.Colour(red=245, blue=245, green=245))

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
        self.message_textctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        message_hbox.Add(self.message_textctrl, proportion=1, flag=wx.EXPAND)
        vertical_sizer_box.Add(message_hbox, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.EXPAND | wx.TOP,
                               border=5)

        # Add gap between box and buttons
        vertical_sizer_box.Add((-1, 10))

        # Add buttons and field for recipients file
        buttons_hbox = wx.BoxSizer(wx.HORIZONTAL)
        recipients_stext = wx.StaticText(panel, label='Recipients File:')
        recipients_stext.SetFont(font)
        buttons_hbox.Add(recipients_stext, flag=wx.ALIGN_CENTER_VERTICAL | wx.LEFT, border=5)
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


        # Add events to buttons
        self.Bind(wx.EVT_BUTTON, self.on_send_message, id=send_message_button.GetId())
        self.Bind(wx.EVT_BUTTON, self.on_select_file, id=select_file_button.GetId())
        self.Bind(wx.EVT_BUTTON, self.on_tags, id=tags_button.GetId())

        # This event is called any time a menu is about to be opened
        # This should be changed to work only on the configuration menu if more menus are added
        self.Bind(wx.EVT_MENU_OPEN, self.on_configuration)

    # Here we will put the code for when the message is going to be sent
    def on_send_message(self, event):
        print(self.message_textctrl.GetValue())

    # Here we will put the code for when you need to select the recipients file
    def on_select_file(self, event):
        print("Select the file yo")

    # Here we will put the code for when to show the tags
    def on_tags(self, event):
        print("Open up the GUI for selecting the tags")

    # Here we will show the configuration menu
    def on_configuration(self, event):
        print("Select your configuration")


if __name__ == '__main__':
    app = wx.App()
    PrimaryGUI(None, title='KY Iota Notification System')
    app.MainLoop()
