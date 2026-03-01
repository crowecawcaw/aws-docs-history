# Amazon EMR on EKS 6.8.0 releases

The following Amazon EMR 6.8.0 releases are available for Amazon EMR on EKS. Select a specific **emr-6.8.0-XXXX** release to view more details such as the related container
image tag.

- [emr-6.8.0-latest](emr-eks-6.8.md "emr-eks-6.8.md")
- [emr-6.8.0-20230905](emr-eks-6.8.md "emr-eks-6.8.md")
- [emr-6.8.0-20230624](emr-eks-6.8.md "emr-eks-6.8.md")
- [emr-6.8.0-20221219](emr-eks-6.8.md "emr-eks-6.8.md")
- [emr-6.8.0-20220802](emr-eks-6.8.md "emr-eks-6.8.md")
  **Release notes for Amazon EMR 6.8.0**

- Supported applications ‐ AWS SDK for Java 1.12.170, Spark 3.3.0-amzn-0, Hudi 0.11.1-amzn-0,
  Iceberg 0.14.0-amzn-0.
- Supported components ‐ `aws-sagemaker-spark-sdk`, `emr-ddb`,
  `emr-goodies`, `emr-s3-select`, `emrfs`,
  `hadoop-client`, `hudi`, `hudi-spark`, `iceberg`,
  `spark-kubernetes`.
- Supported configuration classifications:

| Classifications   | Descriptions                                       |
| ----------------- | -------------------------------------------------- |
| `core-site`       | Change values in Hadoop’s core-site.xml file.      |
| `emrfs-site`      | Change EMRFS settings.                             |
| `spark-metrics`   | Change values in Spark's metrics.properties file.  |
| `spark-defaults`  | Change values in Spark's spark-defaults.conf file. |
| `spark-env`       | Change values in the Spark environment.            |
| `spark-hive-site` | Change values in Spark's hive-site.xml file.       |
| `spark-log4j`     | Change values in Spark's log4j.properties file.    |

Configuration classifications allow you to customize applications. These often correspond
to a configuration XML file for the application, such as `spark-hive-site.xml`. For
more information, see [Configure
Applications](../ReleaseGuide/emr-configure-apps.md "../ReleaseGuide/emr-configure-apps.md").
**Notable features**

- **Spark3.3.0** ‐ Amazon EMR on EKS 6.8 includes Spark 3.3.0,
  which supports using separate node selector labels for Spark driver executor pods. These new
  labels enable you to define the node types for the driver and executor pods separately in the
  StartJobRun API, without using pod templates.
  - Driver node selector property: spark.kubernetes.driver.node.selector.[labelKey]
  - Executor node selector property:
    spark.kubernetes.executor.node.selector.[labelKey]

- **Enhanced job failure message** ‐ This release
  introduces the configuration `spark.stage.extraDetailsOnFetchFailures.enabled` and
  `spark.stage.extraDetailsOnFetchFailures.maxFailuresToInclude` to track task
  failures due to user code. These details will be used to enhance the failure message displayed
  in the driver log when a stage is aborted due to shuffle fetch failure.

| Property name                                                  | Default value | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Since version |
| -------------------------------------------------------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `spark.stage.extraDetailsOnFetchFailures.enabled`              | false         | If set to `true`, this property is used to enhance the job failure message<br>displayed in the driver log when a stage is aborted due to Shuffle Fetch Failures. By<br>default the last 5 task failures caused by user code is tracked, and the failure error<br>message is appended in the Driver Logs.<br>To increase the number of task failures with user exceptions to track, see the<br>config `spark.stage.extraDetailsOnFetchFailures.maxFailuresToInclude`. | emr-6.8       |
| `spark.stage.extraDetailsOnFetchFailures.maxFailuresToInclude` | 5             | Number of task failures to track per stage and attempt. This property is used to<br>enhance the job failure message with user exceptions displayed in the driver log when a<br>stage is aborted due to Shuffle Fetch Failures.<br>This property works only if Config spark.stage.extraDetailsOnFetchFailures.enabled is<br>set to true.                                                                                                                              | emr-6.8       |

For more information see the [Apache Spark
configuration documentation](https://spark.apache.org/docs/latest/running-on-kubernetes.html#configuration "https://spark.apache.org/docs/latest/running-on-kubernetes.html#configuration").

**Known issue**

- Amazon EMR on EKS 6.8.0 incorrectly populates the build hash in Parquet files metadata generated
  using [Apache Spark](https://aws.amazon.com/emr/features/spark/ "https://aws.amazon.com/emr/features/spark/"). This issue
  may cause tools that parse the metadata version string from Parquet files generated by
  Amazon EMR on EKS 6.8.0 to fail. Customers who parse the version string from Parquet metadata and
  depend on build hash should switch to a different Amazon EMR version and rewrite the file.
  **Resolved issue**

- **Interrupt Kernel capability for pySpark kernels** ‐ In
  progress interactive workloads that are triggered by executing cells in a notebook can be
  stopped by using the `Interrupt Kernel` capability. A fix has been introduced so
  that this functionality works for pySpark kernels. This is also available in open source at
  [Changes for
  handling interrupts for PySpark Kubernetes Kernel #1115](https://github.com/jupyter-server/enterprise_gateway/pull/1115 "https://github.com/jupyter-server/enterprise_gateway/pull/1115").
