# Launching a Spark application with the

Amazon Redshift integration for Apache Spark

To use the integration with EMR Serverless 6.9.0, pass the required
Spark-Redshift dependencies with your Spark job. Use `--jars` to
include Redshift connector related libraries. To access other file locations supported
by the `--jars` option, refer to the [Advanced Dependency Management](https://spark.apache.org/docs/latest/submitting-applications.html#advanced-dependency-management "https://spark.apache.org/docs/latest/submitting-applications.html#advanced-dependency-management") section of the Apache Spark
documentation.

- `spark-redshift.jar`
- `spark-avro.jar`
- `RedshiftJDBC.jar`
- `minimal-json.jar`
  Amazon EMR releases 6.10.0 and higher don't require the `minimal-json.jar`
  dependency, and automatically install the other dependencies to each cluster by
  default. The following examples demonstrate how to launch a Spark application with the
  Amazon Redshift integration for Apache Spark.

Amazon EMR 6.10.0 +
Launch a Spark job on Amazon EMR Serverless with the Amazon Redshift integration for Apache Spark on
EMR Serverless release 6.10.0 and higher.

```
spark-submit my_script.py
```

Amazon EMR 6.9.0
To launch a Spark job on Amazon EMR Serverless with the Amazon Redshift integration for Apache Spark
on EMR Serverless release 6.9.0, use the `--jars`
option as shown in the following example. Note that the paths listed
with the `--jars` option are the default paths for
the JAR files.

```
--jars
    /usr/share/aws/redshift/jdbc/RedshiftJDBC.jar,
    /usr/share/aws/redshift/spark-redshift/lib/spark-redshift.jar,
    /usr/share/aws/redshift/spark-redshift/lib/spark-avro.jar,
    /usr/share/aws/redshift/spark-redshift/lib/minimal-json.jar
```

```
spark-submit \
  --jars /usr/share/aws/redshift/jdbc/RedshiftJDBC.jar,/usr/share/aws/redshift/spark-redshift/lib/spark-redshift.jar,/usr/share/aws/redshift/spark-redshift/lib/spark-avro.jar,/usr/share/aws/redshift/spark-redshift/lib/minimal-json.jar \
  my_script.py
```
