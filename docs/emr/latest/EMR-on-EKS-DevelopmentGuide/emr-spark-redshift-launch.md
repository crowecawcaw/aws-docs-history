# Launching a Spark application using the Amazon Redshift integration for Apache Spark

To use the integration, you must pass the required Spark Redshift dependencies
with your Spark job. You must use `--jars` to include Redshift
connector-related libraries. To see other file locations supported by the
`--jars` option, see the [Advanced Dependency Management](https://spark.apache.org/docs/latest/submitting-applications.html#advanced-dependency-management "https://spark.apache.org/docs/latest/submitting-applications.html#advanced-dependency-management") section of the Apache Spark
documentation.

- `spark-redshift.jar`
- `spark-avro.jar`
- `RedshiftJDBC.jar`
- `minimal-json.jar`
  To launch a Spark application with the Amazon Redshift integration for Apache Spark on Amazon EMR on EKS release 6.9.0
  or later, use the following example command. Note that the paths listed with the
  `--conf spark.jars` option are the default paths for the JAR
  files.

```
aws emr-containers start-job-run \

--virtual-cluster-id `cluster_id` \
--execution-role-arn `arn` \
--release-label `emr-6.9.0-latest`\
--job-driver '{
    "sparkSubmitJobDriver": {
        "entryPoint": "s3://`script_path`",
            "sparkSubmitParameters":
            "--conf spark.kubernetes.file.upload.path=s3://`upload_path`
             --conf spark.jars=
                /usr/share/aws/redshift/jdbc/RedshiftJDBC.jar,
                /usr/share/aws/redshift/spark-redshift/lib/spark-redshift.jar,
                /usr/share/aws/redshift/spark-redshift/lib/spark-avro.jar,
                /usr/share/aws/redshift/spark-redshift/lib/minimal-json.jar"
                            }
            }'
```
