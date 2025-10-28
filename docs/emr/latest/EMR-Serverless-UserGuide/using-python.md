# Using different Python versions with EMR Serverless

In addition to the use case in [Using Python libraries with
EMR Serverless](using-python-libraries.md "using-python-libraries.md"), you can also use Python virtual environments
to work with different Python versions than the version packaged in the Amazon EMR release for
your Amazon EMR Serverless application. To do this, build a Python virtual
environment with the Python version you want to use.

###### To submit a job from a Python virtual environment

1. Build your virtual environment with the commands in the following example. This
   example installs Python 3.9.9 into a virtual environment package and copies the
   archive to an Amazon S3 location.

###### Important

If you use Amazon EMR releases 7.0.0 and higher, run your commands
in an Amazon Linux 2023 environment similar to the one you use for your EMR Serverless applications.

If you use release 6.15.0 or lower,
run the following commands in a similar Amazon Linux 2 environment.

```
# install Python 3.9.9 and activate the venv
yum install -y gcc openssl-devel bzip2-devel libffi-devel tar gzip wget make
wget https://www.python.org/ftp/python/3.9.9/Python-3.9.9.tgz && \
tar xzf Python-3.9.9.tgz && cd Python-3.9.9 && \
./configure --enable-optimizations && \
make altinstall

# create python venv with Python 3.9.9
python3.9 -m venv pyspark_venv_python_3.9.9 --copies
source pyspark_venv_python_3.9.9/bin/activate

# copy system python3 libraries to venv
cp -r /usr/local/lib/python3.9/* ./pyspark_venv_python_3.9.9/lib/python3.9/

# package venv to archive.
# **Note** that you have to supply --python-prefix option
# to make sure python starts with the path where your
# copied libraries are present.
# Copying the python binary to the "environment" directory.
pip3 install venv-pack
venv-pack -f -o pyspark_venv_python_3.9.9.tar.gz --python-prefix /home/hadoop/environment

# stage the archive in S3
aws s3 cp pyspark_venv_python_3.9.9.tar.gz s3://<path>

# optionally, remove the virtual environment directory
rm -fr pyspark_venv_python_3.9.9
```

2. Set your properties to use the Python virtual environment and submit the Spark
   job.

```
# note that the archive suffix "environment" is the same as the directory where you copied the Python binary.
--conf spark.archives=s3://amzn-s3-demo-bucket/EXAMPLE-PREFIX/pyspark_venv_python_3.9.9.tar.gz#environment
--conf spark.emr-serverless.driverEnv.PYSPARK_DRIVER_PYTHON=./environment/bin/python
--conf spark.emr-serverless.driverEnv.PYSPARK_PYTHON=./environment/bin/python
--conf spark.executorEnv.PYSPARK_PYTHON=./environment/bin/python
```

For more on how to use Python virtual environments for PySpark jobs, refer to [Using Virtualenv](https://spark.apache.org/docs/latest/api/python/tutorial/python_packaging.html#using-virtualenv "https://spark.apache.org/docs/latest/api/python/tutorial/python_packaging.html#using-virtualenv"). For more examples of how to submit Spark jobs, refer to [Using Spark configurations when you run EMR Serverless jobs](jobs-spark.md "jobs-spark.md").
