# Launching a Spark application using the Amazon Redshift integration for Apache Spark

For Amazon EMR releases 6.4 through 6.9, you must use the `--jars`
or `--packages` option to specify which of the following JAR
files you want to use. The `--jars` option specifies dependencies
stored locally, in HDFS, or using HTTP/S. To see other file locations supported by
the `--jars` option, see [Advanced Dependency Management](https://spark.apache.org/docs/latest/submitting-applications.html#advanced-dependency-management "https://spark.apache.org/docs/latest/submitting-applications.html#advanced-dependency-management") in the Spark documentation. The
`--packages` option specifies dependencies stored in the
public Maven repo.

- `spark-redshift.jar`
- `spark-avro.jar`
- `RedshiftJDBC.jar`
- `minimal-json.jar`
  Amazon EMR releases 6.10.0 and higher don't require the `minimal-json.jar`
  dependency, and automatically install the other dependencies to each cluster by
  default. The following examples show how to launch a Spark application with the
  Amazon Redshift integration for Apache Spark.

Amazon EMR 6.10.0 +
The following example shows how to launch a Spark application with the
`spark-redshift` connector with Amazon EMR releases 6.10 and
higher.

```
spark-submit my_script.py
```

Amazon EMR 6.4.0 - 6.9.x
To launch a Spark application with the `spark-redshift`
connector on Amazon EMR releases 6.4 through 6.9, you must use the
`--jars` or `--packages`
option, as the following example shows. Note that the paths listed with
the `--jars` option are the default paths for the JAR
files.

```
spark-submit \
  --jars /usr/share/aws/redshift/jdbc/RedshiftJDBC.jar,/usr/share/aws/redshift/spark-redshift/lib/spark-redshift.jar,/usr/share/aws/redshift/spark-redshift/lib/spark-avro.jar,/usr/share/aws/redshift/spark-redshift/lib/minimal-json.jar \
  my_script.py
```
