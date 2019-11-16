# Author: KohnOhgOhlayOrah aka Con Og O Laoghaire
from datetime import datetime
from github import Github
import json
data = {}
data['csStudents'] = []

date = str(datetime.date(datetime.now()))
time = str(datetime.time(datetime.now()))[0:8]
datetime = "|"+date+"|"+time
print(datetime)

class CsStudent:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.followers = 0
        self.starScore = 0
csStudents = []

f = open("3rdYearCS.txt", "r")
year3s = f.read().split()
f = open("4thYearCS.txt", "r")
year4s = f.read().split()
for username in year3s:
    csStudent = CsStudent(username,3)
    csStudents.append(csStudent)
for username in year4s:
    csStudent = CsStudent(username,4)
    csStudents.append(csStudent)

g = Github("e133800e1d00c85d861492c0c8ea65e0f853d7ad")

for csStudent in csStudents:
    user = g.get_user(csStudent.name)
    csStudent.followers += user.followers
    for repo in user.get_repos():
        csStudent.starScore += repo.stargazers_count
    data['csStudents'].append({
        'name': csStudent.name,
        'year': str(csStudent.year),
        'followers': str(csStudent.followers),
        'starScore': str(csStudent.starScore),
    })
    print(str(csStudent.year)+": "+csStudent.name+": "+str(csStudent.followers)+": "+str(csStudent.starScore))
f.close()

with open("Data/GithubScores"+datetime+".json", "w") as outfile:
    json.dump(data, outfile)
