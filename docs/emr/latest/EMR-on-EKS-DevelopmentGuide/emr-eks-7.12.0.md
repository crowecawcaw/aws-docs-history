

# Amazon EMR on EKS 7.12.0 releases
<a name="emr-eks-7.12.0"></a>

This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment. For details about Amazon EMR running on Amazon EC2 and about the Amazon EMR 7.12.0 release in general, see [Amazon EMR 7.12.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-7120-release.html) in the *Amazon EMR Release Guide*.

## Amazon EMR on EKS 7.12 releases
<a name="emr-eks-7.12.0-releases"></a>

The following Amazon EMR 7.12.0 releases are available for Amazon EMR on EKS. Select a specific **emr-7.12.0-XXXX** release to view more details such as the related container image tag.

------
#### [ Flink releases ]

The following Amazon EMR 7.12.0 releases are available for Amazon EMR on EKS when you run Flink applications.
+ [emr-7.12.0-flink-latest](emr-eks-7.12.0-flink-latest.md)
+ [emr-7.12.0-flink-20251111](emr-7.12.0-flink-20251111.md)

------
#### [ Spark releases ]

The following Amazon EMR 7.12.0 releases are available for Amazon EMR on EKS when you run Spark applications.
+ [emr-7.12.0-latest](emr-eks-7.12.0-latest.md)
+ [emr-7.12.0-20251111](emr-eks-7.12.0-20251111.md)
+ emr-7.12.0-spark-rapids-latest
+ emr-7.12.0-spark-rapids-20251111
+ emr-7.12.0-java11-latest
+ emr-7.12.0-java11-20251111
+ emr-7.12.0-java8-latest
+ emr-7.12.0-java8-20251111
+ emr-7.12.0-spark-rapids-java8-latest
+ emr-7.12.0-spark-rapids-java8-20251111
+ notebook-spark/emr-7.12.0-latest
+ notebook-spark/emr-7.12.0-20251111
+ notebook-spark/emr-7.12.0-spark-rapids-latest
+ notebook-spark/emr-7.12.0-spark-rapids-20251111
+ notebook-spark/emr-7.12.0-java11-latest
+ notebook-spark/emr-7.12.0-java11-20251111
+ notebook-spark/emr-7.12.0-java8-latest
+ notebook-spark/emr-7.12.0-java8-20251111
+ notebook-spark/emr-7.12.0-spark-rapids-java8-latest
+ notebook-spark/emr-7.12.0-spark-rapids-java8-20251111
+ notebook-python/emr-7.12.0-latest
+ notebook-python/emr-7.12.0-20251111
+ notebook-python/emr-7.12.0-spark-rapids-latest
+ notebook-python/emr-7.12.0-spark-rapids-20251111
+ notebook-python/emr-7.12.0-java11-latest
+ notebook-python/emr-7.12.0-java11-20251111
+ notebook-python/emr-7.12.0-java8-latest
+ notebook-python/emr-7.12.0-java8-20251111
+ notebook-python/emr-7.12.0-spark-rapids-java8-latest
+ notebook-python/emr-7.12.0-spark-rapids-java8-20251111
+ livy/emr-7.12.0-latest
+ livy/emr-7.12.0-20251111
+ livy/emr-7.12.0-java11-latest
+ livy/emr-7.12.0-java11-20251111
+ livy/emr-7.12.0-java8-latest
+ livy/emr-7.12.0-java8-20251111

------

## Release notes
<a name="emr-eks-7.12.0-rn"></a>

Release notes for Amazon EMR on EKS 7.12.0:
+ **Supported applications** ‐ AWS SDK for Java 2.35.5 and 1.12.792, Apache Spark 3.5.6-amzn-1, Apache Hudi 1.0.2-amzn-1, Apache Iceberg 1.10.0-amzn-0, Delta 3.3.2-amzn-1, Apache Spark RAPIDS 25.04.0-amzn-0, Apache Flink 1.20.0-amzn-6
+ **Supported components** ‐ `emr-ddb`, `emr-goodies`, `emr-s3-select`, `emrfs`, `hadoop-client`, `hudi`, `hudi-spark`, `iceberg`, `spark-kubernetes`.
+ **Supported configuration classifications**

  For use with [StartJobRun](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_StartJobRun.html) and [ CreateManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.html) APIs:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.12.0.html)

  For use specifically with [ CreateManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.html) APIs:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.12.0.html)

  Configuration classifications allow you to customize applications. These often correspond to a configuration XML file for the application, such as `spark-hive-site.xml`. For more information, see [Configure Applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html).

## Changes and features
<a name="emr-eks-7.12.0-changes"></a>

The following features are included with the 7.12.0 release of Amazon EMR on EKS:
+ **Iceberg Materialized Views** – Starting EMR 7.12.0, EMR Spark supports creation and management of Iceberg Materialized Views (MV).
+ **Hudi Full Table Access** – Starting EMR 7.12.0, EMR now supports Full Table Access (FTA) control for Apache Hudi in Apache Spark based on your policies defined in Lake Formation. This feature enables read and write operations from your Amazon EMR Spark jobs on Lake Formation registered tables when the job role has full table access.
+ **Iceberg version upgrade** – EMR 7.12.0 supports Apache Iceberg version 1.10.
+ **Logging for Livy interactive workloads** – Starting EMR 7.12.0, EMR supports extensive logging for key system components to improve troubleshooting for Livy Spark job failures. This feature will provide EMR service with access to additional Livy and SecretAgent logs to simplify troubleshooting.