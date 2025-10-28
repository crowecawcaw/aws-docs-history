Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Using username and

password only

If the server you are connecting to doesn't use SSL, then you only need to
provide your Redshift username and password to authenticate the connection.

###### To configure authentication using your Redshift username and password

only

1. Set the `UID` property to your Redshift username for
   accessing the Amazon Redshift server.
2. Set the PWD property to the password corresponding to your Redshift
   username.
