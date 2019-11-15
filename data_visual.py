import pygal
import json
import operator

class CsStudent:
    def __init__(self, name, year, githubScore):
        self.name = name
        self.year = year
        self.githubScore = githubScore
csStudents = []
amountOfYears = 5

with open('Data/GithubScores|2019-11-14|14:36:29.json') as json_file:
    data = json.load(json_file)
    for entry in data['csStudents']:
        csStudent = CsStudent(entry['name'],entry['year'],entry['githubScore'])
        csStudents.append(csStudent)

csStudents.sort(key=lambda x: int(x.githubScore))
#print([csStudent.name for csStudent in csStudents])
# output: ['Leo', 'Bob', 'Alice']

for csStudent in csStudents:
    print('Name: ' + csStudent.name)
    print('Year: ' + csStudent.year)
    print('GithubScore: ' + csStudent.githubScore+"\n")

yearScores = [0] * amountOfYears
for i in range(amountOfYears):
    yearScores[i] = [0] * len(csStudents)

for i in range(len(csStudents)):
    print("int(csStudents[i].year) = "+csStudents[i].year)
    print("int(csStudents[i].githubScore = "+csStudents[i].githubScore)
    yearScores[int(csStudents[i].year)][i] = int(csStudents[i].githubScore)

for i in range(len(csStudents)):
    print(str(yearScores[0][i])+" "+str(yearScores[1][i])+" "+str(yearScores[2][i])+" "+str(yearScores[3][i])+" "+str(yearScores[4][i])+"\n")

bar_chart = pygal.Bar()
bar_chart.title = 'Trinity CompSci GitHub Scores'
bar_chart.add('3rd year', yearScores[3])
bar_chart.add('4th year', yearScores[4])
bar_chart.render_to_file('bar_chart.svg')
