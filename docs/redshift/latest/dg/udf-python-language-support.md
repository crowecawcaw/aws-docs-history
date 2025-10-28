Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Python language support for UDFs

You can create a custom UDF based on the Python programming language. The [Python 2.7 standard library](https://docs.python.org/2/library/index.html "https://docs.python.org/2/library/index.html")
is available for use in UDFs, with the exception of the following modules:

- ScrolledText
- Tix
- Tkinter
- tk
- turtle
- smtpd
  In addition to the Python Standard Library, the following modules are part of the
  Amazon Redshift implementation:

- [numpy 1.8.2](http://www.numpy.org/ "http://www.numpy.org/")
- [pandas 0.14.1](https://pandas.pydata.org/ "https://pandas.pydata.org/")
- [python-dateutil
  2.2](https://dateutil.readthedocs.org/en/latest/ "https://dateutil.readthedocs.org/en/latest/")
- [pytz 2014.7](https://pypi.org/project/pytz/2014.7/ "https://pypi.org/project/pytz/2014.7/")
- [scipy 0.12.1](https://www.scipy.org/ "https://www.scipy.org/")
- [six 1.3.0](https://pypi.org/project/six/1.3.0/ "https://pypi.org/project/six/1.3.0/")
- [wsgiref 0.1.2](https://pypi.python.org/pypi/wsgiref "https://pypi.python.org/pypi/wsgiref")
  You can also import your own custom Python modules and make them available for use in
  UDFs by executing a [CREATE LIBRARY](r_CREATE_LIBRARY.md "r_CREATE_LIBRARY.md")
  command. For more information, see [Example: Importing custom Python
  library modules](udf-importing-custom-python-library-modules.md "udf-importing-custom-python-library-modules.md").

###### Important

Amazon Redshift blocks all network access and write access to the file system through
UDFs.

###### Note

Python 3 isn’t available for Python UDFs.
To get Python 3 support for Amazon Redshift UDFs, use
[Scalar Lambda UDFs](udf-creating-a-lambda-sql-udf.md "udf-creating-a-lambda-sql-udf.md") instead.
