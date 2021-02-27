from mycroft import MycroftSkill, intent_file_handler


class MycroftFoxyTurtlesimTurtleBackup(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('backup.turtle.turtlesim.foxy.mycroft.intent')
    def handle_backup_turtle_turtlesim_foxy_mycroft(self, message):
    self.speak_dialog('backup.turtle.turtlesim.foxy.mycroft')


def create_skill():
    return MycroftFoxyTurtlesimTurtleBackup()

