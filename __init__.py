from mycroft import MycroftSkill, intent_handler


class TurnLightOn(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('on.light.turn.intent')
    def handle_on_light_turn(self, message):
        self.speak_dialog('on.light.turn')


def create_skill():
    return TurnLightOn()

