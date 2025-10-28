# Considerations with Sqoop on Amazon EMR

Consider the following items when you run Sqoop on Amazon EMR.

## Using Sqoop with HCatalog integration

Sqoop on Amazon EMR supports [Sqoop-HCatalog integration](https://sqoop.apache.org/docs/1.4.4/SqoopUserGuide.html#_sqoop_hcatalog_integration "https://sqoop.apache.org/docs/1.4.4/SqoopUserGuide.html#_sqoop_hcatalog_integration").
When you use Sqoop to write output to an HCatalog table in Amazon S3, disable Amazon EMR direct write by setting the `mapred.output.direct.NativeS3FileSystem` and `mapred.output.direct.EmrFileSystem` properties to `false`. For more information, see [Using HCatalog](emr-hcatalog-using.md "emr-hcatalog-using.md"). You can use the
Hadoop `-D mapred.output.direct.NativeS3FileSystem=false` and `-D
 mapred.output.direct.EmrFileSystem=false` commands. If you don't disable
direct write, no error occurs, but the table is created in Amazon S3 and no data is
written.

## Sqoop JDBC and database

support

By default, Sqoop has a MariaDB and PostgreSQL driver installed. The PostgreSQL
driver installed for Sqoop only works for PostgreSQL 8.4. To install an alternate
set of JDBC connectors for Sqoop, connect to the cluster master node and install
them in `/usr/lib/sqoop/lib`. The following are links for various
JDBC connectors:

- MariaDB: [About
  MariaDB Connector/J](https://mariadb.com/kb/en/mariadb/about-mariadb-connector-j/ "https://mariadb.com/kb/en/mariadb/about-mariadb-connector-j/").
- PostgreSQL: [PostgreSQL JDBC
  driver](https://jdbc.postgresql.org/ "https://jdbc.postgresql.org/").
- SQLServer: [Download Microsoft JDBC driver for SQL Server](https://docs.microsoft.com/en-us/sql/connect/jdbc/download-microsoft-jdbc-driver-for-sql-server "https://docs.microsoft.com/en-us/sql/connect/jdbc/download-microsoft-jdbc-driver-for-sql-server").
- MySQL: [Download
  Connector/J](https://dev.mysql.com/downloads/connector/j/ "https://dev.mysql.com/downloads/connector/j/")
- Oracle: [Get Oracle JDBC drivers and UCP from the Oracle Maven
  repository](http://www.oracle.com/technetwork/database/features/jdbc/index-091264.html "http://www.oracle.com/technetwork/database/features/jdbc/index-091264.html")

The supported databases for Sqoop are listed at the following url,
http://sqoop.apache.org/docs/`version`/SqoopUserGuide.html#\_supported\_databases,
where `version` is the version of Sqoop you are using, for
example 1.4.6. If the JDBC connect string does not match those in this list, you
must specify a driver.

For example, you can export to an Amazon Redshift database table with the following command
(for JDBC 4.1):

```
sqoop export --connect jdbc:redshift://$`MYREDSHIFTHOST`:5439/`mydb` --table `mysqoopexport` --export-dir s3://`amzn-s3-demo-bucket/myinputfiles/` --driver com.amazon.redshift.jdbc41.Driver --username `master` --password `Mymasterpass1`
```

You can use both the MariaDB and MySQL connection strings but if you specify the
MariaDB connection string, you need to specify the driver:

```
sqoop export --connect jdbc:mariadb://$`HOSTNAME`:3306/`mydb` --table `mysqoopexport` --export-dir s3://`amzn-s3-demo-bucket/myinputfiles/` --driver org.mariadb.jdbc.Driver --username `master` --password `Mymasterpass1`
```

If you are using Secure Socket Layer encryption to access your database, you need
to use a JDBC URI like in the following Sqoop export example:

```
sqoop export --connect jdbc:mariadb://$`HOSTNAME`:3306/`mydb`?verifyServerCertificate=false&useSSL=true&requireSSL=true --table `mysqoopexport` --export-dir s3://`amzn-s3-demo-bucket/myinputfiles/` --driver org.mariadb.jdbc.Driver --username `master` --password `Mymasterpass1`
```

For more information about SSL encryption in RDS, see [Using SSL to encrypt a connection to a
DB instance](../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md "../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md") in the Amazon RDS User Guide.

For more information, see the [Apache
Sqoop](http://sqoop.apache.org "http://sqoop.apache.org") documentation.

## Securing your password

There are several methods that you might choose from to securely pass your
password:

Java KeyStore
The preferred method encrypts the password with a Java KeyStore (JKS),
eliminating the need to store the password in a readable format.

1. Create a password alias. On prompt, enter the password that
   you use to access the database.

```
hadoop credential create mydb.password.alias -provider jceks://hdfs/user/root/mysql.password.jceks
```

2. Use the password alias to launch the Sqoop job:

```
sqoop export -Dhadoop.security.credential.provider.path=jceks://hdfs/user/root/mysql.password.jceks --connect jdbc:mariadb://$HOSTNAME:3306/mydb --table mysqoopexport --export-dir s3://amzn-s3-demo-bucket/myinputfiles/ --driver org.mariadb.jdbc.Driver --username master --password-alias mydb.password.alias
```

--password-file
You can use the `--password-file` command to pass the
password through a file as shown in the following example:

1. Create a new file that contains the password:

```
echo -n 'Mymasterpass1' > /home/hadoop/mysql-pass.password
```

2. Use the file to launch the Sqoop job:

```
sqoop export --connect jdbc:mariadb://$HOSTNAME:3306/mydb --table mysqoopexport --export-dir s3://amzn-s3-demo-bucket/myinputfiles/ --driver org.mariadb.jdbc.Driver --username master --password-file /home/hadoop/mysql-pass.password
```

-P
You can use the `-P` command to enter the password through
a prompt as shown in the following example:

```
sqoop export --connect jdbc:mariadb://$HOSTNAME:3306/mydb --table mysqoopexport --export-dir s3://amzn-s3-demo-bucket/myinputfiles/ --driver org.mariadb.jdbc.Driver --username master -P

```
