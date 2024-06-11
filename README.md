# pysyn

A simple additive synthesizer.

## Acknowledgements

Many thanks to my friend, Uzay Islek, who guided me through the intricacies of music theory and provided feedback on my ideas; the project would not have moved forward without his musical expertise.

## Objectives

Overall, create a simple additive synthesizer in Python.

### Short-term

1. Implement four basic oscillators: sine, square, triangle and sawtooth
2. Implement a "mixer" which:
    - Is able to handle several "tracks"
    - Can change the level/volume of the "tracks" in the mix
    - Is the interface for making any changes on the actual "track"
    - Compiles all the "tracks"
3. The "track" will be an internal object which will be responsible for:
    - Compiling the oscillator assigned to this track using a step sequence
4. Implement a scripted step-sequence - a way to write sheet music as code
    - Explore existing solutions:
        - [MIDI](https://en.wikipedia.org/wiki/MIDI) (?)
        - [LilyPond](https://lilypond.org/)
    - Update (11.06.2024): Create a parser for [abc notation](https://abcnotation.com/) - clean syntax, get sheet music, and easily expandable.

### Long-term

1. Implement envelopes and ADSR for oscillators
2. Improve sound richness by adding harmonics - a new oscillator class (?)
3. Implement filters e.g. low pass, or high pass
4. Add samples from real instruments
5. Create a GUI for the synthesizer

### Potential Issues

1. Implementing sheet-music into code may prove to be a huge challenge...
    - May require some simplifications
2. Making more complex sounds could be computationally expensive
    - Can explore HPC technqiues or store data of samples

### Desired Product

```python

import pysyn

mix = pysyn.Mixer()

mix.add_track(
    osc=pysyn.Oscillator(wave=pysyn.Oscillators.SIN),
    steps=[...],  # Step sequence of some song
    name='Track 1'
)

mix.set_level(track='Track 1', level=0.7)

mix.add_filter(
    track='Track 1',
    filter=pysyn.LowPassFilter(cutoff=440),
    start=5  # seconds
)

mix.compile_play()

```

For current progress refer to `example.py`.

## Tech Stack

- [Python](https://www.python.org/) 3.10+
- [NumPy](https://numpy.org/) - For fast array calculations and mathematical constants and functions.

## Further Reading

- Additive synthesis - [https://en.wikipedia.org/wiki/Additive_synthesis](https://en.wikipedia.org/wiki/Additive_synthesis)
