from enum import Enum

# Define an enumeration using the Enum class
class Command(Enum):
    TYPE = 1
    CHAMPIONS = 2
    BRACKET_OPEN = 3
    BRACKET_END = 4
    COMMA = 5
    EVENT = 6
    TOURNAMENT = 7
    DATE_START = 8
    DATE_END = 9
    REWARD = 10
    FRAGMENT = 12
    INFO = 13

    @staticmethod
    def assignEnumerator(token):
        switch = {
            'TYPE' : Command.TYPE,
            'CHAMPIONS' : Command.CHAMPIONS,
            'BRACKET_OPEN' : Command.BRACKET_OPEN,
            'BRACKET_END' : Command.BRACKET_END,
            'COMMA' : Command.COMMA,
            'EVENT' : Command.EVENT,
            'TOURNAMENT' : Command.TOURNAMENT,
            'DATE_START' : Command.DATE_START,
            'DATE_END' : Command.DATE_END,
            'REWARD' : Command.REWARD,
            'FRAGMENT' : Command.FRAGMENT,
            'INFO' : Command.INFO
        }

        return switch.get(token, Command.INFO)

