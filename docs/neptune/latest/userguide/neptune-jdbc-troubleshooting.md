# Troubleshooting a JDBC driver connection

If the driver fails to connect to the server, use the `isValid` function
of the JDBC `Connection` object to check whether the connection is valid.
If the function returns `false`, meaning that the connection is invalid,
check that the endpoint being connected to is correct and that you are in the VPC
of your Neptune DB cluster or that you have a valid SSH tunnel to the cluster.

If you get a `No suitable driver found for `(connection
string)``response from the`DriverManager.getConnection`
call, there is likely an issue at the beginning of your connection string.
Make sure that your connection string starts like this:

```
jdbc:neptune:`opencypher`://`...`
```

To gather more information about the connection, you can add a `LogLevel`
to your connection string like this:

```
jdbc:neptune:`opencypher`://`(JDBC URL)`:`(port)`;logLevel=trace
```

Alternatively, you can add `properties.put("logLevel", "trace")` in
your input properties to log trace information.
