Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# stored\_proc\_log\_min\_messages

## Values (default in bold)

**LOG**, INFO, NOTICE, WARNING, EXCEPTION

## Description

Specifies the minimum logging level of raised stored procedure messages. Messages at
or above the specified level are logged. The default is LOG (all messages are logged).
The order of log levels from highest to lowest is as follows:

1. EXCEPTION
2. WARNING
3. NOTICE
4. INFO
5. LOG

For example if you specify a value of NOTICE, then messages are only logged for NOTICE, WARNING, and EXCEPTION.
