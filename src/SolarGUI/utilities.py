"""
Created on May 26 01:47:13 2022
"""

import tkinter as tk
from typing import Union, Any

import numpy as np
from astropy.constants import codata2018 as c_2018
from astropy.units.quantity import Quantity

try:
    from . import tk_functions as tk_f
except ImportError:
    import tk_functions as tk_f


def convert(parameter: Quantity, change_to: str) -> Quantity:
    """
    Change the unit of given Quantity to change_to unit string.

    Parameters
    ----------
    parameter : Quantity
        Input value for the celestial object parameter of which the unit is to be changed.
    change_to : str
        String representing the unit to change the quantity into.

    Returns
    -------
    Quantity
        The celestial object parameter with changed unit.

    """
    return parameter.to(change_to)


class PhysicalParameters:
    """
    Class to determine the physical parameters for the celestial objects.

    """

    def __init__(self, mass: float, radius: float):
        """
        Initialization function for PhysicalParameter class.

        Parameters
        ----------
        mass : TYPE
            Mass of the celestial object.
        radius : TYPE
            Radius of the celestial object.

        Returns
        -------
        None.

        """
        self.mass = mass
        self.radius = radius

    def volume(self):
        """
        Calculate the volume of the celestial object assuming the object in spherical.

        Returns
        -------
        Quantity
            Volume of the celestial object.

        """
        return (4 / 3) * np.pi * self.radius**3

    def density(self):
        """
        Calculate the mass density of the celestial object.

        Returns
        -------
        Quantity
            Density of the celestial object.

        """
        return (self.mass / self.volume()).to('g/cm^3')

    def surface_area(self):
        """
        Calculate the surface area of the celestial object.

        Returns
        -------
        Quantity
            Surface are of the celestial object.

        """
        return 4 * np.pi * self.radius**2

    def surface_gravity(self):
        """
        Calculate the surface gravity of the celestial object.

        Returns
        -------
        Quantity
            Surface gravity of the celestial object.

        """
        return (c_2018.G * (self.mass / self.radius**2)).si

    def get(self):
        """
        Get the values of volume, density, surface area, and surface gravity of the
        celestial object.

        """
        return self.volume(), self.density(), self.surface_area(), self.surface_gravity()


def comparison(c_win: Union[tk.Tk, tk.Toplevel], p_ojb: Any, c_obj: Any, c_lbl: str,
               reset: bool = False):
    """
    Compares the attributes of given celestial object (o_obj) with comparison celestial
    object (c_obj).

    Parameters
    ----------
    c_win : Union[tk.Tk, tk.Toplevel]
        tk.Tk or tk.Toplevel window to build the object inside.
    p_ojb : Any
        The object clas to which the comparison is being done.
    c_obj : Any
        The object class with which the comparison is being done.
    c_lbl : str
        Text representing the comparison celestial object.
    reset : bool, optional
        Option to set the comparison entries to null. The default is False.

    Returns
    -------
    None.

    """
    # get all the class attributes
    attributes = p_ojb.__dict__.keys()
    # get their number
    num_attributes = len(attributes)

    # divide the celestial object attribute values to that of comparison celestial
    # object attributes
    out = [p_ojb.__getattribute__(attr) / c_obj.__getattribute__(attr) for attr
           in attributes]

    # place the entries on the comparison window or reset them
    for value, num in zip(out, range(1, num_attributes + 1)):
        if value < 0.001:
            value = f'{value:.5e} × {c_lbl}'
        else:
            value = f'{np.round(value, 5)} × {c_lbl}'

        if not reset:
            tk_f.entry_placement(window=c_win, value=value, row=num, columns=4, width=20)
        else:
            tk_f.entry_placement(window=c_win, value='', row=num, columns=4, width=20)
