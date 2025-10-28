Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Configuring logging

You can turn on logging in the driver to assist in diagnosing issues.

You can log driver information by using the following methods:

- To save logged information in .log files, see [Using log files](jdbc20-using-log-files.md "jdbc20-using-log-files.md").
- To send logged information to the LogStream or LogWriter specified in the
  DriverManager, see [Using LogStream or LogWriter](jdbc20-logstream-option.md "jdbc20-logstream-option.md").
  You provide the configuration information to the driver in the connection URL. For
  more information about the syntax of the connection URL, see [Building the connection URL](jdbc20-build-connection-url.md "jdbc20-build-connection-url.md").
