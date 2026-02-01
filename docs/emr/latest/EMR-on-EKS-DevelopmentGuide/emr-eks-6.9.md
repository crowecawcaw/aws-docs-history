# Amazon EMR on EKS 6.9.0 releases

The following Amazon EMR 6.9.0 releases are available for Amazon EMR on EKS. Select a specific **emr-6.9.0-XXXX** release to view more details such as the related container
image tag.

- [emr-6.9.0-latest](emr-eks-6.9.md "emr-eks-6.9.md")
- [emr-6.9.0-20230905](emr-eks-6.9.md "emr-eks-6.9.md")
- [emr-6.9.0-20230624](emr-eks-6.9.md "emr-eks-6.9.md")
- [emr-6.9.0-20221108](emr-eks-6.9.md "emr-eks-6.9.md")
- emr-6.9.0-spark-rapids-latest
- emr-6.9.0-spark-rapids-20230624
- emr-6.9.0-spark-rapids-20221108
- notebook-spark/emr-6.9.0-latest
- notebook-spark/emr-6.9.0-20230624
- notebook-spark/emr-6.9.0-20221108
- notebook-python/emr-6.9.0-latest
- notebook-python/emr-6.9.0-20230624
- notebook-python/emr-6.9.0-20221108
  **Release notes for Amazon EMR 6.9.0**

- Supported applications ‐ AWS SDK for Java 1.12.331, Spark 3.3.0-amzn-1, Hudi 0.12.1-amzn-0,
  Iceberg 0.14.1-amzn-0, Delta 2.1.0.
- Supported components ‐ `aws-sagemaker-spark-sdk`, `emr-ddb`,
  `emr-goodies`, `emr-s3-select`, `emrfs`,
  `hadoop-client`, `hudi`, `hudi-spark`, `iceberg`,
  `spark-kubernetes`.
- Supported configuration classifications:

For use with [StartJobRun](../../../emr-on-eks/latest/APIReference/API_StartJobRun.md "../../../emr-on-eks/latest/APIReference/API_StartJobRun.md") and [CreateManagedEndpoint](../../../emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.md "../../../emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.md") APIs:

| Classifications   | Descriptions                                       |
| ----------------- | -------------------------------------------------- |
| `core-site`       | Change values in Hadoop’s core-site.xml file.      |
| `emrfs-site`      | Change EMRFS settings.                             |
| `spark-metrics`   | Change values in Spark's metrics.properties file.  |
| `spark-defaults`  | Change values in Spark's spark-defaults.conf file. |
| `spark-env`       | Change values in the Spark environment.            |
| `spark-hive-site` | Change values in Spark's hive-site.xml file.       |
| `spark-log4j`     | Change values in Spark's log4j.properties file.    |

For use specifically with [CreateManagedEndpoint](../../../emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.md "../../../emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.md") APIs:

| Classifications            | Descriptions                                                                                |
| -------------------------- | ------------------------------------------------------------------------------------------- |
| `jeg-config`               | Change values in Jupyter Enterprise Gateway<br>`jupyter_enterprise_gateway_config.py` file. |
| `jupyter-kernel-overrides` | Change value for the Kernel Image in Jupyter Kernel Spec file.                              |

Configuration classifications allow you to customize applications. These often correspond
to a configuration XML file for the application, such as `spark-hive-site.xml`. For
more information, see [Configure
Applications](../ReleaseGuide/emr-configure-apps.md "../ReleaseGuide/emr-configure-apps.md").
**Notable features**

- **Nvidia RAPIDS Accelerator for Apache Spark** ‐
  Amazon EMR on EKS to accelerate Spark using EC2 graphics processing unit (GPU) instance types. To use
  the Spark image with RAPIDS Accelerator, specify release label as
  emr-6.9.0-spark-rapids-latest. Visit the [documentation
  page](tutorial-spark-rapids.md "tutorial-spark-rapids.md") to learn more.
- **Spark-Redshift connector** ‐
  The Amazon Redshift integration for Apache Spark is included in Amazon EMR releases 6.9.0 and later. Previously an open-source tool, the native integration is a Spark connector that you can use to build Apache Spark applications that read from and write to data in Amazon Redshift and Amazon Redshift Serverless. For more information, see [Using Amazon Redshift integration for Apache Spark on Amazon EMR on EKS](emr-spark-redshift.md "emr-spark-redshift.md").
- **Delta Lake** ‐ [Delta
  Lake](https://delta.io/ "https://delta.io/") is an open-source storage format that enables building data lakes with
  transactional consistency, consistent definition of datasets, schema evolution changes, and
  data mutations support. Visit [Using Delta Lake](tutorial-delta-lake.md "tutorial-delta-lake.md") to
  learn more.
- **Modify PySpark parameters** ‐ Interactive endpoints
  now support modifying Spark parameters associated with PySpark sessions in the EMR Studio
  Jupyter Notebook. Visit [Modifying PySpark session
  parameters](modify-pyspark-parameters.md "modify-pyspark-parameters.md") to learn more.
  **Resolved issues**

- When you use the DynamoDB connector with Spark on Amazon EMR versions 6.6.0, 6.7.0, and 6.8.0, all reads from your table
  return an empty result, even though the input split references non-empty data. Amazon EMR release 6.9.0 fixes this issue.
- Amazon EMR on EKS 6.8.0 incorrectly populates the build hash in Parquet files metadata generated
  using [Apache Spark](https://aws.amazon.com//emr/features/spark "https://aws.amazon.com//emr/features/spark"). This issue may
  cause tools that parse the metadata version string from Parquet files generated by Amazon EMR on EKS
  6.8.0 to fail.
  **Known issue**

- If you use the Amazon Redshift integration for Apache Spark and have a time, timetz, timestamp, or timestamptz with microsecond precision in Parquet format, the connector rounds the time values to the nearest millisecond value. As a workaround, use the text unload format `unload_s3_format` parameter.
