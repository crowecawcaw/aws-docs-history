# Amazon EMR on EKS 7.2.0 releases

This page describes the new and updated functionality for Amazon EMR that is specific to the
Amazon EMR on EKS deployment. For details about Amazon EMR running on Amazon EC2 and about the Amazon EMR 7.2.0 release
in general, see [Amazon EMR 7.2.0](../ReleaseGuide/emr-720-release.md "../ReleaseGuide/emr-720-release.md") in the _Amazon EMR Release Guide_.

## Amazon EMR on EKS 7.2 releases

The following Amazon EMR 7.2.0 releases are available for Amazon EMR on EKS. Select a specific **emr-7.2.0-XXXX** release to view more details such as the related
container image tag.

Flink releases
The following Amazon EMR 7.2.0 releases are available for Amazon EMR on EKS when you run Flink
applications.

- [emr-7.2.0-flink-latest](emr-eks-7.2.md "emr-eks-7.2.md")
- [emr-7.2.0-flink-20240610](emr-eks-7.2.md "emr-eks-7.2.md")

Spark releases
The following Amazon EMR 7.2.0 releases are available for Amazon EMR on EKS when you run Spark
applications.

- [emr-7.2.0-latest](emr-eks-7.2.md "emr-eks-7.2.md")
- [emr-7.2.0-20240610](emr-eks-7.2.md "emr-eks-7.2.md")
- emr-7.2.0-spark-rapids-latest
- emr-7.2.0-spark-rapids-20240610
- emr-7.2.0-java11-latest
- emr-7.2.0-java11-20240610
- emr-7.2.0-java8-latest
- emr-7.2.0-java8-20240610
- emr-7.2.0-spark-rapids-java8-latest
- emr-7.2.0-spark-rapids-java8-20240610
- notebook-spark/emr-7.2.0-latest
- notebook-spark/emr-7.2.0-20240610
- notebook-spark/emr-7.2.0-spark-rapids-latest
- notebook-spark/emr-7.2.0-spark-rapids-20240610
- notebook-spark/emr-7.2.0-java11-latest
- notebook-spark/emr-7.2.0-java11-20240610
- notebook-spark/emr-7.2.0-java8-latest
- notebook-spark/emr-7.2.0-java8-20240610
- notebook-spark/emr-7.2.0-spark-rapids-java8-latest
- notebook-spark/emr-7.2.0-spark-rapids-java8-20240610
- notebook-python/emr-7.2.0-latest
- notebook-python/emr-7.2.0-20240610
- notebook-python/emr-7.2.0-spark-rapids-latest
- notebook-python/emr-7.2.0-spark-rapids-20240610
- notebook-python/emr-7.2.0-java11-latest
- notebook-python/emr-7.2.0-java11-20240610
- notebook-python/emr-7.2.0-java8-latest
- notebook-python/emr-7.2.0-java8-20240610
- notebook-python/emr-7.2.0-spark-rapids-java8-latest
- notebook-python/emr-7.2.0-spark-rapids-java8-20240610
- livy/emr-7.2.0-latest
- livy/emr-7.2.0-20240610
- livy/emr-7.2.0-java11-latest
- livy/emr-7.2.0-java11-20240610
- livy/emr-7.2.0-java8-latest
- livy/emr-7.2.0-java8-20240610

## Release notes

Release notes for Amazon EMR on EKS 7.2.0

- **Supported applications** ‐ AWS SDK for Java
  2.23.18 and 1.12.705, Apache Spark 3.5.1-amzn-1, Apache Hudi 0.14.1-amzn-0,
  Apache Iceberg 1.5.0-amzn-0, Delta 3.1.0, Apache Spark RAPIDS 24.02.0-amzn-1,
  Jupyter Enterprise Gateway 2.6.0, Apache Flink 1.18.1-amzn-0, Flink Operator 1.8.0-amzn-1
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
| `spark-log4j2`      | Change values in the `log4j2.properties` Spark file.                                           |
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

The following features are included with the 7.2.0 release of Amazon EMR on EKS.

- Application upgrades – Amazon EMR on EKS 7.2.0 application upgrades include Spark 3.5.1,
  Flink 1.18.1, and [Flink Operator](jobruns-flink-kubernetes-operator.md "jobruns-flink-kubernetes-operator.md") 1.8.0.
- [Autoscaler for Flink updates](jobruns-flink-autoscaler.md "jobruns-flink-autoscaler.md") – The 7.2.0 release uses the open source configuration
  `job.autoscaler.restart.time-tracking.enabled` to enable rescale time estimation, so you no longer
  have to manually assign empirical values to restart time. If you run 7.1.0 or lower, you can still use Amazon EMR autoscaling.
- [Apache Hudi integration Apache Flink on Amazon EMR on EKS](tutorial-hudi-for-flink.md "tutorial-hudi-for-flink.md") – This release adds an integration
  between Apache Hudi and Apache Flink, so you can use the Flink Kubernetes operator to run Hudi jobs. Hudi lets you
  use record-level operations that you can use to simplify data management and data pipeline development.
- [Amazon S3 Express One Zone integration with Amazon EMR on EKS](upload-data-s3-express.md "upload-data-s3-express.md") – With 7.2.0 and higher, you can upload
  data into the S3 Express One Zone with Amazon EMR on EKS. S3 Express One Zone is a a high-performance, single-zone Amazon S3
  storage class that delivers consistent, single-digit millisecond data access for most latency-sensitive applications.
  At the time of its release, S3 Express One Zone delivers the lowest latency and highest performance cloud object storage in Amazon S3.
- [Support for default configurations in the Spark operator](spark-operator-gs.md "spark-operator-gs.md") – Spark operator on Amazon EKS now supports the same default
  configurations as the start job run model on Amazon EMR on EKS for 7.2.0 and higher. This means that features such as
  Amazon S3 and EMRFS no longer require manual configurations in the yaml file.
