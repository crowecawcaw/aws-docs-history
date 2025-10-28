# Using Python libraries with

EMR Serverless

When you run PySpark jobs on Amazon EMR Serverless applications, package various
Python libraries as dependencies. To do this, use native Python features, build a virtual environment, or directly configure your PySpark jobs to use Python libraries. This page covers each approach.

## Using native Python features

When you set the following configuration, use PySpark to upload Python files
(`.py`), zipped Python packages (`.zip`), and Egg files
(`.egg`) to Spark executors.

```
--conf spark.submit.pyFiles=s3://`amzn-s3-demo-bucket`/`EXAMPLE-PREFIX`/`<.py|.egg|.zip file>`
```

For more details about how to use Python virtual environments for PySpark jobs, refer to
[Using PySpark Native Features](https://spark.apache.org/docs/latest/api/python/tutorial/python_packaging.html#using-pyspark-native-features "https://spark.apache.org/docs/latest/api/python/tutorial/python_packaging.html#using-pyspark-native-features").

When using EMR Notebook, you can make the Python dependency available in your Notebook by executing
the following code:

```
    %%configure -f
 {
    "conf": {
    "spark.submit.pyFiles":"s3:///`amzn-s3-demo-bucket`/`EXAMPLE-PREFIX`/`<.py|.egg|.zip file>`
                   }
 }
```

## Building a Python virtual environment

To package multiple Python libraries for a PySpark job, create isolated Python
virtual environments.

1. To build the Python virtual environment, use the following commands. The example
   shown installs the packages `scipy` and `matplotlib` into a
   virtual environment package and copies the archive to an Amazon S3 location.

###### Important

You must run the following commands in a similar Amazon Linux 2 environment with
the same version of Python as you use in EMR Serverless, that is, Python
3.7.10 for Amazon EMR release 6.6.0. You can find an example Dockerfile in the
[EMR Serverless Samples](https://github.com/aws-samples/emr-serverless-samples/tree/main/examples/pyspark/dependencies "https://github.com/aws-samples/emr-serverless-samples/tree/main/examples/pyspark/dependencies") GitHub repository.

```
# initialize a python virtual environment
python3 -m venv pyspark_venvsource
source pyspark_venvsource/bin/activate

# optionally, ensure pip is up-to-date
pip3 install --upgrade pip

# install the python packages
pip3 install scipy
pip3 install matplotlib

# package the virtual environment into an archive
pip3 install venv-pack
venv-pack -f -o pyspark_venv.tar.gz

# copy the archive to an S3 location
aws s3 cp pyspark_venv.tar.gz s3://`amzn-s3-demo-bucket`/`EXAMPLE-PREFIX`/

# optionally, remove the virtual environment directory
rm -fr pyspark_venvsource
```

2. Submit the Spark job with your properties set to use the Python virtual
   environment.

```
--conf spark.archives=s3://`amzn-s3-demo-bucket`/`EXAMPLE-PREFIX`/pyspark_venv.tar.gz#environment
--conf spark.emr-serverless.driverEnv.PYSPARK_DRIVER_PYTHON=./environment/bin/python
--conf spark.emr-serverless.driverEnv.PYSPARK_PYTHON=./environment/bin/python
--conf spark.executorEnv.PYSPARK_PYTHON=./environment/bin/python
```

Note that if you don't override the original Python binary, the second
configuration in the preceding sequence of settings will be `--conf
 spark.executorEnv.PYSPARK_PYTHON=python`.

For more on how to use Python virtual environments for PySpark jobs, refer to
[Using Virtualenv](https://spark.apache.org/docs/latest/api/python/tutorial/python_packaging.html#using-virtualenv "https://spark.apache.org/docs/latest/api/python/tutorial/python_packaging.html#using-virtualenv"). For more examples of how to submit Spark jobs,
refer to [Using Spark configurations when you run EMR Serverless jobs](jobs-spark.md "jobs-spark.md").

## Configuring PySpark jobs to use Python libraries

With Amazon EMR releases 6.12.0 and higher, you can directly configure EMR Serverless PySpark
jobs to use popular data science Python libraries like [pandas](https://pandas.pydata.org/docs/user_guide/index.html "https://pandas.pydata.org/docs/user_guide/index.html"), [NumPy](https://numpy.org/doc/stable/user/index.html "https://numpy.org/doc/stable/user/index.html"), and [PyArrow](https://arrow.apache.org/docs/python/index.html "https://arrow.apache.org/docs/python/index.html") without any
additional setup.

The following examples demonstrate how to package each Python library for a PySpark
job.

NumPy
NumPy is a Python library for scientific computing that offers
multidimensional arrays and operations for math, sorting, random simulation, and
basic statistics. To use NumPy, run the following command:

```
import numpy
```

pandas
pandas is a Python library that is built on NumPy. The pandas library provides datas scientists
with [DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html "https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html") data structures and data analysis tools. To use
pandas, run the following command:

```
import pandas
```

PyArrow
PyArrow is a Python library that manages in-memory columnar data for improved job performance. PyArrow is based on the Apache Arrow cross-language development specification, which is a standard way to represent and exchange data in a columnar format. To use PyArrow, run the following command:

```
import pyarrow
```
