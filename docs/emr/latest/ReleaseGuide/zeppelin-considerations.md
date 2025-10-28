# Considerations when using Zeppelin on Amazon EMR

- Connect to Zeppelin using the same [SSH tunneling method](../ManagementGuide/emr-ssh-tunnel.md "../ManagementGuide/emr-ssh-tunnel.md") to connect to other web servers on the
  master node. Zeppelin server is found at port 8890.
- Zeppelin on Amazon EMR release versions 5.0.0 and later supports [Shiro authentication](https://zeppelin.apache.org/docs/0.8.0/setup/security/shiro_authentication.html "https://zeppelin.apache.org/docs/0.8.0/setup/security/shiro_authentication.html").
- Zeppelin on Amazon EMR release versions 5.8.0 and later supports using AWS Glue Data Catalog as the metastore for Spark SQL. For more information, see [Using AWS Glue Data Catalog as the metastore for Spark SQL.](emr-spark-glue.md "emr-spark-glue.md")
- Zeppelin does not use some of the settings defined in your cluster's
  `spark-defaults.conf` configuration file, even though it
  instructs YARN to allocate executors dynamically if you have set `spark.dynamicAllocation.enabled` to `true`. You must set executor settings, such as memory and cores, using the Zeppelin **Interpreter** tab, and then restart the interpreter for them to be used.
- Amazon EMR releases 6.10.0 and higher support Apache Zeppelin integration with Apache Flink.
  See [Working with Flink jobs from Zeppelin in Amazon EMR](flink-zeppelin.md "flink-zeppelin.md") for more information.
- Zeppelin on Amazon EMR does not support the SparkR interpreter.
