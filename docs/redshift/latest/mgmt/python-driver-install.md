Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Installing the Amazon Redshift Python connector

You can use any of the following methods to install the Amazon Redshift Python
connector:

- Python Package Index (PyPI)
- Conda
- Cloning the GitHub repository

## Installing the Python connector from

PyPI

To install the Python connector from the Python Package Index (PyPI), you can use
pip. To do this, run the following command.

```
>>> pip install redshift_connector
```

You can install the connector within a virtual environment. To do this, run the
following command.

```
>>> pip install redshift_connector
```

Optionally, you can install pandas and NumPy with the connector.

```
>>> pip install 'redshift_connector[full]'
```

For more information on pip, see the [pip site](https://pip.pypa.io/en/stable/ "https://pip.pypa.io/en/stable/").

## Installing the Python connector from

Conda

You can install the Python connector from Anaconda.org.

```
>>>conda install -c conda-forge redshift_connector
```

## Installing the Python connector by

cloning the GitHub repository from AWS

To install the Python connector from source, clone the GitHub repository from
AWS. After you install Python and virtualenv, set up your environment and install
the required dependencies by running the following commands.

```
$ git clone https://github.com/aws/amazon-redshift-python-driver.git
$ cd amazon-redshift-python-driver
$ virtualenv venv
$ . venv/bin/activate
$ python -m pip install -r requirements.txt
$ python -m pip install -e .
$ python -m pip install redshift_connector
```
