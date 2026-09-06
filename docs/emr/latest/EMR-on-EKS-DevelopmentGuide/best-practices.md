

# Links to Amazon EMR on EKS best practices guides on GitHub
<a name="best-practices"></a>

We've built the [Amazon EMR on EKS Best Practices Guide](https://aws.github.io/aws-emr-containers-best-practices/) using open source community collaboration so that we can iterate quickly and provide recommendations for aspects of creating and running a virtual cluster. We recommend that you use the [Amazon EMR on EKS best practices guide](https://aws.github.io/aws-emr-containers-best-practices/) for the sections. Choose the links in each section to go to the GitHub site.

## Security
<a name="security"></a>

**Note**  
For more information on security with Amazon EMR on EKS, see [Amazon EMR on EKS security best practices](security-best-practices.md).

[Encryption best practices:](https://aws.github.io/aws-emr-containers-best-practices/security/docs/spark/encryption/) how to use encryption for data at rest and in transit.

[Managing network security](https://aws.github.io/aws-emr-containers-best-practices/security/docs/spark/network-security/) describes how to configure security groups for pods for Amazon EMR on EKS while you connect to data sources that are hosted in AWS services like Amazon RDS and Amazon Redshift.

[Using AWS secrets manager to store secrets](https://aws.github.io/aws-emr-containers-best-practices/security/docs/spark/encryption/).

## Pyspark job submission
<a name="pyspark-job-submission"></a>

[Pyspark job submission:](https://aws.github.io/aws-emr-containers-best-practices/submit-applications/docs/spark/pyspark/) specifies different types of packaging for pySpark applications using packaging formats like zip, egg, wheel, and pex.

## Storage
<a name="storage"></a>

[Using EBS volumes:](https://aws.github.io/aws-emr-containers-best-practices/storage/docs/spark/ebs/): how to use static and dynamic provisioning for jobs that need EBS volumes.

[Using Amazon FSx for Lustre volumes:](https://aws.github.io/aws-emr-containers-best-practices/storage/docs/spark/fsx-lustre/) how to use static and dynamic provisioning for jobs that need Amazon FSx for Luster volumes.

[Using Instance store volumes:](https://aws.github.io/aws-emr-containers-best-practices/storage/docs/spark/instance-store/) how to use instance store volumes for job processing.

## Metastore integration
<a name="metastore-integration"></a>

[Using Hive metastore:](https://aws.github.io/aws-emr-containers-best-practices/metastore-integrations/docs/hive-metastore/) offers different ways to use Hive metastore.

[Using AWS Glue:](https://aws.github.io/aws-emr-containers-best-practices/metastore-integrations/docs/hive-metastore/) offers different ways to configure AWS Glue catalog.

## Debugging
<a name="debugging"></a>

[Using Spark debugging:](https://aws.github.io/aws-emr-containers-best-practices/troubleshooting/docs/change-log-level/) how to change the log level.

[Connecting to Spark UI on the driver pod](https://aws.github.io/aws-emr-containers-best-practices/troubleshooting/docs/connect-spark-ui/).

[How to use self-hosted Spark history server with Amazon EMR on EKS](https://aws.github.io/aws-emr-containers-best-practices/troubleshooting/docs/self-hosted-shs/).

## Troubleshooting Amazon EMR on EKS issues
<a name="troubleshooting"></a>

[Troubleshooting](https://aws.github.io/aws-emr-containers-best-practices/troubleshooting/docs/where-to-look-for-spark-logs/).

## Node placement
<a name="node-placement"></a>

[Using Kubernetes node selectors](https://aws.github.io/aws-emr-containers-best-practices/node-placement/docs/eks-node-placement/) for `single-az` and other use cases.

[Using Fargate node placement](https://aws.github.io/aws-emr-containers-best-practices/node-placement/docs/fargate-node-placement/).

## Performance
<a name="performance"></a>

[Using Dynamic Resource Allocation (DRA)](https://aws.github.io/aws-emr-containers-best-practices/performance/docs/dra/).

By default, `spark.dynamicAllocation.preallocateExecutors` is enabled in Amazon EMR Spark. When `spark.dynamicAllocation.initialExecutors` and `spark.dynamicAllocation.minExecutors` are not set, Spark may request a large number of executors at startup based on estimated task counts, even for small workloads. To avoid excessive container churn, use one of the following approaches:
+ Set `spark.dynamicAllocation.initialExecutors` or `spark.dynamicAllocation.minExecutors` to a value appropriate for your workload size.
+ Set `spark.dynamicAllocation.preallocateExecutors.maxEstimatedTasks` to a lower value to limit the number of executors requested at startup.
+ Set `spark.dynamicAllocation.preallocateExecutors` to `false` to disable executor preallocation entirely.

[EKS best practices](https://aws.github.io/aws-emr-containers-best-practices/best-practices-and-recommendations/eks-best-practices/) for the Amazon VPC Container Network Interface plugin (CNI), Cluster Autoscaler, and Core DNS.

## Cost optimization
<a name="cost-optimization"></a>

[Using spot instances:](https://aws.github.io/aws-emr-containers-best-practices/cost-optimization/docs/cost-optimization/) Amazon EC2 spot instance best practices and how to use the Spark node decommission feature.

## Using AWS Outposts
<a name="using-outposts"></a>

[Running Amazon EMR on EKS using AWS Outposts](https://aws.github.io/aws-emr-containers-best-practices/outposts/emr-containers-on-outposts/)