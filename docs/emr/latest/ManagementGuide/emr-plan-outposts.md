# EMR clusters on AWS Outposts

Beginning with Amazon EMR 5.28.0, you can create and run EMR clusters on AWS Outposts. AWS Outposts enables
native AWS services, infrastructure, and operating models in on-premises facilities. In
AWS Outposts environments, you can use the same AWS APIs, tools, and infrastructure that you use
in the AWS Cloud. Amazon EMR on AWS Outposts is ideal for low latency workloads that need to be run in
close proximity to on-premises data and applications. For more information about AWS Outposts, see
[AWS Outposts User
Guide](../../../outposts/latest/userguide.md "../../../outposts/latest/userguide.md").

## Prerequisites

The following are the prerequisites for using Amazon EMR on AWS Outposts:

- You must have installed and configured AWS Outposts in your on-premises data
  center.
- You must have a reliable network connection between your Outpost environment
  and an AWS Region.
- You must have sufficient capacity for Amazon EMR supported instance types available
  in your Outpost.

## Limitations

The following are the limitations of using Amazon EMR on AWS Outposts:

- On-Demand Instances are the only supported option for Amazon EC2 instances. Spot
  Instances are not available for Amazon EMR on AWS Outposts.
- If you need additional Amazon EBS storage volumes, only General Purpose SSD (GP2)
  is supported.
- When you use AWS Outposts with Amazon EMR releases 5.28 through 6.x, you can only use S3
  buckets that store objects in an AWS Region that you specify. With Amazon EMR 7.0.0
  and higher, Amazon EMR on AWS Outposts is also supported with the S3A
  filesystem client, prefix `s3a://`.
- Only the following instance types are supported by Amazon EMR on AWS Outposts:

| Instance class        | Instance types |
| --------------------- | -------------- | -------------- | -------------- | -------------- | --------------- | --------------- | ------------- | -------------- | -------------- | -------------- |
| **General purpose**   | `m5.xlarge`    | `m5.2xlarge`   | `m5.4xlarge`   | `m5.12xlarge`  | `m5.24xlarge`   | `m5d.xlarge`    | `m5d.2xlarge` | `m5d.4xlarge`  | `m5d.12xlarge` | `m5d.24xlarge` |
| **Compute-optimized** | `c5.xlarge`    | `c5.2xlarge`   | `c5.4xlarge`   | `c5.18xlarge`  | `c5d.xlarge`    | `c5d.2xlarge`   | `c5d.4xlarge` | `c5d.18xlarge` |
| **Memory-optimized**  | `r5.xlarge`    | `r5.2xlarge`   | `r5.4xlarge`   | `r5.12xlarge`  | `r5d.xlarge`    | `r5d.2xlarge`   | `r5d.4xlarge` | `r5d.12xlarge` | `r5d.24xlarge` |
| **Storage-optimized** | `i3en.xlarge`  | `i3en.2xlarge` | `i3en.3xlarge` | `i3en.6xlarge` | `i3en.12xlarge` | `i3en.24xlarge` |

| ## Network connectivity considerations <br>• If network connectivity between your Outpost and its AWS Region is lost, your clusters will continue to run. However, you cannot create new clusters or take new actions on existing clusters until connectivity is restored. In case of instance failures, the instance will not be automatically replaced. Additionally, actions such as adding steps to a running cluster, checking step execution status, and sending CloudWatch metrics and events will be delayed. <br>• We recommend that you provide reliable and highly available network connectivity between your Outpost and the AWS Region. If network connectivity between your Outpost and its AWS Region is lost for more than a few hours, clusters that have enabled terminate protection will continue to run, and clusters that have disabled terminate protection may be terminated. <br>• If network connectivity will be impacted due to routine maintenance, we recommend proactively enabling terminate protection. More generally, connectivity interruption means that any external dependencies that are not local to the Outpost or customer network will not be accessible. This includes Amazon S3, DynamoDB used with EMRFS consistency view, and Amazon RDS if an in-region instance is used for an Amazon EMR cluster with multiple primary nodes. ## Creating an Amazon EMR cluster on AWS Outposts Creating an Amazon EMR cluster on AWS Outposts is similar to creating an Amazon EMR cluster in the AWS Cloud. When you create an Amazon EMR cluster on AWS Outposts, you must specify an Amazon EC2 subnet associated with your Outpost. An Amazon VPC can span all of the Availability Zones in an AWS Region. AWS Outposts are extensions of Availability Zones, and you can extend an Amazon VPC in an account to span multiple Availability Zones and associated Outpost locations. When you configure your Outpost, you associate a subnet with it to extend your Regional VPC environment to your on-premises facility. Outpost instances and related services appear as part of your Regional VPC, similar to an Availability Zone with associated subnets. For information, see [AWS Outposts User Guide](../../../outposts/latest/userguide.md "../../../outposts/latest/userguide.md"). **Console** To create a new Amazon EMR cluster on AWS Outposts with the AWS Management Console, specify an Amazon EC2 subnet that is associated with your Outpost. Console ###### To create a cluster on AWS Outposts with the console 1. Sign in to the AWS Management Console, and open the Amazon EMR console at [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr"). 2. Under **EMR on EC2** in the left navigation pane, choose **Clusters**, and then choose **Create cluster**. 3. Under **Cluster configuration**, select **Instance groups** or **Instance fleets**. Then, choose an instance type from the **Choose EC2 instance type** dropdown menu or select **Actions** and choose **Add EBS volumes**. Amazon EMR on AWS Outposts supports limited Amazon EBS volume and instance types. 4. Under **Networking**, select an EC2 subnet with an Outpost ID in this format: op-123456789. 5. Choose any other options that apply to your cluster. 6. To launch your cluster, choose **Create cluster**. CLI ###### To create a cluster on AWS Outposts with the AWS CLI <br>• To create a new Amazon EMR cluster on AWS Outposts with the AWS CLI, specify an EC2 subnet that is associated with your Outpost, as in the following example. Replace `subnet-22XXXX01` with your own Amazon EC2 subnet ID. ``aws emr create-cluster \ --name "Outpost cluster" \ --release-label `emr-7.10.0` \ --applications Name=Spark \ --ec2-attributes KeyName=myKey SubnetId=`subnet-22XXXX01` \ --instance-type m5.xlarge --instance-count 3 --use-default-roles``
