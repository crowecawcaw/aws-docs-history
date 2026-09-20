

# Amazon EMR on EKS 7.13.0 releases
<a name="emr-eks-7.13.0"></a>

This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment. For details about Amazon EMR running on Amazon EC2 and about the Amazon EMR 7.13.0 release in general, see [Amazon EMR 7.13.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-7130-release.html) in the *Amazon EMR Release Guide*.

## Amazon EMR on EKS 7.13 releases
<a name="emr-eks-7.13.0-releases"></a>

The following Amazon EMR 7.13.0 releases are available for Amazon EMR on EKS. Select a specific **emr-7.13.0-XXXX** release to view more details such as the related container image tag.

------
#### [ Flink releases ]

The following Amazon EMR 7.13.0 releases are available for Amazon EMR on EKS when you run Flink applications.
+ [emr-7.13.0-flink-latest](emr-eks-7.13.0-flink-latest.md)
+ [emr-7.13.0-flink-20260410](emr-eks-7.13.0-flink-20260410.md)

------
#### [ Spark releases ]

The following Amazon EMR 7.13.0 releases are available for Amazon EMR on EKS when you run Spark applications.
+ [emr-7.13.0-latest](emr-eks-7.13.0-latest.md)
+ [emr-7.13.0-20260410](emr-eks-7.13.0-20260410.md)
+ emr-7.13.0-spark-rapids-latest
+ emr-7.13.0-spark-rapids-20260410
+ emr-7.13.0-java11-latest
+ emr-7.13.0-java11-20260410
+ emr-7.13.0-java8-latest
+ emr-7.13.0-java8-20260410
+ emr-7.13.0-spark-rapids-java8-latest
+ emr-7.13.0-spark-rapids-java8-20260410
+ notebook-spark/emr-7.13.0-latest
+ notebook-spark/emr-7.13.0-20260410
+ notebook-spark/emr-7.13.0-spark-rapids-latest
+ notebook-spark/emr-7.13.0-spark-rapids-20260410
+ notebook-spark/emr-7.13.0-java11-latest
+ notebook-spark/emr-7.13.0-java11-20260410
+ notebook-spark/emr-7.13.0-java8-latest
+ notebook-spark/emr-7.13.0-java8-20260410
+ notebook-spark/emr-7.13.0-spark-rapids-java8-latest
+ notebook-spark/emr-7.13.0-spark-rapids-java8-20260410
+ notebook-python/emr-7.13.0-latest
+ notebook-python/emr-7.13.0-20260410
+ notebook-python/emr-7.13.0-spark-rapids-latest
+ notebook-python/emr-7.13.0-spark-rapids-20260410
+ notebook-python/emr-7.13.0-java11-latest
+ notebook-python/emr-7.13.0-java11-20260410
+ notebook-python/emr-7.13.0-java8-latest
+ notebook-python/emr-7.13.0-java8-20260410
+ notebook-python/emr-7.13.0-spark-rapids-java8-latest
+ notebook-python/emr-7.13.0-spark-rapids-java8-20260410
+ livy/emr-7.13.0-latest
+ livy/emr-7.13.0-20260410
+ livy/emr-7.13.0-java11-latest
+ livy/emr-7.13.0-java11-20260410
+ livy/emr-7.13.0-java8-latest
+ livy/emr-7.13.0-java8-20260410

------

## Release notes
<a name="emr-eks-7.13.0-rn"></a>

Release notes for Amazon EMR on EKS 7.13.0:
+ **Supported applications** ‐ AWS SDK for Java 2.42.12 and 1.12.797, Apache Spark 3.5.6-amzn-2, Apache Hudi 1.0.2-amzn-2, Apache Iceberg 1.10.0-amzn-1, Delta 3.3.2-amzn-2, Apache Spark RAPIDS 25.04.0-amzn-0, Apache Flink 1.20.0-amzn-7
+ **Supported components** ‐ `emr-ddb`, `emr-goodies`, `emr-s3-select`, `emrfs`, `hadoop-client`, `hudi`, `hudi-spark`, `iceberg`, `spark-kubernetes`.
+ **Supported configuration classifications**

  For use with [StartJobRun](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_StartJobRun.html) and [ CreateManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.html) APIs:


<table>
<thead>
  <tr><th>Classifications</th><th>Descriptions</th></tr>
</thead>
<tbody>
  <tr><td><code>core-site</code></td><td>Change values in the <code>core-site.xml</code> Hadoop file.</td></tr>
  <tr><td><code>emrfs-site</code></td><td>Change EMRFS settings.</td></tr>
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
<a name="emr-eks-7.13.0-changes"></a>

The following features are included with the 7.13.0 release of Amazon EMR on EKS:
+ **Python 3.11 default for PySpark and Spark workloads** – Python 3.11 is now the default Python version for PySpark and Spark workloads. Python 3.9 remains the default for all other applications. Both Python 3.9 and 3.11 are included in the release.