# Python program for implementation of Radix Sort

# A function to do counting sort of arr[] according to
# the digit represented by exp.
def countingSort(arr, exp1, arrCopyChanges):

    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)
    outputCopyChages = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (arr[i]/exp1)
        count[ (index)%10 ] += 1

    # Change count[i] so that count[i] now contains actual
    #  position of this digit in output array
    for i in range(1,10):
        count[i] += count[i-1]

    # Build the output array
    i = n-1
    while i>=0:
        index = (arr[i]/exp1)
        output[ count[ (index)%10 ] - 1] = arr[i]
        outputCopyChages[ count[ (index)%10 ] - 1] = arrCopyChanges[i]
        count[ (index)%10 ] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0,len(arr)):
        arr[i] = output[i]
        arrCopyChanges[i] = outputCopyChages[i]

# Method to do Radix Sort
def radixSort(arr, arrCopyChanges):

    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1/exp > 0:
        countingSort(arr,exp,arrCopyChanges)
        exp *= 10
########################Above stolen from: www.geeksforgeeks.org/radix-sort

import pygal
import json
import operator
import sys

class CsStudent:
    def __init__(self, name, year, followers, starScore):
        self.name = name
        self.year = int(year)
        self.followers = int(followers)
        self.starScore = int(starScore)
        self.githubScore = followers + starScore
        if(followers != 0):
            self.ratio = float(starScore)/float(followers)
        if(followers == 0):
            self.ratio = 0
csStudents = []
amountOfStudents = 0
amountOfYears = 5
maxHighlightable = 2
widthHeightScaling = 0.02
yearScores = [0,0,0,0,0] # year = offset

######## USE EXTRACT ###############
import extract
####################################
import os
cwd = os.getcwd()+"/Data"

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(cwd) if isfile(join(cwd, f))]
comparableTimes = [0] * len(onlyfiles)
i = 0
for file in onlyfiles:
    comparableTimes[i] = onlyfiles[i].replace('|', '')
    comparableTimes[i] = comparableTimes[i].replace('.', '')
    comparableTimes[i] = comparableTimes[i].replace(':', '')
    comparableTimes[i] = comparableTimes[i].replace('-', '')
    comparableTimes[i] = int(str(comparableTimes[i])[12:26])
    #print(comparableTimes[i])
    i+=1
radixSort(comparableTimes, onlyfiles)

# for i in range(len(comparableTimes)):
#     print(str(comparableTimes[i])+" "+str(onlyfiles[i]))
print(onlyfiles[15])

with open('Data/'+onlyfiles[15]) as json_file:
    data = json.load(json_file)
    for entry in data['csStudents']:
        csStudent = CsStudent(entry['name'],entry['year'],int(entry['followers']),int(entry['starScore']))
        if(csStudent.year == 3):
            yearScores[3] += csStudent.githubScore
        if(csStudent.year == 4):
            yearScores[4] += csStudent.githubScore
        csStudents.append(csStudent)
        amountOfStudents += 1

csStudents.sort(key=lambda x: int(x.githubScore))
# for csStudent in csStudents:
#     print('Name: ' + csStudent.name)
#     print('Year: ' + str(csStudent.year))
#     print('Followers: ' + str(csStudent.followers))
#     print("StarScore: "+str(csStudent.starScore)+"\n")

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
    return 1 + (y * widthHeightScaling)


highlightCount = len(sys.argv)-1
if(highlightCount > maxHighlightable):
    highlightCount = maxHighlightable
highlightedScores = [0] * highlightCount
highlightedStudents = [0] * highlightCount
for i in range(highlightCount):
    highlightedStudents[i] = str(sys.argv[i+1])
    #print(highlightedStudents[i])

#print("amountOfYears:"+str(amountOfYears))
#print("highlightCount"+str(highlightCount))
yearBarSets = [(0,0,0)] * (amountOfYears + 1 + highlightCount)
for i in range(amountOfYears + 1 + highlightCount):
    yearBarSets[i] = [(0,0,0)] * amountOfStudents
    #print(str(yearBarSets[i])+"\n\n\n")

currentX = 0
# (height, xFrom, xTo)
for i in range(amountOfStudents):
    student = csStudents[i]
    githubScore = student.githubScore
    width = calculateWidth(githubScore)
    if(githubScore == 0): githubScore = 0.2
    matched = False
    for j in range(highlightCount):
        if(student.name == highlightedStudents[j]):
            yearBarSets[amountOfYears+j][i] = (githubScore, currentX, currentX + width)
            highlightedScores[j] = githubScore
            matched = True
    if(matched == False):
        yearBarSets[int(student.year)][i] = (githubScore, currentX, currentX + width)
    currentX += width


#for i in range(amountOfStudents):
#    print(str(yearBarSets[0][i])+" "+str(yearBarSets[1][i])+" "+str(yearBarSets[2][i])+" "+str(yearBarSets[3][i])+" "+str(yearBarSets[4][i])+" "+str(yearBarSets[5][i])+" "+str(yearBarSets[6][i])+"\n")

hist = pygal.Histogram(legend_at_bottom=True)
hist.add('3rd year| '+str(yearScores[3]), yearBarSets[3])
hist.add('4th year| '+str(yearScores[4]), yearBarSets[4])
for i in range(highlightCount):
    hist.add(highlightedStudents[i]+'| '+str(highlightedScores[i]), yearBarSets[amountOfYears+i])
hist.title = 'GitHub Scores: Trinity CompSci'
hist.x_labels = ['']
hist.render_to_file('histogram.svg')
