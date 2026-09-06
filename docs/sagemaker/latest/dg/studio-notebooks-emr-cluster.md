

# Data preparation using Amazon EMR
<a name="studio-notebooks-emr-cluster"></a>

**Important**  
Amazon SageMaker Studio and Amazon SageMaker Studio Classic are two of the machine learning environments that you can use to interact with SageMaker AI.  
If your domain was created after November 30, 2023, Studio is your default experience.  
If your domain was created before November 30, 2023, Amazon SageMaker Studio Classic is your default experience. To use Studio if Amazon SageMaker Studio Classic is your default experience, see [Migration from Amazon SageMaker Studio Classic](studio-updated-migrate.md).  
When you migrate from Amazon SageMaker Studio Classic to Amazon SageMaker Studio, there is no loss in feature availability. Studio Classic also exists as an application within Amazon SageMaker Studio to help you run your legacy machine learning workflows.

Amazon SageMaker Studio and Studio Classic come with built-in integration with [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html). Within JupyterLab and Studio Classic notebooks, data scientists and data engineers can discover and connect to existing Amazon EMR clusters, then interactively explore, visualize, and prepare large-scale data for machine learning using [Apache Spark](https://aws.amazon.com/emr/features/spark), [Apache Hive](https://aws.amazon.com/emr/features/hive), or [Presto](https://aws.amazon.com/emr/features/presto). With a single click, they can access the Spark UI to monitor the status and metrics of their Spark jobs without leaving their notebook.

Administrators can create [CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) that define Amazon EMR clusters. They can then make those cluster templates available in the [AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/userguide/end-user-console.html) for Studio and Studio Classic users to launch. Data scientists can then choose a predefined template to self-provision an Amazon EMR cluster directly from their Studio environment. Administrators can further parameterize the templates to let users choose aspects of the cluster within predefined values. For example, users may want to specify the number of core nodes or select the instance type of a node from a dropdown menu.

Using CloudFormation, administrators can control the organizational, security, and networking setup of Amazon EMR clusters. Data scientists and data engineers can then customize those templates for their workloads to create on-demand Amazon EMR clusters directly from Studio and Studio Classic without setting up complex configurations. Users can terminate Amazon EMR clusters after use.
+ **If you are an administrator**:

  Ensure that you have enabled communication between Studio or Studio Classic and Amazon EMR clusters. For instructions, see the [Configure network access for your Amazon EMR cluster](studio-notebooks-emr-networking.md) section. Once this communication is enabled, you can:
  + [Configure Amazon EMR CloudFormation templates in the Service Catalog](studio-notebooks-set-up-emr-templates.md)
  + [Configure listing Amazon EMR clusters](studio-notebooks-configure-discoverability-emr-cluster.md)
+ **If you are a data scientist or data engineer**, you can:
  + [Launch an Amazon EMR cluster from Studio or Studio Classic](studio-notebooks-launch-emr-cluster-from-template.md)
  + [List Amazon EMR clusters from Studio or Studio Classic](discover-emr-clusters.md)
  + [Connect to an Amazon EMR cluster from SageMaker Studio or Studio Classic](connect-emr-clusters.md)
  + [Terminate an Amazon EMR cluster from Studio or Studio Classic](terminate-emr-clusters.md)
  + [Access Spark UI from Studio or Studio Classic](studio-notebooks-access-spark-ui.md)

**Topics**
+ [Quickstart: Create a SageMaker AI sandbox domain to launch Amazon EMR clusters in Studio](studio-notebooks-emr-cluster-quickstart.md)
+ [Admin guide](studio-emr-admin-guide.md)
+ [User guide](studio-emr-user-guide.md)
+ [Blogs and whitepapers](studio-notebooks-emr-resources.md)
+ [Troubleshooting](studio-notebooks-emr-troubleshooting.md)