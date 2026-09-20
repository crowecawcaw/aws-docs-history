

# AWS runtime for Apache Spark (emr-spark-8.0.0) on EKS
<a name="emr-eks-spark-8.0.0"></a>

This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment. For details about Amazon EMR running on Amazon EC2 and about the Amazon EMR Spark 8.0.0 release in general, see [AWS runtime for Apache Spark (emr-spark-8.0.0)](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark800-release.html) in the *Amazon EMR Release Guide*.

## AWS runtime for Apache Spark (emr-spark-8.0.0) on EKS
<a name="emr-eks-spark-8.0.0-releases"></a>

The following emr-spark-8.0.0 releases are available for AWS runtime for Apache Spark on EKS. Select a specific **emr-spark-8.0.0-XXXX** release to view more details such as the related container image tag.

------
#### [ Spark releases ]

The following emr-spark-8.0.0 releases are available for AWS runtime for Apache Spark on EKS when you run Spark applications. Select a `spark/` release to view details such as the release label and container image tag. The `notebook-spark/`, `notebook-python/`, and `livy/` variants use the same release label format (for example, `emr-spark-8.0.0-latest`) with the corresponding container image prefix.
+ [emr-spark-8.0.0-latest](emr-eks-spark-8.0.0-latest.md)
+ [emr-spark-8.0.0-20260421](emr-eks-spark-8.0.0-20260421.md)
+ notebook-spark/emr-spark-8.0.0-latest
+ notebook-spark/emr-spark-8.0.0-20260421
+ notebook-python/emr-spark-8.0.0-latest
+ notebook-python/emr-spark-8.0.0-20260421
+ livy/emr-spark-8.0.0-latest
+ livy/emr-spark-8.0.0-20260421

------

## Release notes
<a name="emr-eks-spark-8.0.0-rn"></a>

Release notes for AWS runtime for Apache Spark (emr-spark-8.0.0) on EKS:
+ **Supported applications** ‐ AWS SDK for Java 2.41.32, Apache Spark 4.0.2-amzn-0, Apache Hudi 1.1.0-amzn-0, Apache Iceberg 1.10.1-amzn-0, Delta Lake 4.0.0-amzn-1-spark
+ **Supported components** ‐ `emr-ddb`, `emr-goodies`, `hadoop-client`, `hudi`, `hudi-spark`, `iceberg`, `spark-kubernetes`.
+ **Supported configuration classifications**

  For use with [StartJobRun](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_StartJobRun.html) and [ CreateManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.html) APIs:


<table>
<thead>
  <tr><th>Classifications</th><th>Descriptions</th></tr>
</thead>
<tbody>
  <tr><td><code>core-site</code></td><td>Change values in the <code>core-site.xml</code> Hadoop file.</td></tr>
  <tr><td><code>spark-metrics</code></td><td>Change values in the <code>metrics.properties</code> Spark file.</td></tr>
  <tr><td><code>spark-defaults</code></td><td>Change values in the <code>spark-defaults.conf</code> Spark file.</td></tr>
  <tr><td><code>spark-env</code></td><td>Change values in the Spark environment.</td></tr>
  <tr><td><code>spark-hive-site</code></td><td>Change values in the <code>hive-site.xml</code> Spark file.</td></tr>
  <tr><td><code>spark-log4j2</code></td><td>Change values in the <code>log4j2.properties</code> Spark file.</td></tr>
  <tr><td><code>emr-job-submitter</code></td><td>Configuration for <a href="emr-eks-job-submitter.md">job submitter pod</a>.</td></tr>
</tbody>
</table>


  For use specifically with [ CreateManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.html) APIs:


<table>
<thead>
  <tr><th>Classifications</th><th>Descriptions</th></tr>
</thead>
<tbody>
  <tr><td><code>jeg-config</code></td><td>Change values in Jupyter Enterprise Gateway <code>jupyter_enterprise_gateway_config.py</code> file.</td></tr>
  <tr><td><code>jupyter-kernel-overrides</code></td><td>Change value for the Kernel Image in Jupyter Kernel Spec file.</td></tr>
</tbody>
</table>


  Configuration classifications allow you to customize applications. These often correspond to a configuration XML file for the application, such as `spark-hive-site.xml`. For more information, see [Configure Applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html).

## Changes and features
<a name="emr-eks-spark-8.0.0-changes"></a>

The following features are included with the emr-spark-8.0.0 release of AWS runtime for Apache Spark on EKS:
+ **Apache Spark 4.0.2 GA** – First production-ready release of Spark 4.x on Amazon EMR on EKS, featuring ANSI SQL mode, SQL PIPE syntax, VARIANT data type, SQL scripting, and streaming enhancements.
+ **Python 3.11 default** – Python 3.11 is the default for PySpark and Spark workloads. Python 3.12 and 3.13 are also available.