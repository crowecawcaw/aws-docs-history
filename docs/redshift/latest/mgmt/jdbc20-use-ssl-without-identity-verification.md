

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Using SSL without identity verification
<a name="jdbc20-use-ssl-without-identity-verification"></a>

If the server you are connecting to uses SSL but doesn't require identity verification, then you can configure the driver to use a non-validating SSL factory. 

**To configure an SSL connection without identity verification**

1. Set the `UID` property to your Redshift username for accessing the Amazon Redshift server.

1. Set the `PWD` property to the password corresponding to your Redshift username.

1. Set the `SSLFactory` property to `com.amazon.redshift.ssl.NonValidatingFactory`.