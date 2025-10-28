# Connecting to RDS for PostgreSQL with the

Amazon Web Services (AWS) JDBC Driver

The Amazon Web Services (AWS) JDBC Driver is designed as an advanced JDBC wrapper. This wrapper is
complementary to and extends the functionality of an existing JDBC driver. The driver is
drop-in compatible with the community pgJDBC driver.

To install the AWS JDBC Driver, append the AWS JDBC Driver .jar file (located in the
application `CLASSPATH`), and keep references to the respective community
driver. Update the respective connection URL prefix as follows:

- `jdbc:postgresql://` to
  `jdbc:aws-wrapper:postgresql://`
  For more information about the AWS JDBC Driver and complete instructions for using it,
  see the [Amazon Web Services (AWS) JDBC Driver GitHub repository](https://github.com/awslabs/aws-advanced-jdbc-wrapper "https://github.com/awslabs/aws-advanced-jdbc-wrapper").
