# Modifying PySpark session parameters

Starting with Amazon EMR on EKS release 6.9.0, in Amazon EMR Studio you can adjust the Spark
configuration associated with a PySpark session by executing the `%%configure`
magic command in the EMR notebook cell.

The following example shows a sample payload that you can use to modify memory, cores,
and other properties for the Spark driver and executor. For the `conf` settings,
you can configure any Spark configuration mentioned in the [Apache Spark configuration
documentation](https://spark.apache.org/docs/latest/configuration.html "https://spark.apache.org/docs/latest/configuration.html").

```
%%configure -f
{
  "driverMemory": "16G",
  "driverCores": 4,
  "executorMemory" : "32G",
  "executorCores": 2,
  "conf": {
     "spark.dynamicAllocation.maxExecutors" : 10,
     "spark.dynamicAllocation.minExecutors": 1
  }
}
```

The following example shows a sample payload that you can use to add files, pyFiles, and
jar dependencies to a Spark runtime.

```
%%configure -f
{
  "files": "s3://`amzn-s3-demo-bucket-emr-eks/sample_file`.txt",
  "pyFiles": : "`path-to-python-files`",
  "jars" : "`path-to-jars`
}
```
