# Getting started with the Neptune JDBC driver

To use the Neptune JDBC driver to connect to a Neptune instance, either the JDBC
driver must be deployed on an Amazon EC2 instance in the same VPC as your Neptune DB
cluster, or the instance must be available through an SSH tunnel or load balancer.
An SSH tunnel can be set up in the driver internally, or it can be set up externally.

You can download the driver [here](https://github.com/aws/amazon-neptune-jdbc-driver/releases "https://github.com/aws/amazon-neptune-jdbc-driver/releases").
The driver comes packaged as a single JAR file with a name like
`neptune-jdbc-1.0.0-all.jar`. To use it, place the JAR file
in the `classpath` of your application. Or, if your application uses Maven
or Gradle, you can use the appropriate Maven or Gradle commands to install the driver
from the JAR.

The driver needs a JDBC connection URL to connect with Neptune, in a form like
this:

```
jdbc:neptune:`(connection type)`://`(host)`;`property`=`value`;`property`=`value`;`...`;`property`=`value`
```

The sections for each query language in the GitHub project describe the
properties that you can set in the JDBC connection URL for that query language.

If the JAR file is in your application's `classpath`, no other
configuration is necessary. You can connect the driver using the JDBC
`DriverManager` interface and a Neptune connection string. For
example, if your Neptune DB cluster is accessible through the endpoint
`neptune-example.com` on port 8182, you would be able to connect
with openCypher like this:

```
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

void example() {
    String url = "jdbc:neptune:opencypher://bolt://neptune-example:8182";

    Connection connection = DriverManager.getConnection(url);
    Statement statement = connection.createStatement();

    connection.close();
}
```

The documentation sections in the GitHub project for each query language
describe how to construct the connection string when using that query language.
