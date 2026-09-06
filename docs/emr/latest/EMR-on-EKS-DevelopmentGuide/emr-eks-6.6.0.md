

# Amazon EMR on EKS 6.6.0 releases
<a name="emr-eks-6.6.0"></a>

The following Amazon EMR 6.6.0 releases are available for Amazon EMR on EKS. Select a specific **emr-6.6.0-XXXX** release to view more details such as the related container image tag.
+ [emr-6.6.0-latest](emr-eks-6.6.0-latest.md)
+ [emr-6.6.0-20240321](emr-eks-6.6.0-20240321.md)
+ [emr-6.6.0-20230624](emr-eks-6.6.0-20230624.md)
+ [emr-6.6.0-20221219](emr-eks-6.6.0-20221219.md)
+ [emr-6.6.0-20220411](emr-eks-6.6.0-20220411.md)

**Release notes for Amazon EMR 6.6.0**
+ Supported applications ‐ Spark 3.2.0-amzn-0, Jupyter Enterprise Gateway (endpoints, public preview), Hudi 0.10.1-amzn-0, Iceberg 0.13.1.
+ Supported components ‐ `aws-hm-client` (Glue connector), `aws-sagemaker-spark-sdk`, `emr-s3-select`, `emrfs`, `emr-ddb`, `hudi-spark`.
+ Supported configuration classifications:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.6.0.html)

  Configuration classifications allow you to customize applications. These often correspond to a configuration XML file for the application, such as spark-hive-site.xml. For more information, see [Configuring Applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html).

**Known issue**
+ Spark pod template functionality with interactive endpoints is not working in Amazon EMR on EKS release 6.4, 6.5, and 6.6.

**Resolved issue**
+ Interactive endpoint logs are uploaded to Cloudwatch and S3.