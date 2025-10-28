# Connecting to your MySQL DB instance on

Amazon RDS with SSL/TLS from the MySQL command-line client (encrypted)

The `mysql` client program parameters are slightly different depending on
which version of MySQL or MariaDB you are using.

To find out which version you have, run the `mysql` command with the
`--version` option. In the following example, the output shows that the
client program is from MariaDB.

```
$ mysql --version
mysql  Ver 15.1 Distrib 10.5.15-MariaDB, for osx10.15 (x86_64) using readline 5.1
```

Most Linux distributions, such as Amazon Linux, CentOS, SUSE, and Debian have replaced
MySQL with MariaDB, and the `mysql` version in them is from MariaDB.

To connect to your DB instance using SSL/TLS, follow these steps:

###### To connect to a DB instance with SSL/TLS using the MySQL command-line

client

1. Download a root certificate that works for all AWS Regions.

For information about downloading certificates, see [Using SSL/TLS to encrypt a connection to a DB
instance or cluster](UsingWithRDS.md "UsingWithRDS.md"). 2. Use a MySQL command-line client to connect to a DB instance with SSL/TLS
encryption. For the `-h` parameter, substitute the DNS name
(endpoint) for your DB instance. For the `--ssl-ca` parameter,
substitute the SSL/TLS certificate file name. For the `-P` parameter,
substitute the port for your DB instance. For the `-u` parameter,
substitute the user name of a valid database user, such as the master user.
Enter the master user password when prompted.

The following example shows how to launch the client using the
`--ssl-ca` parameter using the MySQL 5.7 client or later:

```
mysql -h `mysql–instance1.123456789012.us-east-1.rds.amazonaws.com` --ssl-ca=`global-bundle.pem` --ssl-mode=REQUIRED -P 3306 -u `myadmin` -p
```

To require that the SSL/TLS connection verifies the DB instance endpoint
against the endpoint in the SSL/TLS certificate, enter the following
command:

```
mysql -h `mysql–instance1.123456789012.us-east-1.rds.amazonaws.com` --ssl-ca=`global-bundle.pem` --ssl-mode=VERIFY_IDENTITY -P 3306 -u `myadmin` -p
```

The following example shows how to launch the client using the
`--ssl-ca` parameter using the MariaDB client:

```
mysql -h `mysql–instance1.123456789012.us-east-1.rds.amazonaws.com` --ssl-ca=`global-bundle.pem` --ssl -P 3306 -u `myadmin` -p
```

3. Enter the master user password when prompted.
   You will see output similar to the following.

```
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9738
Server version: 8.0.28 Source distribution

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

mysql>
```
