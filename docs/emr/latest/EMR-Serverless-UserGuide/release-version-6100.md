# EMR Serverless 6.10.0

The following table lists the application versions available with
EMR Serverless 6.10.0.

| Application  | Version |
| ------------ | ------- |
| Apache Spark | 3.3.1   |
| Apache Hive  | 3.1.3   |
| Apache Tez   | 0.10.2  |

###### EMR Serverless 6.10.0 release notes

- For EMR Serverless applications with release 6.10.0 or higher, the default value for the
  `spark.dynamicAllocation.maxExecutors` property is `infinity`. Earlier
  releases default to `100`. For more information, refer to [Spark job properties](jobs-spark.md#spark-defaults "jobs-spark.md#spark-defaults").
