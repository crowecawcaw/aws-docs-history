# Connecting to your MariaDB DB instance

After Amazon RDS provisions your DB instance, you can use any standard MariaDB client
application or utility to connect to the instance. In the connection string, you specify the
Domain Name System (DNS) address from the DB instance endpoint as the host parameter. You
also specify the port number from the DB instance endpoint as the port parameter.

You can connect to an Amazon RDS for MariaDB DB instance by using tools like the MySQL command-line
client. For more information on using the MySQL command-line client, see [mysql command-line
client](http://mariadb.com/kb/en/mariadb/mysql-command-line-client/ "http://mariadb.com/kb/en/mariadb/mysql-command-line-client/") in the MariaDB documentation. One GUI-based application that you can use
to connect is Heidi. For more information, see the [Download HeidiSQL](http://www.heidisql.com/download.php "http://www.heidisql.com/download.php") page.
For information about installing MySQL (including the MySQL command-line client), see [Installing and upgrading
MySQL](https://dev.mysql.com/doc/refman/8.0/en/installing.html "https://dev.mysql.com/doc/refman/8.0/en/installing.html").

Most Linux distributions include the MariaDB client instead of the Oracle MySQL client.
To install the MySQL command-line client on Amazon Linux 2023, run the following command:

```
sudo dnf install mariadb105
```

To install the MySQL command-line client on Amazon Linux 2, run the following command:

```
sudo yum install mariadb
```

To install the MySQL command-line client on most DEB-based Linux distributions, run the following command.

```
apt-get install mariadb-client
```

To check the version of your MySQL command-line client, run the following command.

```
mysql --version
```

To read the MySQL documentation for your current client version, run the following command.

```
man mysql
```

To connect to a DB instance from outside of a virtual private cloud (VPC) based on Amazon VPC,
the DB instance must be publicly accessible. Also, access must be granted using the inbound
rules of the DB instance's security group, and other requirements must be met. For more
information, see [Can't connect to Amazon RDS DB instance](CHAP_Troubleshooting.md#CHAP_Troubleshooting.Connecting "CHAP_Troubleshooting.md#CHAP_Troubleshooting.Connecting").

You can use SSL encryption on connections to a MariaDB DB instance. For information,
see [SSL/TLS support for MariaDB DB instances
on Amazon RDS](MariaDB.Concepts.md "MariaDB.Concepts.md").

To find and connect to a RDS for MariaDB DB instance, see the following topics.

###### Topics

- [Finding the connection information for a MariaDB DB instance](USER_ConnectToMariaDBInstance.md "USER_ConnectToMariaDBInstance.md")
- [Connecting from the MySQL command-line client (unencrypted) for RDS for MariaDB](USER_ConnectToMariaDBInstance.md "USER_ConnectToMariaDBInstance.md")
- [Connecting to RDS for MariaDB with the
  AWS JDBC Driver and AWS Python Driver;](MariaDB.Connecting.md "MariaDB.Connecting.md")
- [Troubleshooting
  connections to your MariaDB DB instance](USER_ConnectToMariaDBInstance.md "USER_ConnectToMariaDBInstance.md")
