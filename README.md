# Statispy

Satisfy your cravings for statistics using `statispy`. It's a python toolset what will help you in your journey of statistical analysis through a plug and play manner. All you need to do is import the tools, feed the data, and collect the result, all through one single line of code. Our mission: Make statistics easy for non-coding statisticians.


Table of contents
=================
   * [Prerequisites](Prerequisites)
   * [Installating](Installing)
   * [Documentation](Documentation)
      * [sample](##sample)
      * [stats](##stats)
      * [correlation](##correlation)
      
Prerequisites
==================
As of now, the statispy toolset supports only the Pandas Dataframe format for data. The dependencies that you need to use this toolset are

```python
Python >=3.6
pandas==1.0.1
```

Installing
===============
Installing the package is a no brainer. 

```bash
pip install statispy
```

Documentation
========
Please read the documentation to understand how to use the toolset.

## sample
Sample is a sub-package that deals with sampling data. Currently the tools support only basic sampling techniques, which includes : *Random sampling* and *Systematic sampling*.

To import the sampling tools use 
```python
from statispy import sample
```

### Basic sampling
```python
sample.basic_sample(data, size, method = 'random')
```
1. data: pandas DataFrame object, containing the statistical dataset (population)
2. size: Sample size
3. method: sampling technique. ```method = 'random'``` creates a random sample. ```method = 'systematic'``` creates a systematic sample.
Returns : Dataframe

## stats
The stats sub-package offers basic statistical tools which includes : *Mean*, *Root mean square*,*Standard deviation* and *variance*

To import the sampling tools use 
```python
from statispy import stats
```

### Mean
```python
stats.mean(data, col, weight = None)
```
1. data: pandas DataFrame object, containing the statistical dataset (population)
2. col: column whose mean is to be calculated
3. weight: Default value is ```None```. To calculate weighted mean, set ```weight``` as the column name which contains the weight

Returns : Float/integer

### Root mean square
```python
stats.RMS(data, col)
```
1. data: pandas DataFrame object, containing the statistical dataset (population)
2. col: column whose mean is to be calculated

Returns : Float/integer


### Variance
```python
stats.variance(data, col)
```
1. data: pandas DataFrame object, containing the statistical dataset (population)
2. col: column whose mean is to be calculated

Returns : Float/integer

### Standard Deviation
```python
stats.SD(data, col)
```
1. data: pandas DataFrame object, containing the statistical dataset (population)
2. col: column whose mean is to be calculated

Returns : Float/integer

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/Shankhanil/statispy/tags). 

## Authors

* **Shankhanil Ghosh** - *Initial work*

See also the list of [contributors](https://github.com/Shankhanil/statispy/contributors) who participated in this project.

## License

This project is licensed under the Apache-2.0 License - see the [LICENSE.md](LICENSE.md) file for details
