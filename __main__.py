import gui
import json
import os



def main():

    #Open config file
    try:
        config_file = open("config.json", 'r+')
    except FileNotFoundError:
        print("No Config File Found")
        config_file = open("config.json", 'w')
        default_data = {'sid': 0, 'authtoken': 0, 'phonenumber': 0, 'default_csv': "default.csv"}
        json.dump(default_data, config_file)
        config_file.close()
        config_file = open("config.json", 'r+')

    #Translate json file to dictionary and open gui app. Pass in config data
    config_data = json.loads(config_file.read())
    app = gui.wx.App()
    gui.PrimaryGUI(None, title='KY Iota Notification System', sid=config_data.get("sid"), authtoken=config_data.get("authtoken"), phonenumber=config_data.get("phonenumber"), default_csv=config_data.get("default_csv"), config_file=config_file)
    app.MainLoop()


if __name__ == '__main__':
    main()
