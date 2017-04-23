''' OpenSees Visual Interface
This package will watch your OpenSees file(s) and generate a live preview
'''
import os
import time
import matplotlib.pyplot as pl
import matplotlib.animation as animation
from tcl_handler import flatten_tcl

# Declare OpenSees tcl files to watch and refresh rate
# NB: Must be tuple. If only one file, make sure it is in parentheses and
#     followed by a comma. Eg tclfiles = ('example.tcl',)
tclfiles = ('samplemodel.tcl',)
refresh_rate = 1 # refresh rate in seconds

# Create figure
fig = pl.figure(figsize=(6, 6))
ax = fig.add_subplot(1, 1, 1, aspect=1, frameon=False)

# Set viewport visual style
fig.set_facecolor('lightgrey') # background color
pl.rc('font', family='Monospace', size=10) # set font for labels
node_style = {'color':'black', 'marker':'.', 'markersize':10} # nodes
ele_style = {'color':'black', 'linewidth':1, 'linestyle':'-'} # elements
axis_style = {'color':'grey', 'linewidth':1, 'linestyle':'--'} # x=0, y=0 lines
bc_style = {'color':'black', 'markeredgewidth':1, 'markersize':9,
            'fillstyle':'none'} # node translation fixity (boundary conditions)
bcrot_style = {'color':'black', 'markeredgewidth':1, 'markersize':10,
            'fillstyle':'none'} # node rotation fixity (boundary conditions)
fig.text(0.01, 0.01, ', '.join(tclfiles),
         va='bottom', ha='left', color='grey', fontweight='bold') # display file
offset = 0.05 #offset for text
fig.subplots_adjust(left=0.08, bottom=0.08, right=0.92, top=0.92)

def update_viewport(frame, tclfiles):
    tclfile = flatten_tcl(tclfiles)
    ax.clear()
    ax.set_xticks([]); ax.set_yticks([]) # hide axis tick marks/scale
    ax.axhline(**axis_style); ax.axvline(**axis_style) # draw axis lines

    # Read node info
    nodes = []
    with open(tclfile) as f:
        for line in f:
            if 'node' in line[:4] and len(line.split()) == 4:
                # Append [node tag, coordinate 1, coordinate 2]
                node = line.split()
                nodes.append((int(node[1]), float(node[2]), float(node[3])))

    # Read element info
    elements = []
    with open(tclfile) as f:
        for line in f:
            if 'element' in line[:7] and len(line.split()) >= 5:
                # Append [element type, element tag, iNode, jNode]
                ele = line.split()
                elements.append((ele[1], int(ele[2]), int(ele[3]), int(ele[4])))

    # Read boundary conditions
    fixities = []
    with open(tclfile) as f:
        for line in f:
            if 'fix' in line[:3] and len(line.split()) == 5:
                # Append [node tag, df1, df2, df3]
                fix = line.split()
                fixities.append((int(fix[1]), int(fix[2]),
                                 int(fix[3]), int(fix[4])))


    # Display nodes
    if nodes: # make sure some nodes exist before using them
        for node in nodes:
            ax.plot(node[1], node[2], linewidth=0, **node_style)
            ax.text(node[1]+offset, node[2]+offset,
                    'N'+str(node[0]), fontweight='bold') #label node

    # Function that returns node coords from a nodetag
    def nodecoords(nodetag, nodes=nodes):
        for node in nodes:
            if node[0] == nodetag:
                return node[1], node[2] # Coord-1 and Coord-2
                break

    # Display elements
    if nodes and elements: # make sure some elements exist before using them
        for element in elements:
            iNode = nodecoords(element[2])
            jNode = nodecoords(element[3])
            if iNode and jNode: # make sure both nodes exist before using them
                ax.plot((iNode[0], jNode[0]), (iNode[1], jNode[1]),
                         marker='', **ele_style)
                ax.text(offset+(iNode[0]+jNode[0])/2,
                        offset+(iNode[1]+jNode[1])/2,
                        'E'+str(element[1])) #label element

    # Display boundary conditions
    if fixities: # make sure some boundary conditions exist before using them
        for fixity in fixities:
            if any(fixity[0] in node for node in nodes): # make sure node exists
                node_x, node_y = nodecoords(fixity[0])
                if fixity[1] == 1: # DOF 1 fixed
                    ax.plot(node_x-offset, node_y, marker='>', **bc_style)
                if fixity[2] == 1: # DOF 2 fixed
                    ax.plot(node_x, node_y-offset, marker='^', **bc_style)
                if fixity[3] == 1: # DOF 3 fixed
                    ax.plot(node_x, node_y, marker='o', **bcrot_style)

    os.remove(tclfile)


ani = animation.FuncAnimation(fig, update_viewport, interval=refresh_rate*1000,
                              fargs=(tclfiles,))
pl.show()
