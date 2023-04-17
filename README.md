# AUC-Python
Area Under the Curve Python

This Python script compute the Area Under the Curve (AUC) from an input CSV file.
It was designed to quantify AUC from Sholl analysis on multiple cells across different groups (i.e. treatments/conditions).
The script reads and writes CSV files and handles multiple separators. For now, the used separator must be specified by the user at line #20 of the script 'csvDelimiter'. This iteger is, by default set to ','.
The boolean 'computeAUC_using_X_axis_values' option at line #21 defines the way the area is calculated. If set to 'True', the dx used is the one provided by the user in the input CSV file. If set to 'False', the dx used is set to 1.

+--------------------+
| The input CSV file | 
+--------------------+
In this example, the experiment has n groups, i cells in group 1 and j cells in group n

group,cell_id,radius,intersections    <-- line 0 is the header, ones can change the name of columns
group_1,0,0,0                         <-- starting at groupe 1, cell 0, sholl radius 0.
group_1,0,5,14                                                "intersections" stand for the number of intersections on the current Sholl sphere (called 'radius' here)
group_1,0,10,28
group_1,0,15,35
group_1,0,20,35
group_1,0,25,15
group_1,0,30,8
group_1,0,30,0
...
group_1,i,0,0                         <-- Here  ending the group 1 with the cell number i
group_1,i,5,14                                         
group_1,i,10,28
group_1,i,15,35
group_1,i,20,35
group_1,i,25,15
group_1,i,30,8
group_1,i,30,0
...                                   <-- here are the groups ]1;n[
...
group_n,j,0,0                         <-- ending with the group n and cell j
group_n,j,5,14                                         
group_n,j,10,28
group_n,j,15,35
group_n,j,20,35
group_n,j,25,15
group_n,j,30,8
group_n,j,30,0

+--------------------+
| END input CSV file | 
+--------------------+

NB: do not leave blanck cell or row, especially at the end of the CSV file. If the user experiences errors, he must look at the console. The script usually stops at the last group/cell with correct arguments. The user just has to go to the cell N+1 and check if the CSV is correct (no char. instead of int, no empty cell, ...).
NBB: each group can have different number of cells.
NBBB: each cells from the same group can have different number of radius.
