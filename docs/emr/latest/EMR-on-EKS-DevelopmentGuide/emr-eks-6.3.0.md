

# Amazon EMR on EKS 6.3.0 releases
<a name="emr-eks-6.3.0"></a>

The following Amazon EMR 6.3.0 releases are available for Amazon EMR on EKS. Select a specific **emr-6.3.0-XXXX** release to view more details such as the related container image tag.
+ [emr-6.3.0-latest](emr-eks-6.3.0-latest.md)
+ [emr-6.3.0-20240321](emr-eks-6.3.0-20240321.md)
+ [emr-6.3.0-20220802](emr-eks-6.3.0-20220802.md)
+ [emr-6.3.0-20211008](emr-eks-6.3.0-20211008.md)
+ [emr-6.3.0-20210802](emr-eks-6.3.0-20210802.md)
+ [emr-6.3.0-20210429](emr-eks-6.3.0-20210429.md)

**Release notes for Amazon EMR 6.3.0**
+ New features ‐ Beginning with Amazon EMR 6.3.0 in the 6.x release series, Amazon EMR on EKS supports Spark’s pod template feature. You can also turn on the Spark event log rotation feature for Amazon EMR on EKS. For more information, see [Using pod templates](pod-templates.md) and [Using Spark event log rotation](emr-eks-log-rotation.md).
+ Supported applications ‐ Spark 3.1.1-amzn-0, Jupyter Enterprise Gateway (endpoints, public preview).
+ Supported components ‐ `aws-hm-client` (Glue connector), `aws-sagemaker-spark-sdk`, `emr-s3-select`, `emrfs`, `emr-ddb`, `hudi-spark`.
+ Supported configuration classifications:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.3.0.html)

  Configuration classifications allow you to customize applications. These often correspond to a configuration XML file for the application, such as spark-hive-site.xml. For more information, see [Configuring Applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html).