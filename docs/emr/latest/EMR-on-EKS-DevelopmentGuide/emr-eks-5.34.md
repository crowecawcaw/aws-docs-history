# Amazon EMR on EKS 5.34.0 releases

The following Amazon EMR 5.34.0 releases are available for Amazon EMR on EKS. Select a specific **emr-5.34.0-XXXX** release to view more details such as the related
container image tag.

- [emr-5.34.0-latest](emr-eks-5.34.md "emr-eks-5.34.md")
- [emr-5.34.0-20240321](emr-eks-5.34.md "emr-eks-5.34.md")
- [emr-5.34.0-20220802](emr-eks-5.34.md "emr-eks-5.34.md")
  **Release notes for Amazon EMR 5.34.0**

- Supported applications ‐ Spark 2.4.8-amzn-0, Jupyter Enterprise Gateway (endpoints,
  public preview; Scala kernel is not supported).
- Supported components ‐ `aws-hm-client` (Glue connector),
  `aws-sagemaker-spark-sdk`, `emr-s3-select`, `emrfs`,
  `emr-ddb`, `hudi-spark`.
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
to a configuration XML file for the application, such as spark-hive-site.xml. For more
information, see [Configuring
Applications](../ReleaseGuide/emr-configure-apps.md "../ReleaseGuide/emr-configure-apps.md").
