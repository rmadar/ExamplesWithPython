# Python Examples

Example of python macros dedicated to various purposes (FFT of a temporal signal, quick exploration of pandas dataframe, etc ...). Also, concrete examples based on jupyter notebook with
typical analysis or data visualization is stored on this repository.

For an interactive version of the notebooks [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/rmadar/ExamplesWithPython/master?filepath=NotebookExamples)

## Fast Fourier Transform (scipy)

The full study with detailed explanations can be seen in [this notebook](http://nbviewer.jupyter.org/github/rmadar/ExamplesWithPython/blob/master/NotebookExamples/ExampleFFT.ipynb)

### Approximation of an integral using Riemann sum (basic of FFT).

![Riemann sum](https://github.com/rmadar/ExamplesWithPython/blob/master/NotebookExamples/RiemannSum.png)


### Example of signal filtering using FFT

![Filtering example](https://github.com/rmadar/ExamplesWithPython/blob/master/NotebookExamples/FilteringExample.png)



## Manipulating rain dataset (pandas)

The full study can be seen in [this notebook](http://nbviewer.jupyter.org/github/rmadar/ExamplesWithPython/blob/master/NotebookExamples/PluviometryAnalysis.ipynb)

Cumulative rain amount is shown below:
![RainAmount.png](https://github.com/rmadar/ExamplesWithPython/blob/master/NotebookExamples/RainAmount.png)

One can also look at the average per year or per month:
![AveragedRain.png](https://github.com/rmadar/ExamplesWithPython/blob/master/NotebookExamples/AveragedRain.png)

Checking correlation between month might also be interesting:
![MonthToMonthCorrelation.png](https://github.com/rmadar/ExamplesWithPython/blob/master/NotebookExamples/MonthToMonthCorrelation.png)

A 2D histogram showing a calendar of the rain amount:
![NotebookExamples/RainCalandar.png](https://github.com/rmadar/ExamplesWithPython/blob/master/NotebookExamples/RainCalandar.png)
