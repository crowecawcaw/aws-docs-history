# Encrypted connections

With AWS DMS, you can secure data transmission between the replication instance and the source or target database by using encrypted connections. Encrypted connections provide a private encrypted tunnel for data transfer, protecting sensitive information from unauthorized access or interception.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences |
| -------------------------------- | ---------------------------------- | ------------------------- | --------------- |
| Three star feature compatibility | N/A                                | N/A                       | N/A             |

## Oracle usage

Oracle Database supports encrypting incoming data out of the box using native Oracle Net Services. You can encode data that is sent to and from the server using Advanced Encryption Standard (AES) algorithm, ARIA(Academia, Research Institute, and Agency) algorithm, GOsudarstvennyy STandart (GOST) algorithm, Korea Information Security Agency SEED algorithm and Triple-DES encryption (3DES).

Algorithms can be specified in the `sqlnet.ora` file for the clients and servers.

For more information, see [Configuring Oracle Database Network Encryption and Data Integrity](https://docs.oracle.com/database/121/DBSEG/asoconfg.htm#DBSEG020 "https://docs.oracle.com/database/121/DBSEG/asoconfg.htm#DBSEG020") in the _Oracle documentation_.

SSL/TLS connections to the Oracle database are supported starting with Oracle 12c in the standard edition.

For more information, see [SSL Connection to Oracle DB using JDBC, TLSv1.2, JKS or Oracle Wallets (12.2 and lower)](https://blogs.oracle.com/developers/post/ssl-connection-to-oracle-db-using-jdbc-tlsv12-jks-or-oracle-wallets-122-and-lower "https://blogs.oracle.com/developers/post/ssl-connection-to-oracle-db-using-jdbc-tlsv12-jks-or-oracle-wallets-122-and-lower") in the _Oracle Developers Blog_.

## MySQL usage

MySQL supports encrypted connections between clients and the server using the TLS (Transport Layer Security) protocol. TLS is sometimes referred to as SSL (Secure Sockets Layer) but MySQL does not actually use the SSL protocol for encrypted connections because its encryption is weak.

OpenSSL 1.1.1 supports the TLS v1.3 protocol for encrypted connections.

###### Note

Amazon Relational Database Service (Amazon RDS) for MySQL version 8.0.16 and higher supports TLS v1.3 as well if both the server and client are compiled using OpenSSL 1.1.1 or higher. For more information, see [Encrypted Connection TLS Protocols and Ciphers](https://dev.mysql.com/doc/refman/5.7/en/encrypted-connection-protocols-ciphers.html "https://dev.mysql.com/doc/refman/5.7/en/encrypted-connection-protocols-ciphers.html") in the _MySQL documentation_.
