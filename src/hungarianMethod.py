""" Hungarian Method """

import sys
from copy import copy, deepcopy


# reference
# http://www.math.harvard.edu/archive/20_spring_05/handouts/assignment_overheads.pdf

class CostMatrix:
    def __init__(self):
        return

    def setValues(self, costMatrixIn): # takes in a square (n-by-n) cost matrix array [[x,x,x],[x,x,x],[x,x,x]]
        # sanity check - matrix needs to be square
        if costMatrixIn.__len__() != costMatrixIn[0].__len__() :
            raise Exception("in CostMatrix - the input matrix was not square")

        # squirrel away the cost matrix, and its size
        self.costMatrixOriginal = deepcopy(costMatrixIn)
        self.costMatrix = deepcopy(costMatrixIn)
        self.size = costMatrixIn[0].__len__()

        # create lists of rows and columns that have been "crossed out"
        self.crossedOutRows = [False for i in range(self.size)]
        self.crossedOutColumns = [False for i in range(self.size)]

    def getSize(self):
        return self.size

    def getValue(self, row, col):
        return self.costMatrix[row][col]

    def getValueOriginal(self, row, col):
        return self.costMatrixOriginal[row][col]

    def getMatrix(self):
        return self.costMatrix

    def getMatrixOriginal(self):
        return self.costMatrixOriginal

    def resetCrossedOutRows(self):
        for col in range(self.crossedOutRows.__len__()):
            self.crossedOutRows[col] = False

    def resetCrossedOutColumns(self):
        for row in range(self.crossedOutColumns.__len__()):
            self.crossedOutColumns[row] = False

    def getCrossedOutRows(self):
        return self.crossedOutRows

    def getCrossedOutColumns(self):
        return self.crossedOutColumns

    def getCost(self,row,col):
        return self.costMatrix[row][col]

    def subtractSmallestEntryFromRows(self):
        for row in range(self.getSize()) :
            minVal = sys.maxsize
            for col in range(self.getSize()) :
                if self.costMatrix[row][col] < minVal :
                    minVal = self.costMatrix[row][col]
            for col in range(self.getSize()) :
                self.costMatrix[row][col] -= minVal

    def subtractSmallestEntryFromColumns(self):
        for col in range(self.getSize()):
            minVal = sys.maxsize
            for row in range(self.getSize()):
                if self.costMatrix[row][col] < minVal:
                    minVal = self.costMatrix[row][col]
            for row in range(self.getSize()):
                self.costMatrix[row][col] -= minVal

    def countRemainingUncoveredZeros(self):
        numZeros = 0
        for rowNum in range(self.costMatrix.__len__()) :
            for colNum in range(self.costMatrix.__len__()):
                if self.isZeroAndUncovered(rowNum,colNum):
                    numZeros += 1
        return numZeros

    def findRowsWithNUncoveredZeros(self, n): # returns a list of rows that have "n" zeros uncovered
        rowList = []
        for row in range(self.getSize()):
            numZerosThisRow = 0
            for col in range(self.getSize()):
                if self.isZeroAndUncovered(row,col):
                    numZerosThisRow += 1
            if numZerosThisRow == n :
                rowList.append(row)
        return rowList

    def findColumnsWithNUncoveredZeros(self, n):  # returns a list of columns that have "n" zeros
        colList = []
        for col in range(self.getSize()):
            numZerosThisCol = 0
            for row in range(self.getSize()):
                if self.isZeroAndUncovered(row,col):
                    numZerosThisCol += 1
            if numZerosThisCol == n:
                colList.append(col)
        return colList

    def isUncovered(self, row, col):
        return (self.crossedOutRows[row] == False) and (self.crossedOutColumns[col] == False)

    def isZero(self, row, col):
        return self.costMatrix[row][col] == 0

    def isZeroAndUncovered(self, row, col):
        myIsZero = self.isZero(row,col)
        myIsUncovered = self.isUncovered(row, col)
        return myIsZero and myIsUncovered

    def crossOutRows(self, rowList): # crosses out the rows in the "rowList"
        for row in rowList:
            self.crossedOutRows[row] = True

    def crossOutColumns(self, columnList):  # crosses out the columns in the "columnList"
        for col in columnList:
            self.crossedOutColumns[col] = True

    def numberOfCrossedOutRows(self):  # returns the number of crossed out columns
        count = 0
        for row in self.crossedOutRows:
            if (row):
                count += 1
        return count

    def numberOfCrossedOutColumns(self): # returns the number of crossed out columns
        count = 0
        for col in self.crossedOutColumns:
            if (col):
                count += 1
        return count

    def getSmallestUncoveredEntry(self):
        minVal = sys.maxsize
        for row in range(self.getSize()) :
            for col in range(self.getSize()) :
                if (self.costMatrix[row][col] < minVal) and self.isUncovered(row,col) :
                    minVal = self.costMatrix[row][col]
        return minVal

    def subtractFromEachUncoveredRow(self, n):
        for row in range(self.getSize()):
            if not self.crossedOutRows[row]:
                for col in range(self.getSize()):
                    self.costMatrix[row][col] -= n

    def addToEachCoveredColumn(self, n):
        for col in range(self.getSize()):
            if self.crossedOutColumns[col]:
                for row in range(self.getSize()):
                    self.costMatrix[row][col] += n

    def findFirstUncoveredZeroInRow(self,row):
        for col in range(self.getSize()):
            if self.isZeroAndUncovered(row, col):
                return col

    def getZerosForColumn(self, colNum):
        rowList = []
        for rowNum in range(self.getSize()):
            if self.isZero(rowNum, colNum):
                rowList.append(rowNum)
        return rowList

    def countUncoveredInColumn(self, col):
        count = 0
        for rowNum in range(self.getSize()):
            if self.isZeroAndUncovered(rowNum, col):
                count += 1
        return count

    def countUncoveredInRow(self, row):
        count = 0
        for colNum in range(self.getSize()):
            if self.isZeroAndUncovered(row,colNum):
                count += 1
        return count


    def findUnmarkedEntryWithFewestUnmarkedAdjacentZeros(self):
        currentMinCount = sys.maxsize
        self.currentRow = -1
        self.currentCol = -1
        for row in range(self.getSize()):
            for col in range(self.getSize()):
                if self.isZeroAndUncovered(row, col):
                    adjacentUncoveredZeros = self.countUncoveredInColumn(col) + self.countUncoveredInRow(row) - 2
                    if adjacentUncoveredZeros < currentMinCount:
                        currentMinCount = adjacentUncoveredZeros
                        self.currentRow = row
                        self.currentCol = col

    def getCurrentRowNum(self):
        return self.currentRow

    def getCurrentColNum(self):
        return self.currentCol





