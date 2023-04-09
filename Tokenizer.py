import re
from Enum import *

class TokenTools:
    def __init__(self):
        self.structToken = []
        self.structData = []
        self.cursorPointer = 0
        self.cursorEnd = 0
        self.statusSyntactic = False

    @staticmethod
    def split(string):
        patternRegex = r'\W+'
        return re.split(patternRegex, string)
    
    @staticmethod
    def recognizer(self, splitList):
        token = []
        data = []

        for token in splitList:
            token.append(Command.assignEnumerator(token))
            data.append(token)
        
        return token, data
    
    def syntactic(self, string):
        splitList = TokenTools.split(string)
        for token, data in TokenTools.recognizer(splitList):
            self.structToken = token
            self.structData = data

        self.statusSyntactic = True
        self.cursorEnd = len(self.structToken) - 1
        while (self.statusSyntactic is True):
            switch = {
                Command.TYPE : self.synType(),
                Command.CHAMPIONS : self.synType(),
                Command.BRACKET_OPEN : self.synType(),
                Command.BRACKET_END : self.synType(),
                Command.COMMA : self.synType(),
                Command.EVENT : self.synType(),
                Command.TOURNAMENT : self.synType(),
                Command.DATE_START : self.synType(),
                Command.DATE_END : self.synType(),
                Command.REWARD : self.synType(),
                Command.FRAGMENT : self.synType(),
                Command.INFO : self.synType()
            }

            switch.get(self.structToken[self.cursorPointer])

    def synType(self):
        switch = {
            Command.FRAGMENT : 1,
            Command.CHAMPIONS: 1
        }

        counterSwitch += switch.get(self.structToken[self.cursorPointer + 1], 0)

    def synChampions(self):
        pass

    def synEvent(self):
        pass

    def synTournament(self):
        pass

    def synReward(self):
        pass

    def synFragment(self):
        pass