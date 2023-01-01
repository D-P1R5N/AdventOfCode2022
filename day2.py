import os
class Match:
    def __init__(self, result, opp):
        self.opp = opp
        self.result = result
class Win(Match):
    def __init__(self, result, opp):
        super().__init__(result, opp)

    def __int__(self):
        return 6

    def __iadd__(self, score):
        return score + 6

    def player(self):
        if self.opp == "ROCK":
            return "PAPER"
        elif self.opp == "PAPER":
            return "SCISSORS"
        elif self.opp == "SCISSORS":
            return "ROCK"
        else: raise Exception("PLAYER INCOMPAT")

class Lose(Match):
    def __init__(self, result, opp):
        super().__init__(result, opp)

    def __int__(self):
        return 0

    def __iadd__(self, score):
        return score

    def player(self):
        if self.opp == "ROCK":
            return "SCISSORS"
        elif self.opp == "PAPER":
            return "ROCK"
        elif self.opp == "SCISSORS":
            return "PAPER"
        else: raise Exception("PLAYER ERROR")

class Draw(Match):
    def __init__(self, result, opp):
        super().__init__(result, opp)

    def __int__(self):
        return 3

    def __iadd__(self, score):
        return score + 3

    def player(self):
        return self.opp

class Base:
    def __init__(self, id):
        self.id = id
    def __eq__(self, other):
        if self.id == other.id:
            return True

class Rock(Base):
    def __init__(self, id):
        super().__init__(id)
    def __int__(self):
        return 1
    def __iadd__(self, score):
        return score + 1
    def __lt__(self, other):
        if other.id == "PAPER":
            return True
        else:
            return False    
    def __gt__(self, other):
        if other.id == "SCISSORS":
            return True
        else:
            return False

class Paper(Base):
    def __init__(self, id):
        super().__init__(id)
    def __int__(self):
        return 2
    def __iadd__(self, score):
        return score + 2
    def __lt__(self, other):
        if other.id == "SCISSORS":
            return True
        else: return False
    def __gt__(self, other):
        if other.id == "ROCK":
            return True
        else: return False

class Scissors(Base):
    def __init__(self, id):
        super().__init__(id)
    def __int__(self):
        return 3
    def __iadd__(self,score):
        return score + 3
    def __lt__(self, other):
        if other.id == "ROCK":
            return True
        else: return False
    def __gt__(self, other):
        if other.id == "PAPER":
            return True
        else: return False

            
REFERENCE = {
    "ROCK": Rock,
    "SCISSORS": Scissors,
    "PAPER": Paper,
    "WIN": Win,
    "DRAW": Draw,
    "LOSE": Lose
    }

SYMBOLS = {
    "ROCK":['A','X'],
    "PAPER":['B', 'Y'],
    "SCISSORS":['C', 'Z']
    }

SYMBOLS2 = {
    "ROCK": 'A',
    "PAPER": 'B',
    "SCISSORS": 'C',
    "LOSE": 'X',
    "DRAW": 'Y',
    "WIN": 'Z'
}

SCORES = {
    "WIN": 6,
    "DRAW": 3,
    "LOSE": 0,
    "ROCK": 1,
    "PAPER": 2,
    "SCISSORS": 3
}
    
def transmog(match):
    opp, you = match
    for _ in match:
        for k in SYMBOLS:
            if opp in SYMBOLS[k]:
                opp = k
            if you in SYMBOLS[k]:
                you = k
    return (opp, you)

def transmog2(match):
    opp, result = match
    for _ in match:
        for k in SYMBOLS2:
            if opp in SYMBOLS2[k]:
                opp = k
            if result in SYMBOLS2[k]:
                result = k
    return [opp, result]


def rock_paper_scissors(match):
    opp, you = match
    opp = REFERENCE[opp](opp)
    you = REFERENCE[you](you)
    if opp > you:
        return ("LOSE", you.id)
    elif opp < you:
        return ("WIN", you.id)
    elif opp == you:
        return ("DRAW", you.id)
    else:
        raise Exception("There is a RPS error: You:" + you.id + "Opp:" + opp.id) 

def rock_paper_scissors2(match):
    opp, result = match
    _result = REFERENCE[result](result,opp)
    opp = REFERENCE[opp](opp)
    you = _result.player()
    #you = REFERENCE[you](you)
    return [result, you]
if __name__ == "__main__" : 
    cwd = os.getcwd()
    with open(cwd + "/AdventOfCode/inputs/day2input.txt") as txt:
        data = txt.read().split('\n')
        data = [tuple(i.split(' ')) for i in data if i]
    
    score = 0
    for _ in data:
        match = transmog2(_)
        print(match)
        results = rock_paper_scissors2(match)
        print(results)
        for i in results:
            score += SCORES[i]
        print(score)