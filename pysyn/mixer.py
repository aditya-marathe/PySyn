"""
pysyn / mixer.py
--------------------------------------------------------------------------------
Aditya Marathe

Mixer class.
"""

__all__ = ['Mixer']

from typing import Any

from pysyn.osc import Oscillator
from pysyn.track import Track


class Mixer:
    """\
    Mixer:

    Mixes the tracks of several oscillators.
    """
    def __init__(self) -> None:
        self._tracks: dict[str, Track] = {}
        self._levels: dict[str, float] = {}

    def add_track(
            self,
            osc: Oscillator,
            steps: Any,
            name: str
        ) -> None:
        """\
        Registers a new track to this mixer.

        Notes:

        If a track of the same name already exists, this track will not be
        added to the mix.
        """
        self._tracks.setdefault(name, Track(osc=osc, steps=steps))
        self._levels.setdefault(name, 1.)  # Defaults to 100% volume

    def compile_(self) -> None:
        """
        Compiles all the tracks in this mix.
        """
        for name, track in self._tracks.items():
            compiled_track = track.compile_()

            # TODO: Need to first implement the step sequencer...


    def play(self) -> None:
        ...

    def compile_play(self) -> None:
        """\
        
        """
        self.compile_()
        self.play()

    def __str__(self) -> str:
        return 'Mixer()'

    def __repr__(self) -> str:
        return str(self)