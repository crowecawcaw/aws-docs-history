

# Amazon EMR on EKS 7.10.0 releases
<a name="emr-eks-7.10.0"></a>

This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment. For details about Amazon EMR running on Amazon EC2 and about the Amazon EMR 7.10.0 release in general, see [Amazon EMR 7.10.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-7100-release.html) in the *Amazon EMR Release Guide*.

## Amazon EMR on EKS 7.10 releases
<a name="emr-eks-7.10.0-releases"></a>

The following Amazon EMR 7.10.0 releases are available for Amazon EMR on EKS. Select a specific **emr-7.10.0-XXXX** release to view more details such as the related container image tag.

------
#### [ Flink releases ]

The following Amazon EMR 7.10.0 releases are available for Amazon EMR on EKS when you run Flink applications.
+ [emr-7.10.0-flink-latest](emr-eks-7.10.0-flink-latest.md)
+ [emr-7.10.0-flink-20250801](emr-7.10.0-flink-20250801.md)

------
#### [ Spark releases ]

The following Amazon EMR 7.10.0 releases are available for Amazon EMR on EKS when you run Spark applications.
+ [emr-7.10.0-latest](emr-eks-7.10.0-latest.md)
+ [emr-7.10.0-20250801](emr-eks-7.10.0-20250801.md)
+ emr-7.10.0-spark-rapids-latest
+ emr-7.10.0-spark-rapids-20250801
+ emr-7.10.0-java11-latest
+ emr-7.10.0-java11-20250801
+ emr-7.10.0-java8-latest
+ emr-7.10.0-java8-20250801
+ emr-7.10.0-spark-rapids-java8-latest
+ emr-7.10.0-spark-rapids-java8-20250801
+ notebook-spark/emr-7.10.0-latest
+ notebook-spark/emr-7.10.0-20250801
+ notebook-spark/emr-7.10.0-spark-rapids-latest
+ notebook-spark/emr-7.10.0-spark-rapids-20250801
+ notebook-spark/emr-7.10.0-java11-latest
+ notebook-spark/emr-7.10.0-java11-20250801
+ notebook-spark/emr-7.10.0-java8-latest
+ notebook-spark/emr-7.10.0-java8-20250801
+ notebook-spark/emr-7.10.0-spark-rapids-java8-latest
+ notebook-spark/emr-7.10.0-spark-rapids-java8-20250801
+ notebook-python/emr-7.10.0-latest
+ notebook-python/emr-7.10.0-20250801
+ notebook-python/emr-7.10.0-spark-rapids-latest
+ notebook-python/emr-7.10.0-spark-rapids-20250801
+ notebook-python/emr-7.10.0-java11-latest
+ notebook-python/emr-7.10.0-java11-20250801
+ notebook-python/emr-7.10.0-java8-latest
+ notebook-python/emr-7.10.0-java8-20250801
+ notebook-python/emr-7.10.0-spark-rapids-java8-latest
+ notebook-python/emr-7.10.0-spark-rapids-java8-20250801
+ livy/emr-7.10.0-latest
+ livy/emr-7.10.0-20250801
+ livy/emr-7.10.0-java11-latest
+ livy/emr-7.10.0-java11-20250801
+ livy/emr-7.10.0-java8-latest
+ livy/emr-7.10.0-java8-20250801

------

## Release notes
<a name="emr-eks-7.10.0-rn"></a>

Release notes for Amazon EMR on EKS 7.10.0:
+ **Supported applications** ‐ AWS SDK for Java 2.31.48 and 1.12.782, Apache Spark 3.5.5-amzn-1, Apache Hudi 0.15.0-amzn-7, Apache Iceberg 1.8.1-amzn-0, Delta 3.3.0-amzn-2, Apache Spark RAPIDS 25.04.0-amzn-0, Apache Flink 1.20.0-amzn-4, Flink Kubernetes Operator 1.10.0-amzn-4
+ **Supported components** ‐ `emr-ddb`, `emr-goodies`, `emr-s3-select`, `emrfs`, `hadoop-client`, `hudi`, `hudi-spark`, `iceberg`, `spark-kubernetes`.
+ **Supported configuration classifications**

  For use with [StartJobRun](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_StartJobRun.html) and [ CreateManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.html) APIs:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.10.0.html)

  For use specifically with [ CreateManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.html) APIs:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.10.0.html)

  Configuration classifications allow you to customize applications. These often correspond to a configuration XML file for the application, such as `spark-hive-site.xml`. For more information, see [Configure Applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html).

## Changes and features
<a name="emr-eks-7.10.0-changes"></a>

The following features are included with the 7.10.0 release of Amazon EMR on EKS:
+  **S3A filesystem** – Starting from the 7.10.0 release, the S3A filesystem has replaced EMRFS as the default EMR S3 connector. For more information, see [EMR File System (EMRFS)](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-s3a-migrate.html). 