"""\
pysyn / osc.py
--------------------------------------------------------------------------------
Aditya Marathe

Defines functions and classes related to oscillators and wave generation.
"""

__all__ = [
    'add_oscillator',
    'print_oscillators',
    'Oscillators',
    'Oscillator',
    'fourier_transform'
]

from typing import Callable
from typing import TypeAlias
from typing import Literal

from enum import Enum

import numpy as np
import numpy.typing as npt


from pysyn.time import Time


Wave: TypeAlias = Literal['Sine', 'Square', 'Triangle', 'Sawtooth']
WaveGenerator: TypeAlias = Callable[[npt.NDArray, float, float], npt.NDArray]

# Wave generation stuff --------------------------------------------------------


def _generate_sin(t: npt.NDArray, freq: float, phase: float) -> npt.NDArray:
    """\
    [PySyn Internal] Sine wave generator.

    Args:

    t: npt.NDArray
        Time array which defines the duration of the oscillations.

    freq: float
        Frequency of the oscillator.

    phase: float
        Phase of the oscillator in radians.

    Returns:

    npt.NDArray
        The generated waveform at the given parameters.
    """
    return np.sin(2 * np.pi * freq * t + phase)


def _generate_sqr(t: npt.NDArray, freq: float, phase: float) -> npt.NDArray:
    """\
    [PySyn Internal] Square wave generator.

    Args:

    t: npt.NDArray
        Time array which defines the duration of the oscillations.

    freq: float
        Frequency of the oscillator.

    phase: float
        Phase of the oscillator in radians.

    Returns:

    npt.NDArray
        The generated waveform at the given parameters.
    """
    return np.sign(np.sin(2 * np.pi * freq * t + phase))


def _generate_tri(t: npt.NDArray, freq: float, phase: float) -> npt.NDArray:
    """\
    [PySyn Internal] Triangle wave generator.

    Args:

    t: npt.NDArray
        Time array which defines the duration of the oscillations.

    freq: float
        Frequency of the oscillator.

    phase: float
        Phase of the oscillator in radians.

    Returns:

    npt.NDArray
        The generated waveform at the given parameters.
    """
    return 2 * np.arcsin(np.sin(2 * np.pi * freq * t + phase)) / np.pi


def _generate_saw(t: npt.NDArray, freq: float, phase: float) -> npt.NDArray:
    """\
    [PySyn Internal] Sawtooth wave generator.

    Args:

    t: npt.NDArray
        Time array which defines the duration of the oscillations.

    freq: float
        Frequency of the oscillator.

    phase: float
        Phase of the oscillator in radians.

    Returns:

    npt.NDArray
        The generated waveform at the given parameters.
    """
    offset = phase / (2 * np.pi)
    return 2 * (freq * t + offset - np.floor(0.5 + freq * t + offset))


_oscs: dict[str, WaveGenerator] = {
    # Initialises with the default PySyn oscillators
    'Sine': _generate_sin,
    'Square': _generate_sqr,
    'Triangle': _generate_tri,
    'Sawtooth': _generate_saw
}


def add_oscillator(name: str, wave_func: WaveGenerator) -> None:
    """\
    Add a custom oscillator.

    Args:

    name: str
        Oscillator name.

    wave_func: WaveGenerator
        A function which defines the oscillator - see Notes.

    Notes:

    The `wave_func` argument accepts any callable which accepts a NumPy array of
    the time, a floating point frequency value, and a floating point phase
    value. The callable should return a NumPy array of the same length as the
    time array.
    """
    if name in _oscs:
        raise NameError(f'Wave name \'{name}\' already exists!')

    _oscs[name] = wave_func


def print_oscillators() -> None:
    """\
    Prints the avalible oscillators.
    """
    print('[PySyn] Avalible oscillators: ' + ', '.join(_oscs.keys()) + '.')


# Oscillator class -------------------------------------------------------------


class Oscillators(Enum):
    """\
    Oscillators:

    Enum of the (default) avalible oscillators.

    Notes:

    The default PySyn oscillators are: Sine, Square, Triangle and Sawtooth.
    """
    SIN = 'Sine'
    SQR = 'Square'
    TRI = 'Triangle'
    SAW = 'Sawtooth'


class Oscillator:
    """\
    Oscillator:

    An oscillator of any form. All oscillator objects depend on the global 
    sampling rate and must be defined by a frequency.

    Attributes:

    freq: float
        Frequency of the oscillator.

    phase: float
        Phase of the oscillator in radians.

    Methods:

    oscillate(t: npt.NDArray) -> npt.NDArray
    """

    __slots__ = ['_wave', '_wave_func']

    def __init__(self, wave: str | Wave) -> None:
        """\
        Instantiates an oscillator.

        Args:

        wave: str | Wave
            Name of the wave/oscillator.
        """
        self._wave: str | Wave = wave

        if _oscs.get(self._wave) is None:
            raise NameError(f'Wave \'{self._wave}\' does not exist!')

        self._wave_func: WaveGenerator = _oscs[self._wave]

    def oscillate(self, t: Time, freq: float, phase: float) -> npt.NDArray:
        """\
        Oscillates to produce a periodic wave.

        Args:

        t: Time
            Time object which defines the duration of the oscillator.

        freq: float
            Frequency of the oscillator.

        phase: float
            Phase of the oscillator in radians. Defaults to 0.

        Returns:

        npt.NDarray
            Array of the waveform at a particular sampling rate.
        """
        return self._wave_func(t.get_array(), freq, phase)

    def __str__(self) -> str:
        return f'Oscillator(wave=\'{self._wave}\')'

    def __repr__(self) -> str:
        return str(self)


# Oscillator calculations ------------------------------------------------------


def fourier_transform(wave: npt.NDArray) -> tuple[npt.NDArray, npt.NDArray]:
    """\
    Calculates the Fourier transform for a given oscillator.

    Args:

    wave: npt.NDArray
        Waveform (calculated from some oscillator).
    """
    fft_arr = np.fft.fft(wave)
    freq_arr = np.fft.fftfreq(len(fft_arr), 1/Time.get_sampling_rate())

    return freq_arr, fft_arr
