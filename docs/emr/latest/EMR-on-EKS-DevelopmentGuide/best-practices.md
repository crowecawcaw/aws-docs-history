# Links to Amazon EMR on EKS best practices guides on GitHub

We've built the [Amazon EMR on EKS Best Practices Guide](https://aws.github.io/aws-emr-containers-best-practices/ "https://aws.github.io/aws-emr-containers-best-practices/") using open source community collaboration so
that we can iterate quickly and provide recommendations for aspects of creating and running a virtual cluster. We
recommend that you use the [Amazon EMR on EKS best practices
guide](https://aws.github.io/aws-emr-containers-best-practices/ "https://aws.github.io/aws-emr-containers-best-practices/") for the sections. Choose the links in each section to go to the GitHub
site.

## Security

###### Note

For more information on security with Amazon EMR on EKS, see [Amazon EMR on EKS security best practices](security-best-practices.md "security-best-practices.md").

[Encryption best practices:](https://aws.github.io/aws-emr-containers-best-practices/security/docs/spark/encryption/ "https://aws.github.io/aws-emr-containers-best-practices/security/docs/spark/encryption/") how to use encryption for data at rest and in
transit.

[Managing network security](https://aws.github.io/aws-emr-containers-best-practices/security/docs/spark/network-security/ "https://aws.github.io/aws-emr-containers-best-practices/security/docs/spark/network-security/") describes how to configure security groups for
pods for Amazon EMR on EKS while you connect to data sources that are hosted in AWS services
like Amazon RDS and Amazon Redshift.

[Using AWS secrets manager to store secrets](https://aws.github.io/aws-emr-containers-best-practices/security/docs/spark/encryption/ "https://aws.github.io/aws-emr-containers-best-practices/security/docs/spark/encryption/").

## Pyspark job submission

[Pyspark job submission:](https://aws.github.io/aws-emr-containers-best-practices/submit-applications/docs/spark/pyspark/ "https://aws.github.io/aws-emr-containers-best-practices/submit-applications/docs/spark/pyspark/") specifies different types of packaging for pySpark
applications using packaging formats like zip, egg, wheel, and pex.

## Storage

[Using EBS volumes:](https://aws.github.io/aws-emr-containers-best-practices/storage/docs/spark/ebs/ "https://aws.github.io/aws-emr-containers-best-practices/storage/docs/spark/ebs/"): how to use static and dynamic provisioning for jobs
that need EBS volumes.

[Using Amazon FSx for Lustre volumes:](https://aws.github.io/aws-emr-containers-best-practices/storage/docs/spark/fsx-lustre/ "https://aws.github.io/aws-emr-containers-best-practices/storage/docs/spark/fsx-lustre/") how to use static and dynamic provisioning
for jobs that need Amazon FSx for Luster volumes.

[Using Instance store volumes:](https://aws.github.io/aws-emr-containers-best-practices/storage/docs/spark/instance-store/ "https://aws.github.io/aws-emr-containers-best-practices/storage/docs/spark/instance-store/") how to use instance store volumes for job
processing.

## Metastore integration

[Using Hive metastore:](https://aws.github.io/aws-emr-containers-best-practices/metastore-integrations/docs/hive-metastore/ "https://aws.github.io/aws-emr-containers-best-practices/metastore-integrations/docs/hive-metastore/") offers different ways to use Hive metastore.

[Using AWS Glue:](https://aws.github.io/aws-emr-containers-best-practices/metastore-integrations/docs/hive-metastore/ "https://aws.github.io/aws-emr-containers-best-practices/metastore-integrations/docs/hive-metastore/") offers different ways to configure AWS Glue catalog.

## Debugging

[Using Spark debugging:](https://aws.github.io/aws-emr-containers-best-practices/troubleshooting/docs/change-log-level/ "https://aws.github.io/aws-emr-containers-best-practices/troubleshooting/docs/change-log-level/") how to change the log level.

[Connecting to Spark UI on the driver pod](https://aws.github.io/aws-emr-containers-best-practices/troubleshooting/docs/connect-spark-ui/ "https://aws.github.io/aws-emr-containers-best-practices/troubleshooting/docs/connect-spark-ui/").

[How to use self-hosted Spark history server with Amazon EMR on EKS](https://aws.github.io/aws-emr-containers-best-practices/troubleshooting/docs/self-hosted-shs/ "https://aws.github.io/aws-emr-containers-best-practices/troubleshooting/docs/self-hosted-shs/").

## Troubleshooting Amazon EMR on EKS issues

[Troubleshooting](https://aws.github.io/aws-emr-containers-best-practices/troubleshooting/docs/where-to-look-for-spark-logs/ "https://aws.github.io/aws-emr-containers-best-practices/troubleshooting/docs/where-to-look-for-spark-logs/").

## Node placement

[Using Kubernetes node selectors](https://aws.github.io/aws-emr-containers-best-practices/node-placement/docs/eks-node-placement/ "https://aws.github.io/aws-emr-containers-best-practices/node-placement/docs/eks-node-placement/") for `single-az` and other use
cases.

[Using Fargate node placement](https://aws.github.io/aws-emr-containers-best-practices/node-placement/docs/fargate-node-placement/ "https://aws.github.io/aws-emr-containers-best-practices/node-placement/docs/fargate-node-placement/").

## Performance

[Using Dynamic Resource Allocation (DRA)](https://aws.github.io/aws-emr-containers-best-practices/performance/docs/dra/ "https://aws.github.io/aws-emr-containers-best-practices/performance/docs/dra/").

[EKS best practices](https://aws.github.io/aws-emr-containers-best-practices/best-practices-and-recommendations/eks-best-practices/ "https://aws.github.io/aws-emr-containers-best-practices/best-practices-and-recommendations/eks-best-practices/") for the Amazon VPC Container Network Interface plugin (CNI),
Cluster Autoscaler, and Core DNS.

## Cost optimization

[Using spot instances:](https://aws.github.io/aws-emr-containers-best-practices/cost-optimization/docs/cost-optimization/ "https://aws.github.io/aws-emr-containers-best-practices/cost-optimization/docs/cost-optimization/") Amazon EC2 spot instance best practices and how to use the
Spark node decommission feature.

## Using AWS Outposts

[Running Amazon EMR on EKS using AWS Outposts](https://aws.github.io/aws-emr-containers-best-practices/outposts/emr-containers-on-outposts/ "https://aws.github.io/aws-emr-containers-best-practices/outposts/emr-containers-on-outposts/")
