# EMR clusters on AWS Local Zones

Beginning with Amazon EMR version 5.28.0, you can create and run Amazon EMR clusters on an
AWS Local Zones subnet as a logical extension of an AWS Region that supports Local Zones.
A Local Zone enables Amazon EMR features and a subset of AWS services, like compute and storage
services, to be located closer to users to provide very low latency access to applications
running locally. For a list of available Local Zones, see [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/ "https://aws.amazon.com/about-aws/global-infrastructure/localzones/"). For information about accessing available AWS Local Zones, see [Regions, Availability Zones, and local zones](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md").

## Supported instance types

The following instance types are available for Amazon EMR clusters on Local Zones. Instance
type availability may vary by Region.

| Instance class        | Instance types |
| --------------------- | -------------- | ------------ | ------------ | ------------ | ------------- | ------------- | ----------- | ------------ | ------------ | ------------ |
| **General purpose**   | m5.xlarge      | m5.2xlarge   | m5.4xlarge   | m5.12xlarge  | m5.24xlarge   | m5d.xlarge    | m5d.2xlarge | m5d.4xlarge  | m5d.12xlarge | m5d.24xlarge |
| **Compute-optimized** | c5.xlarge      | c5.2xlarge   | c5.4xlarge   | c5.9xlarge   | c5.18xlarge   | c5d.xlarge    | c5d.2xlarge | c5d.4xlarge  | c5d.9xlarge  | c5d.18xlarge |
| **Memory-optimized**  | r5.xlarge      | r5.2xlarge   | r5.4xlarge   | r5.12xlarge  | r5d.xlarge    | r5d.2xlarge   | r5d.4xlarge | r5d.12xlarge | r5d.24xlarge |
| **Storage-optimized** | i3en.xlarge    | i3en.2xlarge | i3en.3xlarge | i3en.6xlarge | i3en.12xlarge | i3en.24xlarge |

## Creating an Amazon EMR cluster on Local Zones

Create an Amazon EMR cluster on AWS Local Zones by launching the Amazon EMR cluster into an Amazon VPC
subnet that is associated with a Local Zone. You can access the cluster using the
Local Zone name, such as us-west-2-lax-1a in the US West (Oregon) Console.

Local Zones don't currently support Amazon EMR Notebooks or connections directly to Amazon EMR using
interface VPC endpoint (AWS PrivateLink).

Console

###### To create a cluster on a Local Zone with the console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left navigation pane, choose
   **Clusters**, and then choose **Create
   cluster**.
3. Under **Networking**, select an EC2 subnet with a Local Zone ID in
   this format: subnet 123abc | us-west-2-lax-1a.
4. Choose an instance type or add Amazon EBS storage volumes for uniform instance groups or
   instance fleets.
5. Choose any other options that apply to your cluster.
6. To launch your cluster, choose **Create
   cluster**.

CLI

###### To create a cluster on a Local Zone with the AWS CLI

- Use the create-cluster command, along with the SubnetId for the Local Zone as shown in the
  following example. Replace subnet-22XXXX1234567 with the Local Zone SubnetId and
  replace other options as necessary. For more information, see
  [https://docs.aws.amazon.com/cli/latest/reference/emr/create-cluster.html](../../../cli/latest/reference/emr/create-cluster.md "../../../cli/latest/reference/emr/create-cluster.md").

```
aws emr create-cluster \
--name "Local Zones cluster" \
--release-label `emr-5.29.0` \
--applications Name=Spark \
--ec2-attributes KeyName=myKey,SubnetId=`subnet-22XXXX1234567` \
--instance-type m5.xlarge --instance-count 3 --use-default-roles
```
