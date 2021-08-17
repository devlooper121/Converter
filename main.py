from tkinter import *
from tkinter import ttk

units_and_const_length = {"meter": (1, 'm'),
                          "kilometer": (1000, 'Km'),
                          "centimeter": (0.01, 'cm'),
                          "foot": (0.3048, 'ft'),
                          "yard": (0.9144, 'yd'),
                          "mile": (1609.344, 'Mi'),
                          "inch": (0.0245, 'in')}

units_and_const_mass = {"gram": (1, 'g'),
                        "kilogram": (1000, 'Kg'),
                        "milligram": (0.001, 'mg'),
                        "metricTon": (1000000, 'MT'),
                        "Quantile": (100000, 'QT'),
                        "pound": (453.59237, 'lb'),
                        "stone": (6350.29317, 'st'),
                        "grain": (0.06479891, 'gr')}

units_and_const_area = {"sq. meter": (1, 'm\u00b2'),
                        "sq. kilometer": (1000000, 'Km\u00b2'),
                        "sq. centimeter": (0.01, 'cm\u00b2'),
                        "sq. foot": (0.3048, 'ft\u00b2'),
                        "sq. yard": (0.9144, 'yd\u00b2'),
                        "sq. mile": (1609.344, 'Mi\u00b2'),
                        "sq. inch": (0.0245, 'in\u00b2'),
                        "hectare": (10000, 'hectare'),
                        "Acre": (4046.85642, 'Acre')}

units_and_const_volume = {"liter": (1, 'l'),
                          "Hogshead": (238.480942, 'Hogshead'),
                          "milliliter": (0.001, 'ml'),
                          "cubic. meter": (1000, 'm\u00b3'),
                          "cubic. foot": (28.318466, 'ft\u00b3'),
                          "cubic. yard": (764.554858, 'yd\u00b3'),
                          "Oil barrel": (158.987295, 'barrel'),
                          "US gallon": (3.78541178, 'US gallon'),
                          "US tablespoon": (0.01478676, 'tablespoon'),
                          "US teaspoon": (0.00492892, 'teaspoon')}

units_and_const_speed = {"meter/second": (1, 'mps'),
                         "kilometer/hour": (0.27777778, 'Kph'),
                         "foot/second": (0.44704, 'ftps'),
                         "Knot": (0.5144444, 'Knot'),
                         "mile/hour": (0.44704, 'Mph')}

display = Tk()
display.title("The Converter")
display.geometry("595x300")
# display.config(padx=40,pady=40)

my_notebook = ttk.Notebook(display)
my_notebook.grid(pady=0)

my_frame1 = Frame(my_notebook, width=450, height=250, bg="sky blue")
my_frame2 = Frame(my_notebook, width=450, height=250, bg="light green")
my_frame3 = Frame(my_notebook, width=450, height=250, bg="light yellow")
my_frame4 = Frame(my_notebook, width=450, height=250, bg="pink")
my_frame5 = Frame(my_notebook, width=450, height=250, bg="light blue")
my_frame6 = Frame(my_notebook, width=450, height=250, bg="blue")

my_frame1.grid()
my_frame2.grid()
my_frame3.grid()
my_frame4.grid()
my_frame5.grid()
my_frame6.grid()

my_notebook.add(my_frame1, text="length")
my_notebook.add(my_frame2, text="volume")
my_notebook.add(my_frame3, text="mass")
my_notebook.add(my_frame4, text="Area")
my_notebook.add(my_frame5, text="speed")
my_notebook.add(my_frame6, text="")
my_notebook.hide(5)

label1 = Label(my_frame1, text="length")
label2 = Label(my_frame2, text="volume")
label3 = Label(my_frame3, text="mass")
label4 = Label(my_frame4, text="area")
label5 = Label(my_frame5, text="speed")

label1.grid()
label2.grid()
label3.grid()
label4.grid()
label5.grid()


def converter_function(in_unit, out_unit, input_value, all_units) -> float:
    secret_data1 = all_units[in_unit][0]
    secret_data2 = all_units[out_unit][0]
    temp = secret_data1 * input_value
    return temp / secret_data2


