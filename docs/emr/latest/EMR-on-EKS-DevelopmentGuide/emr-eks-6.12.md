# Amazon EMR on EKS 6.12.0 releases

This page describes the new and updated functionality for Amazon EMR that is specific to the
Amazon EMR on EKS deployment. For details about Amazon EMR running on Amazon EC2 and about the Amazon EMR 6.12.0 release
in general, see [Amazon EMR 6.12.0](../ReleaseGuide/emr-6120-release.md "../ReleaseGuide/emr-6120-release.md") in the _Amazon EMR Release Guide_.

## Amazon EMR on EKS 6.12 releases

The following Amazon EMR 6.12.0 releases are available for Amazon EMR on EKS. Select a specific
**emr-6.12.0-XXXX** release to view more details such as the
related container image tag.

- [emr-6.12.0-latest](emr-eks-6.12.md "emr-eks-6.12.md")
- [emr-6.12.0-20240321](emr-eks-6.12.md "emr-eks-6.12.md")
- [emr-6.12.0-20230701](emr-eks-6.12.md "emr-eks-6.12.md")
- emr-6.12.0-spark-rapids-latest
- emr-6.12.0-spark-rapids-20230701
- emr-6.12.0-java11-latest
- emr-6.12.0-java11-20230701
- emr-6.12.0-java17-latest
- emr-6.12.0-java17-20230701
- emr-6.12.0-spark-rapids-java17-latest
- emr-6.12.0-spark-rapids-java17-20230701
- notebook-spark/emr-6.12.0-latest
- notebook-spark/emr-6.12.0-20230701
- notebook-spark/emr-6.12.0-spark-rapids-latest
- notebook-spark/emr-6.12.0-spark-rapids-20230701
- notebook-python/emr-6.12.0-latest
- notebook-python/emr-6.12.0-20230701
- notebook-python/emr-6.12.0-spark-rapids-latest
- notebook-python/emr-6.12.0-spark-rapids-20230701

## Release notes

Release notes for Amazon EMR on EKS 6.12.0

- **Supported applications** ‐ AWS SDK for Java 1.12.490,
  Apache Spark 3.4.0-amzn-0, Apache Hudi 0.13.1-amzn-0, Apache Iceberg 1.3.0-amzn-0, Delta
  2.4.0, Apache Spark RAPIDS 23.06.0-amzn-0, Jupyter Enterprise Gateway 2.6.0
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

The following features are included with the 6.12 release of Amazon EMR on EKS.

- **Java 17** - With Amazon EMR on EKS 6.12 and higher, you can launch
  Spark with Java 17 runtime. To do this, pass `emr-6.12.0-java17-latest` as a
  release label. We recommend that you validate and run performance tests before you move your
  production workloads from earlier versions of the Java image to the Java 17 image.
