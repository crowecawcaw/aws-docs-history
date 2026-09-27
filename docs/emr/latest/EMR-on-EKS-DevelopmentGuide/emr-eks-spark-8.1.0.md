

# AWS runtime for Apache Spark (emr-spark-8.1.0) on EKS
<a name="emr-eks-spark-8.1.0"></a>

This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment. For details about Amazon EMR running on Amazon EC2 and about the Amazon EMR Spark 8.1.0 release in general, see [AWS runtime for Apache Spark (emr-spark-8.1.0)](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark810-release.html) in the *Amazon EMR Release Guide*.

## AWS runtime for Apache Spark (emr-spark-8.1.0) on EKS
<a name="emr-eks-spark-8.1.0-releases"></a>

The following emr-spark-8.1.0 image tags are available for AWS runtime for Apache Spark on EKS.

------
#### [ Spark releases ]

The following emr-spark-8.1.0 image tags are available when you run Spark applications on EKS.
+ emr-spark-8.1.0-latest
+ emr-spark-8.1.0-20260812
+ emr-spark-8.1.0-rapids-latest
+ emr-spark-8.1.0-rapids-20260812
+ notebook-spark/emr-spark-8.1.0-latest
+ notebook-spark/emr-spark-8.1.0-20260812
+ notebook-spark/emr-spark-8.1.0-rapids-latest
+ notebook-spark/emr-spark-8.1.0-rapids-20260812
+ notebook-python/emr-spark-8.1.0-latest
+ notebook-python/emr-spark-8.1.0-20260812
+ livy/emr-spark-8.1.0-latest
+ livy/emr-spark-8.1.0-20260812

------

## Release notes
<a name="emr-eks-spark-8.1.0-rn"></a>

Release notes for AWS runtime for Apache Spark (emr-spark-8.1.0) on EKS:
+ **Supported applications** ‐ AWS SDK for Java 2.x 2.44.5, Apache Spark 4.1.1-amzn-0, Apache Hudi 1.1.1-amzn-0, Apache Iceberg 1.11.0-amzn-0, Delta Lake 4.2.0-amzn-0, Apache Spark RAPIDS 26.04.2-amzn-0
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
  <tr><td><code>emr-job-submitter</code></td><td>Configuration for job submitter pod.</td></tr>
</tbody>
</table>


  For use specifically with CreateManagedEndpoint APIs:


<table>
<thead>
  <tr><th>Classifications</th><th>Descriptions</th></tr>
</thead>
<tbody>
  <tr><td><code>jeg-config</code></td><td>Change values in Jupyter Enterprise Gateway <code>jupyter_enterprise_gateway_config.py</code> file.</td></tr>
  <tr><td><code>jupyter-kernel-overrides</code></td><td>Change value for the Kernel Image in Jupyter Kernel Spec file.</td></tr>
</tbody>
</table>


  Configuration classifications allow you to customize applications. For more information, see [Configure applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html).

## Changes and features
<a name="emr-eks-spark-8.1.0-changes"></a>

The following features are included with the emr-spark-8.1.0 release of AWS runtime for Apache Spark on EKS:
+ **Spark Connect on Amazon EMR on EKS** — Amazon EMR on EKS clusters running emr-spark-8.1.0 now support Spark Connect endpoints with token-based authentication. For setup and configuration, see [Run interactive sessions with Amazon EMR on EKS through Spark Connect](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-spark-connect.html) in the *Amazon EMR on EKS Development Guide*.
+ **Amazon EMR on EKS job runner pod graceful termination** — The Amazon EMR on EKS `jobsubmitter.gracefulTermination` configuration is enabled by default for emr-spark-8.1.0 and subsequent releases. For setup and configuration, see [Using job submitter classification](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-job-submitter.html) in the *Amazon EMR on EKS Development Guide*.

**Resolved issues**
+ **Livy endpoint stability after Kubernetes token rotation** — Fixed an issue where Amazon EMR on EKS managed Livy endpoints could become unusable after the Kubernetes service-account token rotates, previously requiring a pod restart to recover. Livy now automatically refreshes its credentials when the projected service-account token is rotated.
+ **Fixed Spark Operator applications on IPv6-only EKS clusters** — Spark Operator applications on IPv6-only EKS clusters no longer fail to submit due to a malformed Kubernetes API server URL for emr-spark-8.1.0 and subsequent releases. For setup and configuration, see [Running EMR on EKS on IPv6 clusters](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-ipv6.html) in the *Amazon EMR on EKS Development Guide*.