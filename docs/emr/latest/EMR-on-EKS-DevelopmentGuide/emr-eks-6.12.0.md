

# Amazon EMR on EKS 6.12.0 releases
<a name="emr-eks-6.12.0"></a>

This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment. For details about Amazon EMR running on Amazon EC2 and about the Amazon EMR 6.12.0 release in general, see [Amazon EMR 6.12.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-6120-release.html) in the *Amazon EMR Release Guide*.

## Amazon EMR on EKS 6.12 releases
<a name="emr-eks-6.12.0-releases"></a>

The following Amazon EMR 6.12.0 releases are available for Amazon EMR on EKS. Select a specific **emr-6.12.0-XXXX** release to view more details such as the related container image tag.
+ [emr-6.12.0-latest](emr-eks-6.12.0-latest.md)
+  [emr-6.12.0-20240321](emr-eks-6.12.0-20240321.md) 
+ [emr-6.12.0-20230701](emr-eks-6.12.0-20230701.md)
+ emr-6.12.0-spark-rapids-latest
+ emr-6.12.0-spark-rapids-20230701
+ emr-6.12.0-java11-latest
+ emr-6.12.0-java11-20230701
+ emr-6.12.0-java17-latest
+ emr-6.12.0-java17-20230701
+ emr-6.12.0-spark-rapids-java17-latest
+ emr-6.12.0-spark-rapids-java17-20230701
+ notebook-spark/emr-6.12.0-latest
+ notebook-spark/emr-6.12.0-20230701
+ notebook-spark/emr-6.12.0-spark-rapids-latest
+ notebook-spark/emr-6.12.0-spark-rapids-20230701
+ notebook-python/emr-6.12.0-latest
+ notebook-python/emr-6.12.0-20230701
+ notebook-python/emr-6.12.0-spark-rapids-latest
+ notebook-python/emr-6.12.0-spark-rapids-20230701

## Release notes
<a name="emr-eks-6.12.0-rn"></a>

Release notes for Amazon EMR on EKS 6.12.0
+ **Supported applications** ‐ AWS SDK for Java 1.12.490, Apache Spark 3.4.0-amzn-0, Apache Hudi 0.13.1-amzn-0, Apache Iceberg 1.3.0-amzn-0, Delta 2.4.0, Apache Spark RAPIDS 23.06.0-amzn-0, Jupyter Enterprise Gateway 2.6.0****
+ **Supported components** ‐ `aws-sagemaker-spark-sdk`, `emr-ddb`, `emr-goodies`, `emr-s3-select`, `emrfs`, `hadoop-client`, `hudi`, `hudi-spark`, `iceberg`, `spark-kubernetes`.
+ **Supported configuration classifications**

  For use with [StartJobRun](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_StartJobRun.html) and [ CreateManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.html) APIs:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.12.0.html)

  For use specifically with [ CreateManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.html) APIs:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.12.0.html)

  Configuration classifications allow you to customize applications. These often correspond to a configuration XML file for the application, such as `spark-hive-site.xml`. For more information, see [Configure Applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html).

## Notable features
<a name="emr-eks-6.12.0-features"></a>

The following features are included with the 6.12 release of Amazon EMR on EKS.
+ **Java 17** - With Amazon EMR on EKS 6.12 and higher, you can launch Spark with Java 17 runtime. To do this, pass `emr-6.12.0-java17-latest` as a release label. We recommend that you validate and run performance tests before you move your production workloads from earlier versions of the Java image to the Java 17 image.