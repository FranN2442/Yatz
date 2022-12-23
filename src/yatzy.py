class Yatzy:

    @staticmethod
    def chance(*dice):
        total = 0
        for dado in dice:
            total += dado
        return total

    @staticmethod
    def yatzy(*dice):
        lista = []
        listaDados = list(dice)
        for dado in dice:
            for i in range(4):
                if dado in listaDados[i]:
                    lista.append(dado)
                else:
                    return 0 
        if len(lista) == 5:
            return 50 + 5 * listaDados[0]

    
    @staticmethod
    def ones(*dice):
        sumOnes = 0
        for dado in dice:
            if dado == 1:
                sumOnes += dado
        return sumOnes
    
    @staticmethod
    def twos(*dice):
        sumTwos = 0
        for dado in dice:
            if dado == 2:
                sumTwos += dado
        return sumTwos
    
    @staticmethod
    def threes(*dice):
        sumThrees = 0
        for dado in dice:
            if dado == 3:
                sumThrees += dado
        return sumThrees
    
    def fours(*dice):
        sumFours = 0
        for dado in dice: 
            if dado == 4:
                sumFours += dado 
        return sumFours
    

    def fives(*dice):
        sumFives = 0
        for dado in dice: 
            if dado == 5:
                sumFives += dado 
        return sumFives
    

    def sixes(*dice):
        sumSixes = 0
        for dado in dice: 
            if dado == 6:
                sumSixes += dado
        return sumSixes
    
    
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
    def fullHouse( d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2): 
                _2 = True
                _2_at = i+1
            

        for i in range(6):
            if (tallies[i] == 3): 
                _3 = True
                _3_at = i+1
            

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0