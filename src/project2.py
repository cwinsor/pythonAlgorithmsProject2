""" CS2223 Project 2 - Comparing Exhaustive Search with Greedy Algorithms """

import class_hungarian_method


class Project2:

    def run(self):

        print("")
        print("CS2223 Project 2 - Comparing Exhaustive Search with Greedy Algorithms")
        print("Chris Winsor - 23-April-2016")
        print("")

        while True:

            print("Would you like to:")
            print("1 -> run (read 'cost_file.txt' and run exhaustive and greedy searches)")
            print("2 -> exit")
            choice = str(input("=>"))
            if (choice == "2"):
                break


            costMatrixIn = []
            f = open('cost_file.txt', 'r')

            for line in f :
                foo = line.strip()
                p = foo.split(',')
                r = [int(i) for i in p]
                costMatrixIn.append(r)

            print("the cost matrix is %s" % costMatrixIn)

            # create and run using the Hungarian Method
            if (choice == "1"):
                print("---------------------------")
                print("after running Hungarian Method...")
                hungarianMachine = class_hungarian_method.ClassHungarianMethod()
                hungarianMachine.setCostMatrix(costMatrixIn)
                hungarianMachine.run()

            print("---------------------------")
            print("after running Exhaustive Search...")


            if (choice == "3") :

                costMatrix = class_hungarian_method.CostMatrix()
                costMatrix.setValues(costMatrixIn)

                print("costMatrix %s" % costMatrix.getMatrix())
                print("crossedOutRows %s" % costMatrix.getCrossedOutRows())
                print("crossedOutCols %s" % costMatrix.getCrossedOutColumns())

                costMatrix.subtractSmallestEntryFromRows();
                print("after subtracting smallest value from rows %s" % costMatrix.getMatrix())
                costMatrix.subtractSmallestEntryFromColumns();
                print("after subtracting smallest value from cols %s" % costMatrix.getMatrix())

                print("number of remaining zeros %d" % costMatrix.countRemainingZeros())

                print("rows with 3 uncovered zeros %s" % costMatrix.findRowsWithNUncoveredZeros(3))
                print("cols with 3 uncovered zeros %s" % costMatrix.findColumnsWithNUncoveredZeros(3))

                rows = costMatrix.findRowsWithNUncoveredZeros(2)
                print("rows with 2 uncovered zeros %s" % rows)
                costMatrix.crossOutRows(rows)
                rows = costMatrix.findRowsWithNUncoveredZeros(2)
                print("rows with 2 uncovered zeros %s" % rows)

                print("cols with 2 uncovered zeros %s" % costMatrix.findColumnsWithNUncoveredZeros(2))

                rows = costMatrix.findRowsWithNUncoveredZeros(1)
                print("rows with 1 uncovered zeros %s" % rows)
                costMatrix.crossOutRows(rows)
                rows = costMatrix.findRowsWithNUncoveredZeros(1)
                print("rows with 1 uncovered zeros %s" % rows)

                print("cols with 1 uncovered zeros %s" % costMatrix.findColumnsWithNUncoveredZeros(1))

            if (choice == "4"):
                costMatrixIn = [[35, 0, 0, 0], [0, 30, 0, 5], [55, 5, 0, 10], [0, 45, 30, 45]]
                hungarianMachine = class_hungarian_method.HungarianMachine()
                hungarianMachine.setCostMatrix(costMatrixIn)
                hungarianMachine.step3()
                print("results %s" % hungarianMachine.getCostMatrix())

            if (choice == "5"):
                costMatrixIn = [[40, 0, 5, 0], [0, 25, 0, 0], [55, 0, 0, 5], [0, 40, 30, 40]]
                hungarianMachine = class_hungarian_method.HungarianMachine()
                hungarianMachine.setCostMatrix(costMatrixIn)
                taskAssignments = hungarianMachine.step8()
                hungarianMachine.step9(taskAssignments)

            break

        print("---------------------------")
        print("Thank you, goodbye")


Project2().run()
