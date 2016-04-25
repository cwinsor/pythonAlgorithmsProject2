""" ClassCostMatrix - a utility class representing a cost matrix """


import class_cost_matrix
import sys
from copy import copy, deepcopy



class ClassCostMatrix:
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




