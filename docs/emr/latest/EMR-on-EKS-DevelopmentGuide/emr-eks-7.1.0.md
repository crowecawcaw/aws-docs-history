

# Amazon EMR on EKS 7.1.0 releases
<a name="emr-eks-7.1.0"></a>

This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment. For details about Amazon EMR running on Amazon EC2 and about the Amazon EMR 7.1.0 release in general, see [Amazon EMR 7.1.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-710-release.html) in the *Amazon EMR Release Guide*.

## Amazon EMR on EKS 7.1 releases
<a name="emr-eks-7.1.0-releases"></a>

The following Amazon EMR 7.1.0 releases are available for Amazon EMR on EKS. Select a specific **emr-7.1.0-XXXX** release to view more details such as the related container image tag.

------
#### [ Flink releases ]

The following Amazon EMR 7.1.0 releases are available for Amazon EMR on EKS when you run Flink applications.
+ [emr-7.1.0-flink-latest](emr-eks-7.1.0-flink-latest.md)
+ [emr-7.1.0-flink-20240321](emr-eks-7.1.0-flink-20240321.md)

------
#### [ Spark releases ]

The following Amazon EMR 7.1.0 releases are available for Amazon EMR on EKS when you run Spark applications.
+ [emr-7.1.0-latest](emr-eks-7.1.0-latest.md)
+ [emr-7.1.0-20240321](emr-eks-7.1.0-20240321.md)
+ emr-7.1.0-spark-rapids-latest
+ emr-7.1.0-spark-rapids-20240321
+ emr-7.1.0-java11-latest
+ emr-7.1.0-java11-20240321
+ emr-7.1.0-java8-latest
+ emr-7.1.0-java8-20240321
+ emr-7.1.0-spark-rapids-java8-latest
+ emr-7.1.0-spark-rapids-java8-20240321
+ notebook-spark/emr-7.1.0-latest
+ notebook-spark/emr-7.1.0-20240321
+ notebook-spark/emr-7.1.0-spark-rapids-latest
+ notebook-spark/emr-7.1.0-spark-rapids-20240321
+ notebook-spark/emr-7.1.0-java11-latest
+ notebook-spark/emr-7.1.0-java11-20240321
+ notebook-spark/emr-7.1.0-java8-latest
+ notebook-spark/emr-7.1.0-java8-20240321
+ notebook-spark/emr-7.1.0-spark-rapids-java8-latest
+ notebook-spark/emr-7.1.0-spark-rapids-java8-20240321
+ notebook-python/emr-7.1.0-latest
+ notebook-python/emr-7.1.0-20240321
+ notebook-python/emr-7.1.0-spark-rapids-latest
+ notebook-python/emr-7.1.0-spark-rapids-20240321
+ notebook-python/emr-7.1.0-java11-latest
+ notebook-python/emr-7.1.0-java11-20240321
+ notebook-python/emr-7.1.0-java8-latest
+ notebook-python/emr-7.1.0-java8-20240321
+ notebook-python/emr-7.1.0-spark-rapids-java8-latest
+ notebook-python/emr-7.1.0-spark-rapids-java8-20240321
+ livy/emr-7.1.0-latest
+ livy/emr-7.1.0-20240321
+ livy/emr-7.1.0-java11-latest
+ livy/emr-7.1.0-java11-20240321
+ livy/emr-7.1.0-java8-latest
+ livy/emr-7.1.0-java8-20240321

------

## Release notes
<a name="emr-eks-7.1.0-rn"></a>

Release notes for Amazon EMR on EKS 7.1.0
+ **Supported applications** ‐ AWS SDK for Java 2.23.18 and 1.12.656, Apache Spark 3.5.0-amzn-1, Apache Hudi 0.14.1-amzn-0, Apache Iceberg 1.4.3-amzn-0, Delta 3.0.0, Apache Spark RAPIDS 23.10.0-amzn-1, Jupyter Enterprise Gateway 2.6.0, Apache Flink 1.18.1-amzn-0, Flink Operator 1.6.1-amzn-1
+ **Supported components** ‐ `aws-sagemaker-spark-sdk`, `emr-ddb`, `emr-goodies`, `emr-s3-select`, `emrfs`, `hadoop-client`, `hudi`, `hudi-spark`, `iceberg`, `spark-kubernetes`.
+ **Supported configuration classifications**

  For use with [StartJobRun](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_StartJobRun.html) and [ CreateManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.html) APIs:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.1.0.html)

  For use specifically with [ CreateManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.html) APIs:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.1.0.html)

  Configuration classifications allow you to customize applications. These often correspond to a configuration XML file for the application, such as `spark-hive-site.xml`. For more information, see [Configure Applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html).

## Notable features
<a name="emr-eks-7.1.0-features"></a>

The following features are included with the 7.1.0 release of Amazon EMR on EKS.
+ **[Apache Livy support for Amazon EMR on EKS](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/job-runs-apache-livy.html)** – With Amazon EMR on EKS releases 7.1.0 and higher, you can use Apache Livy on an Amazon EKS cluster to create an Apache Livy REST interface to submit Spark jobs or snippets of Spark code. Doing so lets you retrieve results synchronously and asynchronously, while still leveraging Amazon EMR on EKS benefits, such as Amazon EMR-optimized Spark runtime, SSL-enabled Livy endpoints, and a programmatic set-up experience.