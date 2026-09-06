

# Amazon EMR on EKS 6.11.0 releases
<a name="emr-eks-6.11.0"></a>

This page describes the new and updated functionality for Amazon EMR that is specific to the Amazon EMR on EKS deployment. For details about Amazon EMR running on Amazon EC2 and about the Amazon EMR 6.11.0 release in general, see [Amazon EMR 6.11.0](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-6110-release.html) in the *Amazon EMR Release Guide*.

## Amazon EMR on EKS 6.11 releases
<a name="emr-eks-6.11.0-releases"></a>

The following Amazon EMR 6.11.0 releases are available for Amazon EMR on EKS. Select a specific **emr-6.11.0-XXXX** release to view more details such as the related container image tag.
+ [emr-6.11.0-latest](emr-eks-6.11.0-latest.md)
+  [emr-6.11.0-20230905](emr-eks-6.11.0-20230905.md) 
+ [emr-6.11.0-20230509](emr-eks-6.11.0-20230509.md)
+ emr-6.11.0-spark-rapids-latest
+ emr-6.11.0-spark-rapids-20230509
+ emr-6.11.0-java11-latest
+ emr-6.11.0-java11-20230509
+ notebook-spark/emr-6.11.0-latest
+ notebook-spark/emr-6.11.0-20230509
+ notebook-python/emr-6.11.0-latest
+ notebook-python/emr-6.11.0-20230509

## Release notes
<a name="emr-eks-6.11.0-rn"></a>

Release notes for Amazon EMR on EKS 6.11.0
+ **Supported applications** ‐ AWS SDK for Java 1.12.446, Apache Spark 3.3.2-amzn-0, Apache Hudi 0.13.0-amzn-0, Apache Iceberg 1.2.0-amzn-0, Delta 2.2.0, Apache Spark RAPIDS 23.02.0-amzn-0, Jupyter Enterprise Gateway 2.6.0
+ **Supported components** ‐ `aws-sagemaker-spark-sdk`, `emr-ddb`, `emr-goodies`, `emr-s3-select`, `emrfs`, `hadoop-client`, `hudi`, `hudi-spark`, `iceberg`, `spark-kubernetes`.
+ **Supported configuration classifications**

  For use with [StartJobRun](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_StartJobRun.html) and [ CreateManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.html) APIs:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.11.0.html)

  For use specifically with [ CreateManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.html) APIs:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.11.0.html)

  Configuration classifications allow you to customize applications. These often correspond to a configuration XML file for the application, such as `spark-hive-site.xml`. For more information, see [Configure Applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html).

## Notable features
<a name="emr-eks-6.11.0-features"></a>

The following features are included with the 6.11 release of Amazon EMR on EKS.
+ **[Amazon EMR on EKS base image in Amazon ECR Public Gallery](docker-custom-images.md)** – If you use the [custom image](docker-custom-images.md) capability, our base image provides the essential jars, configuration, and libraries to interact with Amazon EMR on EKS. You can now find the base image in the [Amazon ECR Public Gallery](https://gallery.ecr.aws/emr-on-eks).
+ **[Spark container log rotation](emr-eks-log-rotation-container.md)** – Amazon EMR on EKS 6.11 supports Spark container log rotation. You can enable the capability with `containerLogRotationConfiguration` within the `MonitoringConfiguration` operation of the `StartJobRun` API. You can configure the `rotationSize` and `maxFilestoKeep` to specify the number and size of the log files that you want Amazon EMR on EKS to keep in the Spark driver and executor pods. For more information, see [Using Spark container log rotation](emr-eks-log-rotation-container.md).
+ **Volcano support in Spark operator and spark-submit** – Amazon EMR on EKS 6.11 supports running Spark jobs with Volcano as Kubernetes custom scheduler in [Spark operator]() and [spark-submit](). You can use features like gang scheduling, queue management, preemption, and fair-share scheduling to achieve high scheduling throughput and optimized capacity. For more information, see [Using Volcano as a custom scheduler for Apache Spark on Amazon EMR on EKS](tutorial-volcano.md).