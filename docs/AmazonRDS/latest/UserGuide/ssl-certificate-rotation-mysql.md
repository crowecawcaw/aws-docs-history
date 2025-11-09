# Updating applications to connect to MySQL

DB instances using new SSL/TLS certificates

As of January 13, 2023, Amazon RDS has published new Certificate Authority (CA) certificates
for connecting to your RDS DB instances using Secure Socket Layer or Transport Layer
Security (SSL/TLS). Following, you can find information about updating your applications to
use the new certificates.

This topic can help you to determine whether any client applications use SSL/TLS to
connect to your DB instances. If they do, you can further check whether those applications
require certificate verification to connect.

###### Note

Some applications are configured to connect to MySQL DB instances only if they can
successfully verify the certificate on the server. For such applications, you must update your
client application trust stores to include the new CA certificates.

You can specify the following SSL modes: `disabled`,
`preferred`, and `required`. When you use the
`preferred` SSL mode and the CA certificate doesn't exist or
isn't up to date, the connection falls back to not using SSL and connects without encryption.

We recommend avoiding `preferred` mode. In `preferred` mode, if the
connection encounters an invalid certificate, it stops using encryption and proceeds unencrypted.

After you update your CA certificates in the client application trust stores, you can
rotate the certificates on your DB instances. We strongly recommend testing these
procedures in a development or staging environment before implementing them in your
production environments.

For more information about certificate rotation, see
[Rotating your SSL/TLS
certificate](UsingWithRDS.md "UsingWithRDS.md").
For more information about downloading certificates, see [Using SSL/TLS to encrypt a connection to a DB
instance or cluster](UsingWithRDS.md "UsingWithRDS.md"). For information about
using SSL/TLS with MySQL DB instances, see [SSL/TLS support for MySQL DB instances on
Amazon RDS](MySQL.Concepts.md "MySQL.Concepts.md").

###### Topics

