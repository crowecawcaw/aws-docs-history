# Get started with the JDBC 3.x

driver

Use the information in this section to get started with the Amazon Athena JDBC 3.x
driver.

###### Topics

- [Installation
  Instructions](#jdbc-v3-driver-installation-instructions "#jdbc-v3-driver-installation-instructions")
- [Running the driver](#jdbc-v3-driver-running-the-driver "#jdbc-v3-driver-running-the-driver")
- [Configuring the driver](#jdbc-v3-driver-configuring-the-driver "#jdbc-v3-driver-configuring-the-driver")
- [Upgrading from the Athena JDBC v2 driver](#jdbc-v3-driver-upgrading-from-the-athena-jdbc-v2-driver-to-v3 "#jdbc-v3-driver-upgrading-from-the-athena-jdbc-v2-driver-to-v3")

## Installation

Instructions

You can use the JDBC 3.x driver in custom application or from a third-party SQL
client.

### In a custom

application

Download the `.zip` file that contains the driver jar and its
dependencies. Each dependency has its own `.jar` file. Add the
driver jar as a dependency in your custom application. Selectively add the
dependencies of the driver jar based on whether you have already added those
dependencies to your application from another source.

### In a

third-party SQL client

Download the driver uber jar file and add it to the third-party SQL client
following the instructions for that client.

## Running the driver

To run the driver, you can use a custom application or a third-party SQL
client.

### In a custom

application

Use the JDBC interface to interact with the JDBC driver from a program. The
following code shows a sample custom Java application.

```
public static void main(String args[]) throws SQLException {
    Properties connectionParameters = new Properties();
    connectionParameters.setProperty("Workgroup", "primary");
    connectionParameters.setProperty("Region", "us-east-2");
    connectionParameters.setProperty("Catalog", "AwsDataCatalog");
    connectionParameters.setProperty("Database","sampledatabase");
    connectionParameters.setProperty("OutputLocation","s3://amzn-s3-demo-bucket");
    connectionParameters.setProperty("CredentialsProvider","DefaultChain");
    String url = "jdbc:athena://";
    AthenaDriver driver = new AthenaDriver();
    Connection connection = driver.connect(url, connectionParameters);
    Statement statement = connection.createStatement();
    String query = "SELECT * from sample_table LIMIT 10";
    ResultSet resultSet = statement.executeQuery(query);
    printResults(resultSet); // A custom-defined method for iterating over a
                             // result set and printing its contents
}
```

### In a

third-party SQL client

Follow the documentation for the SQL client that you are using. Typically, you use
the SQL client's graphical user interface to enter and submit the query, and the
query results are displayed in the same interface.

## Configuring the driver

You can use connection parameters to configure the Amazon Athena JDBC driver. For
supported connection parameters, see [Amazon Athena JDBC
3.x connection parameters](jdbc-v3-driver-connection-parameters.md "jdbc-v3-driver-connection-parameters.md").

### In a custom

application

To set the connection parameters for the JDBC driver in a custom application, do
one of the following:

- Add the parameter names and their values to a `Properties`
  object. When you call `Connection#connect`, pass that object
  along with the URL. For an example, see the sample Java application in [Running the driver](#jdbc-v3-driver-running-the-driver "#jdbc-v3-driver-running-the-driver").
- In the connection string (the URL), use the following format to add the
  parameter names and their values directly after the protocol prefix.

```
`<parameterName>`=`<parameterValue>`;
```

Use a semi-colon at the end of each parameter name/parameter value pair,
and leave no white space after the semicolon, as in the following
example.

```
String url = "jdbc:athena://WorkGroup=primary;Region=us-east-1;...;";AthenaDriver driver = new AthenaDriver();Connection connection = driver.connect(url, null);
```

###### Note

If a parameter is specified both in the connection string and in the
`Properties` object, the value in the connection string
takes precedence. Specifying the same parameter in both places is not
recommended.

- Add the parameter values as arguments to the methods of
  `AthenaDataSource`, as in the following example.

```
AthenaDataSource dataSource = new AthenaDataSource();
    dataSource.setWorkGroup("primary");
    dataSource.setRegion("us-east-2");
    ...
    Connection connection = dataSource.getConnection();
    ...
```

### In a

third-party SQL client

Follow the instructions of the SQL client that you are using. Typically, the
client provides a graphical user interface to input the parameter names and their
values.

## Upgrading from the Athena JDBC v2 driver

Most of the JDBC version 3 connection parameters are backwards-compatible with the
version 2 (Simba) JDBC driver. This means that a version 2 connection string can be
reused with version 3 of the driver. However, some connection parameters have changed.
These changes are described
here.
When you upgrade to the version 3 JDBC driver, update your existing
configuration if
necessary.

### Driver class

Some BI tools ask you to provide the driver class from the JDBC driver
`.jar` file. Most tools find this class automatically. The
fully qualified name of the class in the version 3 driver is
`com.amazon.athena.jdbc.AthenaDriver`. In the version 2 driver, the
class was `com.simba.athena.jdbc.Driver`.

### Connection

string

The version
3 driver uses `jdbc:athena://` for the protocol at the beginning of the
JDBC connection string URL. The version 3 driver also supports the version 2
protocol `jdbc:awsathena://`, but the use of the version 2 protocol is
deprecated. To avoid undefined behaviors, version 3 does not accept connection
strings that start with `jdbc:awsathena://` if version 2 (or any other
driver that accepts connection strings that start with
`jdbc:awsathena://`) has been registered with the [DriverManager](https://docs.oracle.com/javase/8/docs/api/java/sql/DriverManager.html "https://docs.oracle.com/javase/8/docs/api/java/sql/DriverManager.html") class.

### Credentials

providers

The version 2 driver uses fully qualified names to identify different credentials
providers (for example,
`com.simba.athena.amazonaws.auth.DefaultAWSCredentialsProviderChain`.
The version 3 driver uses shorter names (for example, `DefaultChain`).
The new names are described in the corresponding sections for each credentials
provider.

Custom credentials providers written for the version 2 driver need to be modified
for the version 3 driver to implement the [AwsCredentialsProvider](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/auth/credentials/AwsCredentialsProvider.html "https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/auth/credentials/AwsCredentialsProvider.html") interface from the new AWS SDK for Java instead of the
[AWSCredentialsProvider](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/auth/AWSCredentialsProvider.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/auth/AWSCredentialsProvider.md") interface from the previous AWS SDK for Java.

The `PropertiesFileCredentialsProvider` is not supported in the JDBC
3.x driver. The provider was used in the JDBC 2.x driver but belongs to the previous
version of the AWS SDK for Java which is approaching end of support. To achieve
the same functionality in the JDBC 3.x driver, use the [AWS
configuration profile credentials](jdbc-v3-driver-aws-configuration-profile-credentials.md "jdbc-v3-driver-aws-configuration-profile-credentials.md") provider
instead.

### Log level

The following table shows the differences in the `LogLevel` parameters
in the JDBC version 2 and version 3 drivers.

| JDBC driver version | Parameter name | Parameter type | Default value | Possible values                      | Connection string example |
| ------------------- | -------------- | -------------- | ------------- | ------------------------------------ | ------------------------- |
| v2                  | `LogLevel`     | Optional       | 0             | 0-6                                  | `LogLevel=6;`             |
| v3                  | `LogLevel`     | Optional       | TRACE         | OFF, ERROR, WARN, INFO, DEBUG, TRACE | `LogLevel=INFO;`          |

### Query ID

retrieval

In the version 2 driver, you unwrap a `Statement` instance to
`com.interfaces.core.IStatementQueryInfoProvider`, an interface that
has two methods: `#getPReparedQueryId` and `#getQueryId`. You
can use these methods to obtain the query execution ID of a query that has
run.

In the version 3 driver, you unwrap `Statement`,
`PreparedStatement`, and `ResultSet` instances to the
`com.amazon.athena.jdbc.AthenaResultSet` interface. The interface has
one method: `#getQueryExecutionId`.
