import numpy as np


class Citizen():
    def __init__(self):
        self.isAlive = True # 생존여부

    def status():
        return Citizen

class mafia():
    def __init__(self):
        self.isAlive = True # 생존여부

    def status():
        return mafia

class mafiaGame():

    def vote(self, numOfVoter):

        beElected = []
        beElected[numOfVoter]
        i = 0
        for i in len(numOfVoter):
            n = np.random.randint(0, len(numOfVoter))
            beElected[n]+=1

        chosen = max(beElected)

        if  self.member[chosen].status() == Citizen:
            self.aliveCitizen-=1
        else:
            self.aliveMafia-=1

    def night(self):
        self.aliveCitizen-=1

    def mafiaGame(self, numOfCitizen, numOfMafia):

        self.member[numOfCitizen+numOfMafia]
        i = 0
        while(i>numOfCitizen): #시민의 수를 파라미터 만큼 생성
            self.member[i] = Citizen()
            i+=1
        while(i>numOfCitizen+numOfMafia): # 마피아의 수를 파라미터 만큼 생성
            self.member[i] = mafia()
            i+=1

        self.vote(self.member)
        print(numOfCitizen,numOfMafia)
        self.night(self.member)
        print(numOfCitizen,numOfMafia)



aliveCitizen = 10
aliveMafia = 2

while(aliveCitizen == aliveMafia or aliveMafia == 0):
    mafiaGame(aliveCitizen, aliveMafia)
    
print("mafia win") if aliveCitizen == aliveMafia else print("Citizen win")


    
        
    