

# Amazon EMR on EKS 7.2.0 releases
<a name="emr-eks-7.2.0"></a>

This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment. For details about Amazon EMR running on Amazon EC2 and about the Amazon EMR 7.2.0 release in general, see [Amazon EMR 7.2.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-720-release.html) in the *Amazon EMR Release Guide*.

## Amazon EMR on EKS 7.2 releases
<a name="emr-eks-7.2.0-releases"></a>

The following Amazon EMR 7.2.0 releases are available for Amazon EMR on EKS. Select a specific **emr-7.2.0-XXXX** release to view more details such as the related container image tag.

------
#### [ Flink releases ]

The following Amazon EMR 7.2.0 releases are available for Amazon EMR on EKS when you run Flink applications.
+ [emr-7.2.0-flink-latest](emr-eks-7.2.0-flink-latest.md)
+ [emr-7.2.0-flink-20240610](emr-eks-7.2.0-flink-20240610.md)

------
#### [ Spark releases ]

The following Amazon EMR 7.2.0 releases are available for Amazon EMR on EKS when you run Spark applications.
+ [emr-7.2.0-latest](emr-eks-7.2.0-latest.md)
+ [emr-7.2.0-20240610](emr-eks-7.2.0-20240610.md)
+ emr-7.2.0-spark-rapids-latest
+ emr-7.2.0-spark-rapids-20240610
+ emr-7.2.0-java11-latest
+ emr-7.2.0-java11-20240610
+ emr-7.2.0-java8-latest
+ emr-7.2.0-java8-20240610
+ emr-7.2.0-spark-rapids-java8-latest
+ emr-7.2.0-spark-rapids-java8-20240610
+ notebook-spark/emr-7.2.0-latest
+ notebook-spark/emr-7.2.0-20240610
+ notebook-spark/emr-7.2.0-spark-rapids-latest
+ notebook-spark/emr-7.2.0-spark-rapids-20240610
+ notebook-spark/emr-7.2.0-java11-latest
+ notebook-spark/emr-7.2.0-java11-20240610
+ notebook-spark/emr-7.2.0-java8-latest
+ notebook-spark/emr-7.2.0-java8-20240610
+ notebook-spark/emr-7.2.0-spark-rapids-java8-latest
+ notebook-spark/emr-7.2.0-spark-rapids-java8-20240610
+ notebook-python/emr-7.2.0-latest
+ notebook-python/emr-7.2.0-20240610
+ notebook-python/emr-7.2.0-spark-rapids-latest
+ notebook-python/emr-7.2.0-spark-rapids-20240610
+ notebook-python/emr-7.2.0-java11-latest
+ notebook-python/emr-7.2.0-java11-20240610
+ notebook-python/emr-7.2.0-java8-latest
+ notebook-python/emr-7.2.0-java8-20240610
+ notebook-python/emr-7.2.0-spark-rapids-java8-latest
+ notebook-python/emr-7.2.0-spark-rapids-java8-20240610
+ livy/emr-7.2.0-latest
+ livy/emr-7.2.0-20240610
+ livy/emr-7.2.0-java11-latest
+ livy/emr-7.2.0-java11-20240610
+ livy/emr-7.2.0-java8-latest
+ livy/emr-7.2.0-java8-20240610

------

## Release notes
<a name="emr-eks-7.2.0-rn"></a>

Release notes for Amazon EMR on EKS 7.2.0
+ **Supported applications** ‐ AWS SDK for Java 2.23.18 and 1.12.705, Apache Spark 3.5.1-amzn-1, Apache Hudi 0.14.1-amzn-0, Apache Iceberg 1.5.0-amzn-0, Delta 3.1.0, Apache Spark RAPIDS 24.02.0-amzn-1, Jupyter Enterprise Gateway 2.6.0, Apache Flink 1.18.1-amzn-0, Flink Operator 1.8.0-amzn-1
+ **Supported components** ‐ `aws-sagemaker-spark-sdk`, `emr-ddb`, `emr-goodies`, `emr-s3-select`, `emrfs`, `hadoop-client`, `hudi`, `hudi-spark`, `iceberg`, `spark-kubernetes`.
+ **Supported configuration classifications**

  For use with [StartJobRun](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_StartJobRun.html) and [ CreateManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.html) APIs:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.2.0.html)

  For use specifically with [ CreateManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.html) APIs:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-7.2.0.html)

  Configuration classifications allow you to customize applications. These often correspond to a configuration XML file for the application, such as `spark-hive-site.xml`. For more information, see [Configure Applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html).

## Notable features
<a name="emr-eks-7.2.0-features"></a>

The following features are included with the 7.2.0 release of Amazon EMR on EKS.
+ **Application upgrades** – Amazon EMR on EKS 7.2.0 application upgrades include Spark 3.5.1, Flink 1.18.1, and [Flink Operator](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-kubernetes-operator.html) 1.8.0.
+ **[ Autoscaler for Flink updates](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-autoscaler.html)** – The 7.2.0 release uses the open source configuration `job.autoscaler.restart.time-tracking.enabled` to enable rescale time estimation, so you no longer have to manually assign empirical values to restart time. If you run 7.1.0 or lower, you can still use Amazon EMR autoscaling. 
+ **[ Apache Hudi integration Apache Flink on Amazon EMR on EKS](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/tutorial-hudi-for-flink.html)** – This release adds an integration between Apache Hudi and Apache Flink, so you can use the Flink Kubernetes operator to run Hudi jobs. Hudi lets you use record-level operations that you can use to simplify data management and data pipeline development.
+ **[ Amazon S3 Express One Zone integration with Amazon EMR on EKS](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/upload-data-s3-express.html)** – With 7.2.0 and higher, you can upload data into the S3 Express One Zone with Amazon EMR on EKS. S3 Express One Zone is a a high-performance, single-zone Amazon S3 storage class that delivers consistent, single-digit millisecond data access for most latency-sensitive applications. At the time of its release, S3 Express One Zone delivers the lowest latency and highest performance cloud object storage in Amazon S3.
+ **[ Support for default configurations in the Spark operator](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/spark-operator-gs.html)** – Spark operator on Amazon EKS now supports the same default configurations as the start job run model on Amazon EMR on EKS for 7.2.0 and higher. This means that features such as Amazon S3 and EMRFS no longer require manual configurations in the yaml file.