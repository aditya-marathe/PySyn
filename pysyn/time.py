"""\
pysyn / time.py
--------------------------------------------------------------------------------
Aditya Marathe

Time class.
"""

__all__ = ['Time']

import numpy as np
import numpy.typing as npt


class Time:
    """\
    Time:

    Time keeper for the oscillators.

    Methods:

    get_array() -> npt.NDArray
    """

    __slots__ = ['duration', 'start']

    # Keeps a global sampling rate

    _sampling_rate: int = 44_100  # Hz

    def __init__(self, duration: float, start: float = 0.) -> None:
        """\
        Instantiates a time keeper for an oscillator.
        """
        self.duration = duration
        self.start = start

    def get_array(self) -> npt.NDArray:
        """\
        Calculates an array for the duration of the oscillator.
        
        Returns:

        npt.NDArray
            Array defining the duration of the oscillator.
        """
        return np.linspace(
            self.start,
            self.start + self.duration,
            int(Time._sampling_rate * self.duration),
            endpoint=False
        )

    @classmethod
    def get_sampling_rate(cls) -> int:
        """\
        Getter for the global sampling rate.
        """
        return Time._sampling_rate
