# Connecting to RDS for MySQL with the

AWS JDBC Driver, AWS Python Driver, and AWS ODBC Driver for MySQL

Connect to RDS for MySQL DB instances with the AWS JDBC Driver, the AWS Python Driver, and the AWS ODBC Driver for MySQL. For more information, see the following topics.

###### Topics

- [Connecting to RDS for MySQL with the
  Amazon Web Services (AWS) JDBC Driver](#MySQL.Connecting.JDBCDriver "#MySQL.Connecting.JDBCDriver")
- [Connecting to RDS for MySQL with the
  Amazon Web Services (AWS) Python Driver](#MySQL.Connecting.PythonDriver "#MySQL.Connecting.PythonDriver")
- [Connecting to RDS for MySQL with
  the Amazon Web Services (AWS) ODBC Driver for MySQL](#USER_ConnectToInstance.ODBCDriverMySQL "#USER_ConnectToInstance.ODBCDriverMySQL")

## Connecting to RDS for MySQL with the

Amazon Web Services (AWS) JDBC Driver

The Amazon Web Services (AWS) JDBC Driver is designed as an advanced JDBC wrapper. This wrapper is
complementary to and extends the functionality of an existing JDBC driver. The driver is
drop-in compatible with the community MySQL Connector/J driver and the community MariaDB
Connector/J driver.

To install the AWS JDBC Driver, append the AWS JDBC Driver .jar file (located in the
application `CLASSPATH`), and keep references to the respective community
driver. Update the respective connection URL prefix as follows:

- `jdbc:mysql://` to `jdbc:aws-wrapper:mysql://`
- `jdbc:mariadb://` to
  `jdbc:aws-wrapper:mariadb://`

For more information about the AWS JDBC Driver and complete instructions for using it,
see the [Amazon Web Services (AWS) JDBC Driver GitHub repository](https://github.com/awslabs/aws-advanced-jdbc-wrapper "https://github.com/awslabs/aws-advanced-jdbc-wrapper").

## Connecting to RDS for MySQL with the

Amazon Web Services (AWS) Python Driver

The Amazon Web Services (AWS) Python Driver is designed as an advanced Python wrapper. This wrapper is
complementary to and extends the functionality of the open-source Psycopg driver. The
AWS Python Driver supports Python versions 3.8 and higher. You can install the
`aws-advanced-python-wrapper` package using the `pip` command,
along with the `psycopg` open-source packages.

For more information about the AWS Python Driver and complete instructions for using it,
see the [Amazon Web Services (AWS) Python Driver GitHub repository](https://github.com/awslabs/aws-advanced-python-wrapper "https://github.com/awslabs/aws-advanced-python-wrapper").

## Connecting to RDS for MySQL with

the Amazon Web Services (AWS) ODBC Driver for MySQL

The AWS ODBC Driver for MySQL is a client driver designed for the high availability of RDS for MySQL. The driver can exist
alongside the MySQL Connector/ODBC driver and is compatible with the same workflows.

For more information about the AWS ODBC Driver for MySQL and complete instructions for
installing and using it, see the [Amazon Web Services (AWS) ODBC Driver for MySQL](https://github.com/aws/aws-mysql-odbc "https://github.com/aws/aws-mysql-odbc") GitHub repository.
