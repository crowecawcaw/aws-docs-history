# Using Java 17 with Amazon EMR Serverless

With Amazon EMR releases 6.11.0 and higher, configure EMR Serverless Spark jobs to use
Java 17 runtime for the Java Virtual Machine (JVM). Use one of the following methods to
configure Spark with Java 17.

## `JAVA_HOME`

To override the JVM setting for EMR Serverless 6.11.0 and higher, supply the
`JAVA_HOME` setting to its `spark.emr-serverless.driverEnv`
and `spark.executorEnv` environment classifications.

x86_64
Set the required properties to specify Java 17 as the
`JAVA_HOME` configuration for the Spark driver and
executors:

```
--conf spark.emr-serverless.driverEnv.JAVA_HOME=/usr/lib/jvm/java-17-amazon-corretto.x86_64/
--conf spark.executorEnv.JAVA_HOME=/usr/lib/jvm/java-17-amazon-corretto.x86_64/
```

arm_64
Set the required properties to specify Java 17 as the
`JAVA_HOME` configuration for the Spark driver and
executors:

```
--conf spark.emr-serverless.driverEnv.JAVA_HOME=/usr/lib/jvm/java-17-amazon-corretto.aarch64/
--conf spark.executorEnv.JAVA_HOME=/usr/lib/jvm/java-17-amazon-corretto.aarch64/
```

## `spark-defaults`

Alternatively, you can specify Java 17 in the `spark-defaults`
classification to override the JVM setting for EMR Serverless 6.11.0 and higher.

x86_64
Specify Java 17 in the `spark-defaults` classification:

```
{
"applicationConfiguration": [
         {
            "classification": "spark-defaults",
            "properties": {
               "spark.emr-serverless.driverEnv.JAVA_HOME" : "/usr/lib/jvm/java-17-amazon-corretto.x86_64/",
               "spark.executorEnv.JAVA_HOME": "/usr/lib/jvm/java-17-amazon-corretto.x86_64/"
            }
         }
      ]
}
```

arm_64
Specify Java 17 in the `spark-defaults` classification:

```
{
"applicationConfiguration": [
         {
            "classification": "spark-defaults",
            "properties": {
               "spark.emr-serverless.driverEnv.JAVA_HOME" : "/usr/lib/jvm/java-17-amazon-corretto.aarch64/",
               "spark.executorEnv.JAVA_HOME": "/usr/lib/jvm/java-17-amazon-corretto.aarch64/"
            }
         }
      ]
}
```
