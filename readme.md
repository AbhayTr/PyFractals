# PyFractals

## Visualising the equation which revolutionized maths!

Python Module which creates the fractals design.

## Mandelbrot equation: 

**ƒ(z) = z² + c** where **c is any complex number** is used to make the famous mandel brot fractals.

It can show the fractals design by:

- Plotting the fractals design on graph.
- Save the fractals design as an image file.

## Installation

Simply using PyPi: 

```
pip install pyfractals
```
## Usage

Simply run the following python code:

```python
from pyfractals import MandelBrot

MandelBrot(mode = "image/graph", optional_params)
```

Thats it!

## Parameters

- **mode (Required):** Specifies how one wants to visualize the fractals design, "image" for saving the design as a picture file, "graph" for plotting the design on graph.
- **accuracy_factor (Optional):** Greater the accuracy_factor, more detailed is the fractals design and more processing power and time is required (Defualt: 1000).
- **save_file_path (Optional):** If mode is set to "image", then this specefies the path were the image file has to be saved (Default: Same as your python file).

So go ahead and enjoy the beautiful and complex MandelBrot Fractals Design!
