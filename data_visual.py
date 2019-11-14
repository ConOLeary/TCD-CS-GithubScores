import pygal
import json

class CsStudent:
    def __init__(self, name, year, githubScore):
        self.name = name
        self.year = year
        self.githubScore = githubScore
csStudents = []

with open('Data/GithubScores|2019-11-14|14:36:29.json') as json_file:
    data = json.load(json_file)
    for entry in data['csStudents']:
        csStudent = CsStudent(entry['name'],entry['year'],entry['githubScore'])
        csStudents.append(csStudent)


for csStudent in csStudents:
    print('Name: ' + csStudent.name)
    print('Year: ' + csStudent.year)
    print('GithubScore: ' + csStudent.githubScore+"\n")

print(csStudents[2].githubScore)
scores = [0] * len(csStudents)
for i in range(len(csStudents)):
    scores[i] = int(csStudents[i].githubScore)

bar_chart = pygal.Bar()                                            # Then create a bar graph object
bar_chart.add('Fibonacci', scores)  # Add some values
bar_chart.render_to_file('bar_chart.svg')
