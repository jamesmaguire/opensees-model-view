# OpenSees Model View

OpenSees model view is a Python package that can be used to visualise your OpenSees model as it is written. The script monitors a specified tcl file (or files) in which you define nodes, elements and fix conditions, and produces a drawing of the model. The model drawing will be updated each time you save the tcl file(s). The script will work for 2D/3dof and 3D/6dof models; but not for other combinations at the moment.

The visual feedback is intended to help you identify some model errors before execution, but mostly just makes you feel good.

At this stage, the project is best suited to structural models using elements that have an iNode and a jNode. I'm not sure if it will play nicely with geo elements.

### How it works

1. Copy `model_view.py` into the directory where you keep your tcl files.
2. Open `model_view.py` in a text editor and set the values for `tclfiles` and `refresh_rate`. You can also change the style options to change the look of the view.
3. Run `model_view.py` and then edit your tcl file as normal. The viewer will refresh after you have saved your file and the `refresh_rate` duration has been reached.

### Examples

![Example usage gif](https://cloud.githubusercontent.com/assets/22332883/25312657/25d0a1d4-2873-11e7-82f8-ac6cb2522550.gif)

2D model example | 3D model example
:---------:|:---------:
![2D example](https://cloud.githubusercontent.com/assets/22332883/25365954/6983dfa6-29c0-11e7-8d72-615aad79d4e2.png) | ![3D example](https://cloud.githubusercontent.com/assets/22332883/25365961/754aeb7c-29c0-11e7-97c9-3e3881de5056.png)

### Dependencies

The package is written in `Python3` with `matplotlib`. I run `Python3.6` and `matplotlib2.0`, but I have no reason to think that this wouldn't work on earlier versions, as long as they are not too old. `OpenSees` is not needed.

### Feature wish-list

- [x] Plot nodes are they are saved in a watched tcl script
- [x] Add node labels
- [x] Add support for elements
- [x] Add support for fixity conditions
- [x] Add support for variables and expressions in tcl script
- [x] Add support for watching multiple tcl files (for those models made up of many files)
- [ ] Add support for loads
- [ ] Add support for nodes created within loop
- [x] Add support for 3D models
        - [ ] Add support for rotational dofs

I'd really appreciate to hear from anyone who uses this package. I'm sure that it can be improved to better suit more people.
