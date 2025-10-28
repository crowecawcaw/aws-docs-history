Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Using LogStream or LogWriter

Only turn on logging long enough to capture an issue. Logging decreases
performance and can consume a large quantity of disk space.

Set the LogLevel key in your connection URL to turn on logging and specify the
amount of detail sent to the LogStream or LogWriter specified in the DriverManager.

###### To turn on logging that uses the LogStream or LogWriter:

1. To configure the driver to log general information that describes the
   progress of the driver, set the LogLevel property to 1 or INFO.
2. To make sure that the new settings take effect, restart your JDBC
   application and reconnect to the server.
