# AWS runtime for Apache Spark (emr-spark-8.0.0) on EKS

This page describes the new and updated functionality for Amazon EMR that is specific to the
Amazon EMR on EKS deployment. For details about Amazon EMR running on Amazon EC2 and about the Amazon EMR Spark 8.0.0 release
in general, see [AWS runtime for Apache Spark (emr-spark-8.0.0)](../ReleaseGuide/emr-spark800-release.md "../ReleaseGuide/emr-spark800-release.md") in the _Amazon EMR Release Guide_.

## AWS runtime for Apache Spark (emr-spark-8.0.0) on EKS

The following emr-spark-8.0.0 releases are available for AWS runtime for Apache Spark on EKS.

- spark/emr-spark-8.0.0-latest
- spark/emr-spark-8.0.0-20260421
- notebook-spark/emr-spark-8.0.0-latest
- notebook-spark/emr-spark-8.0.0-20260421
- notebook-python/emr-spark-8.0.0-latest
- notebook-python/emr-spark-8.0.0-20260421
- livy/emr-spark-8.0.0-latest
- livy/emr-spark-8.0.0-20260421

## Release notes

Release notes for AWS runtime for Apache Spark (emr-spark-8.0.0) on EKS:

- **Supported applications** ‐ AWS SDK for Java
  2.41.32, Apache Spark 4.0.2-amzn-0, Apache Hudi 1.1.0-amzn-0,
  Apache Iceberg 1.10.1-amzn-0, Delta Lake 4.0.0-amzn-1-spark
- **Supported components** ‐
  `emr-ddb`, `emr-goodies`,
  `hadoop-client`,
  `hudi`, `hudi-spark`, `iceberg`,
  `spark-kubernetes`.
- **Supported configuration classifications**

For use with [StartJobRun](../../../emr-on-eks/latest/APIReference/API_StartJobRun.md "../../../emr-on-eks/latest/APIReference/API_StartJobRun.md") and [CreateManagedEndpoint](../../../emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.md "../../../emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.md") APIs:

| Classifications     | Descriptions                                                                                |
| ------------------- | ------------------------------------------------------------------------------------------- |
| `core-site`         | Change values in the `core-site.xml` Hadoop file.                                           |
| `spark-metrics`     | Change values in the `metrics.properties` Spark file.                                       |
| `spark-defaults`    | Change values in the `spark-defaults.conf` Spark file.                                      |
| `spark-env`         | Change values in the Spark environment.                                                     |
| `spark-hive-site`   | Change values in the `hive-site.xml` Spark file.                                            |
| `spark-log4j2`      | Change values in the `log4j2.properties` Spark file.                                        |
| `emr-job-submitter` | Configuration for [job submitter pod](emr-eks-job-submitter.md "emr-eks-job-submitter.md"). |

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

The following features are included with the emr-spark-8.0.0 release of AWS runtime for Apache Spark on EKS:

- **Apache Spark 4.0.2 GA** – First production-ready release of Spark 4.x on Amazon EMR on EKS, featuring ANSI SQL mode, SQL PIPE syntax, VARIANT data type, SQL scripting, and streaming enhancements.
- **Python 3.11 default** – Python 3.11 is the default for PySpark and Spark workloads. Python 3.12 and 3.13 are also available.
