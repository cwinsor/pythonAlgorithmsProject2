""" Hungarian Method """

import sys

# reference
# http://www.math.harvard.edu/archive/20_spring_05/handouts/assignment_overheads.pdf

class CostMatrix:
    def __init__(self):
        return

    def setValues(self, costMatrix): # takes in a square (n-by-n) cost matrix array [[x,x,x],[x,x,x],[x,x,x]]
        # sanity check - matrix needs to be square
        if costMatrix.__len__() != costMatrix[0].__len__() :
            raise Exception("in CostMatrix - the input matrix was not square")

        # squirrel away the cost matrix, and its size
        self.costMatrix = costMatrix
        self.size = costMatrix[0].__len__()

        # create lists of rows and columns that have been "crossed out"
        self.crossedOutRows = [False for i in range(self.size)]
        self.crossedOutColumns = [False for i in range(self.size)]

    def getSize(self):
        return self.size

    def getMatrix(self):
        return self.costMatrix

    def resetCrossedOutRows(self):
        for item in self.crossedOutRows:
            item = False

    def resetCrossedOutColumns(self):
        for item in self.crossedOutColumns:
            item = False

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
        return self.isZero(row,col) and self.isUncovered(row,col)

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
        taskAssignments = self.step6()



    #Subtract the smallest entry in each row from all the entries of its row
    def step1(self):
        self.cm.subtractSmallestEntryFromRows()

    #Subtract the smallest entry in each column from all the entries of its column.
    def step2(self):
        self.cm.subtractSmallestEntryFromColumns()

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

    def step7(self):
        self.finalPathList = []
        pathSoFar = {}
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
            pathSoFar[rowNum] = columnNum;
            self.doIt(columnNum + 1, pathSoFar)
