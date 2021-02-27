from mycroft import MycroftSkill, intent_file_handler
import subprocess

class MycroftFoxyTurtlesimTurtleBackup(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('backup.turtle.turtlesim.foxy.mycroft.intent')
    def handle_backup_turtle_turtlesim_foxy_mycroft(self, message):
        self.speak_dialog('backup.turtle.turtlesim.foxy.mycroft')
        subprocess.call(["ros2 topic pub --once /turtle1/cmd_vel geometry_msgs/msg/Twist '{linear: {x: -2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}'"],shell=True)

def create_skill():
    return MycroftFoxyTurtlesimTurtleBackup()

