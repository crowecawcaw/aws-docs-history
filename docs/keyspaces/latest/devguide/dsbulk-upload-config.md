# Step 4: Configure `DSBulk`

settings to upload data from the CSV file to the target table

This section outlines the steps required to configure DSBulk for data upload to Amazon Keyspaces. You configure DSBulk by using a configuration file. You specify the
configuration file directly from the command line.

1. Create a DSBulk configuration file for the migration to Amazon Keyspaces, in this example we use the file name `dsbulk_keyspaces.conf`.
   Specify the following settings in the DSBulk configuration file.
   1. _`PlainTextAuthProvider`_ – Create the authentication provider with the `PlainTextAuthProvider` class. `ServiceUserName` and
      `ServicePassword` should match the user name and password you obtained when you generated the service-specific credentials by
      following the steps at [Create credentials for programmatic access to Amazon Keyspaces](programmatic.md "programmatic.md") .
   2. _`local-datacenter`_ – Set the
      value for `local-datacenter` to the AWS Region that you're
      connecting to. For example, if the application is connecting to
      `cassandra.`us-east-1`.amazonaws.com`, then set the local
      data center to `us-east-1`. For all available AWS Regions,
      see [Service endpoints for Amazon Keyspaces](programmatic.md "programmatic.md"). To avoid replicas,
      set `slow-replica-avoidance` to `false`.
   3. _`SSLEngineFactory`_ – To
      configure SSL/TLS, initialize the `SSLEngineFactory` by
      adding a section in the configuration file with a single line that
      specifies the class with `class = DefaultSslEngineFactory`.
      Provide the path to `cassandra_truststore.jks` and
      the password that you created previously.
   4. _`consistency`_ – Set the consistency level to `LOCAL
QUORUM`. Other write consistency levels are not supported, for
      more information see [Supported Apache Cassandra read and write consistency levels and associated costs](consistency.md "consistency.md").
   5. The number of connections per pool is configurable in the Java driver. For this example, set
      `advanced.connection.pool.local.size` to 3.The following is the complete sample configuration file.

```
datastax-java-driver {
basic.contact-points = [ "cassandra.`us-east-1`.amazonaws.com:9142"]
advanced.auth-provider {
    class = PlainTextAuthProvider
    username = "`ServiceUserName`"
    password = "`ServicePassword`"
}

basic.load-balancing-policy {
    local-datacenter = "`us-east-1`"
    slow-replica-avoidance = false
}

basic.request {
    consistency = LOCAL_QUORUM
    default-idempotence = true
}
advanced.ssl-engine-factory {
    class = DefaultSslEngineFactory
    truststore-path = "./cassandra_truststore.jks"
    truststore-password = "`my_password`"
    hostname-validation = false
  }
advanced.connection.pool.local.size = 3
}
```

2.  Review the parameters for the DSBulk `load` command.
    1. _`executor.maxPerSecond`_ – The maximum number of rows that the load command attempts to process
       concurrently per second. If unset, this setting is disabled with -1.

    Set `executor.maxPerSecond` based on the number of WCUs that you provisioned to the target destination table. The `executor.maxPerSecond`
    of the `load` command isn’t a limit – it’s a target average. This means it can (and often does) burst above the number you set. To allow for
    bursts and make sure that enough capacity is in place to handle the data load requests, set `executor.maxPerSecond` to 90% of the table’s write capacity.

    ```
    executor.maxPerSecond = WCUs * .90
    ```

    In this tutorial, we set `executor.maxPerSecond` to 5.

    ###### Note

    If you are using DSBulk 1.6.0 or higher, you can use `dsbulk.engine.maxConcurrentQueries` instead. 2. Configure these additional parameters for the DSBulk `load` command.

        * *`batch-mode`* – This parameter tells the system to group operations by partition key.
         We recommend to disable batch mode, because it can result in hot key scenarios and cause `WriteThrottleEvents`.
        * *`driver.advanced.retry-policy-max-retries`* – This determines
         how many times to retry a failed query. If unset, the default is 10. You can adjust this value as needed.
        * *`driver.basic.request.timeout`* – The time in minutes the system waits for a query
         to return. If unset, the default is "5 minutes". You can adjust this value as needed.
