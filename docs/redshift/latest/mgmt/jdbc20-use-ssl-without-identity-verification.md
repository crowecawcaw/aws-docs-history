Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Using SSL without

identity verification

If the server you are connecting to uses SSL but doesn't require identity
verification, then you can configure the driver to use a non-validating SSL factory.

###### To configure an SSL connection without identity verification

1. Set the `UID` property to your Redshift username for accessing
   the Amazon Redshift server.
2. Set the `PWD` property to the password corresponding to your
   Redshift username.
3. Set the `SSLFactory` property to
   `com.amazon.redshift.ssl.NonValidatingFactory`.
