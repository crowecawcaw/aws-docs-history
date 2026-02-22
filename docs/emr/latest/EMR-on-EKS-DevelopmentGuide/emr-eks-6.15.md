# Amazon EMR on EKS 6.15.0 releases

This page describes the new and updated functionality for Amazon EMR that is specific to the
Amazon EMR on EKS deployment. For details about Amazon EMR running on Amazon EC2 and about the Amazon EMR 6.15.0 release
in general, see [Amazon EMR 6.15.0](../ReleaseGuide/emr-6115-release.md "../ReleaseGuide/emr-6115-release.md") in the _Amazon EMR Release Guide_.

## Amazon EMR on EKS 6.15 releases

The following Amazon EMR 6.15.0 releases are available for Amazon EMR on EKS. Select a specific
**emr-6.15.0-XXXX** release to view more details such as the
related container image tag.

Flink releases
The following Amazon EMR 6.15.0 releases are available for Amazon EMR on EKS when you run Flink
applications.

- [emr-6.15.0-flink-latest](emr-eks-6.15.md "emr-eks-6.15.md")
- [emr-6.15.0-flink-20240105](emr-eks-6.15.md "emr-eks-6.15.md")
- [emr-6.15.0-flink-20231109](emr-eks-6.15.md "emr-eks-6.15.md")

Spark releases
The following Amazon EMR 6.15.0 releases are available for Amazon EMR on EKS when you run Spark
applications.

- [emr-6.15.0-latest](emr-eks-6.15.md "emr-eks-6.15.md")
- [emr-6.15.0-20231109](emr-eks-6.15.md "emr-eks-6.15.md")
- emr-6.15.0-spark-rapids-latest
- emr-6.15.0-spark-rapids-20231109
- emr-6.15.0-java11-latest
- emr-6.15.0-java11-20231109
- emr-6.15.0-java17-latest
- emr-6.15.0-java17-20231109
- emr-6.15.0-java17-al2023-latest
- emr-6.15.0-java17-al2023-20231109
- emr-6.15.0-spark-rapids-java17-latest
- emr-6.15.0-spark-rapids-java17-20231109
- emr-6.15.0-spark-rapids-java17-al2023-latest
- emr-6.15.0-spark-rapids-java17-al2023-20231109
- notebook-spark/emr-6.15.0-latest
- notebook-spark/emr-6.15.0-20231109
- notebook-spark/emr-6.15.0-spark-rapids-latest
- notebook-spark/emr-6.15.0-spark-rapids-20231109
- notebook-spark/emr-6.15.0-java11-latest
- notebook-spark/emr-6.15.0-java11-20231109
- notebook-spark/emr-6.15.0-java17-latest
- notebook-spark/emr-6.15.0-java17-20231109
- notebook-spark/emr-6.15.0-java17-al2023-latest
- notebook-spark/emr-6.15.0-java17-al2023-20231109
- notebook-python/emr-6.15.0-latest
- notebook-python/emr-6.15.0-20231109
- notebook-python/emr-6.15.0-spark-rapids-latest
- notebook-python/emr-6.15.0-spark-rapids-20231109
- notebook-python/emr-6.15.0-java11-latest
- notebook-python/emr-6.15.0-java11-20231109
- notebook-python/emr-6.15.0-java17-latest
- notebook-python/emr-6.15.0-java17-20231109
- notebook-python/emr-6.15.0-java17-al2023-latest
- notebook-python/emr-6.15.0-java17-al2023-20231109

## Release notes

Release notes for Amazon EMR on EKS 6.15.0

- **Supported applications** ‐ AWS SDK for Java
  1.12.569, Apache Spark 3.4.1-amzn-2, Apache Flink 1.17.1-amzn-1, Apache Hudi 0.14.0-amzn-0, Apache Iceberg 1.4.0-amzn-0,
  Delta 2.4.0, Apache Spark RAPIDS 23.08.01-amzn-0, Jupyter Enterprise Gateway 2.6.0
- **Supported components** ‐
  `aws-sagemaker-spark-sdk`, `emr-ddb`, `emr-goodies`,
  `emr-s3-select`, `emrfs`, `hadoop-client`,
  `hudi`, `hudi-spark`, `iceberg`,
  `spark-kubernetes`.
- **Supported configuration classifications**

For use with [StartJobRun](../../../emr-on-eks/latest/APIReference/API_StartJobRun.md "../../../emr-on-eks/latest/APIReference/API_StartJobRun.md") and [CreateManagedEndpoint](../../../emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.md "../../../emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.md") APIs:

| Classifications     | Descriptions                                                                                   |
| ------------------- | ---------------------------------------------------------------------------------------------- |
| `core-site`         | Change values in the `core-site.xml` Hadoop file.                                              |
| `emrfs-site`        | Change EMRFS settings.                                                                         |
| `spark-metrics`     | Change values in the `metrics.properties` Spark file.                                          |
| `spark-defaults`    | Change values in the `spark-defaults.conf` Spark file.                                         |
| `spark-env`         | Change values in the Spark environment.                                                        |
| `spark-hive-site`   | Change values in the `hive-site.xml` Spark file.                                               |
| `spark-log4j`       | Change values in the `log4j2.properties` Spark file.                                           |
| `emr-job-submitter` | Configuration for [job submitter<br>pod](emr-eks-job-submitter.md "emr-eks-job-submitter.md"). |

For use specifically with [CreateManagedEndpoint](../../../emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.md "../../../emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.md") APIs:

| Classifications            | Descriptions                                                                                |
| -------------------------- | ------------------------------------------------------------------------------------------- |
| `jeg-config`               | Change values in Jupyter Enterprise Gateway<br>`jupyter_enterprise_gateway_config.py` file. |
| `jupyter-kernel-overrides` | Change value for the Kernel Image in Jupyter Kernel Spec file.                              |

Configuration classifications allow you to customize applications. These often correspond
to a configuration XML file for the application, such as `spark-hive-site.xml`. For
more information, see [Configure
Applications](../ReleaseGuide/emr-configure-apps.md "../ReleaseGuide/emr-configure-apps.md").

## Notable features

The following features are included with the 6.15 release of Amazon EMR on EKS.

- [Amazon EMR on EKS with Apache
  Flink](run-flink-jobs.md "run-flink-jobs.md") - With Amazon EMR on EKS 6.15.0, you can run your Apache Flink-based
  application along with other types of applications on the same Amazon EKS cluster. This helps
  improve resource utilization and simplify infrastructure management. You can leverage Spot
  Instances in a Flink application with graceful decommission, and achieve faster restart times
  with fine-grained recovery and task-local recovery with Amazon EBS. Accessibility and monitoring
  features include the ability to launch a Flink application with jars that are stored in Amazon S3,
  access to the AWS Glue Data Catalog, monitoring integration with Amazon S3 and Amazon CloudWatch, and container log
  rotation.
