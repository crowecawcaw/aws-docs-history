

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Configuring logging
<a name="jdbc20-configuring-logging"></a>

You can turn on logging in the driver to assist in diagnosing issues.

You can log driver information by using the following methods:
+ To save logged information in .log files, see [Using log files](jdbc20-using-log-files.md).
+ To send logged information to the LogStream or LogWriter specified in the DriverManager, see [Using LogStream or LogWriter](jdbc20-logstream-option.md). 

You provide the configuration information to the driver in the connection URL. For more information about the syntax of the connection URL, see [Building the connection URL](jdbc20-build-connection-url.md).