class ConverterGui:
    def __init__(self, root1, all_units, color):
        self.color = color
        self.all_units = all_units
        self.display1 = root1
        # Dropdown menu 1
        self.name_units = [key for key in all_units]
        self.symbol_units = [new_value[1] for (key, new_value) in all_units.items()]
        self.option1 = StringVar()
        self.drop1 = OptionMenu(self.display1, self.option1, *self.name_units)
        self.option1.set(self.name_units[0])
        self.drop1.grid(column=1, row=1)  # packing of element
        # blank text spacing
        self.blank_text0 = Label(text="     ")
        self.blank_text0.grid(column=1, row=2)  # packing of element
        # Dropdown menu 2
        self.option2 = StringVar()
        self.drop2 = OptionMenu(self.display1, self.option2, *self.name_units)
        self.option2.set(self.name_units[1])
        self.drop2.grid(column=1, row=3)  # packing of element
        # input Box
        self.first_box = Entry(self.display1, font=("Arial", 15, "bold"), width=20)
        self.first_box.grid(column=2, row=1)  # packing of element
        # Blank text for spacing
        self.blank_text1 = Label(self.display1, text="     ", bg=color)
        self.blank_text1.grid(column=2, row=2)  # packing of element
        # output text
        self.second_box = Label(self.display1, text="0", font=("Arial", 15, "bold"), width=20, bg=color)
        self.second_box.grid(column=2, row=3)  # packing of element

        # output text of unit
        self.unit_box = Label(self.display1, text=self.symbol_units[0], font=("Arial", 15, "bold"), width=15, bg=color)
        self.unit_box.grid(column=3, row=1)  # packing of element
        # Blank text for spacing
        self.blank_text2 = Label(self.display1, text="     ", bg=color)
        self.blank_text2.grid(column=3, row=2)  # packing of element
        # output text of unit
        self.unit_box2 = Label(self.display1, text=self.symbol_units[1], font=("Arial", 15, "bold"), width=15, bg=color)
        self.unit_box2.grid(column=3, row=3)  # packing of element
        # Blank text for spacing
        self.blank_text3 = Label(self.display1, text="     ", bg=self.color)
        self.blank_text3.grid(column=2, row=4)  # packing of element
        self.my_button = Button(self.display1, text="calculate", command=self.calculate, font=("Arial", 10, "bold"),
                                bg="light green")
        self.my_button.grid(column=2, row=5)

    def calculate_by_key(self, event):
        self.calculate()

    def calculate(self):
        # Choice of dropdown buttons
        first_unit = self.option1.get()
        second_unit = self.option2.get()
        # units selection for output screen
        u1 = self.all_units[first_unit][1]
        u2 = self.all_units[second_unit][1]
        # input from Input box
        first_data = self.first_box.get()
        # string conversion to float if possible
        try:
            float(first_data)
        except TypeError:
            first_data = 0
        except ValueError:
            first_data = 0
        else:
            first_data = float(first_data)
        if first_data != 0:
            second_data = converter_function(first_unit, second_unit, first_data, self.all_units)
            self.second_box.config(text=f"{round(second_data, 8)}", font=("Arial", 15, "bold"))
            self.unit_box.config(text=u1, font=("Arial", 15, "bold"))
            self.unit_box2.config(text=u2, font=("Arial", 15, "bold"))
        else:
            self.second_box.config(text="0", font=("Arial", 15, "bold"))


first1 = ConverterGui(my_frame1, units_and_const_length, "sky blue")

first2 = ConverterGui(my_frame2, units_and_const_volume, "light green")

first3 = ConverterGui(my_frame3, units_and_const_mass, "light yellow")

first4 = ConverterGui(my_frame4, units_and_const_area, "pink")

first5 = ConverterGui(my_frame5, units_and_const_speed, "light blue")


def calculate_by_key(event):
    first1.calculate_by_key('<KeyPress>')
    first2.calculate_by_key('<KeyPress>')
    first3.calculate_by_key('<KeyPress>')
    first4.calculate_by_key('<KeyPress>')
    first5.calculate_by_key('<KeyPress>')


if __name__=='__main__':
    display.bind('<KeyPress>', calculate_by_key)
    display.mainloop()