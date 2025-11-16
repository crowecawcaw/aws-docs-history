# Oracle Secure Sockets Layer

To enable SSL encryption for an RDS for Oracle DB instance, add the Oracle SSL option to the
option group associated with the DB instance. Amazon RDS uses a second port, as required by Oracle, for
SSL connections. This approach allows both clear text and SSL-encrypted communication to
occur at the same time between a DB instance and SQL\*Plus. For example, you can use the port with
clear text communication to communicate with other resources inside a VPC while using the
port with SSL-encrypted communication to communicate with resources outside the VPC.

###### Note

You can use either SSL or Native Network Encryption (NNE) on the same RDS for Oracle
DB instance, but not both. If you use SSL encryption, make sure to turn off any other
connection encryption. For more information, see [Oracle native network encryption](Appendix.Oracle.Options.md "Appendix.Oracle.Options.md").

SSL/TLS and NNE are no longer part of Oracle Advanced Security. In RDS for Oracle, you can
use SSL encryption with all licensed editions of the following database versions:

- Oracle Database 21c (21.0.0)
- Oracle Database 19c (19.0.0)

###### Topics

- [TLS versions for the Oracle SSL option](#Appendix.Oracle.Options.SSL.TLS "#Appendix.Oracle.Options.SSL.TLS")
- [Cipher suites for the Oracle SSL option](#Appendix.Oracle.Options.SSL.CipherSuites "#Appendix.Oracle.Options.SSL.CipherSuites")
- [FIPS support](#Appendix.Oracle.Options.SSL.FIPS "#Appendix.Oracle.Options.SSL.FIPS")
- [Certificate compatibility with cipher suites](#Appendix.Oracle.Options.SSL.CertificateCompatibility "#Appendix.Oracle.Options.SSL.CertificateCompatibility")
- [Adding the SSL option](Appendix.Oracle.Options.SSL.md "Appendix.Oracle.Options.SSL.md")
- [Configuring SQL\*Plus to
  use SSL with an RDS for Oracle DB instance](Appendix.Oracle.Options.SSL.md "Appendix.Oracle.Options.SSL.md")
- [Connecting to an RDS for Oracle DB instance using SSL](Appendix.Oracle.Options.SSL.md "Appendix.Oracle.Options.SSL.md")
- [Setting up an SSL connection over JDBC](Appendix.Oracle.Options.SSL.md "Appendix.Oracle.Options.SSL.md")
- [Enforcing a DN match with an SSL connection](Appendix.Oracle.Options.SSL.md "Appendix.Oracle.Options.SSL.md")
- [Troubleshooting SSL
  connections](Appendix.Oracle.Options.SSL.md "Appendix.Oracle.Options.SSL.md")

## TLS versions for the Oracle SSL option

Amazon RDS for Oracle supports Transport Layer Security (TLS) versions 1.0 and 1.2.
When you add a new Oracle SSL option, set `SQLNET.SSL_VERSION` explicitly to
a valid value. The following values are allowed for this option setting:

- `"1.0"` – Clients can connect to the DB instance using TLS version 1.0
  only. For existing Oracle SSL options, `SQLNET.SSL_VERSION` is set to
  `"1.0"` automatically. You can change the setting if
  necessary.
- `"1.2"` – Clients can connect to the DB instance using TLS 1.2 only.
- `"1.2 or 1.0"` – Clients can connect to the DB instance using either TLS 1.2 or 1.0.

## Cipher suites for the Oracle SSL option

Amazon RDS for Oracle supports multiple SSL cipher suites. By default, the Oracle SSL
option is configured to use the `SSL_RSA_WITH_AES_256_CBC_SHA` cipher suite.
To specify a different cipher suite to use over SSL connections, use the
`SQLNET.CIPHER_SUITE` option setting.

You can specify multiple values for `SQLNET.CIPHER_SUITE`. This technique
is useful if you have database links between your DB instances and decide to update your
cipher suites.

The following table summarizes SSL support for RDS for Oracle in all editions of Oracle
Database 19c and 21c.

| Cipher suite (SQLNET.CIPHER_SUITE)      | TLS version support (SQLNET.SSL_VERSION) | FIPS support | FedRAMP compliant |
| --------------------------------------- | ---------------------------------------- | ------------ | ----------------- |
| SSL_RSA_WITH_AES_256_CBC_SHA (default)  | 1.0 and 1.2                              | Yes          | No                |
| SSL_RSA_WITH_AES_256_CBC_SHA256         | 1.2                                      | Yes          | No                |
| SSL_RSA_WITH_AES_256_GCM_SHA384         | 1.2                                      | Yes          | No                |
| TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384   | 1.2                                      | Yes          | Yes               |
| TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256   | 1.2                                      | Yes          | Yes               |
| TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384   | 1.2                                      | Yes          | Yes               |
| TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256   | 1.2                                      | Yes          | Yes               |
| TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA      | 1.2                                      | Yes          | Yes               |
| TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA      | 1.2                                      | Yes          | Yes               |
| TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 | 1.2                                      | Yes          | Yes               |
| TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384 | 1.2                                      | Yes          | Yes               |

## FIPS support

RDS for Oracle allows you to use the Federal Information Processing Standard (FIPS)
standard for 140-2. FIPS 140-2 is a United States government standard that defines
cryptographic module security requirements. You turn on the FIPS standard by setting
`FIPS.SSLFIPS_140` to `TRUE` for the Oracle SSL option. When
FIPS 140-2 is configured for SSL, the cryptographic libraries encrypt data between the
client and the RDS for Oracle DB instance.

Clients must use the cipher suite that is FIPS-compliant. When establishing a
connection, the client and RDS for Oracle DB instance negotiate which cipher suite to use when
transmitting messages back and forth. The table in [Cipher suites for the Oracle SSL option](#Appendix.Oracle.Options.SSL.CipherSuites "#Appendix.Oracle.Options.SSL.CipherSuites") shows the FIPS-compliant
SSL cipher suites for each TLS version. For more information, see [Oracle database FIPS 140-2 settings](https://docs.oracle.com/en/database/oracle/oracle-database/12.2/dbseg/oracle-database-fips-140-settings.html#GUID-DDBEB3F9-B216-44BB-8C18-43B5E468CBBB "https://docs.oracle.com/en/database/oracle/oracle-database/12.2/dbseg/oracle-database-fips-140-settings.html#GUID-DDBEB3F9-B216-44BB-8C18-43B5E468CBBB") in the Oracle Database
documentation.

## Certificate compatibility with cipher suites

RDS for Oracle supports both RSA and Elliptic Curve Digital Signature Algorithm (ECDSA)
certificates. When you configure SSL for your DB instance, you must ensure that the cipher
suites you specify in the `SQLNET.CIPHER_SUITE` option setting are compatible
with the certificate type used by your DB instance.

The following table shows the compatibility between certificate types and cipher suites:

| Certificate type                                                     | Compatible cipher suites                                                                                                                                                                                                                                                                                                                           | Incompatible cipher suites                                                                                                                                                                                                                                                                                                                         |
| -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RSA certificates (rds-ca-2019, rds-ca-rsa2048-g1, rds-ca-rsa4096-g1) | SSL_RSA_WITH_AES_256_CBC_SHA<br>SSL_RSA_WITH_AES_256_CBC_SHA256<br>SSL_RSA_WITH_AES_256_GCM_SHA384<br>TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384<br>TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256<br>TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384<br>TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256<br>TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA<br>TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA | TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384<br>TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384                                                                                                                                                                                                                                                                 |
| ECDSA certificates (rds-ca-ecc384-g1)                                | TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384<br>TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384                                                                                                                                                                                                                                                                 | SSL_RSA_WITH_AES_256_CBC_SHA<br>SSL_RSA_WITH_AES_256_CBC_SHA256<br>SSL_RSA_WITH_AES_256_GCM_SHA384<br>TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384<br>TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256<br>TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384<br>TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256<br>TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA<br>TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA |

When you specify multiple cipher suites in the `SQLNET.CIPHER_SUITE` option setting, make sure to include at least one cipher suite that is compatible with the certificate type used by your DB instance. If you're using an option group with multiple DB instances that have different certificate types, include at least one cipher suite for each certificate type.

If you attempt to associate an option group with an SSL option that contains only cipher suites incompatible with the certificate type of a DB instance, the operation will fail with an error message indicating the incompatibility.
