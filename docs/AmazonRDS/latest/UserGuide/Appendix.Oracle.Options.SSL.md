

# Oracle Secure Sockets Layer
<a name="Appendix.Oracle.Options.SSL"></a>

To enable SSL encryption for an RDS for Oracle DB instance, add the Oracle SSL option to the option group associated with the DB instance. Amazon RDS uses a second port, as required by Oracle, for SSL connections. This approach allows both clear text and SSL-encrypted communication to occur at the same time between a DB instance and SQL\*Plus. For example, you can use the port with clear text communication to communicate with other resources inside a VPC while using the port with SSL-encrypted communication to communicate with resources outside the VPC.

**Note**  
You can use either SSL or Native Network Encryption (NNE) on the same RDS for Oracle DB instance, but not both. If you use SSL encryption, make sure to turn off any other connection encryption. For more information, see [Oracle native network encryption](Appendix.Oracle.Options.NetworkEncryption.md).

SSL/TLS and NNE are no longer part of Oracle Advanced Security. In RDS for Oracle, you can use SSL encryption with all licensed editions of the following database versions:
+ Oracle Database 26ai (26.0.0.0)
+ Oracle Database 21c (21.0.0.0)
+ Oracle Database 19c (19.0.0.0)

**Note**  
For Oracle Database 26ai, the Oracle SSL option supports only TLS 1.2, and the default cipher suite is `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`. Oracle Database 26ai supports the following cipher suites:  
`TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384` (default)
`TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384`
`TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`
`TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384`

