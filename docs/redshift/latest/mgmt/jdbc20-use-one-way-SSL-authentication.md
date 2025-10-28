Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Using one-way SSL

authentication

If the server you are connecting to uses SSL and has a certificate, then you can
configure the driver to verify the identity of the server using one-way
authentication.

One-way authentication requires a signed, trusted SSL certificate for verifying
the identity of the server. You can configure the driver to use a specific
certificate or access a TrustStore that contains the appropriate certificate. If you
don't specify a certificate or TrustStore, then the driver uses the default
Java TrustStore (typically either `jssecacerts` or `cacerts`).

###### To configure one-way SSL authentication

1. Set the UID property to your Redshift username for accessing the Amazon Redshift
   server.
2. Set the PWD property to the password corresponding to your Redshift
   username.
3. Set the SSL property to true.
4. Set the SSLRootCert property to the location of your root CA
   certificate.
5. If you aren't using one of the default Java TrustStores, then do one
   of the following:
   - To specify a server certificate, set the SSLRootCert property to
     the full path of the certificate.
   - To specify a TrustStore, do the following:
     1. Use the keytool program to add the server certificate to
        the TrustStore that you want to use.
     2. Specify the TrustStore and password to use when starting
        the Java application using the driver. For example:

     ```
     -Djavax.net.ssl.trustStore=[TrustStoreName]
     -Djavax.net.ssl.trustStorePassword=[TrustStorePassword]
     -Djavax.net.ssl.trustStoreType=[TrustStoreType]
     ```

6. Choose one:
   - To validate the certificate, set the SSLMode property to
     verify-ca.
   - To validate the certificate and verify the host name in the
     certificate, set the SSLMode property to verify-full.
