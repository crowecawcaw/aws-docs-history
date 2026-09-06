

# Amazon EMR on EKS 7.0.0 releases
<a name="emr-eks-7.0.0"></a>

This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment. For details about Amazon EMR running on Amazon EC2 and about the Amazon EMR 7.0.0 release in general, see [Amazon EMR 7.0.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-700-release.html) in the *Amazon EMR Release Guide*.

## Amazon EMR on EKS 7.0 releases
<a name="emr-eks-7.0.0-releases"></a>

The following Amazon EMR 7.0.0 releases are available for Amazon EMR on EKS. Select a specific **emr-7.0.0-XXXX** release to view more details such as the related container image tag.

------
#### [ Flink releases ]

The following Amazon EMR 7.0.0 releases are available for Amazon EMR on EKS when you run Flink applications.
+ [emr-7.0.0-flink-latest](emr-eks-7.0.0-flink-latest.md)
+  [emr-7.0.0-flink-2024321](emr-eks-7.0.0-flink-2024321.md) 
+ [emr-7.0.0-flink-20231211](emr-eks-7.0.0-flink-20231211.md)

------
#### [ Spark releases ]

The following Amazon EMR 7.0.0 releases are available for Amazon EMR on EKS when you run Spark applications.
+ [emr-7.0.0-latest](emr-eks-7.0.0-latest.md)
+ [emr-7.0.0-20231211](emr-eks-7.0.0-20231211.md)
+ emr-7.0.0-spark-rapids-latest
+ emr-7.0.0-spark-rapids-20231211
+ emr-7.0.0-java11-latest
+ emr-7.0.0-java11-20231211
+ emr-7.0.0-java8-latest
+ emr-7.0.0-java8-20231211
+ emr-7.0.0-spark-rapids-java8-latest
+ emr-7.0.0-spark-rapids-java8-20231211
+ notebook-spark/emr-7.0.0-latest
+ notebook-spark/emr-7.0.0-20231211
+ notebook-spark/emr-7.0.0-spark-rapids-latest
+ notebook-spark/emr-7.0.0-spark-rapids-20231211
+ notebook-spark/emr-7.0.0-java11-latest
+ notebook-spark/emr-7.0.0-java11-20231211
+ notebook-spark/emr-7.0.0-java8-latest
+ notebook-spark/emr-7.0.0-java8-20231211
+ notebook-spark/emr-7.0.0-spark-rapids-java8-latest
+ notebook-spark/emr-7.0.0-spark-rapids-java8-20231211
+ notebook-python/emr-7.0.0-latest
+ notebook-python/emr-7.0.0-20231211
+ notebook-python/emr-7.0.0-spark-rapids-latest
+ notebook-python/emr-7.0.0-spark-rapids-20231211
+ notebook-python/emr-7.0.0-java11-latest
+ notebook-python/emr-7.0.0-java11-20231211
+ notebook-python/emr-7.0.0-java8-latest
+ notebook-python/emr-7.0.0-java8-20231211
+ notebook-python/emr-7.0.0-spark-rapids-java8-latest
+ notebook-python/emr-7.0.0-spark-rapids-java8-20231211

------

## Release notes
<a name="emr-eks-7.0.0-rn"></a>

Release notes for Amazon EMR on EKS 7.0.0
+ **Supported applications** ‐ AWS SDK for Java 2.20.160-amzn-0 and 1.12.595, Apache Spark 3.5.0-amzn-0, Apache Flink 1.18.0-amzn-0, Flink Operator 1.6.1, Apache Hudi 0.14.0-amzn-1, Apache Iceberg 1.4.2-amzn-0, Delta 3.0.0, Apache Spark RAPIDS 23.10.0-amzn-0, Jupyter Enterprise Gateway 2.6.0
+ **Supported components** ‐ `aws-sagemaker-spark-sdk`, `emr-ddb`, `emr-goodies`, `emr-s3-select`, `emrfs`, `hadoop-client`, `hudi`, `hudi-spark`, `iceberg`, `spark-kubernetes`.
+ **Supported configuration classifications**

  For use with [StartJobRun](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_StartJobRun.html) and [ CreateManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.html) APIs:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.0.0.html)

  For use specifically with [ CreateManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.html) APIs:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.0.0.html)

  Configuration classifications allow you to customize applications. These often correspond to a configuration XML file for the application, such as `spark-hive-site.xml`. For more information, see [Configure Applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html).

## Notable features
<a name="emr-eks-7.0.0-features"></a>

The following features are included with the 7.0 release of Amazon EMR on EKS.
+ **Application upgrades** – Amazon EMR on EKS 7.0.0 application upgrades include Spark 3.5, Flink 1.18, and [Flink Operator](jobruns-flink-kubernetes-operator.md) 1.6.1.
+ **Flink Autoscaler parameter auto-tuning** – The default parameters that Flink Autoscaler uses for its scaling calculations might not be the optimal value for a given job. Amazon EMR on EKS 7.0.0 uses historical trends of specific captured metrics to calculate the optimal parameter tailored for the job. 

## Changes
<a name="emr-eks-7.0.0-changes"></a>

The following changes are included with the 7.0 release of Amazon EMR on EKS.
+ **Amazon Linux 2023** – With Amazon EMR on EKS 7.0.0 and higher, all container images are based on Amazon Linux 2023.
+ **Spark uses Java 17 as default runtime** – Amazon EMR on EKS 7.0.0 Spark uses Java 17 as default runtime. If you need to, you can switch to use Java 8 or Java 11 with the corresponding release label as provided in the [Amazon EMR on EKS 7.0 releases](#emr-eks-7.0.0-releases) list.