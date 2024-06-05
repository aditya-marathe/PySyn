"""
pysyn / mixer.py
--------------------------------------------------------------------------------
Aditya Marathe

Track class.
"""

__all__ = ['Track']

import numpy as np
import numpy.typing as npt

from pysyn.osc import Oscillator


class Track:
    """\
    [PySyn Internal] Track:
    
    The track manages an oscillator and step sequence, and is responsible for
    compilation of music.
    """

    def __init__(
            self,
            osc: Oscillator,
            steps: list[tuple[str, str]]
        ) -> None:
        """\
        
        """
        self._osc: Oscillator = osc
        self._steps: list[tuple[str, str]] = steps

        self._filters = []  # TODO

    def compile_(self) -> npt.NDArray:
        """
        WIP:

        1. Convert the steps into frequencies and durations
        2. Oscillate at the given frequencies and durations
        3. Append or sum the resulting waves

        """
        ...