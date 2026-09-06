

# Encrypted connections for Aurora MySQL
<a name="chap-sql-server-aurora-mysql.security.encryptedconnections"></a>

This topic provides reference information about encrypted connections in Microsoft SQL Server and MySQL, with a focus on how these concepts apply to Amazon Aurora MySQL migration. You’ll learn about the protocols and technologies used for secure data transmission in both database systems.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-mysql-migration-playbook/images/pb-compatibility-3.png)  |  ![No automation](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-mysql-migration-playbook/images/pb-automation-0.png)  | N/A | N/A | 

## SQL Server Usage
<a name="chap-sql-server-aurora-mysql.security.encryptedconnections.sqlserver"></a>

In SQL Server, you can encrypt data across communication channels. Encrypted connections are enabled for an instance of the SQL Server Database Engine and use SQL Server Configuration Manager to specify a certificate.

Make sure that the server has a certificate provisioned. To provision the certificate on the server, make sure to import it into Windows. The client machine must be set up to trust the certificate’s root authority.

**Note**  
Starting with SQL Server 2016 (13.x), Secure Sockets Layer (SSL) has been discontinued. Use Transport Layer Security (TLS) instead.

## MySQL Usage
<a name="chap-sql-server-aurora-mysql.security.encryptedconnections.mysql"></a>

MySQL supports encrypted connections between clients and the server using the TLS (Transport Layer Security) protocol. TLS is sometimes referred to as SSL (Secure Sockets Layer) but MySQL doesn’t actually use the SSL protocol for encrypted connections because its encryption is weak.

OpenSSL 1.1.1 supports the TLS v1.3 protocol for encrypted connections.

**Note**  
 Amazon Relational Database Service (Amazon RDS) for MySQL 8.0.16 and higher supports TLS v1.3 as well if both the server and client are compiled using OpenSSL 1.1.1 or higher. For more information, see [Encrypted Connection TLS Protocols and Ciphers](https://dev.mysql.com/doc/refman/5.7/en/encrypted-connection-protocols-ciphers.html) in the *MySQL documentation*.