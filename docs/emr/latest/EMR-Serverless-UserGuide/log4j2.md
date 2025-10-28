# Configure Apache Log4j2 properties for

Amazon EMR Serverless

This page describes how to configure custom [Apache Log4j 2.x](https://logging.apache.org/log4j/2.x/ "https://logging.apache.org/log4j/2.x/") properties for
EMR Serverless jobs at `StartJobRun`. If you want to configure Log4j
classifications at the application level, refer to [Default application configuration for EMR Serverless](default-configs.md "default-configs.md").

## Configure Spark Log4j2 properties for

Amazon EMR Serverless

With Amazon EMR releases 6.8.0 and higher, you can customize [Apache Log4j 2.x](https://logging.apache.org/log4j/2.x/ "https://logging.apache.org/log4j/2.x/") properties
to specify fine-grained log configurations. This simplifies troubleshooting of your
Spark jobs on EMR Serverless. To configure these properties, use the
`spark-driver-log4j2` and `spark-executor-log4j2`
classifications.

###### Topics

- [Log4j2 classifications for Spark](#log4j2-spark-class "#log4j2-spark-class")
- [Log4j2 configuration example for
  Spark](#log4j2-spark-example "#log4j2-spark-example")
- [Log4j2 in sample Spark jobs](#log4j2-spark-jobs "#log4j2-spark-jobs")
- [Log4j2 considerations for
  Spark](#log4j2-spark-considerations "#log4j2-spark-considerations")

### Log4j2 classifications for Spark

To customize the Spark log configurations, use the following classifications
with [`applicationConfiguration`](../../../emr-serverless/latest/APIReference/API_ConfigurationOverrides.md#emrserverless-Type-ConfigurationOverrides-applicationConfiguration "../../../emr-serverless/latest/APIReference/API_ConfigurationOverrides.md#emrserverless-Type-ConfigurationOverrides-applicationConfiguration"). To configure the Log4j
2.x properties, use the following [`properties`](../../../emr-serverless/latest/APIReference/API_Configuration.md#emrserverless-Type-Configuration-properties "../../../emr-serverless/latest/APIReference/API_Configuration.md#emrserverless-Type-Configuration-properties").

**`spark-driver-log4j2`**

This classification sets the values in the
`log4j2.properties` file for the
driver.

**`spark-executor-log4j2`**

This classification sets the values in the
`log4j2.properties` file for the
executor.

### Log4j2 configuration example for

Spark

The following example shows how to submit a Spark job with
`applicationConfiguration` to customize Log4j2 configurations for
the Spark driver and executor.

To configure Log4j classifications at the application level instead of when
you submit the job, refer to [Default application configuration for EMR Serverless](default-configs.md "default-configs.md").

```
aws emr-serverless start-job-run \
    --application-id application-id \
    --execution-role-arn job-role-arn \
    --job-driver '{
        "sparkSubmit": {
            "entryPoint": "/usr/lib/spark/examples/jars/spark-examples.jar",
            "entryPointArguments": ["1"],
            "sparkSubmitParameters": "--class org.apache.spark.examples.SparkPi --conf spark.executor.cores=4 --conf spark.executor.memory=20g --conf spark.driver.cores=4 --conf spark.driver.memory=8g --conf spark.executor.instances=1"
        }
    }'
    --configuration-overrides '{
        "applicationConfiguration": [
             {
                "classification": "spark-driver-log4j2",
                "properties": {
                    "rootLogger.level":"error", // will only display Spark error logs
                    "logger.`IdentifierForClass`.name": "`classpath for setting logger`",
                    "logger.`IdentifierForClass`.level": "info"

                }
            },
            {
                "classification": "spark-executor-log4j2",
                "properties": {
                    "rootLogger.level":"error", // will only display Spark error logs
                    "logger.`IdentifierForClass`.name": "`classpath for setting logger`",
                    "logger.`IdentifierForClass`.level": "info"
                }
            }
       ]
    }'
```

### Log4j2 in sample Spark jobs

The following code samples demonstrate how to create a Spark application while
you initialize a custom Log4j2 configuration for the application.

Python

###### Example - Using Log4j2 for a Spark job with Python

```
import os
import sys

from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

app_name = "`PySparkApp`"
if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName(app_name)\
        .getOrCreate()

    spark.sparkContext._conf.getAll()
    sc = spark.sparkContext
    log4jLogger = sc._jvm.org.apache.log4j
    LOGGER = log4jLogger.LogManager.getLogger(app_name)

    LOGGER.info("pyspark script logger info")
    LOGGER.warn("pyspark script logger warn")
    LOGGER.error("pyspark script logger error")

    // `your code here`

    spark.stop()
```

To customize Log4j2 for the driver when you execute a Spark
job, use the following configuration:

```
{
   "classification": "spark-driver-log4j2",
      "properties": {
          "rootLogger.level":"error", // only display Spark error logs
          "logger.PySparkApp.level": "info",
          "logger.PySparkApp.name": "`PySparkApp`"
      }
}
```

Scala

###### Example - Using Log4j2 for a Spark job with Scala

```
import org.apache.log4j.Logger
import org.apache.spark.sql.SparkSession

object ExampleClass {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession
    .builder
    .appName(this.getClass.getName)
    .getOrCreate()

    val logger = Logger.getLogger(this.getClass);
    logger.info("script logging info logs")
    logger.warn("script logging warn logs")
    logger.error("script logging error logs")

// `your code here`
    spark.stop()
  }
}
```

To customize Log4j2 for the driver when you execute a Spark
job, use the following configuration:

```
{
   "classification": "spark-driver-log4j2",
      "properties": {
          "rootLogger.level":"error", // only display Spark error logs
          "logger.ExampleClass.level": "info",
          "logger.ExampleClass.name": "ExampleClass"
      }
}
```

### Log4j2 considerations for

Spark

The following Log4j2.x properties are not configurable for Spark
processes:

- `rootLogger.appenderRef.stdout.ref`
- `appender.console.type`
- `appender.console.name`
- `appender.console.target`
- `appender.console.layout.type`
- `appender.console.layout.pattern`

For detailed information about the Log4j2.x properties that configure,
refer to the [`log4j2.properties.template` file](https://github.com/apache/spark/blob/v3.3.0/conf/log4j2.properties.template "https://github.com/apache/spark/blob/v3.3.0/conf/log4j2.properties.template") on
GitHub.
