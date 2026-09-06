

# Amazon EMR on EKS 6.7.0 releases
<a name="emr-eks-6.7.0"></a>

The following Amazon EMR 6.7.0 releases are available for Amazon EMR on EKS. Select a specific **emr-6.7.0-XXXX** release to view more details such as the related container image tag.
+ [emr-6.7.0-latest](emr-eks-6.7.0-latest.md)
+ [emr-6.7.0-20240321](emr-eks-6.7.0-20240321.md)
+ [emr-6.7.0-20230624](emr-eks-6.7.0-20230624.md)
+ [emr-6.7.0-20221219](emr-eks-6.7.0-20221219.md)
+ [emr-6.7.0-20220630](emr-eks-6.7.0-20220630.md)

**Release notes for Amazon EMR 6.7.0**
+ Supported applications ‐ Spark 3.2.1-amzn-0, Jupyter Enterprise Gateway 2.6, Hudi 0.11-amzn-0, Iceberg 0.13.1.
+ Supported components ‐ `aws-hm-client` (Glue connector), `aws-sagemaker-spark-sdk`, `emr-s3-select`, `emrfs`, `emr-ddb`, `hudi-spark`.
+ With the upgrade to JEG 2.6, kernel management is now asynchronous, which means that JEG does not block transactions when a kernel launch is in progress. This greatly improves the user experience by providing the following:
  + capability to execute commands in currently running notebooks when other kernel launches are in progress
  + capability to launch multiple kernels simultaneously without impacting already running kernels
+ Supported configuration classifications:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-6.7.0.html)

  Configuration classifications allow you to customize applications. These often correspond to a configuration XML file for the application, such as `spark-hive-site.xml`. For more information, see [Configuring Applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html).

**Resolved issues**
+ Amazon EMR on EKS 6.7 fixes an issue in 6.6 when using Apache Spark's pod templates functionality with interactive endpoints. The issue was present in Amazon EMR on EKS releases 6.4, 6.5 and 6.6. You can now use pod templates to define how your Spark driver and executor pods start when using interactive endpoints to run interactive analytics.
+ In previous Amazon EMR on EKS releases, Jupyter Enterprise Gateway would block transactions when kernel launch was in progress, and this impeded the execution of currently running notebook sessions. You can now execute commands in currently running notebooks when other kernel launches are in progress. You can also launch multiple kernels simultaneously without the risk of losing connectivity to kernels that are already running.