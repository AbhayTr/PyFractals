'''

*************************************************************************************************************************************************************************

                                                                                   WELCOME TO PYFRACTALS

The equation which revolutionized MATHS!

A Python Class which creates the fractals design.

This module can:

1. Plot the fractals design on graph.
2. Save the fractals design as an image file.

@params

1. accuracy_factor (Optional): Greater the accuracy_factor, more detailed is the mandelbrot graph and more processing power and time is required (Defualt: 1000).
2. mode (Required): Specifies how one wants to visualize the mandel bot design, 'image' for saving the design as a picture file OR 'graph' for plotting the design on graph.
3. save_file_path (Optional): If mode is set to 'image', then this specefies the path were the image file has to be saved (Default: Same as your python file).

So go ahead and enjoy the beautiful and complex Fractals Design.

This module is made and intended for non-commercial use only.

© Abhay Tripathi

*************************************************************************************************************************************************************************

'''

from PIL import Image
import colorsys
import numpy as np
import matplotlib.pyplot as plt
from consolebar import ConsoleBar

class MandelBrot:

    def __init__(self, mode, accuracy_factor = 1000, save_file_path = ""):
        self.x = np.linspace(-4, 4, accuracy_factor)
        self.y = np.linspace(-4, 4, accuracy_factor)
        self.x_axis = []
        self.y_axis = []
        self.save_file_path = save_file_path
        if type(accuracy_factor) == int:
            self.accuracy_factor = accuracy_factor
        else:
            print("************************************")
            print()
            print("Accuracy factor has to be numerical!")
            print()
            print("************************************")
            print()
            input("Press any key to exit...")
            return "Accuracy factor has to be numerical!"
        if mode == "graph":
            self.show()
        elif mode == "image":
            self.show_image()
        else:
            print("*****************************************************")
            print()
            print("Incorrect mode!")
            print()
            print("Mode has to be either:")
            print()
            print("'graph': To plot mandelbrot design on a graph.")
            print("'image': To save mandelbrot design as a picture file.")
            print()
            print("*****************************************************")
            print()
            input("Press any key to exit...")

    def mandelbrot_equation(self, c, times_executed, return_colour = False):
        z = 0
        for i in range(times_executed):
            if return_colour:
                if abs(z) > 2:
                    return self.rgb_conv(i)
            z = z*z + c
        if return_colour:
            return (0, 0, 0)
        else:
            return z

    def show(self):
        for abscissa in ConsoleBar(self.x, "Creating MandelBrot Design:", "Created", 30):
            for ordinate in self.y:
                complex_number = np.complex(abscissa, ordinate)
                complex_number_value = self.mandelbrot_equation(complex_number, 80)
                if abs(complex_number_value) < 2:
                    self.x_axis.append(abscissa)
                    self.y_axis.append(ordinate)
        plt.plot(self.x_axis, self.y_axis)
        plt.show()
        print()
        print("************************************************")
        print()
        print("Successfully plotted mandelbrot design on graph!")
        print()
        print("************************************************")
        print()
        input("Press any key to exit...")

    def rgb_conv(self, i):
        color = 255 * np.array(colorsys.hsv_to_rgb(i / 255.0, 1.0, 0.5)) 
        return tuple(color.astype(int))

    def show_image(self):
        self.WIDTH = 1024
        image = Image.new("RGB", (self.WIDTH, int(self.WIDTH / 2))) 
        pixels = image.load()
        for x in ConsoleBar(range(image.size[0]), "Creating MandelBrot Design:", "Created", 30):
            for y in range(image.size[1]):
                x_pixel = (x - (0.75 * self.WIDTH)) / (self.WIDTH / 4)
                y_pixel = (y - (self.WIDTH / 4)) / (self.WIDTH / 4)
                complex_number = np.complex(x_pixel, y_pixel)
                pixels[x, y] = self.mandelbrot_equation(complex_number, self.accuracy_factor, True)
        path_to_picture_file = self.save_file_path + "mandelbrot.png"
        image.save(path_to_picture_file)
        success_line1 = "MandelBrot Design saved succesfully in picture file!"
        success_line2 = "Path to picture file: " + path_to_picture_file
        design_line = ""
        if len(success_line1) > len(success_line2):
            design_line = "*" * len(success_line1)
        else:
            design_line = "*" * len(success_line2)
        print()
        print(design_line)
        print()
        print(success_line1)
        print(success_line2)
        print()
        print(design_line)
        print()
        input("Press any key to exit...")
