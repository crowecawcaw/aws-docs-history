

# Amazon EMR on EKS 7.3.0 releases
<a name="emr-eks-7.3.0"></a>

This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment. For details about Amazon EMR running on Amazon EC2 and about the Amazon EMR 7.3.0 release in general, see [Amazon EMR 7.3.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-730-release.html) in the *Amazon EMR Release Guide*.

## Amazon EMR on EKS 7.3 releases
<a name="emr-eks-7.3.0-releases"></a>

The following Amazon EMR 7.3.0 releases are available for Amazon EMR on EKS. Select a specific **emr-7.3.0-XXXX** release to view more details such as the related container image tag.

------
#### [ Flink releases ]

The following Amazon EMR 7.3.0 releases are available for Amazon EMR on EKS when you run Flink applications.
+ [emr-7.3.0-flink-latest](emr-eks-7.3.0-flink-latest.md)
+ [emr-7.3.0-flink-29240920](emr-eks-7.3.0-flink-29240920.md)

------
#### [ Spark releases ]

The following Amazon EMR 7.3.0 releases are available for Amazon EMR on EKS when you run Spark applications.
+ [emr-7.3.0-latest](emr-eks-7.3.0-latest.md)
+ [emr-7.3.0-20240920](emr-eks-7.3.0-29240920.md)
+ emr-7.3.0-spark-rapids-latest
+ emr-7.3.0-spark-rapids-29240920
+ emr-7.3.0-java11-latest
+ emr-7.3.0-java11-29240920
+ emr-7.3.0-java8-latest
+ emr-7.3.0-java8-29240920
+ emr-7.3.0-spark-rapids-java8-latest
+ emr-7.3.0-spark-rapids-java8-29240920
+ notebook-spark/emr-7.3.0-latest
+ notebook-spark/emr-7.3.0-20240920
+ notebook-spark/emr-7.3.0-spark-rapids-latest
+ notebook-spark/emr-7.3.0-spark-rapids-29240920
+ notebook-spark/emr-7.3.0-java11-latest
+ notebook-spark/emr-7.3.0-java11-29240920
+ notebook-spark/emr-7.3.0-java8-latest
+ notebook-spark/emr-7.3.0-java8-29240920
+ notebook-spark/emr-7.3.0-spark-rapids-java8-latest
+ notebook-spark/emr-7.3.0-spark-rapids-java8-29240920
+ notebook-python/emr-7.3.0-latest
+ notebook-python/emr-7.3.0-20240920
+ notebook-python/emr-7.3.0-spark-rapids-latest
+ notebook-python/emr-7.3.0-spark-rapids-29240920
+ notebook-python/emr-7.3.0-java11-latest
+ notebook-python/emr-7.3.0-java11-29240920
+ notebook-python/emr-7.3.0-java8-latest
+ notebook-python/emr-7.3.0-java8-29240920
+ notebook-python/emr-7.3.0-spark-rapids-java8-latest
+ notebook-python/emr-7.3.0-spark-rapids-java8-29240920
+ livy/emr-7.3.0-latest
+ livy/emr-7.3.0-20240920
+ livy/emr-7.3.0-java11-latest
+ livy/emr-7.3.0-java11-29240920
+ livy/emr-7.3.0-java8-latest
+ livy/emr-7.3.0-java8-29240920

------

## Release notes
<a name="emr-eks-7.3.0-rn"></a>

Release notes for Amazon EMR on EKS 7.3.0
+ **Supported applications** ‐ AWS SDK for Java 2.25.70 and 1.12.747, Apache Spark 3.5.1-amzn-1, Apache Hudi 0.15.0-amzn-0, Apache Iceberg 1.5.2-amzn-0, Delta 3.2.0-amzn-0, Apache Spark RAPIDS 24.06.1-amzn-0, Jupyter Enterprise Gateway 2.6.0, Apache Flink 1.18.1-amzn-2, Flink Operator 1.9.0-amzn-0
+ **Supported components** ‐ `aws-sagemaker-spark-sdk`, `emr-ddb`, `emr-goodies`, `emr-s3-select`, `emrfs`, `hadoop-client`, `hudi`, `hudi-spark`, `iceberg`, `spark-kubernetes`.
+ **Supported configuration classifications**

  For use with [StartJobRun](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_StartJobRun.html) and [ CreateManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.html) APIs:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.3.0.html)

  For use specifically with [ CreateManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.html) APIs:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.3.0.html)

  Configuration classifications allow you to customize applications. These often correspond to a configuration XML file for the application, such as `spark-hive-site.xml`. For more information, see [Configure Applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html).

## Notable features
<a name="emr-eks-7.3.0-features"></a>

The following features are included with the 7.3.0 release of Amazon EMR on EKS.
+ **Application upgrades** – Amazon EMR on EKS now includes [Flink Operator](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-kubernetes-operator.html) 1.9.0. In addition to other features, the Flink Kubernetes now lets you set CPU and memory quotas for the autoscaler.
+ **Apache Iceberg support for Apache Flink** – Apache Iceberg is an open-source high-performance format huge analytic tables. Starting with Amazon EMR 7.3.0, you can use Apache Iceberg tables when you run Apache Flink on Amazon EMR on EKS. For more information, see the Amazon EMR on EKS [Using Apache Iceberg with Amazon EMR on EKS](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/tutorial-iceberg.html).
+ **Delta Lake support for Apache Flink** – Delta Lake is a storage layer framework for lakehouse architectures commonly built on Amazon S3. With Amazon EMR 7.3.0 and higher, you can use Delta tables when you run Apache Flink on Amazon EMR on EKS. For more information, see [Using Delta Lake with Amazon EMR on EKS](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/tutorial-delta-lake.html).

## Changes
<a name="emr-eks-7.3.0-changes"></a>

The following changes are included with the 7.3.0 release of Amazon EMR on EKS.
+ With Amazon EMR on EKS 7.3.0 and higher, Apache Flink now uses Java 17 runtime by default.