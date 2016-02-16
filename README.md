# PyPerlin
PyPerlin is an implementation of Ken Perlin's Perlin Noise in two dimensions.

## Dependencies
In order to use just the Perlin Noise (`pyperlin.py`) you just need out-of-the-box Python 3. 

If you want to run the test script (`test.py`), you need the PILLOW module for image functionalities.

## Usage
In order to use the module, just instantiate the noise selecting the desired parameters. A noise have the following attributes:

- `frequency` - the frequency of the noise
- `amplitude` - the variation between the maximum and minimum values of the noise (hardcoded default is 1)
- `octaves` - number of iterations of noise generation
- `persistence` - a value multiplied by the amplitude at each octave
- `seed` - a random or pseudo-random value that will randomize the generated noise (default is 0)

In pseudocode, what happens is the following:

```
for i = (0 .. octaves-1):
    total = total + noise(x * frequency, y * frequency) * amplitude
    amplitude = amplitude * persistence
    frequency = frequency * 2

return total
```

See `test.py` for details on how visualize the results.

## License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see [http://www.gnu.org/licenses/](http://www.gnu.org/licenses/).