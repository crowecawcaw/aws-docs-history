# Connecting to your MySQL DB instance

Before you can connect to a DB instance running the MySQL database engine, you must create a DB instance.
For information, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").
After Amazon RDS provisions your DB instance, you can use any standard MySQL
client application or utility to connect to the instance. In the connection string, you
specify the DNS address from the DB instance endpoint as the host parameter, and specify the
port number from the DB instance endpoint as the port parameter.

To authenticate to your RDS DB instance, you can use one of the authentication methods for
MySQL and AWS Identity and Access Management (IAM) database authentication:

- To learn how to authenticate to MySQL using one of the authentication methods for MySQL,
  see [Authentication method](https://dev.mysql.com/doc/internals/en/authentication-method.html "https://dev.mysql.com/doc/internals/en/authentication-method.html") in the MySQL documentation.
- To learn how to authenticate to MySQL using IAM database authentication, see
  [IAM database authentication for MariaDB, MySQL, and PostgreSQL](UsingWithRDS.md "UsingWithRDS.md").
  You can connect to a MySQL DB instance by using tools like the MySQL command-line client.
  For more information on using the MySQL command-line client, see [mysql - the MySQL command-line
  client](https://dev.mysql.com/doc/refman/8.0/en/mysql.html "https://dev.mysql.com/doc/refman/8.0/en/mysql.html") in the MySQL documentation. One GUI-based application you can use to
  connect is MySQL Workbench. For more information, see the [Download MySQL Workbench](http://dev.mysql.com/downloads/workbench/ "http://dev.mysql.com/downloads/workbench/") page.
  For information about installing MySQL (including the MySQL command-line client), see [Installing and upgrading
  MySQL](https://dev.mysql.com/doc/refman/8.0/en/installing.html "https://dev.mysql.com/doc/refman/8.0/en/installing.html").

To connect to a DB instance from outside of its Amazon VPC, the DB instance must be publicly accessible, access must be granted
using the inbound rules of the DB instance's security group, and other requirements must be met. For more information,
see [Can't connect to Amazon RDS DB instance](CHAP_Troubleshooting.md#CHAP_Troubleshooting.Connecting "CHAP_Troubleshooting.md#CHAP_Troubleshooting.Connecting").

You can use Secure Sockets Layer (SSL) or Transport Layer Security (TLS) encryption on connections to a MySQL DB instance.
For information, see [SSL/TLS support for MySQL DB instances on
Amazon RDS](MySQL.Concepts.md "MySQL.Concepts.md"). If you are using AWS Identity and Access Management (IAM) database
authentication, make sure to use an SSL/TLS connection. For information, see [IAM database authentication for MariaDB, MySQL, and PostgreSQL](UsingWithRDS.md "UsingWithRDS.md").

You can also connect to a DB instance from a web server. For more information, see [Tutorial: Create a web server and an
Amazon RDS DB instance](TUT_WebAppWithRDS.md "TUT_WebAppWithRDS.md").

###### Note

For information on connecting to a MariaDB DB instance, see [Connecting to your MariaDB DB instance](USER_ConnectToMariaDBInstance.md "USER_ConnectToMariaDBInstance.md").

To find and connect to a RDS for MySQL DB instance, see the following topics.

###### Topics

- [Finding the connection
  information for an RDS for MySQL DB instance](USER_ConnectToInstance.md "USER_ConnectToInstance.md")
- [Installing the MySQL command-line client](mysql-install-cli.md "mysql-install-cli.md")
- [Connecting from the MySQL command-line client (unencrypted)](USER_ConnectToInstance.md "USER_ConnectToInstance.md")
- [Connecting from MySQL Workbench](USER_ConnectToInstance.md "USER_ConnectToInstance.md")
- [Connecting to RDS for MySQL with the
  AWS JDBC Driver, AWS Python Driver, and AWS ODBC Driver for MySQL](MySQL.Connecting.md "MySQL.Connecting.md")
- [Troubleshooting
  connections to your MySQL DB instance](USER_ConnectToInstance.md "USER_ConnectToInstance.md")
