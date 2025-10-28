# Other JDBC 3.x

configuration

The following sections describe some additional configuration settings for the JDBC
3.x driver.

## Network timeout

The network timeout controls the amount of time in milliseconds that the driver
waits for a network connection to be established. This includes the time it takes to
send API requests. After this time, the driver throws a timeout exception. In rare
circumstances, it may be useful to change the network timeout. For example, you
might want to increase the timeout for long garbage collection pauses.

To set it, call the `setNetworkTimeout` method on a JDBC
`Connection` object. This value can be changed during the lifecycle
of the JDBC connection. For more information, see [setNetworkTimeout](https://docs.oracle.com/javase/8/docs/api/java/sql/Connection.html#setNetworkTimeout-java.util.concurrent.Executor-int- "https://docs.oracle.com/javase/8/docs/api/java/sql/Connection.html#setNetworkTimeout-java.util.concurrent.Executor-int-") in the Oracle JDBC API documentation. Using the
`setNetworkTimeout` method is equivalent to setting the [Network timeout](jdbc-v3-driver-advanced-connection-parameters.md#jdbc-v3-driver-networktimeoutmillis "jdbc-v3-driver-advanced-connection-parameters.md#jdbc-v3-driver-networktimeoutmillis") connection parameter.

The following example sets the network timeout to 5000 milliseconds.

```
...
AthenaDriver driver = new AthenaDriver();
Connection connection = driver.connect(url, connectionParameters);
connection.setNetworkTimeout(null, 5000);
...
```

## Query timeout

The amount of time, in seconds, the driver will wait for a query to complete on
Athena after a query has been submitted. After this time, the driver attempts to
cancel the submitted query and throws a timeout exception.

The query timeout cannot be set as a connection parameter. To set it, call the
`setQueryTimeout` method on a JDBC `Statement` object.
This value can be changed during the lifecycle of a JDBC statement. The default
value of this parameter is `0` (zero). A value of `0` means
that queries can run until they complete (subject to [Service Quotas](service-limits.md "service-limits.md")).

The following example sets the query timeout to 5 seconds.

```
...
AthenaDriver driver = new AthenaDriver();
Connection connection = driver.connect(url, connectionParameters);
Statement statement = connection.createStatement();
statement.setQueryTimeout(5);
...
```
