

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Using LogStream or LogWriter
<a name="jdbc20-logstream-option"></a>

Only turn on logging long enough to capture an issue. Logging decreases performance and can consume a large quantity of disk space. 

Set the LogLevel key in your connection URL to turn on logging and specify the amount of detail sent to the LogStream or LogWriter specified in the DriverManager. 

**To turn on logging that uses the LogStream or LogWriter:**

1. To configure the driver to log general information that describes the progress of the driver, set the LogLevel property to 1 or INFO.

1. To make sure that the new settings take effect, restart your JDBC application and reconnect to the server.