- [Determining whether any applications are connecting to your MySQL DB instance using SSL](#ssl-certificate-rotation-mysql.determining-server "#ssl-certificate-rotation-mysql.determining-server")
- [Determining whether a client requires certificate verification to connect](#ssl-certificate-rotation-mysql.determining-client "#ssl-certificate-rotation-mysql.determining-client")
- [Updating your application trust store](#ssl-certificate-rotation-mysql.updating-trust-store "#ssl-certificate-rotation-mysql.updating-trust-store")
- [Example Java code for establishing SSL connections](#ssl-certificate-rotation-mysql.java-example "#ssl-certificate-rotation-mysql.java-example")

## Determining whether any applications are connecting to your MySQL DB instance using SSL

If you are using Amazon RDS for MySQL version 5.7, 8.0, or 8.4 and the Performance Schema
is enabled, run the following query to check if connections are using SSL/TLS. For
information about enabling the Performance Schema, see [Performance Schema quick start](https://dev.mysql.com/doc/refman/8.0/en/performance-schema-quick-start.html "https://dev.mysql.com/doc/refman/8.0/en/performance-schema-quick-start.html") in the MySQL documentation.

```

mysql> SELECT id, user, host, connection_type
       FROM performance_schema.threads pst
       INNER JOIN information_schema.processlist isp
       ON pst.processlist_id = isp.id;

```

In this sample output, you can see both your own session (`admin`) and an application logged in as
`webapp1` are using SSL.

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

The following example with MySQL Connector/J 8.0 shows one way to check an application's JDBC connection properties
to determine whether successful connections require a valid certificate. For more information on all of the JDBC connection
options for MySQL, see [Configuration properties](https://dev.mysql.com/doc/connector-j/en/connector-j-reference-configuration-properties.html "https://dev.mysql.com/doc/connector-j/en/connector-j-reference-configuration-properties.html") in the MySQL documentation.

When using the MySQL Connector/J 8.0, an SSL connection requires verification against the DB server certificate if your connection
properties have `sslMode` set to `VERIFY_CA` or `VERIFY_IDENTITY`, as in the following example.

```

Properties properties = new Properties();
properties.setProperty("sslMode", "VERIFY_IDENTITY");
properties.put("user", DB_USER);
properties.put("password", DB_PASSWORD);

```

###### Note

If you use either the MySQL Java Connector v5.1.38 or later, or the MySQL Java Connector v8.0.9 or later to connect to your databases,
even if you haven't explicitly configured your applications to use SSL/TLS when connecting to your databases, these client drivers
default to using SSL/TLS. In addition, when using SSL/TLS, they perform partial certificate verification and fail to connect if the
database server certificate is expired.

### MySQL

The following examples with the MySQL Client show two ways to check a
script's MySQL connection to determine whether successful connections require a
valid certificate. For more information on all of the connection options with the
MySQL Client, see [Client-side configuration for encrypted connections](https://dev.mysql.com/doc/refman/8.0/en/using-encrypted-connections.html#using-encrypted-connections-client-side-configuration "https://dev.mysql.com/doc/refman/8.0/en/using-encrypted-connections.html#using-encrypted-connections-client-side-configuration") in the MySQL
documentation.

When using the MySQL Client version 5.7 and higher, an SSL connection requires
verification against the server CA certificate if for the `--ssl-mode`
option you specify `VERIFY_CA` or `VERIFY_IDENTITY`, as in the
following example.

```

mysql -h mysql-database.rds.amazonaws.com -uadmin -ppassword --ssl-ca=/tmp/`ssl-cert.pem` --ssl-mode=VERIFY_CA

```

## Updating your application trust store

For information about updating the trust store for MySQL applications, see
[Installing SSL certificates](https://dev.mysql.com/doc/mysql-monitor/8.0/en/mem-ssl-installation.html "https://dev.mysql.com/doc/mysql-monitor/8.0/en/mem-ssl-installation.html") in the MySQL documentation.

For information about downloading the root certificate, see [Using SSL/TLS to encrypt a connection to a DB
instance or cluster](UsingWithRDS.md "UsingWithRDS.md").

For sample scripts that import certificates, see [Sample
script for importing certificates into your trust store](UsingWithRDS.md#UsingWithRDS.SSL-certificate-rotation-sample-script "UsingWithRDS.md#UsingWithRDS.SSL-certificate-rotation-sample-script").

###### Note

When you update the trust store, you can retain older certificates in addition to adding the new certificates.

If you are using the mysql JDBC driver in an application, set the following properties in the application.

```

System.setProperty("javax.net.ssl.trustStore", `certs`);
System.setProperty("javax.net.ssl.trustStorePassword", "`password`");

```

When you start the application, set the following properties.

```

java -Djavax.net.ssl.trustStore=`/path_to_trust_store/MyTruststore.jks` -Djavax.net.ssl.trustStorePassword=`my_trust_store_password` `com.companyName.MyApplication`

```

###### Note

Specify a password other than the prompt shown here as a security best practice.

## Example Java code for establishing SSL connections

The following code example shows how to set up the SSL connection that validates the server certificate using JDBC.

```

public class MySQLSSLTest {

        private static final String DB_USER = "`username`";
        private static final String DB_PASSWORD = "`password`";
        // This trust store has only the prod root ca.
        private static final String TRUST_STORE_FILE_PATH = "`file-path-to-trust-store`";
        private static final String TRUST_STORE_PASS = "`trust-store-password`";

        public static void test(String[] args) throws Exception {
            Class.forName("com.mysql.jdbc.Driver");

            System.setProperty("javax.net.ssl.trustStore", TRUST_STORE_FILE_PATH);
            System.setProperty("javax.net.ssl.trustStorePassword", TRUST_STORE_PASS);

            Properties properties = new Properties();
            properties.setProperty("sslMode", "VERIFY_IDENTITY");
            properties.put("user", DB_USER);
            properties.put("password", DB_PASSWORD);


            Connection connection = null;
            Statement stmt = null;
            ResultSet rs = null;
            try {
                connection = DriverManager.getConnection("jdbc:mysql://`mydatabase.123456789012.us-east-1.rds.amazonaws.com:3306`",properties);
                stmt = connection.createStatement();
                rs=stmt.executeQuery("SELECT 1 from dual");
            } finally {
                if (rs != null) {
                    try {
                        rs.close();
                    } catch (SQLException e) {
                    }
                }
                if (stmt != null) {
                   try {
                        stmt.close();
                    } catch (SQLException e) {
                   }
                }
                if (connection != null) {
                    try {
                        connection.close();
                    } catch (SQLException e) {
                        e.printStackTrace();
                    }
                }
            }
            return;
        }
    }

```

###### Important

After you have determined that your database connections use SSL/TLS and have
updated your application trust store, you can update your database to use the
rds-ca-rsa2048-g1 certificates. For instructions, see step 3 in [Updating
your CA certificate by modifying your DB instance or cluster](UsingWithRDS.md#UsingWithRDS.SSL-certificate-rotation-updating "UsingWithRDS.md#UsingWithRDS.SSL-certificate-rotation-updating").

Specify a password other than the prompt shown here as a security best practice.
