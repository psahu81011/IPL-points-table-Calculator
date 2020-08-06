class details:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.draws = 0

    def update(self, result):
        if result[0] == self.name:
            if result[2] == 'win':
                self.wins += 1
            if result[2] == 'loss':
                self.losses += 1
            if result[2] == 'draw':
                self.draws += 1
        if result[1] == self.name:
            if result[2] == 'win':
                self.losses += 1
            if result[2] == 'loss':
                self.wins += 1
            if result[2] == 'draw':
                self.draws += 1
        self.points = 2*self.wins + 1*self.draws
        self.mp = self.wins + self.losses + self.draws

total = int(input("Enter total number of matches:"))
results = []
print("Enter results of matches in following sequence....\nTeam1;Team2;Result")
for k in range(total):
    results.append([i for i in input().split(';')])

teamlist = []
for [t1,t2,O] in results:
    if t1 not in teamlist and t2 in teamlist:
        teamlist.append(t1)
    if t1 in teamlist and t2 not in teamlist:
        teamlist.append(t2)
    if t1 not in teamlist and t2 not in teamlist:
        teamlist.append(t1)
        teamlist.append(t2)
classlist = []
for team in teamlist:
    classlist.append(details(team))
for i in classlist:
    for j in results:
        i.update(j)
classlists = sorted(classlist, key = lambda x: (-x.points, x.name))
print("{:<23} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2} |".format('Team', 'MP', 'W','D', 'L', 'P'))
for i in classlists:
    print("{:<23} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2} |".format(i.name, i.mp, i.wins, i.draws, i.losses, i.points))
