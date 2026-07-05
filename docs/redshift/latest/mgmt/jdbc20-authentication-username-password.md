Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Using username and password only

If the server you are connecting to doesn't use SSL, then you only need to
provide your Redshift username and password to authenticate the connection.

###### To configure authentication using your Redshift username and password only

1. Set the `UID` property to your Redshift username for
   accessing the Amazon Redshift server.
2. Set the PWD property to the password corresponding to your Redshift
   username.
