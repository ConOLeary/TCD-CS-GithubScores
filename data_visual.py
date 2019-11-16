import pygal
import json
import operator

class CsStudent:
    def __init__(self, name, year, followers, starScore):
        self.name = name
        self.year = year
        self.followers = followers
        self.starScore = starScore
        if(followers != 0):
            self.ratio = float(starScore)/float(followers)
        if(followers == 0):
            self.ratio = 0
csStudents = []
amountOfStudents = 0
amountOfYears = 5
widthHeightScaling = 2
yearScores = [0,0,0,0,0] # year = offset

with open('Data/GithubScores|2019-11-16|01:19:58.json') as json_file:
    data = json.load(json_file)
    for entry in data['csStudents']:
        csStudent = CsStudent(entry['name'],entry['year'],int(entry['followers']),int(entry['starScore']))
        if(csStudent.year == 3):
            yearScores[3] += (csStudent.followers + csStudent.starScore)
        if(csStudent.year == 4):
            yearScores[4] += csStudent.followers + csStudent.starScore
        csStudents.append(csStudent)
        amountOfStudents += 1

csStudents.sort(key=lambda x: int(x.ratio))
for csStudent in csStudents:
    print('Name: ' + csStudent.name)
    print('Year: ' + str(csStudent.year))
    print('Followers: ' + str(csStudent.followers))
    print("StarScore: "+str(csStudent.starScore)+"\n")

#------------BAR_CHAR-------------------------------------
'''
studentScores = [0] * amountOfYears
for i in range(amountOfYears):
    studentScores[i] = [0] * amountOfStudents
for i in range(len(csStudents)):
    studentScores[csStudents[i].year][i] = csStudents[i].githubScore

bar_chart = pygal.Bar()
bar_chart.title = 'Trinity CompSci GitHub Scores'
bar_chart.add('3rd year', studentScores[3])
bar_chart.add('4th year', studentScores[4])
bar_chart.render_to_file('bar_chart.svg')
'''
#----------HISTO-------------------------------------------
def calculateWidth(y):
    #return round((1 + y * widthHeightScaling), 2)
    return 100 + (y * widthHeightScaling * widthHeightScaling)

yearBarSets = [(0,0,0)] * amountOfYears
for i in range(amountOfYears):
    yearBarSets[i] = [(0,0,0)] * amountOfStudents

yearBarSets[1][1] = (1,1,1)
currentX = 0

# (height, xFrom, xTo)
for i in range(amountOfStudents):
    student = csStudents[i]
    ratioScore = student.ratio
    width = calculateWidth(ratioScore)
    #if(ratioScore == 0): ratioScore = 0.1
    yearBarSets[int(student.year)][i] = (ratioScore, currentX, currentX + width)
    currentX += width


for i in range(amountOfStudents):
    print(str(yearBarSets[0][i])+" "+str(yearBarSets[1][i])+" "+str(yearBarSets[2][i])+" "+str(yearBarSets[3][i])+" "+str(yearBarSets[4][i])+"\n")
hist = pygal.Histogram(legend_at_bottom=True)
hist.add('3rd year| Total score: '+str(yearScores[3]), yearBarSets[3])
hist.add('4th year| Total score: '+str(yearScores[4]), yearBarSets[4])
hist.title = 'GitHub StarCount/Followers: Trinity CompSci'
hist.x_labels = ['']
hist.render_to_file('histogram.svg')
