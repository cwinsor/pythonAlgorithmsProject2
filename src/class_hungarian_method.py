""" Hungarian Method - perform hungarian method for worker-task assignment """

import class_cost_matrix
import sys

# reference
# http://www.math.harvard.edu/archive/20_spring_05/handouts/assignment_overheads.pdf

class ClassHungarianMethod:
    def __init__(self):
        return

    def setCostMatrix(self, costMatrixIn):
        self.cm = class_cost_matrix.ClassCostMatrix()
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
        self.debugPrint("entering step 1 costMatrix: %s" % self.cm.getMatrix())
        self.cm.subtractSmallestEntryFromRows()
        self.debugPrint("leaving step 1 costMatrix: %s" % self.cm.getMatrix())

    #Subtract the smallest entry in each column from all the entries of its column.
    def step2(self):
        self.cm.subtractSmallestEntryFromColumns()
        self.debugPrint("leaving step 2 costMatrix: %s" % self.cm.getMatrix())

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
        self.debugPrint("after step 3 costMatrix: %s" % self.cm.getMatrix())
        self.debugPrint("after step 3 crossedOutRows: %s" % self.cm.crossedOutRows)
        self.debugPrint("after step 3 crossedOutCols: %s" % self.cm.crossedOutColumns)


    def step4(self):
        ncr = self.cm.numberOfCrossedOutRows()
        ncc = self.cm.numberOfCrossedOutColumns()
        if   (self.cm.numberOfCrossedOutRows() + self.cm.numberOfCrossedOutColumns()) == self.cm.getSize() :
            weAreDone = True
        elif (self.cm.numberOfCrossedOutRows() + self.cm.numberOfCrossedOutColumns())  < self.cm.getSize() :
            weAreDone = False
        else :
            raise Exception('unexpected result in step 4')
        self.debugPrint("--step 4 is returning weAreDone=%s" % weAreDone)
        return weAreDone

    def step5(self):
        smallestUncoveredEntry = self.cm.getSmallestUncoveredEntry()
        self.cm.subtractFromEachUncoveredRow(smallestUncoveredEntry)
        self.cm.addToEachCoveredColumn(smallestUncoveredEntry)
        self.debugPrint("after step 5: %s" % self.cm.getMatrix())

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
        self.debugPrint("entering step 8 costMatrix: %s" % self.cm.getMatrix())
        self.cm.resetCrossedOutRows()
        self.cm.resetCrossedOutColumns()
        taskAssignments = {}
        self.cm.resetCrossedOutRows()
        self.cm.resetCrossedOutColumns()

        self.debugPrint("entering step 8 crossedOutRows: %s" % self.cm.crossedOutRows)
        self.debugPrint("entering step 8 crossedOutCols: %s" % self.cm.crossedOutColumns)

        currentMin = sys.maxsize
        while (self.cm.countRemainingUncoveredZeros() > 0):
            self.cm.findUnmarkedEntryWithFewestUnmarkedAdjacentZeros()
            row = self.cm.getCurrentRowNum()
            col = self.cm.getCurrentColNum()
            taskAssignments[row] = col
            self.cm.crossOutColumns([col])
            self.cm.crossOutRows([row])
        self.debugPrint("after step 8 the task assignments are: %s" % taskAssignments)
        print("the task assignments (worker:task) are: %s" % taskAssignments)
        return taskAssignments

    def step9(self,list):
        mySum = 0
        for key in list.keys():
            value = list[key]
            mySum += self.cm.getValueOriginal(key,value)
        self.debugPrint("after step9 the sum is: %s" % mySum)
        self.debugPrint("the current  matrix is %s" % self.cm.getMatrix())
        self.debugPrint("the original matrix is %s" % self.cm.getMatrixOriginal())
        print("the sum is: %s" % mySum)


    # debug printing...
    def debugPrint(self, msg):
        #print(msg)
        return
