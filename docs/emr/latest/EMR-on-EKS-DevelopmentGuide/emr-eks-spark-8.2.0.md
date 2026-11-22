

# AWS runtime for Apache Spark (emr-spark-8.2.0) on EKS

This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment. For details about Amazon EMR running on Amazon EC2 and about the Amazon EMR Spark 8.2.0 release in general, see [AWS runtime for Apache Spark (emr-spark-8.2.0)](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark820-release.html) in the *Amazon EMR Release Guide*.

## AWS runtime for Apache Spark (emr-spark-8.2.0) on EKS
<a name="emr-eks-spark-8.2.0-releases"></a>

The following emr-spark-8.2.0 image tags are available for AWS runtime for Apache Spark on EKS.

------
#### [ Spark releases ]

The following emr-spark-8.2.0 image tags are available when you run Spark applications on EKS.
+ emr-spark-8.2.0-latest
+ emr-spark-8.2.0-20261108
+ emr-spark-8.2.0-rapids-latest
+ emr-spark-8.2.0-rapids-20261108
+ notebook-spark/emr-spark-8.2.0-latest
+ notebook-spark/emr-spark-8.2.0-20261108
+ notebook-spark/emr-spark-8.2.0-rapids-latest
+ notebook-spark/emr-spark-8.2.0-rapids-20261108
+ notebook-python/emr-spark-8.2.0-latest
+ notebook-python/emr-spark-8.2.0-20261108
+ livy/emr-spark-8.2.0-latest
+ livy/emr-spark-8.2.0-20261108

------

## Release notes
<a name="emr-eks-spark-8.2.0-rn"></a>

Release notes for AWS runtime for Apache Spark (emr-spark-8.2.0) on EKS:
+ **Supported applications** ‐ AWS SDK for Java 2.x 2.55.8, Apache Spark 4.1.3-amzn-0, Apache Hudi 1.1.1-amzn-0, Apache Iceberg 1.11.0-amzn-0, Delta Lake 4.2.0-amzn-0, Apache Spark RAPIDS 26.08.1-amzn-0
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
<a name="emr-eks-spark-8.2.0-changes"></a>

The following features are included with the emr-spark-8.2.0 release of AWS runtime for Apache Spark on EKS:
+ **Spark Operator version 2** — The Spark Operator for Amazon EMR on EKS is upgraded to version 2, based on open-source Spark Operator 2.5.0. If you don't specify an image tag, the emr-spark-8.2.0 Helm chart uses the latest operator image for your release label. It pulls the image each time a pod starts, so you always run the most recently patched image.
+ **Trusted identity propagation for Amazon EMR on EKS jobs** — Amazon EMR on EKS now supports trusted identity propagation for IAM federated users, for both batch jobs and interactive Spark Connect and Livy sessions. When a federated user submits a job or starts a session, the temporary credentials issued to the job carry that user's identity context. IAM policies and downstream services, including AWS Lake Formation fine-grained access control and Amazon S3 Access Grants, can then evaluate permissions and audit access against the original user rather than the job execution role.

**Resolved issues**
+ **Node selectors for fine-grained access control user executors** — Node selectors configured for Amazon EMR on EKS jobs that use fine-grained access control now apply to user executors. Previously, they weren't applied. System executors are unchanged.