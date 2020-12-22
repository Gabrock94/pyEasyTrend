# pyEasyTrend
A simple entrypoint to perform a trend analysis in Python.

__Repository__
![GitHub release](https://img.shields.io/github/release/Gabrock94/pyEasyTrend.svg)

__PyPI__
![Upload Python Package](https://github.com/Gabrock94/pyEasyTrend/workflows/Upload%20Python%20Package/badge.svg)
[![PyPI](https://img.shields.io/pypi/v/pyEasyTrend.svg)](https://badge.fury.io/py/pyEasyTrend)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/pyEasyTrend.svg)](https://pypi.python.org/pypi/pyEasyTrend/)
[![PyPI status](https://img.shields.io/pypi/status/pyEasyTrend.svg)](https://pypi.python.org/pypi/pyEasyTrend/)

__Documentation__
[![Documentation Status](https://readthedocs.org/projects/pyeasytrend/badge/?version=latest)](http://pyeasytrend.readthedocs.io/en/latest/?badge=latest)
<!--- ([![DOI](https://zenodo.org/badge/109267664.svg)](https://zenodo.org/badge/latestdoi/109267664)) -->

## Installation
pyEasyTrend can be installed using pip:
```bash
pip install pip install pyEasyTrend
```
or downloading / cloning the repository and, from the root folder of the project, running:
```bash
python setup.py install
```

### Updating the package
To update the package via pip, you can use:
```bash
pip install --user --upgrade pyeasytrend
```

## Documentation
You can check the [full documentation online](https://pyeasytrend.rtfd.io). Alternatively, a copy of the documentation is available [in the docs folder](https://github.com/Gabrock94/pyEasyTrend/tree/master/docs/_build/html)

## Example (Coming soon)
```python
import pyeasytrend
data = {'StudyTime':[24, 44, 21, 45, 54, 26, 57, 34, 33, 12, 17, 21, 58, 41, 29, 55, 42, 40, 21, 9, 39, 30, 17, 31, 51, 42, 30, 3, 20, 21, 4, 16, 26, 6, 18, 50, 60, 13, 23, 13, 3, 35, 38, 51, 12, 35, 7, 42, 20, 41, 37, 56, 19, 57, 12, 49, 15, 6, 43, 7, 40, 12, 35, 4, 46, 29, 6, 38, 36, 33, 21, 33, 50, 54, 25, 38, 48, 17, 28, 48, 16, 50, 24, 15, 40, 54, 40, 42, 2, 20, 24, 21, 37, 15, 52, 36, 5, 7, 29, 21],
        'Score':[18, 47, 21, 60, 80, 18, 100, 28, 41, 7, 12, 17, 82, 45, 33, 94, 41, 55, 9, 6, 53, 24, 13, 35, 62, 43, 33, 2, 17, 10, 0, 7, 14, 0, 14, 72, 94, 7, 14, 3, 0, 43, 39, 80, 5, 39, 4, 43, 14, 37, 39, 80, 16, 94, 7, 55, 13, 2, 45, 6, 55, 7, 35, 0, 69, 18, 0, 45, 43, 27, 11, 37, 67, 82, 16, 41, 74, 10, 19, 55, 14, 60, 18, 7, 55, 64, 37, 60, 2, 10, 17, 14, 30, 6, 69, 32, 2, 1, 32, 10]}
df = pd.DataFrame(data)


```

### Requirements
- Numpy
- Scipy
- Pandas
- Matplotlib

## Contacts
Feel free to contact me for questions, suggestions or to give me advice as well at: giulio001@e.ntu.edu.sg

## Coffee?
<a href='https://ko-fi.com/B0B3K45F' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://az743702.vo.msecnd.net/cdn/kofi2.png?v=0' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>
