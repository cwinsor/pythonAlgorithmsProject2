Algorithms CS2223 Program 1 (fibonacci benchmark)
Chris Winsor - 5-April-2016

README FILE

To run the program type:
python benchmark.py

You will be prompted to choose either the Brute Force or the Recursive algorithm, or exit.

        What fibonicci algorithm would you like to test?
        1 -> brute force
        2 -> recursive
        3 -> exit

and you would type "1", "2" or "3" to make that choice.

You will next be asked to specify the size "n" of the fibonacci series you want
and the number of the runs.  This is entered as a commma delimited list:

        What values of 'n' would you like?
        Enter the values as a comma delimited list
        For Brute Force put in something like:
        10000, 20000, 30000, 40000, 50000, 60000
        For Recursive you want to stay below 30:
        5,10,15,20,25,30

and here you would type (or copy from above)
10000, 20000, 30000, 40000, 50000, 60000
or
5,10,15,20,25,30

The first list is a set of numbers reasonable for Brute Force.
The second list is a set of numbers reasonable for the Recursive algorithm.

The tool will run the benchmarks and publish results (comma delimited)

        Results are
                 n runtime(microseconds)
        ---------- -------------------------
             10000,      8521
             20000,     20141
             50000,     90473
             40000,     61714
             60000,    128730
             30000,     38557

The tool will then loop back to the beginning.

