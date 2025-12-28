# Amazon EMR on EKS 7.0.0 releases

This page describes the new and updated functionality for Amazon EMR that is specific to the
Amazon EMR on EKS deployment. For details about Amazon EMR running on Amazon EC2 and about the Amazon EMR 7.0.0 release
in general, see [Amazon EMR 7.0.0](../ReleaseGuide/emr-700-release.md "../ReleaseGuide/emr-700-release.md") in the _Amazon EMR Release Guide_.

## Amazon EMR on EKS 7.0 releases

The following Amazon EMR 7.0.0 releases are available for Amazon EMR on EKS. Select a specific **emr-7.0.0-XXXX** release to view more details such as the related
container image tag.

Flink releases
The following Amazon EMR 7.0.0 releases are available for Amazon EMR on EKS when you run Flink
applications.

- [emr-7.0.0-flink-latest](emr-eks-7.0.md "emr-eks-7.0.md")
- [emr-7.0.0-flink-2024321](emr-eks-7.0.md "emr-eks-7.0.md")
- [emr-7.0.0-flink-20231211](emr-eks-7.0.md "emr-eks-7.0.md")

Spark releases
The following Amazon EMR 7.0.0 releases are available for Amazon EMR on EKS when you run Spark
applications.

- [emr-7.0.0-latest](emr-eks-7.0.md "emr-eks-7.0.md")
- [emr-7.0.0-20231211](emr-eks-7.0.md "emr-eks-7.0.md")
- emr-7.0.0-spark-rapids-latest
- emr-7.0.0-spark-rapids-20231211
- emr-7.0.0-java11-latest
- emr-7.0.0-java11-20231211
- emr-7.0.0-java8-latest
- emr-7.0.0-java8-20231211
- emr-7.0.0-spark-rapids-java8-latest
- emr-7.0.0-spark-rapids-java8-20231211
- notebook-spark/emr-7.0.0-latest
- notebook-spark/emr-7.0.0-20231211
- notebook-spark/emr-7.0.0-spark-rapids-latest
- notebook-spark/emr-7.0.0-spark-rapids-20231211
- notebook-spark/emr-7.0.0-java11-latest
- notebook-spark/emr-7.0.0-java11-20231211
- notebook-spark/emr-7.0.0-java8-latest
- notebook-spark/emr-7.0.0-java8-20231211
- notebook-spark/emr-7.0.0-spark-rapids-java8-latest
- notebook-spark/emr-7.0.0-spark-rapids-java8-20231211
- notebook-python/emr-7.0.0-latest
- notebook-python/emr-7.0.0-20231211
- notebook-python/emr-7.0.0-spark-rapids-latest
- notebook-python/emr-7.0.0-spark-rapids-20231211
- notebook-python/emr-7.0.0-java11-latest
- notebook-python/emr-7.0.0-java11-20231211
- notebook-python/emr-7.0.0-java8-latest
- notebook-python/emr-7.0.0-java8-20231211
- notebook-python/emr-7.0.0-spark-rapids-java8-latest
- notebook-python/emr-7.0.0-spark-rapids-java8-20231211

## Release notes

Release notes for Amazon EMR on EKS 7.0.0

- **Supported applications** ‐ AWS SDK for Java
  2.20.160-amzn-0 and 1.12.595, Apache Spark 3.5.0-amzn-0, Apache Flink 1.18.0-amzn-0,
  Flink Operator 1.6.1, Apache Hudi 0.14.0-amzn-1, Apache
  Iceberg 1.4.2-amzn-0, Delta 3.0.0, Apache Spark RAPIDS 23.10.0-amzn-0, Jupyter Enterprise
  Gateway 2.6.0
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

The following features are included with the 7.0 release of Amazon EMR on EKS.

- Application upgrades – Amazon EMR on EKS 7.0.0 application
  upgrades include Spark 3.5, Flink 1.18, and [Flink Operator](jobruns-flink-kubernetes-operator.md "jobruns-flink-kubernetes-operator.md") 1.6.1.
- Flink Autoscaler parameter auto-tuning – The
  default parameters that Flink Autoscaler uses for its scaling calculations might not be the
  optimal value for a given job. Amazon EMR on EKS 7.0.0 uses historical trends of specific captured
  metrics to calculate the optimal parameter tailored for the job.

## Changes

The following changes are included with the 7.0 release of Amazon EMR on EKS.

- Amazon Linux 2023 – With Amazon EMR on EKS 7.0.0 and higher, all
  container images are based on Amazon Linux 2023.
- Spark uses Java 17 as default runtime – Amazon EMR on EKS
  7.0.0 Spark uses Java 17 as default runtime. If you need to, you can switch to use Java 8 or
  Java 11 with the corresponding release label as provided in the [Amazon EMR on EKS 7.0 releases](#emr-eks-7.0.0-releases "#emr-eks-7.0.0-releases") list.
