# OpenSees Model View

OpenSees model view is a Python package that can be used to visualise your OpenSees model as it is written. The script monitors a specified tcl file (or files) in which you define nodes, elements and fix conditions, and produces a drawing of the model. The model drawing will be updated each time you save the tcl file(s).

The visual feedback is intended to help you identify some model errors before execution, but mostly just makes you feel good.

At this stage, the project is best suited to structural models using elements that have an iNode and a jNode. I'm not sure if it will play nicely with geo elements.

### How it works

1. Copy `model_view_2d.py` and `tcl_handler.py` into the directory where you keep your tcl files
2. Open `model_view_2d.py` and set the values for `tclfiles` and `refresh_rate`
3. Run `model_view_2d.py` and then just edit your tcl file as normal

![Example usage gif](https://cloud.githubusercontent.com/assets/22332883/25312657/25d0a1d4-2873-11e7-82f8-ac6cb2522550.gif)

The script reads your tcl files to determine node locations, elements and boundary conditions. If you wish, you can tinker with the style properties, which are at close to the top of `model_view_2d.py`.

### Dependencies

I believe that the only two dependencies are `Python3` and `matplotlib`. I run `Python3.6` and `matplotlib2.0`, but I have no reason to think that this wouldn't work on earlier versions. `OpenSees` is not needed.

### Feature wish-list

- [x] Plot nodes are they are saved in a watched tcl script
- [x] Add node labels
- [x] Add support for elements
- [x] Add support for fixity conditions
- [x] Add support for variables and expressions in tcl script
- [x] Add support for watching multiple tcl files (for those models made up of many files)
- [ ] Add support for loads
- [ ] Add support for nodes created within loop
- [ ] Add support for 3D models (probably a separate script needed)

I'd really appreciate to hear from anyone who uses this package. I'm sure that it can be improved to better suit more people.
