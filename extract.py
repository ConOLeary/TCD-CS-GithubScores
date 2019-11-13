# Author: KohnOhgOhlayOrah aka Con Og O Laoghaire
from datetime import datetime
from github import Github

date = str(datetime.date(datetime.now()))
time = str(datetime.time(datetime.now()))[0:8]
datetime = "|"+date+"|"+time
print(datetime)

class CsStudent:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.githubScore = 0
csStudents = []
yearScores = [0,0,0,0,0] # year = offset

g = Github("e133800e1d00c85d861492c0c8ea65e0f853d7ad")

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

f = open("GithubScores"+datetime+".txt","a+")
for csStudent in csStudents:
    user = g.get_user(csStudent.name)
    csStudent.githubScore += user.followers
    for repo in user.get_repos():
        csStudent.githubScore += repo.stargazers_count
    if(csStudent.year == 3):
        yearScores[3] += csStudent.githubScore
    if(csStudent.year == 4):
        yearScores[4] += csStudent.githubScore
    f.write(str(csStudent.year)+":"+csStudent.name+":"+str(csStudent.githubScore)+"\n")
    print(str(csStudent.year)+": "+csStudent.name+": "+str(csStudent.githubScore))
f.close()

print("Year3: "+str(yearScores[3]))
print("Year4: "+str(yearScores[4]))
