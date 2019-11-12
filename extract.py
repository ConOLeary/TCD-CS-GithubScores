# Author: KohnOhgOhlayOrah aka Con Og O Laoghaire

class CsStudent:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.githubScore = 0
csStudents = []
yearScores = [0,0,0,0,0] # year = offset

from github import Github
# Create Github instance using access token
g = Github("6d4005743498048fbef2fd9462b5522b8ddf799f")

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


for csStudent in csStudents:
    user = g.get_user(csStudent.name)
    csStudent.githubScore += user.followers
    for repo in user.get_repos():
        csStudent.githubScore += repo.stargazers_count
    if(csStudent.year == 3):
        yearScores[3] += csStudent.githubScore
    if(csStudent.year == 4):
        yearScores[4] += csStudent.githubScore
    print(csStudent.name+": "+str(csStudent.githubScore))

print("Year3: "+str(yearScores[3]))
print("Year4: "+str(yearScores[4]))
