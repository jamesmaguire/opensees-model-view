model BasicBuilder -ndm 3 -ndf 6

set B1 2.0
set B2 3.5
set D 2.0
set H 1.5

# Create nodes
#          X               Y       Z
node  1    0.0             0.0     0.0
node  2    0.0             0.0     [expr 1*$H]
node  3    0.0             0.0     [expr 2*$H]
node  4    0.0             0.0     [expr 3*$H]
node  5    $B1             0.0     0.0
node  6    $B1             0.0     [expr 1*$H]
node  7    $B1             0.0     [expr 2*$H]
node  8    $B1             0.0     [expr 3*$H]
node  9    [expr $B1+$B2]  0.0     0.0
node 10    [expr $B1+$B2]  0.0     [expr 1*$H]
node 11    [expr $B1+$B2]  0.0     [expr 2*$H]
node 12    0.0             $D      0.0
node 13    0.0             $D      [expr 1*$H]
node 14    0.0             $D      [expr 2*$H]
node 15    0.0             $D      [expr 3*$H]
node 16    $B1             $D      0.0
node 17    $B1             $D      [expr 1*$H]
node 18    $B1             $D      [expr 2*$H]
node 19    $B1             $D      [expr 3*$H]
node 20    [expr $B1+$B2]  $D      0.0
node 21    [expr $B1+$B2]  $D      [expr 1*$H]
node 22    [expr $B1+$B2]  $D      [expr 2*$H]

# Create elements
# Z-dir elements
element truss  1  1  2
element truss  2  2  3
element truss  3  3  4
element truss  4  5  6
element truss  5  6  7
element truss  6  7  8
element truss  7  9 10
element truss  8 10 11
element truss  9 12 13
element truss 10 13 14
element truss 11 14 15
element truss 12 16 17
element truss 13 17 18
element truss 14 18 19
element truss 15 20 21
element truss 16 21 22
# X-dir elements
element truss 17  2  6
element truss 18  3  7
element truss 19  4  8
element truss 20  6 10
element truss 21  7 11
element truss 22 13 17
element truss 23 14 18
element truss 24 15 19
element truss 25 17 21
element truss 26 18 22
# Y-dir elements
element truss 27  2 13
element truss 28  3 14
element truss 29  4 15
element truss 30  6 17
element truss 31  7 18
element truss 32  8 19
element truss 33 10 21
element truss 34 11 22
# Bracings
element truss 35  9 21
element truss 36 20 10
element truss 37 10 22
element truss 38 21 11

# Boundary conditions
fix  1  1 1 1  0 0 0
fix  5  1 1 1  0 0 0
fix  9  1 1 1  0 0 0
fix 12  1 1 1  0 0 0
fix 16  1 1 1  0 0 0
fix 20  1 1 1  0 0 0
