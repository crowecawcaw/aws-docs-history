# Connecting to RDS for MariaDB with the AWS JDBC Driver and AWS Python Driver;

Connect to RDS for MariaDB DB instances with the AWS JDBC Driver and the AWS Python Driver. For more information, see the following topics.

###### Topics

- [Connecting to RDS for MariaDB with the Amazon Web Services (AWS) JDBC Driver](#MariaDB.Connecting.JDBCDriver "#MariaDB.Connecting.JDBCDriver")
- [Connecting to RDS for MariaDB with the Amazon Web Services (AWS) Python Driver](#MariaDB.Connecting.PythonDriver "#MariaDB.Connecting.PythonDriver")

## Connecting to RDS for MariaDB with the Amazon Web Services (AWS) JDBC Driver

The Amazon Web Services (AWS) JDBC Driver is designed as an advanced JDBC wrapper. This wrapper is
complementary to and extends the functionality of an existing JDBC driver. The driver is
drop-in compatible with the community MySQL Connector/J driver and the community MariaDB
Connector/J driver.

To install the AWS JDBC Driver, append the AWS JDBC Driver .jar file (located in the
application `CLASSPATH`), and keep references to the respective community
driver. Update the respective connection URL prefix as follows:

- `jdbc:mysql://` to `jdbc:aws-wrapper:mysql://`
- `jdbc:mariadb://` to `jdbc:aws-wrapper:mariadb://`

For more information about the AWS JDBC Driver and complete instructions for using it, see the
[Amazon Web Services (AWS) JDBC Driver GitHub repository](https://github.com/awslabs/aws-advanced-jdbc-wrapper "https://github.com/awslabs/aws-advanced-jdbc-wrapper").

## Connecting to RDS for MariaDB with the Amazon Web Services (AWS) Python Driver

The Amazon Web Services (AWS) Python Driver is designed as an advanced Python wrapper. This wrapper is
complementary to and extends the functionality of the open-source Psycopg driver. The
AWS Python Driver supports Python versions 3.8 and higher. You can install the
`aws-advanced-python-wrapper` package using the `pip` command,
along with the `psycopg` open-source packages.

For more information about the AWS Python Driver and complete instructions for using it, see the
[Amazon Web Services (AWS) Python Driver GitHub repository](https://github.com/awslabs/aws-advanced-python-wrapper "https://github.com/awslabs/aws-advanced-python-wrapper").
