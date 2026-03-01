# Connecting to Multi-AZ DB clusters with the AWS drivers for Amazon RDS

The AWS suite of drivers has been designed to provide support for faster switchover
and failover times, and authentication with AWS Secrets Manager, AWS Identity and Access Management (IAM), and Federated
Identity. The AWS drivers rely on monitoring DB cluster status and being aware of the
cluster topology to determine the new writer. This approach reduces switchover and
failover times to single-digit seconds, compared to tens of seconds for open-source
drivers.

As new service features are introduced, the goal of the AWS suite of drivers is to
have built-in support for these service features.

## Connecting to Multi-AZ DB clusters with the Amazon Web Services (AWS) JDBC Driver

The Amazon Web Services (AWS) JDBC Driver is designed as an advanced JDBC wrapper to help applications
take advantage of the features of clustered databases. This wrapper is complementary
to and extends the functionality of an existing JDBC driver. The driver is drop-in
compatible with the following community drivers:

- MySQL Connector/J
- MariaDB Connector/J
- pgJDBC

To install the AWS JDBC Driver, append the AWS JDBC Driver .jar file (located in the
application `CLASSPATH`), and keep references to the respective community
driver. Update the respective connection URL prefix as follows:

- `jdbc:mysql://` to
  `jdbc:aws-wrapper:mysql://`
- `jdbc:mariadb://` to
  `jdbc:aws-wrapper:mariadb://`
- `jdbc:postgresql://` to
  `jdbc:aws-wrapper:postgresql://`

For more information about the AWS JDBC Driver and complete instructions for using
it, see the [Amazon Web Services (AWS) JDBC Driver GitHub repository](https://github.com/awslabs/aws-advanced-jdbc-wrapper "https://github.com/awslabs/aws-advanced-jdbc-wrapper").

## Connecting to Multi-AZ DB clusters with the Amazon Web Services (AWS) Python Driver

The Amazon Web Services (AWS) Python Driver is designed as an advanced Python wrapper. This wrapper is
complementary to and extends the functionality of the open-source Psycopg driver.
The AWS Python Driver supports Python versions 3.8 and higher. You can install the
`aws-advanced-python-wrapper` package using the `pip`
command, along with the `psycopg` open-source packages.

For more information about the AWS Python Driver and complete instructions for using
it, see the [Amazon Web Services (AWS) Python Driver GitHub repository](https://github.com/awslabs/aws-advanced-python-wrapper "https://github.com/awslabs/aws-advanced-python-wrapper").
