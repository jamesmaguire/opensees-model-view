model BasicBuilder -ndm 2 -ndf 3

set H 1.5
set B [expr 2*$H]

# Create nodes
node 1 0.0 0.0
node 2 0.0 1.0
node 3 [expr $B/2] $H
node 4 $B 1.0
node 5 $B 0.0

# Create elements
element truss 1 1 2
element truss 2 2 3
element truss 3 3 4
element truss 4 4 5

# Boundary conditions
fix 1  1 1 1
fix 5  1 1 0
