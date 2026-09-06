

# Amazon EMR on EKS 6.14.0 releases
<a name="emr-eks-6.14.0"></a>

This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment. For details about Amazon EMR running on Amazon EC2 and about the Amazon EMR 6.14.0 release in general, see [Amazon EMR 6.14.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-6140-release.html) in the *Amazon EMR Release Guide*.

## Amazon EMR on EKS 6.14 releases
<a name="emr-eks-6.14.0-releases"></a>

The following Amazon EMR 6.14.0 releases are available for Amazon EMR on EKS. Select a specific **emr-6.14.0-XXXX** release to view more details such as the related container image tag.
+ [emr-6.14.0-latest](emr-eks-6.14.0-latest.md)
+ [emr-6.14.0-20231005](emr-eks-6.14.0-20231005.md)
+ emr-6.14.0-spark-rapids-latest
+ emr-6.14.0-spark-rapids-20231005
+ emr-6.14.0-java11-latest
+ emr-6.14.0-java11-20231005
+ emr-6.14.0-java17-latest
+ emr-6.14.0-java17-20231005
+ emr-6.14.0-java17-al2023-latest
+ emr-6.14.0-java17-al2023-20231005
+ emr-6.14.0-spark-rapids-java17-latest
+ emr-6.14.0-spark-rapids-java17-20231005
+ emr-6.14.0-spark-rapids-java17-al2023-latest
+ emr-6.14.0-spark-rapids-java17-al2023-20231005
+ notebook-spark/emr-6.14.0-latest
+ notebook-spark/emr-6.14.0-20231005
+ notebook-spark/emr-6.14.0-spark-rapids-latest
+ notebook-spark/emr-6.14.0-spark-rapids-20231005
+ notebook-spark/emr-6.14.0-java11-latest
+ notebook-spark/emr-6.14.0-java11-20231005
+ notebook-spark/emr-6.14.0-java17-latest
+ notebook-spark/emr-6.14.0-java17-20231005
+ notebook-spark/emr-6.14.0-java17-al2023-latest
+ notebook-spark/emr-6.14.0-java17-al2023-20231005
+ notebook-python/emr-6.14.0-latest
+ notebook-python/emr-6.14.0-20231005
+ notebook-python/emr-6.14.0-spark-rapids-latest
+ notebook-python/emr-6.14.0-spark-rapids-20231005
+ notebook-python/emr-6.14.0-java11-latest
+ notebook-python/emr-6.14.0-java11-20231005
+ notebook-python/emr-6.14.0-java17-latest
+ notebook-python/emr-6.14.0-java17-20231005
+ notebook-python/emr-6.14.0-java17-al2023-latest
+ notebook-python/emr-6.14.0-java17-al2023-20231005

## Release notes
<a name="emr-eks-6.14.0-rn"></a>

Release notes for Amazon EMR on EKS 6.14.0
+ **Supported applications** ‐ AWS SDK for Java 1.12.543, Apache Spark 3.4.1-amzn-1, Apache Hudi 0.13.1-amzn-2, Apache Iceberg 1.3.0-amzn-0, Delta 2.4.0, Apache Spark RAPIDS 23.06.0-amzn-2, Jupyter Enterprise Gateway 2.7.0
+ **Supported components** ‐ `aws-sagemaker-spark-sdk`, `emr-ddb`, `emr-goodies`, `emr-s3-select`, `emrfs`, `hadoop-client`, `hudi`, `hudi-spark`, `iceberg`, `spark-kubernetes`.
+ **Supported configuration classifications**

  For use with [StartJobRun](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_StartJobRun.html) and [ CreateManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.html) APIs:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.14.0.html)

  For use specifically with [ CreateManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.html) APIs:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.14.0.html)

  Configuration classifications allow you to customize applications. These often correspond to a configuration XML file for the application, such as `spark-hive-site.xml`. For more information, see [Configure Applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html).

## Notable features
<a name="emr-eks-6.14.0-features"></a>

The following features are included with the 6.14 release of Amazon EMR on EKS.
+ **[Apache Livy](https://livy.incubator.apache.org/) support** - Amazon EMR on EKS now supports Apache Livy with `spark-submit`.