# reference
# http://www.math.harvard.edu/archive/20_spring_05/handouts/assignment_overheads.pdf

class HungarianMachine:
    def __init__(self):
        return

    def setCostMatrix(self, costMatrixIn):
        self.cm = CostMatrix()
        self.cm.setValues(costMatrixIn)

    def getCostMatrix(self):
        return self.cm.getMatrix()


    # run the Hungarian algorithm
    def run(self):
        self.step1() #Subtract the smallest entry in each row
        self.step2() #Subtract the smallest entry in each column
        self.step3()  # Draw lines through appropriate rows and columns
        while not self.step4(): #Test for optimality
            self.step5() # determine smallest uncovered entry, subtract from uncov. rows, add to uncov. columns
            self.step3() # repeat step 3
        # at this point we have an 'optimal' solution
        # we need to find the matchups...
        taskAssignments = self.step8()
        self.step9(taskAssignments)





    #Subtract the smallest entry in each row from all the entries of its row
    def step1(self):
        print("entering step 1 costMatrix: %s" % self.cm.getMatrix())
        self.cm.subtractSmallestEntryFromRows()
        print("leaving step 1 costMatrix: %s" % self.cm.getMatrix())

    #Subtract the smallest entry in each column from all the entries of its column.
    def step2(self):
        self.cm.subtractSmallestEntryFromColumns()
        print("leaving step 2 costMatrix: %s" % self.cm.getMatrix())

    #Draw lines through appropriate rows and columns so that all the zero entries
    #of the cost matrix are covered and the minimum number of such lines is used.
    def step3(self):

        self.cm.resetCrossedOutRows()
        self.cm.resetCrossedOutColumns()

        # search for rows and columns with zeros in them
        # start by searching for large numbers of zeros and progressively decrease
        lookingForRowColWithZerosTotaling = self.cm.countRemainingUncoveredZeros()
        while self.cm.countRemainingUncoveredZeros() > 0 :

            zona1 = self.cm.crossedOutRows
            zona2 = self.cm.crossedOutColumns

            foundSomething = False

            if (not foundSomething) :
                rowList = self.cm.findRowsWithNUncoveredZeros(lookingForRowColWithZerosTotaling)
                if (rowList.__len__() > 0) :
                    self.cm.crossOutRows(rowList)
                    foundSomething = True;

            if (not foundSomething) :
                colList = self.cm.findColumnsWithNUncoveredZeros(lookingForRowColWithZerosTotaling)
                if (colList.__len__() > 0) :
                    self.cm.crossOutColumns(colList)
                    foundSomething = True;

            if (not foundSomething) :
                lookingForRowColWithZerosTotaling -= 1
        print("after step 3 costMatrix: %s" % self.cm.getMatrix())
        print("after step 3 crossedOutRows: %s" % self.cm.crossedOutRows)
        print("after step 3 crossedOutCols: %s" % self.cm.crossedOutColumns)


    def step4(self):
        ncr = self.cm.numberOfCrossedOutRows()
        ncc = self.cm.numberOfCrossedOutColumns()
        if   (self.cm.numberOfCrossedOutRows() + self.cm.numberOfCrossedOutColumns()) == self.cm.getSize() :
            weAreDone = True
        elif (self.cm.numberOfCrossedOutRows() + self.cm.numberOfCrossedOutColumns())  < self.cm.getSize() :
            weAreDone = False
        else :
            raise Exception('unexpected result in step 4')
        print("--step 4 is returning weAreDone=%s" % weAreDone)
        return weAreDone

    def step5(self):
        smallestUncoveredEntry = self.cm.getSmallestUncoveredEntry()
        self.cm.subtractFromEachUncoveredRow(smallestUncoveredEntry)
        self.cm.addToEachCoveredColumn(smallestUncoveredEntry)
        print("after step 5: %s" % self.cm.getMatrix())

    # we have a matrix with tasks of size "0"
    # we need to pick N of the "0" tasks to represent the task-resource matchup
    #
    # procedure is to step through rows searching
    # searching for rows having "N" zeros
    # start by searching for rows with 1 zero, and increase
    #   if the row has only a single zero then that zero needs to be in the task-resource list
    #   cross off that row (task) and column (resource)
    #   if the row has two zeros - take the first (uncrossed-off)
    #   cross of that row (task) and column (resource)
    #   if the row has three zeros -  etc etc
    # until all zeros are crossed off
    def step6(self):
        taskAssignments = {}
        self.cm.resetCrossedOutRows()
        self.cm.resetCrossedOutColumns()
        searchingForZeroCountOf = 1
        while (self.cm.countRemainingUncoveredZeros()>0):
            rowList = self.cm.findRowsWithNUncoveredZeros(searchingForZeroCountOf)
            for row in rowList:
                col = self.cm.findFirstUncoveredZeroInRow(row)
                taskAssignments[row] = col;
                self.cm.crossOutRows([row])
                self.cm.crossOutColumns([col])
            searchingForZeroCountOf += 1

        print("after step 6 task assignments are: %s" % taskAssignments)
        return taskAssignments

    # an "optimal assignment of zeros is possible"
    # now to find that combination of zeros in the matrix...
    #
    # the task is to pick N of the "0" tasks to represent the task-resource matchup
    # procedure is to repeatedly:
    #   check each non-crossed-out zero for the one that has the fewest other zeros in its row and columns
    #   this is the one we want to assign first (it has the least flexibility)
    #   we then mark that row/column as "assigned"  and proceed to find the next-least-flexible
    #   and so on
    def step8(self):
        print("entering step 8 costMatrix: %s" % self.cm.getMatrix())
        self.cm.resetCrossedOutRows()
        self.cm.resetCrossedOutColumns()
        taskAssignments = {}
        self.cm.resetCrossedOutRows()
        self.cm.resetCrossedOutColumns()

        print("entering step 8 crossedOutRows: %s" % self.cm.crossedOutRows)
        print("entering step 8 crossedOutCols: %s" % self.cm.crossedOutColumns)

        currentMin = sys.maxsize
        while (self.cm.countRemainingUncoveredZeros() > 0):
            self.cm.findUnmarkedEntryWithFewestUnmarkedAdjacentZeros()
            row = self.cm.getCurrentRowNum()
            col = self.cm.getCurrentColNum()
            taskAssignments[row] = col
            self.cm.crossOutColumns([col])
            self.cm.crossOutRows([row])
        print("after step 8 the task assignments are: %s" % taskAssignments)
        return taskAssignments

    def step9(self,list):
        mySum = 0
        for key in list.keys():
            value = list[key]
            mySum += self.cm.getValueOriginal(key,value)
        print("after step9 the sum is: %s" % mySum)
        print("the current  matrix is %s" % self.cm.getMatrix())
        print("the original matrix is %s" % self.cm.getMatrixOriginal())



    def step7(self):
        self.finalPathList = []
        pathSoFar = []
        self.doIt(0,pathSoFar)
        print("after step7 the list of paths is: %s" % self.finalPathList)
        return


    # we need to find combinations of zeros which
    # account for tasks and workers
    # we perform a recursive search on task and worker combinations
    # where the time for the worker/task is zero
    def doIt(self, columnNum, pathSoFar):
        print("entering doIt with pathSoFar %s" % pathSoFar)
        print("                   columnNum %d" % columnNum)

        if (columnNum == self.cm.getSize()): # we've gotten to a leaf
            self.finalPathList.append(pathSoFar) # document this path
            print("found leaf with path: %s" % pathSoFar)
            return
        # squirrel away current path and go to the next level of task
        rowsInThisColumnThatAreZero = self.cm.getZerosForColumn(columnNum)
        for rowNum in rowsInThisColumnThatAreZero:
            zona1 = {}
            zona1[rowNum] = columnNum
            pathSoFar.append(zona1);
            self.doIt(columnNum + 1, pathSoFar)
