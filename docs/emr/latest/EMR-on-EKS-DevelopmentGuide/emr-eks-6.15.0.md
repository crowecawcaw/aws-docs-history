

# Amazon EMR on EKS 6.15.0 releases
<a name="emr-eks-6.15.0"></a>

This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment. For details about Amazon EMR running on Amazon EC2 and about the Amazon EMR 6.15.0 release in general, see [Amazon EMR 6.15.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-6115-release.html) in the *Amazon EMR Release Guide*.

## Amazon EMR on EKS 6.15 releases
<a name="emr-eks-6.15.0-releases"></a>

The following Amazon EMR 6.15.0 releases are available for Amazon EMR on EKS. Select a specific **emr-6.15.0-XXXX** release to view more details such as the related container image tag.

------
#### [ Flink releases ]

The following Amazon EMR 6.15.0 releases are available for Amazon EMR on EKS when you run Flink applications.
+ [emr-6.15.0-flink-latest](emr-eks-6.15.0-flink-latest.md)
+  [emr-6.15.0-flink-20240105](emr-eks-6.15.0-flink-20240105.md) 
+ [emr-6.15.0-flink-20231109](emr-eks-6.15.0-flink-20231109.md)

------
#### [ Spark releases ]

The following Amazon EMR 6.15.0 releases are available for Amazon EMR on EKS when you run Spark applications.
+ [emr-6.15.0-latest](emr-eks-6.15.0-latest.md)
+ [emr-6.15.0-20231109](emr-eks-6.15.0-20231109.md)
+ emr-6.15.0-spark-rapids-latest
+ emr-6.15.0-spark-rapids-20231109
+ emr-6.15.0-java11-latest
+ emr-6.15.0-java11-20231109
+ emr-6.15.0-java17-latest
+ emr-6.15.0-java17-20231109
+ emr-6.15.0-java17-al2023-latest
+ emr-6.15.0-java17-al2023-20231109
+ emr-6.15.0-spark-rapids-java17-latest
+ emr-6.15.0-spark-rapids-java17-20231109
+ emr-6.15.0-spark-rapids-java17-al2023-latest
+ emr-6.15.0-spark-rapids-java17-al2023-20231109
+ notebook-spark/emr-6.15.0-latest
+ notebook-spark/emr-6.15.0-20231109
+ notebook-spark/emr-6.15.0-spark-rapids-latest
+ notebook-spark/emr-6.15.0-spark-rapids-20231109
+ notebook-spark/emr-6.15.0-java11-latest
+ notebook-spark/emr-6.15.0-java11-20231109
+ notebook-spark/emr-6.15.0-java17-latest
+ notebook-spark/emr-6.15.0-java17-20231109
+ notebook-spark/emr-6.15.0-java17-al2023-latest
+ notebook-spark/emr-6.15.0-java17-al2023-20231109
+ notebook-python/emr-6.15.0-latest
+ notebook-python/emr-6.15.0-20231109
+ notebook-python/emr-6.15.0-spark-rapids-latest
+ notebook-python/emr-6.15.0-spark-rapids-20231109
+ notebook-python/emr-6.15.0-java11-latest
+ notebook-python/emr-6.15.0-java11-20231109
+ notebook-python/emr-6.15.0-java17-latest
+ notebook-python/emr-6.15.0-java17-20231109
+ notebook-python/emr-6.15.0-java17-al2023-latest
+ notebook-python/emr-6.15.0-java17-al2023-20231109

------

## Release notes
<a name="emr-eks-6.15.0-rn"></a>

Release notes for Amazon EMR on EKS 6.15.0
+ **Supported applications** ‐ AWS SDK for Java 1.12.569, Apache Spark 3.4.1-amzn-2, Apache Flink 1.17.1-amzn-1, Apache Hudi 0.14.0-amzn-0, Apache Iceberg 1.4.0-amzn-0, Delta 2.4.0, Apache Spark RAPIDS 23.08.01-amzn-0, Jupyter Enterprise Gateway 2.6.0
+ **Supported components** ‐ `aws-sagemaker-spark-sdk`, `emr-ddb`, `emr-goodies`, `emr-s3-select`, `emrfs`, `hadoop-client`, `hudi`, `hudi-spark`, `iceberg`, `spark-kubernetes`.
+ **Supported configuration classifications**

  For use with [StartJobRun](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_StartJobRun.html) and [ CreateManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.html) APIs:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.15.0.html)

  For use specifically with [ CreateManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.html) APIs:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.15.0.html)

  Configuration classifications allow you to customize applications. These often correspond to a configuration XML file for the application, such as `spark-hive-site.xml`. For more information, see [Configure Applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html).

## Notable features
<a name="emr-eks-6.15.0-features"></a>

The following features are included with the 6.15 release of Amazon EMR on EKS.
+ **[Amazon EMR on EKS with Apache Flink](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/run-flink-jobs.html)** - With Amazon EMR on EKS 6.15.0, you can run your Apache Flink-based application along with other types of applications on the same Amazon EKS cluster. This helps improve resource utilization and simplify infrastructure management. You can leverage Spot Instances in a Flink application with graceful decommission, and achieve faster restart times with fine-grained recovery and task-local recovery with Amazon EBS. Accessibility and monitoring features include the ability to launch a Flink application with jars that are stored in Amazon S3, access to the AWS Glue Data Catalog, monitoring integration with Amazon S3 and Amazon CloudWatch, and container log rotation.