# Compute Sholl Analysis AUC from CSV file
#
# CSV file structure:
#                       Group   Cell_ID     Radius      Intersections
#                       Values...
#
# Version 1.1
# Author: Augustin WALTER
# email: augustin.walter@outlook.fr


# CAUTION:  please check the CSV delimiter
#           If user recieve the following error, modify the CSV delimiter:
#               > "if row2[1] != cellID:
#               >    IndexError: list index out of range"
#
# Do not let empty cell in the 'intersections' column, it will result in an error.

# User vars
csvDelimiter = ',' # Do not forget to adjust this value according to your CSV delimiter.
computeAUC_using_X_axis_values = True         # if set to True, AUC values are computed using X axis values


# Internal vars
mainGroups = [] # ZT
cellsID = []
AUC = []

group = ''
cellID = ''

radius = []
radiusValue = 0


import csv
import numpy as np
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import os

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing

csvFilePath = askopenfilename()
file_name, file_extension = os.path.splitext(csvFilePath)
resultCSVFile = csvFilePath.replace(file_extension, "_AUC-result.csv")

# Read CSV
with open(csvFilePath) as csvFile:
    csvLineRead = csv.reader(csvFile, delimiter = csvDelimiter)

    # Count lines in csv file
    csvRowsCount = 0
    for row in open(csvFilePath):
        csvRowsCount += 1

    print("Nb. of lines in CSV file '" + str(csvFilePath) + "'")
    print("    - " + str(csvRowsCount))

    # Collecting intersections values and computing AUC for all cells
    rowID = 0
    group = ''
    cellID = ''

    groupTitle = ''

    AUC = []
    titleGroups = []
    titleCell = []

    y = []
    x = []

    for row2 in csvLineRead:
        #print(row2)
        if rowID > 0:
            if row2[1] != cellID or rowID >= (csvRowsCount - 1):
                if rowID > 0:
                    if not computeAUC_using_X_axis_values:
                        AUC.append(np.trapz(y))

                    else:
                        AUC.append(np.trapz(y, x=x))

                    titleGroups.append(str(group))
                    titleCell.append(str(cellID))

                    print("> Group " + str(groupTitle) + " " + str(group) + ", cell " + str(cellID) + ":")
                    print("     - x = ", x)
                    print("     - y = ", y)
                    print("     - AUC = ", AUC[len(AUC) - 1])



                cellID = row2[1]
                y = []
                x = []
                group = row2[0]

            else:
                y.append(int(row2[3]))
                x.append(int(row2[2]))

        else:
            groupTitle = row2[0]

        rowID += 1



# Save results
with open(resultCSVFile, 'w', newline='') as resultFile:
    writer = csv.writer(resultFile, delimiter=csvDelimiter)
    writer.writerow([str(groupTitle), 'cell_ID', 'AUC'])

    for i in range(1, len(AUC)):
        writer.writerow([titleGroups[i], titleCell[i], AUC[i]])

print("> Result file saved in:")
print("     " + resultCSVFile)