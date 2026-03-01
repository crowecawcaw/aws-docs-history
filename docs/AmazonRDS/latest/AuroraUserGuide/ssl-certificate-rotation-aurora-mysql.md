# Updating applications to connect to Aurora MySQL DB clusters using new TLS certificates

As of January 13, 2023, Amazon RDS has published new Certificate Authority (CA) certificates
for connecting to your Aurora DB clusters using Transport Layer Security (TLS). Following,
you can find information about updating your applications to use the new
certificates.

This topic can help you to determine whether any client applications use TLS to connect to
your DB clusters. If they do, you can further check whether those applications require
certificate verification to connect.

###### Note

Some applications are configured to connect to Aurora MySQL DB clusters only if they can
successfully verify the certificate on the server.

For such applications, you must update your client application trust stores
to include the new CA certificates.

After you update your CA certificates in the client application trust stores, you can
rotate the certificates on your DB clusters. We strongly recommend testing these
procedures in a development or staging environment before implementing them in your
production environments.

For more information about certificate rotation, see [Rotating your SSL/TLS certificate](UsingWithRDS.md "UsingWithRDS.md"). For more information about
downloading certificates, see [Using SSL/TLS to encrypt a connection to a DB cluster](UsingWithRDS.md "UsingWithRDS.md"). For information about using TLS with Aurora MySQL DB
clusters, see [TLS connections to Aurora MySQL DB clusters](AuroraMySQL.md#AuroraMySQL.Security.SSL "AuroraMySQL.md#AuroraMySQL.Security.SSL").

###### Topics

- [Determining whether any applications are connecting to your Aurora MySQL DB cluster using TLS](#ssl-certificate-rotation-aurora-mysql.determining-server "#ssl-certificate-rotation-aurora-mysql.determining-server")
- [Determining whether a client requires certificate verification to connect](#ssl-certificate-rotation-aurora-mysql.determining-client "#ssl-certificate-rotation-aurora-mysql.determining-client")
- [Updating your application trust store](#ssl-certificate-rotation-aurora-mysql.updating-trust-store "#ssl-certificate-rotation-aurora-mysql.updating-trust-store")
- [Example Java code for establishing TLS connections](#ssl-certificate-rotation-aurora-mysql.java-example "#ssl-certificate-rotation-aurora-mysql.java-example")

## Determining whether any applications are connecting to your Aurora MySQL DB cluster using TLS

If you are using Aurora MySQL version 2 (compatible with MySQL 5.7) and the Performance
Schema is enabled, run the following query to check if connections are using TLS. For
information about enabling the Performance Schema, see [Performance Schema quick start](https://dev.mysql.com/doc/refman/8.0/en/performance-schema-quick-start.html "https://dev.mysql.com/doc/refman/8.0/en/performance-schema-quick-start.html") in the MySQL documentation.

```
mysql> SELECT id, user, host, connection_type
       FROM performance_schema.threads pst
       INNER JOIN information_schema.processlist isp
       ON pst.processlist_id = isp.id;

```

In this sample output, you can see both your own session (`admin`) and an
application logged in as `webapp1` are using TLS.

```
+----+-----------------+------------------+-----------------+
| id | user            | host             | connection_type |
+----+-----------------+------------------+-----------------+
|  8 | admin           | 10.0.4.249:42590 | SSL/TLS         |
|  4 | event_scheduler | localhost        | NULL            |
| 10 | webapp1         | 159.28.1.1:42189 | **SSL/TLS**         |
+----+-----------------+------------------+-----------------+
3 rows in set (0.00 sec)
```

## Determining whether a client requires certificate verification to connect

You can check whether JDBC clients and MySQL clients require certificate verification to connect.

### JDBC

The following example with MySQL Connector/J 8.0 shows one way to check an
application's JDBC connection properties to determine whether successful
connections require a valid certificate. For more information on all of the JDBC
connection options for MySQL, see [Configuration properties](https://dev.mysql.com/doc/connector-j/en/connector-j-reference-configuration-properties.html "https://dev.mysql.com/doc/connector-j/en/connector-j-reference-configuration-properties.html") in the MySQL documentation.

When using the MySQL Connector/J 8.0, an TLS connection requires verification
against the server CA certificate if your connection properties have
`sslMode` set to `VERIFY_CA` or
`VERIFY_IDENTITY`, as in the following example.

```
Properties properties = new Properties();
properties.setProperty("sslMode", "VERIFY_IDENTITY");
properties.put("user", DB_USER);
properties.put("password", DB_PASSWORD);

```

###### Note

If you use either the MySQL Java Connector v5.1.38 or later, or the MySQL Java
Connector v8.0.9 or later to connect to your databases, even if you haven't
explicitly configured your applications to use TLS when connecting to your
databases, these client drivers default to using TLS. In addition, when using
TLS, they perform partial certificate verification and fail to connect if the
database server certificate is expired.

### MySQL

The following examples with the MySQL Client show two ways to check a
script's MySQL connection to determine whether successful connections require a
valid certificate. For more information on all of the connection options with the
MySQL Client, see [Client-side configuration for encrypted connections](https://dev.mysql.com/doc/refman/8.0/en/using-encrypted-connections.html#using-encrypted-connections-client-side-configuration "https://dev.mysql.com/doc/refman/8.0/en/using-encrypted-connections.html#using-encrypted-connections-client-side-configuration") in the MySQL
documentation.

When using the MySQL 5.7 or MySQL 8.0 Client, an TLS connection requires
verification against the server CA certificate if for the `--ssl-mode`
option you specify `VERIFY_CA` or `VERIFY_IDENTITY`, as in the
following example.

```
mysql -h mysql-database.rds.amazonaws.com -uadmin -ppassword --ssl-ca=/tmp/`ssl-cert.pem` --ssl-mode=VERIFY_CA
```

When using the MySQL 5.6 Client, an SSL connection requires verification against
the server CA certificate if you specify the `--ssl-verify-server-cert`
option, as in the following example.

```
mysql -h mysql-database.rds.amazonaws.com -uadmin -ppassword --ssl-ca=/tmp/`ssl-cert.pem` --ssl-verify-server-cert
```

## Updating your application trust store

For information about updating the trust store for MySQL applications, see
[Installing SSL certificates](https://dev.mysql.com/doc/mysql-monitor/8.0/en/mem-ssl-installation.html "https://dev.mysql.com/doc/mysql-monitor/8.0/en/mem-ssl-installation.html") in the MySQL documentation.

###### Note

When you update the trust store, you can retain older certificates in addition to adding the new certificates.

### Updating your application trust store for JDBC

You can update the trust store for applications that use JDBC for TLS
connections.

For information about downloading the root certificate, see [Using SSL/TLS to encrypt a connection to a DB cluster](UsingWithRDS.md "UsingWithRDS.md").

For sample scripts that import certificates, see [Sample script for importing certificates into your trust store](UsingWithRDS.md#UsingWithRDS.SSL-certificate-rotation-sample-script "UsingWithRDS.md#UsingWithRDS.SSL-certificate-rotation-sample-script").

If you are using the mysql JDBC driver in an application, set the following properties in the application.

```
System.setProperty("javax.net.ssl.trustStore", `certs`);
System.setProperty("javax.net.ssl.trustStorePassword", "`password`");
```

###### Note

Specify a password other than the prompt shown here as a security best practice.

When you start the application, set the following properties.

```
java -Djavax.net.ssl.trustStore=`/path_to_truststore/MyTruststore.jks` -Djavax.net.ssl.trustStorePassword=`my_truststore_password` `com.companyName.MyApplication`
```

## Example Java code for establishing TLS connections

The following code example shows how to set up the SSL connection that validates the server certificate using JDBC.

```
public class MySQLSSLTest {

        private static final String DB_USER = "`user name`";
        private static final String DB_PASSWORD = "`password`";
        // This key store has only the prod root ca.
        private static final String KEY_STORE_FILE_PATH = "`file-path-to-keystore`";
        private static final String KEY_STORE_PASS = "`keystore-password`";

    public static void test(String[] args) throws Exception {
        Class.forName("com.mysql.jdbc.Driver");


        System.setProperty("javax.net.ssl.trustStore", KEY_STORE_FILE_PATH);
        System.setProperty("javax.net.ssl.trustStorePassword", KEY_STORE_PASS);

        Properties properties = new Properties();
        properties.setProperty("sslMode", "VERIFY_IDENTITY");
        properties.put("user", DB_USER);
        properties.put("password", DB_PASSWORD);

        Connection connection = DriverManager.getConnection("jdbc:mysql://jagdeeps-ssl-test.cni62e2e7kwh.us-east-1.rds.amazonaws.com:3306",properties);
        Statement stmt=connection.createStatement();

        ResultSet rs=stmt.executeQuery("SELECT 1 from dual");

        return;
    }
}
```

###### Important

After you have determined that your database connections use TLS and have
updated your application trust store, you can update your database to use the
rds-ca-rsa2048-g1 certificates. For instructions, see step 3 in [Updating your CA certificate by modifying your DB instance](UsingWithRDS.md#UsingWithRDS.SSL-certificate-rotation-updating "UsingWithRDS.md#UsingWithRDS.SSL-certificate-rotation-updating") .
