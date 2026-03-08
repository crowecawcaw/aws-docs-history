# Amazon EMR on EKS 5.33.0 releases

The following Amazon EMR 5.33.0 releases are available for Amazon EMR on EKS. Select a specific **emr-5.33.0-XXXX** release to view more details such as the related
container image tag.

- [emr-5.33.0-latest](emr-eks-5.33.md "emr-eks-5.33.md")
- [emr-5.33.0-20240321](emr-eks-5.33.md "emr-eks-5.33.md")
- [emr-5.33.0-20221219](emr-eks-5.33.md "emr-eks-5.33.md")
- [emr-5.33.0-20220802](emr-eks-5.33.md "emr-eks-5.33.md")
- [emr-5.33.0-20211008](emr-eks-5.33.md "emr-eks-5.33.md")
- [emr-5.33.0-20210802](emr-eks-5.33.md "emr-eks-5.33.md")
- [emr-5.33.0-20210615](emr-eks-5.33.md "emr-eks-5.33.md")
- [emr-5.33.0-20210323](emr-eks-5.33.md "emr-eks-5.33.md")
  **Release notes for Amazon EMR 5.33.0**

- New feature ‐ Beginning with Amazon EMR 5.33.0 in the 5.x release series, Amazon EMR on EKS
  supports Spark’s pod template feature. For more information, see [Using pod templates](pod-templates.md "pod-templates.md").
- Supported applications ‐ Spark 2.4.7-amzn-1, Jupyter Enterprise Gateway (endpoints,
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