**Topics**
+ [TLS versions for the Oracle SSL option](#Appendix.Oracle.Options.SSL.TLS)
+ [Cipher suites for the Oracle SSL option](#Appendix.Oracle.Options.SSL.CipherSuites)
+ [FIPS support](#Appendix.Oracle.Options.SSL.FIPS)
+ [Certificate compatibility with cipher suites](#Appendix.Oracle.Options.SSL.CertificateCompatibility)
+ [Adding the SSL option](Appendix.Oracle.Options.SSL.OptionGroup.md)
+ [Configuring SQL\*Plus to use SSL with an RDS for Oracle DB instance](Appendix.Oracle.Options.SSL.ClientConfiguration.md)
+ [Connecting to an RDS for Oracle DB instance using SSL](Appendix.Oracle.Options.SSL.Connecting.md)
+ [Setting up an SSL connection over JDBC](Appendix.Oracle.Options.SSL.JDBC.md)
+ [Enforcing a DN match with an SSL connection](Appendix.Oracle.Options.SSL.DNMatch.md)
+ [Troubleshooting SSL connections](Appendix.Oracle.Options.SSL.troubleshooting.md)

## TLS versions for the Oracle SSL option
<a name="Appendix.Oracle.Options.SSL.TLS"></a>

Amazon RDS for Oracle supports Transport Layer Security (TLS) versions 1.0 and 1.2. When you add a new Oracle SSL option, set `SQLNET.SSL_VERSION` explicitly to a valid value. The following table shows the allowed values for this option setting:


| Value | Supported Oracle versions | Description | 
| --- | --- | --- | 
| "1.0" | 19c, 21c | Clients can connect to the DB instance using TLS version 1.0 only. For existing Oracle SSL options, SQLNET.SSL\_VERSION is set to "1.0" automatically. You can change the setting if necessary. | 
| "1.2" | All | Clients can connect to the DB instance using TLS 1.2 only. | 
| "1.2 or 1.0" | 19c, 21c | Clients can connect to the DB instance using either TLS 1.2 or 1.0. | 

## Cipher suites for the Oracle SSL option
<a name="Appendix.Oracle.Options.SSL.CipherSuites"></a>

Amazon RDS for Oracle supports multiple SSL cipher suites. By default, the Oracle SSL option is configured to use the `SSL_RSA_WITH_AES_256_CBC_SHA` cipher suite for Oracle Database 19c and Oracle Database 21c. For Oracle Database 26ai, the default cipher suite is `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`. To specify a different cipher suite to use over SSL connections, use the `SQLNET.CIPHER_SUITE` option setting.

You can specify multiple values for `SQLNET.CIPHER_SUITE`. This technique is useful if you have database links between your DB instances and decide to update your cipher suites.

The following table summarizes SSL support for RDS for Oracle in all editions of Oracle Database 19c, 21c, and 26ai.


| Cipher suite (SQLNET.CIPHER\_SUITE) | TLS version support (SQLNET.SSL\_VERSION) | FIPS support | FedRAMP compliant | Supported Oracle versions | 
| --- | --- | --- | --- | --- | 
| SSL\_RSA\_WITH\_AES\_256\_CBC\_SHA (default for 19c and 21c) | 1.0 and 1.2 | Yes | No | 19c, 21c | 
| SSL\_RSA\_WITH\_AES\_256\_CBC\_SHA256 | 1.2 | Yes | No | 19c, 21c | 
| SSL\_RSA\_WITH\_AES\_256\_GCM\_SHA384 | 1.2 | Yes | No | 19c, 21c | 
| TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384 (default for 26ai) | 1.2 | Yes | Yes | 19c, 21c, 26ai | 
| TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256 | 1.2 | Yes | Yes | 19c, 21c | 
| TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA384 | 1.2 | Yes | Yes | 19c, 21c, 26ai | 
| TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA256 | 1.2 | Yes | Yes | 19c, 21c | 
| TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA | 1.2 | Yes | Yes | 19c, 21c | 
| TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA | 1.2 | Yes | Yes | 19c, 21c | 
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384 | 1.2 | Yes | Yes | 19c, 21c, 26ai | 
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA384 | 1.2 | Yes | Yes | 19c, 21c, 26ai | 

## FIPS support
<a name="Appendix.Oracle.Options.SSL.FIPS"></a>

RDS for Oracle allows you to use the Federal Information Processing Standard (FIPS) standard for 140-2. FIPS 140-2 is a United States government standard that defines cryptographic module security requirements. You turn on the FIPS standard by setting `FIPS.SSLFIPS_140` to `TRUE` for the Oracle SSL option. When FIPS 140-2 is configured for SSL, the cryptographic libraries encrypt data between the client and the RDS for Oracle DB instance.

Clients must use the cipher suite that is FIPS-compliant. When establishing a connection, the client and RDS for Oracle DB instance negotiate which cipher suite to use when transmitting messages back and forth. The table in [Cipher suites for the Oracle SSL option](#Appendix.Oracle.Options.SSL.CipherSuites) shows the FIPS-compliant SSL cipher suites for each TLS version. For more information, see [Oracle database FIPS 140-2 settings](https://docs.oracle.com/en/database/oracle/oracle-database/19/dbseg/oracle-database-fips-140-settings.html) in the Oracle Database documentation.

## Certificate compatibility with cipher suites
<a name="Appendix.Oracle.Options.SSL.CertificateCompatibility"></a>

RDS for Oracle supports both RSA and Elliptic Curve Digital Signature Algorithm (ECDSA) certificates. When you configure SSL for your DB instance, you must ensure that the cipher suites you specify in the `SQLNET.CIPHER_SUITE` option setting are compatible with the certificate type used by your DB instance.

The following table shows the compatibility between certificate types and cipher suites:


| Certificate type | Compatible cipher suites | Incompatible cipher suites | 
| --- | --- | --- | 
| RSA certificates (rds-ca-2019, rds-ca-rsa2048-g1, rds-ca-rsa4096-g1) | SSL\_RSA\_WITH\_AES\_256\_CBC\_SHA<br />SSL\_RSA\_WITH\_AES\_256\_CBC\_SHA256<br />SSL\_RSA\_WITH\_AES\_256\_GCM\_SHA384<br />TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384<br />TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256<br />TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA384<br />TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA256<br />TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA<br />TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA | TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384<br />TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA384 | 
| ECDSA certificates (rds-ca-ecc384-g1) | TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384<br />TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA384 | SSL\_RSA\_WITH\_AES\_256\_CBC\_SHA<br />SSL\_RSA\_WITH\_AES\_256\_CBC\_SHA256<br />SSL\_RSA\_WITH\_AES\_256\_GCM\_SHA384<br />TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384<br />TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256<br />TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA384<br />TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA256<br />TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA<br />TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA | 

When you specify multiple cipher suites in the `SQLNET.CIPHER_SUITE` option setting, make sure to include at least one cipher suite that is compatible with the certificate type used by your DB instance. If you're using an option group with multiple DB instances that have different certificate types, include at least one cipher suite for each certificate type.

If you attempt to associate an option group with an SSL option that contains only cipher suites incompatible with the certificate type of a DB instance, the operation will fail with an error message indicating the incompatibility.