""" CS2223 Project 2 - Comparing Exhaustive Search with Greedy Algorithms """

import hungarianMethod

class Project2:

    def run(self):

        print("")
        print("CS2223 Project 2 - Comparing Exhaustive Search with Greedy Algorithms")
        print("Chris Winsor - 23-April-2016")
        print("")

        while True:

            print("Would you like to:")
            print("1 -> run (read 'cost_matrix.txt' and run exhaustive and greedy searches)")
            print("2 -> exit")
            choice = str(input("=>"))
            if (choice == "2"):
                break

            costMatrix = []
            f = open('cost_matrix.txt', 'r')

            for line in f :
                foo = line.strip()
                p = foo.split(',')
                r = [int(i) for i in p]
                costMatrix.append(r)

            # create and run using the Hungarian Method
            hungarianMachine = hungarianMethod.HungarianMachine()
            hungarianMachine.setCostMatrix(costMatrix)
            hungarianMachine.run()



            # print(costMatrix)2

            #
            # remainingTasks = [];
            # remainingWorkers = [];
            # for i in range(foo):
            #     remainingWorkers.append(1)
            # for i in range(foo):
            #     remainingTasks.append(1)
            #
            # assignmentList = {};
            # for assignmentNum in range(foo) :
            #     lowCostWorker = 0;
            #     lowCostTask = 0;
            #     currentLowCost = 1000;
            #     for workerNum in range (len(costMatrix)) :
            #         for taskNum in range (len(costMatrix[workerNum])) :
            #             #print(costMatrix[rowNum][colNum])
            #             if (costMatrix[workerNum][taskNum] < currentLowCost) & (remainingWorkers[workerNum] == 1) & (remainingTasks[taskNum] == 1) :
            #                 lowCostWorker = workerNum
            #                 lowCostTask = taskNum
            #                 currentLowCost = costMatrix[workerNum][taskNum]
            #     remainingWorkers[lowCostWorker] = 0;
            #     remainingTasks[lowCostTask] = 0;
            #
            #     assignmentList[lowCostWorker] = lowCostTask;
            #
            #     # at the end of the day we will have...
            #     assignments = [[0,2], [1,3], [2,4], [3,0]]
            #     print(assignments)
            #     # then we will sum the costs to print total cost
            #
            #     # to generate the list of permutations...
            #
            #
            #
            # print (assignmentList)
            # blah = 22
            # break


            # exhaustive search
            # for each worker
            #   for each task
            #
            # greedy algorithm
            # search for

                # Creates a list containing N lists, each of N items, all set to 0
#           Matrix = [[0 for x in range(size)] for y in range(size)]
#           Matrix[0][0] = 1
#           Matrix[6][0] = 3 # error! range...
#           Matrix[0][6] = 3 # valid
#            print Matrix[0][0] # prints 1
#            x, y = 0, 6
#            print Matrix[x][y] # prints 3; be careful with indexing!
            break


        print("Thank you, goodbye")


Project2().run()