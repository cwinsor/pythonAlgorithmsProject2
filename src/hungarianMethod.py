""" Hungarian Method """

# reference
# http://www.math.harvard.edu/archive/20_spring_05/handouts/assignment_overheads.pdf

class CostMatrix:
    def __init__(self):
        return

    def setValues(self, costMatrix): # takes in a square (n-by-n) cost matrix array [[x,x,x],[x,x,x],[x,x,x]]
        # sanity check - matrix needs to be square
        if costMatrix.length() != costMatrix[0].length() :
            raise Exception("in CostMatrix - the input matrix was not square")

        # squirrel away the cost matrix, and its size
        self.costMatrix = costMatrix
        self.size = costMatrix[0].length()

        # create lists of rows and columns that have been "crossed out"
        self.crossedOutRows = costMatrix[0]
        self.crossedOutRows[:] = False
        self.crossedOutColumns = costMatrix[0]
        self.crossedOutColumns[:] = False


    def getCost(self,row,col):
        return self.costMatrix[row][col]

    def subtractSmallestEntryFromRows(self):
        return

    def subtractSmallestEntryFromColumns(self):
        return

    def countRemainingZeros(self):
        return

    def findRowsWithNZeros(self, n): # returns a list of rows that have "n" zeros
        return

    def crossOutRows(self, rowList): # crosses out the rows in the "rowList"
        return

    def numberOfCrossedOutRows(self):  # returns the number of crossed out columns
        return

    def findColumnsWithNZeros(self, n): # returns a list of columns that have "n" zeros
        return

    def crossOutColumns(self, columnList):  # crosses out the columns in the "columnList"
        return

    def numberOfCrossedOutColumns(self): # returns the number of crossed out columns
        return



# reference
# http://www.math.harvard.edu/archive/20_spring_05/handouts/assignment_overheads.pdf

class HungarianMachine:
    def __init__(self):
        return

    def setCostMatrix(self, costMatrixIn):
        self.cm = CostMatrix()
        self.cm.setValues(costMatrixIn)

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



    #Subtract the smallest entry in each row from all the entries of its row
    def step1(self):
        self.cm.subtractSmallestEntryFromRows()

    #Subtract the smallest entry in each column from all the entries of its column.
    def step2(self):
        self.cm.subtractSmallestEntryFromColumns()

    #Draw lines through appropriate rows and columns so that all the zero entries
    #of the cost matrix are covered and the minimum number of such lines is used.
    def step3(self):

        lookingForRowColWithZerosTotaling = self.cm.countRemainingZeros()
        while self.cm.countRemainingZeros() > 0 :
            foundSomething = False

            if (not foundSomething) :
                rowList = self.cm.findRowsWithNZeros(lookingForRowColWithZerosTotaling)
                if (rowList.length() > 0) :
                    self.cm.crossOutRows(rowList)
                    foundSomething = True;

            if (not foundSomething) :
                colList = self.cm.findColumnsWithNZeros(lookingForRowColWithZerosTotaling)
                if (colList.length() > 0) :
                    self.cm.crossOutColumns(colList)
                    foundSomething = True;

            if (not foundSomething) :
                lookingForRowColWithZerosTotaling -= 1

    def step4(self):
        if   (self.cm.numberCrossedOutRows.length() + self.cm.numberCrossedOutColumns.length()) == self.cm.getSize() :
            weAreDone = True
            return True
        elif (self.cm.numberCrossedOutRows.length() + self.cm.numberCrossedOutColumns.length())  < self.cm.getSize() :
            weAreDone = False
            return False
        else :
            raise Exception('unexpected result in step 4')

    def step5(self):
        smallestUncoveredEntry = self.cm.getSmallestUncoveredEntry()
        self.cm.subtractFromEachUncoveredRow(smallestUncoveredEntry);
        self.cm.addToEachUncoveredColumn(smallestUncoveredEntry);

    def step6(self):
        print("we are done!!!")



