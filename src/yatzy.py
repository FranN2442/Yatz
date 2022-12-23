class Yatzy:

    @staticmethod
    def chance(*dice):
        total = 0
        for dado in dice:
            total += dado
        return total

    @staticmethod
    def yatzy(*dice):
        for dado in dice:
            if dice.count(dado) == 5:
                return 50 + 5 * dado
            else:
                return 0 
               

    @staticmethod
    def calcTopSide(*dice):
        listaRes = []
        for dado in dice:
            multi = dice.count(dado)
            res = dado * multi
            if res not in listaRes:
                listaRes.append(res)
        return listaRes       
            
    @staticmethod
    def __init__(self, d1, d2, d3, d4, _5):
        self.dice = [0]*5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5

    @staticmethod
    def score_pair(*dice):
        totalPair = 0
        pair = []
        dice = list(dice)

        for dado in dice:
            if dice.count(dado) == 2:
                
                pair.append(dado)
                dice.remove(dado)

        if len(pair) == 1:
            for num in pair:
                totalPair = num * 2 
                return totalPair       
        else:
            return False


    @staticmethod
    def two_pair(*dice):
        totalPair = 0
        pair = []
        dice = list(dice)

        for dado in dice:
            if dice.count(dado) == 2:
                if dado in pair:
                    dice.remove(dado)
                else:
                    pair.append(dado)
                
        if len(pair) == 2:
            for num in pair:
                totalPair += num *2
            return totalPair      
        else:
            return False
            
    
    @staticmethod
    def four_of_a_kind(*dice):
        dice = list(dice)
        for i in range(4):
            if dice.count(dice[i]) == 4:
                return dice[i] * 4
    

    @staticmethod
    def three_of_a_kind(*dice):
        dice = list(dice)
        for i in range(4):
            if dice.count(dice[i]) == 3:
                return dice[i] * 3
                
                  

    @staticmethod
    def smallStraight(*dice):
        dice = list(dice)
        lista = []
        if 6 not in dice:
            for dado in dice:
                if dado not in lista:
                    lista.append(dado)
            if len(lista) == 5:
                return 15
        return 0 

    @staticmethod
    def largeStraight(*dice):
        dice = list(dice)
        lista = []
        if 1 not in dice:
            for dado in dice:
                if dado not in lista:
                    lista.append(dado)
            if len(lista) == 5:
                return 20
        return 0

    @staticmethod
    def fullHouse(*dice):
        if Yatzy.score_pair(*dice) and Yatzy.three_of_a_kind(*dice):
            return Yatzy.score_pair(*dice) + Yatzy.three_of_a_kind(*dice)
        return 0