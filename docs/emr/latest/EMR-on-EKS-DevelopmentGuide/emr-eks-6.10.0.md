

# Amazon EMR on EKS 6.10.0 releases
<a name="emr-eks-6.10.0"></a>

The following Amazon EMR 6.10.0 releases are available for Amazon EMR on EKS. Select a specific **emr-6.10.0-XXXX** release to view more details such as the related container image tag.
+ [emr-6.10.0-latest](emr-eks-6.10.0-latest.md)
+  [emr-6.10.0-20230905](emr-eks-6.10.0-20230905.md) 
+ [emr-6.10.0-20230624](emr-eks-6.10.0-20230624.md)
+ [emr-6.10.0-20230421](emr-eks-6.10.0-20230421.md)
+ [emr-6.10.0-20230403](emr-eks-6.10.0-20230403.md)
+ [emr-6.10.0-20230220](emr-eks-6.10.0-20230220.md)
+ emr-6.10.0-spark-rapids-latest
+ emr-6.10.0-spark-rapids-20230624
+ emr-6.10.0-spark-rapids-20230220
+ emr-6.10.0-java11-latest
+ emr-6.10.0-java11-20230624
+ emr-6.10.0-java11-20230220
+ notebook-spark/emr-6.10.0-latest
+ notebook-spark/emr-6.10.0-20230624
+ notebook-spark/emr-6.10.0-20230220
+ notebook-python/emr-6.10.0-latest
+ notebook-python/emr-6.10.0-20230624
+ notebook-python/emr-6.10.0-20230220

**Release notes for Amazon EMR 6.10.0**
+ Supported applications ‐ AWS SDK for Java 1.12.397, Spark 3.3.1-amzn-0, Hudi 0.12.2-amzn-0, Iceberg 1.1.0-amzn-0, Delta 2.2.0.
+ Supported components ‐ `aws-sagemaker-spark-sdk`, `emr-ddb`, `emr-goodies`, `emr-s3-select`, `emrfs`, `hadoop-client`, `hudi`, `hudi-spark`, `iceberg`, `spark-kubernetes`.
+ Supported configuration classifications:

  For use with [StartJobRun](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_StartJobRun.html) and [ CreateManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.html) APIs:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.10.0.html)

  For use specifically with [ CreateManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.html) APIs:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.10.0.html)

  Configuration classifications allow you to customize applications. These often correspond to a configuration XML file for the application, such as `spark-hive-site.xml`. For more information, see [Configure Applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html).

**Notable features**
+ **Spark operator** - With Amazon EMR on EKS 6.10.0 and higher, you can use the Kubernetes operator for Apache Spark, or *the Spark operator*, to deploy and manage Spark applications with the Amazon EMR release runtime on your own Amazon EKS clusters. For more information, see [Running Spark jobs with the Spark operator](spark-operator.md).
+ **Java 11** - With Amazon EMR on EKS 6.10 and higher, you can launch Spark with Java 11 runtime. To do this, pass `emr-6.10.0-java11-latest` as a release label. We recommend that you validate and run performance tests before you move your production workloads from the Java 8 image to the Java 11 image.
+ For the Amazon Redshift integration for Apache Spark, Amazon EMR on EKS 6.10.0 removes the dependency on `minimal-json.jar`, and automatically adds the required `spark-redshift` related jars to the executor class path for Spark: `spark-redshift.jar`, `spark-avro.jar`, and `RedshiftJDBC.jar`.

**Changes**
+ EMRFS S3-optimized committer is now enabled by default for parquet, ORC, and text-based formats (including CSV and JSON).