

# Amazon EMR on EKS 7.6.0 releases
<a name="emr-eks-7.6.0"></a>

This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment. For details about Amazon EMR running on Amazon EC2 and about the Amazon EMR 7.6.0 release in general, see [Amazon EMR 7.6.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-760-release.html) in the *Amazon EMR Release Guide*.

## Amazon EMR on EKS 7.6 releases
<a name="emr-eks-7.6.0-releases"></a>

The following Amazon EMR 7.6.0 releases are available for Amazon EMR on EKS. Select a specific **emr-7.6.0-XXXX** release to view more details such as the related container image tag.

------
#### [ Flink releases ]

The following Amazon EMR 7.6.0 releases are available for Amazon EMR on EKS when you run Flink applications.
+ [emr-7.6.0-flink-latest](emr-eks-7.6.0-flink-latest.md)
+ [emr-7.6.0-flink-20241213](emr-eks-7.6.0-flink-20241213.md)

------
#### [ Spark releases ]

The following Amazon EMR 7.6.0 releases are available for Amazon EMR on EKS when you run Spark applications.
+ [emr-7.6.0-latest](emr-eks-7.6.0-latest.md)
+ [emr-7.6.0-20241213](emr-eks-7.6.0-20241213.md)
+ emr-7.6.0-spark-rapids-latest
+ emr-7.6.0-spark-rapids-20241213
+ emr-7.6.0-java11-latest
+ emr-7.6.0-java11-20241213
+ emr-7.6.0-java8-latest
+ emr-7.6.0-java8-20241213
+ emr-7.6.0-spark-rapids-java8-latest
+ emr-7.6.0-spark-rapids-java8-20241213
+ notebook-spark/emr-7.6.0-latest
+ notebook-spark/emr-7.6.0-20241213
+ notebook-spark/emr-7.6.0-spark-rapids-latest
+ notebook-spark/emr-7.6.0-spark-rapids-20241213
+ notebook-spark/emr-7.6.0-java11-latest
+ notebook-spark/emr-7.6.0-java11-20241213
+ notebook-spark/emr-7.6.0-java8-latest
+ notebook-spark/emr-7.6.0-java8-20241213
+ notebook-spark/emr-7.6.0-spark-rapids-java8-latest
+ notebook-spark/emr-7.6.0-spark-rapids-java8-20241213
+ notebook-python/emr-7.6.0-latest
+ notebook-python/emr-7.6.0-20241213
+ notebook-python/emr-7.6.0-spark-rapids-latest
+ notebook-python/emr-7.6.0-spark-rapids-20241213
+ notebook-python/emr-7.6.0-java11-latest
+ notebook-python/emr-7.6.0-java11-20241213
+ notebook-python/emr-7.6.0-java8-latest
+ notebook-python/emr-7.6.0-java8-20241213
+ notebook-python/emr-7.6.0-spark-rapids-java8-latest
+ notebook-python/emr-7.6.0-spark-rapids-java8-20241213
+ livy/emr-7.6.0-latest
+ livy/emr-7.6.0-20241213
+ livy/emr-7.6.0-java11-latest
+ livy/emr-7.6.0-java11-20241213
+ livy/emr-7.6.0-java8-latest
+ livy/emr-7.6.0-java8-20241213

------

## Release notes
<a name="emr-eks-7.6.0-rn"></a>

Release notes for Amazon EMR on EKS 7.6.0
+ **Supported applications** ‐ AWS SDK for Java 2.29.25 and 1.12.779, Apache Spark 3.5.3-amzn-0, Apache Hudi 0.15.0-amzn-3, Apache Iceberg 1.6.1-amzn-2, Delta 3.2.1-amzn-1, Apache Spark RAPIDS 24.10.1-amzn-0, Jupyter Enterprise Gateway 2.6.0, Apache Flink 1.20.0-amzn-0, Flink Operator 1.10.0-amzn-0
+ **Supported components** ‐ `aws-sagemaker-spark-sdk`, `emr-ddb`, `emr-goodies`, `emr-s3-select`, `emrfs`, `hadoop-client`, `hudi`, `hudi-spark`, `iceberg`, `spark-kubernetes`.
+ **Supported configuration classifications**

  For use with [StartJobRun](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_StartJobRun.html) and [ CreateManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.html) APIs:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.6.0.html)

  For use specifically with [ CreateManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.html) APIs:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.6.0.html)

  Configuration classifications allow you to customize applications. These often correspond to a configuration XML file for the application, such as `spark-hive-site.xml`. For more information, see [Configure Applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html).

## Notable features
<a name="emr-eks-7.6.0-features"></a>

The following features are included with the 7.6.0 release of Amazon EMR on EKS:
+ **Monitoring Configuration Support for Apache Spark Operator** – Monitoring configuration lets you easily set up log archiving of your Spark application and operator logs to Amazon S3 or to Amazon CloudWatch. You can choose one or both. Doing so adds a log agent sidecar to your Spark operator pod, driver, and executor pods, and subsequently forwards these components' logs to your configured sinks. For more information, see [Using monitoring configuration to monitor the Spark Kubernetes operator and Spark jobs](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/spark-operator-monitoring-configuration.html).

## Changes
<a name="emr-eks-7.6.0-changes"></a>

The following changes are included with the 7.6.0 release of Amazon EMR on EKS:
+ No changes for the release.