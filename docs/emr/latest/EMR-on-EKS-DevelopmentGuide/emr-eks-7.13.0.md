# Amazon EMR on EKS 7.13.0 releases

This page describes the new and updated functionality for Amazon EMR that is specific to the
Amazon EMR on EKS deployment. For details about Amazon EMR running on Amazon EC2 and about the Amazon EMR 7.13.0 release
in general, see [Amazon EMR 7.13.0](../ReleaseGuide/emr-7130-release.md "../ReleaseGuide/emr-7130-release.md") in the _Amazon EMR Release Guide_.

## Amazon EMR on EKS 7.13 releases

The following Amazon EMR 7.13.0 releases are available for Amazon EMR on EKS. Select a specific **emr-7.13.0-XXXX** release to view more details such as the related
container image tag.

Flink releases
The following Amazon EMR 7.13.0 releases are available for Amazon EMR on EKS when you run Flink
applications.

- [emr-7.13.0-flink-latest](emr-eks-7.13.0-flink-latest.md "emr-eks-7.13.0-flink-latest.md")
- [emr-7.13.0-flink-20260410](emr-eks-7.13.0-flink-20260410.md "emr-eks-7.13.0-flink-20260410.md")

Spark releases
The following Amazon EMR 7.13.0 releases are available for Amazon EMR on EKS when you run Spark
applications.

- [emr-7.13.0-latest](emr-eks-7.13.0-latest.md "emr-eks-7.13.0-latest.md")
- [emr-7.13.0-20260410](emr-eks-7.13.0-20260410.md "emr-eks-7.13.0-20260410.md")
- emr-7.13.0-spark-rapids-latest
- emr-7.13.0-spark-rapids-20260410
- emr-7.13.0-java11-latest
- emr-7.13.0-java11-20260410
- emr-7.13.0-java8-latest
- emr-7.13.0-java8-20260410
- emr-7.13.0-spark-rapids-java8-latest
- emr-7.13.0-spark-rapids-java8-20260410
- notebook-spark/emr-7.13.0-latest
- notebook-spark/emr-7.13.0-20260410
- notebook-spark/emr-7.13.0-spark-rapids-latest
- notebook-spark/emr-7.13.0-spark-rapids-20260410
- notebook-spark/emr-7.13.0-java11-latest
- notebook-spark/emr-7.13.0-java11-20260410
- notebook-spark/emr-7.13.0-java8-latest
- notebook-spark/emr-7.13.0-java8-20260410
- notebook-spark/emr-7.13.0-spark-rapids-java8-latest
- notebook-spark/emr-7.13.0-spark-rapids-java8-20260410
- notebook-python/emr-7.13.0-latest
- notebook-python/emr-7.13.0-20260410
- notebook-python/emr-7.13.0-spark-rapids-latest
- notebook-python/emr-7.13.0-spark-rapids-20260410
- notebook-python/emr-7.13.0-java11-latest
- notebook-python/emr-7.13.0-java11-20260410
- notebook-python/emr-7.13.0-java8-latest
- notebook-python/emr-7.13.0-java8-20260410
- notebook-python/emr-7.13.0-spark-rapids-java8-latest
- notebook-python/emr-7.13.0-spark-rapids-java8-20260410
- livy/emr-7.13.0-latest
- livy/emr-7.13.0-20260410
- livy/emr-7.13.0-java11-latest
- livy/emr-7.13.0-java11-20260410
- livy/emr-7.13.0-java8-latest
- livy/emr-7.13.0-java8-20260410

## Release notes

Release notes for Amazon EMR on EKS 7.13.0:

- **Supported applications** ‐ AWS SDK for Java
  2.42.12 and 1.12.797, Apache Spark 3.5.6-amzn-2, Apache Hudi 1.0.2-amzn-2,
  Apache Iceberg 1.10.0-amzn-1, Delta 3.3.2-amzn-2, Apache Spark RAPIDS 25.04.0-amzn-0,
  Apache Flink 1.20.0-amzn-7
- **Supported components** ‐
  `emr-ddb`, `emr-goodies`,
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

## Changes and features

The following features are included with the 7.13.0 release of Amazon EMR on EKS:

- **Python 3.11 default for PySpark and Spark workloads** – Python 3.11 is now the default Python version for PySpark and Spark workloads. Python 3.9 remains the default for all other applications. Both Python 3.9 and 3.11 are included in the release.
