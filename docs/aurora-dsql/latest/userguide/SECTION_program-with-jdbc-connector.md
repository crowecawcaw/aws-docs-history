# Connecting to Aurora DSQL clusters with

a JDBC connector

The [Aurora DSQL Connector for JDBC](https://github.com/awslabs/aurora-dsql-connectors/tree/main/java/jdbc "https://github.com/awslabs/aurora-dsql-connectors/tree/main/java/jdbc") is designed as an authentication plugin that extends the functionality of the PostgreSQL JDBC driver to enable applications to authenticate with Aurora DSQL using IAM credentials. The connector does not connect directly to the database, but provides seamless IAM authentication on top of the underlying PostgreSQL JDBC driver.

The Aurora DSQL Connector for JDBC is built to work with the [PostgreSQL JDBC Driver](https://github.com/pgjdbc/pgjdbc "https://github.com/pgjdbc/pgjdbc") and provides
seamless integration with Aurora DSQL's IAM authentication requirements.

In conjunction with the PostgreSQL JDBC Driver, the Aurora DSQL Connector for JDBC enables IAM-based authentication for Aurora DSQL. It introduces deep integration with AWS authentication services such as [AWS Identity and Access Management](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") (IAM).

## About the connector

Aurora DSQL is a distributed SQL database service that provides high availability and scalability for PostgreSQL-compatible applications. Aurora DSQL requires IAM-based authentication with time-limited tokens that existing JDBC drivers do not natively support.

The main idea behind the Aurora DSQL Connector for JDBC is to add an authentication layer on top of the PostgreSQL JDBC driver that handles IAM token generation, allowing users to connect to Aurora DSQL without changing their existing JDBC workflows.

### What is Aurora DSQL Authentication?

In Aurora DSQL, **authentication** involves:

- **IAM Authentication**: All connections use IAM-based authentication with time-limited tokens
- **Token Generation**: Authentication tokens are generated using AWS credentials and have configurable lifetimes

The Aurora DSQL Connector for JDBC is designed to understand these requirements and automatically generate IAM authentication tokens when establishing connections.

### Benefits of the Aurora DSQL Connector for JDBC

Although Aurora DSQL provides a PostgreSQL-compatible interface, existing PostgreSQL drivers do not currently support Aurora DSQL's IAM authentication requirements. The Aurora DSQL Connector for JDBC allows customers to continue using their existing PostgreSQL workflows while enabling IAM authentication through:

- **Automatic Token Generation**: IAM tokens are generated automatically using AWS credentials
- **Seamless Integration**: Works with existing JDBC connection patterns
- **AWS Credentials Support**: Supports various AWS credential providers (default, profile-based, etc.)

### Using the

Aurora DSQL Connector for JDBC with connection pooling

The Aurora DSQL Connector for JDBC works with connection pooling libraries such as HikariCP. The connector handles IAM token generation during connection establishment, allowing connection pools to operate normally.

## Key features

Automatic Token Generation

IAM tokens are generated automatically using AWS credentials.

Seamless Integration

Works with existing JDBC connection patterns without requiring workflow changes.

AWS Credentials Support

Supports various AWS credential providers (default, profile-based, etc.).

Connection Pooling Compatibility

Works seamlessly with connection pooling libraries like HikariCP.

## Prerequisites

Before you begin, make sure that you have completed the following prerequisites:

- [Created a cluster in Aurora DSQL](getting-started.md "getting-started.md").
- Installed the Java Development Kit (JDK). Make sure that you have version 17 or higher.
- Set up appropriate IAM permissions to allow your application to connect to Aurora DSQL.
- AWS credentials configured (via AWS CLI, environment variables, or IAM roles).

## Using the Aurora DSQL Connector for JDBC

To use the Aurora DSQL Connector for JDBC in your Java application, follow these steps:

1. Add the following dependencies to your Maven project:

```
<dependencies>
    <!-- Aurora DSQL Connector for JDBC -->
    <dependency>
        <groupId>software.amazon.dsql</groupId>
        <artifactId>aurora-dsql-jdbc-connector</artifactId>
        <version>1.0.0</version>
    </dependency>
</dependencies>
```

For Gradle projects, add this dependency:

```
implementation("software.amazon.dsql:aurora-dsql-jdbc-connector:1.0.0")
```

2. Create a basic connection to your Aurora DSQL cluster using the AWS DSQL PostgreSQL connector format:

```
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class DsqlJdbcConnectorExample {
    public static void main(String[] args) {
        // Using AWS DSQL PostgreSQL Connector prefix
        String jdbcUrl = "jdbc:aws-dsql:postgresql://your-cluster.dsql.us-east-1.on.aws/postgres?user=admin";

        try (Connection connection = DriverManager.getConnection(jdbcUrl)) {
            // Use the connection
            try (Statement statement = connection.createStatement()) {
                // Create a table
                statement.execute("CREATE TABLE IF NOT EXISTS test_table (id UUID PRIMARY KEY DEFAULT gen_random_uuid(), name VARCHAR(100))");

                // Insert data
                statement.execute("INSERT INTO test_table (name) VALUES ('Test Name')");

                // Query data
                try (ResultSet resultSet = statement.executeQuery("SELECT * FROM test_table")) {
                    while (resultSet.next()) {
                        System.out.println("ID: " + resultSet.getInt("id") + ", Name: " + resultSet.getString("name"));
                    }
                }
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
```

### Configuration properties

The Aurora DSQL Connector for JDBC supports the following connection properties:

user

Determines the user for the connection and the token generation method used. Example: `admin`

token-duration-secs

Duration in seconds for token validity. For more information on token limits, see [Generating an authentication token in Amazon Aurora DSQL](SECTION_authentication-token.md "SECTION_authentication-token.md").

profile

Used for instantiating a ProfileCredentialsProvider for token generation with the provided profile name.

region

AWS region for Aurora DSQL connections. It is optional. When provided, it will override the region extracted from the URL.

database

The database name to connect to. Default is `postgres`.

### Logging

Enable logging for troubleshooting any issue you might experience while using the
Aurora DSQL JDBC connector.

The connector uses the built-in logging system (java.util.logging) of Java. You can
configure logging levels by creating a `logging.properties` file:

```
# Set root logger level to INFO for clean output
.level = INFO

# Show Aurora DSQL Connector for JDBC FINE logs for detailed debugging
software.amazon.dsql.level = FINE

# Console handler configuration
handlers = java.util.logging.ConsoleHandler
java.util.logging.ConsoleHandler.level = FINE
java.util.logging.ConsoleHandler.formatter = java.util.logging.SimpleFormatter

# Detailed formatter pattern with timestamp and logger name
java.util.logging.SimpleFormatter.format = %1$tH:%1$tM:%1$tS.%1$tL [%4$s] %3$s - %5$s%n
```

### Examples

For more comprehensive examples and use cases, refer to the [Aurora DSQL Connector for JDBC repository](https://github.com/awslabs/aurora-dsql-connectors/tree/main/java/jdbc/examples "https://github.com/awslabs/aurora-dsql-connectors/tree/main/java/jdbc/examples")
