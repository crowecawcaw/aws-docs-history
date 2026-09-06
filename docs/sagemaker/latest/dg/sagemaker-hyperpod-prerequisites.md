

# Prerequisites for using SageMaker HyperPod
<a name="sagemaker-hyperpod-prerequisites"></a>

The following sections walk you through prerequisites before getting started with SageMaker HyperPod.

**Topics**
+ [SageMaker HyperPod quotas](#sagemaker-hyperpod-prerequisites-quotas)
+ [Setting up SageMaker HyperPod with a custom Amazon VPC](#sagemaker-hyperpod-prerequisites-optional-vpc)
+ [Setting up SageMaker HyperPod clusters across multiple AZs](#sagemaker-hyperpod-prerequisites-multiple-availability-zones)
+ [Setting up AWS Systems Manager and Run As for cluster user access control](#sagemaker-hyperpod-prerequisites-ssm)
+ [(Optional) Setting up SageMaker HyperPod with Amazon FSx for Lustre](#sagemaker-hyperpod-prerequisites-optional-fsx)

## SageMaker HyperPod quotas
<a name="sagemaker-hyperpod-prerequisites-quotas"></a>

You can create SageMaker HyperPod clusters given the quotas for *cluster usage* in your AWS account.

**Important**  
To learn more about SageMaker HyperPod pricing, see [SageMaker HyperPod pricing](sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-pricing) and [Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/).

### View Amazon SageMaker HyperPod quotas using the AWS Management Console
<a name="sagemaker-hyperpod-prerequisites-quotas-view"></a>

Look up the default and applied values of a *quota*, also referred to as a *limit*, for *cluster usage*, which is used for SageMaker HyperPod.

1. Open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/).

1. In the left navigation pane, choose **AWS services**.

1. From the **AWS services** list, search for and select **Amazon SageMaker AI**.

1. In the **Service quotas** list, you can see the service quota name, applied value (if it's available), AWS default quota, and whether the quota value is adjustable. 

1. In the search bar, type **cluster usage**. This shows quotas for cluster usage, applied quotas, and the default quotas.

**List of common service quotas to create a HyperPod cluster and its pre-requisites**

You might want to check if you have requested service quota limit increases for the following quotas to create a new HyperPod cluster along with pre-requisites in the SageMaker AI console. Navigate to the **Service Quota** console and search for the following terms.



| No | Quota Name | Search Term | Description | 
| --- | --- | --- | --- | 
| 1 | Maximum number instances allowed per SageMaker HyperPod cluster | Under SageMaker AI search for “Maximum number instances allowed per SageMaker HyperPod cluster” | Your account-level quota value must be more than the number of instance you wish to add to your cluster | 
| 2 | Maximum size of EBS volume in GB for a SageMaker HyperPod cluster instance | Under SageMaker AI search for “Maximum size of EBS volume in GB for a HyperPod cluster instance”  | Your account-level quota value must be more than the EBS volume you wish to add to your cluster | 
| 3 | Total number of instances allowed across SageMaker HyperPod clusters | Under SageMaker AI search for  “Total number of instances allowed across SageMaker HyperPod clusters”  | Your account-level quota value must be more than the total instances you wish to add across all your clusters in your account in aggregate | 
| 4 | Instance Quotas  | Under SageMaker AI search for  "ml.<instance\_type> for cluster usage" eg: ml.p5.48xlarge for cluster usage | Your account-level quota value for the particular instance type (eg: ml.p5.48xlarge) must be greater than the number of instances to add across all your clusters in your account in aggregate. | 
| 5 | VPCs per Region | Under Amazon Virtual Private Cloud (Amazon VPC) search for “VPCs per Region" | Your account-level quota value must be enough to create a new VPC in the account when setting up your HyperPod cluster. Do check if you have already exhausted this quota limit by checking the VPC console. This quota increase is only needed if you will create a new VPC via the Quick or Custom cluster setup option in the SageMaker HyperPod console. | 
| 6 | Internet gateways per Region | Under Amazon Virtual Private Cloud (Amazon VPC) search for “Internet gateways per Region" | Your account-level quota value must be enough to create one additional Internet gateway in the account when setting up your SageMaker HyperPod cluster. This quota increase is only needed if you will create a new VPC via the Quick or Custom cluster setup option in the SageMaker HyperPod console.  | 
| 7 | Network interfaces per Region | Under Amazon Virtual Private Cloud (Amazon VPC) search for “Network interfaces per Region" | Your account-level quota value must have enough Network Interfaces in the account when setting up your HyperPod cluster.  | 
| 8 | EC2-VPC Elastic IPs | Under Amazon Elastic Compute Cloud (Amazon EC2) search for “EC2-VPC Elastic IPs" | Your account-level quota value must be enough to create a new VPC in the account when setting up your HyperPod cluster. Do check whether you have already exhausted this quota limit by checking the VPC console. This quota increase is only needed if you will create a new VPC via the Quick or Custom cluster setup option in the SageMaker HyperPod console. | 

### Request a Amazon SageMaker HyperPod quota increase using the AWS Management Console
<a name="sagemaker-hyperpod-prerequisites-quotas-increase"></a>

Increase your quotas at the account or resource level.

1. To increase the quota of instances for *cluster usage*, select the quota that you want to increase.

1. If the quota is adjustable, you can request a quota increase at either the account level or resource level based on the value listed in the **Adjustability** column.

1. For **Increase quota value**, enter the new value. The new value must be greater than the current value.

1. Choose **Request**.

1. To view any pending or recently resolved requests in the console, navigate to the **Request history** tab from the service's details page, or choose **Dashboard** from the navigation pane. For pending requests, choose the status of the request to open the request receipt. The initial status of a request is **Pending**. After the status changes to **Quota requested**, you see the case number with AWS Support. Choose the case number to open the ticket for your request.

To learn more about requesting a quota increase in general, see [Requesting a Quota Increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *AWS Service Quotas User Guide*.

## Setting up SageMaker HyperPod with a custom Amazon VPC
<a name="sagemaker-hyperpod-prerequisites-optional-vpc"></a>

To set up a SageMaker HyperPod cluster with a custom Amazon VPC, review the following prerequisites.

**Note**  
VPC configuration is mandatory for Amazon EKS orchestration. For Slurm orchestration, VPC setup is optional.
+  Validate [Elastic Network Interface](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) (ENI) capacity in your AWS account before creating a SageMaker HyperPod cluster with a custom VPC. The ENI limit is controlled by Amazon EC2 and varies by AWS Region. SageMaker HyperPod cannot automatically request quota increases. 

**To verify your current ENI quota:**

  1. Open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/).

  1. In the **Manage quotas** section, use the ** AWS Services** drop-down list to search for **VPC**. 

  1. Choose to view the quotas of **Amazon Virtual Private Cloud (Amazon VPC)**. 

  1. Look for the service quota **Network interfaces per Region** or the **Quota code** `L-DF5E4CA3`.

  If your current ENI limit is insufficient for your SageMaker HyperPod cluster needs, request a quota increase. Ensuring adequate ENI capacity beforehand helps prevent cluster deployment failures.
+ When using a custom VPC to connect a SageMaker HyperPod cluster with AWS resources, provide the VPC name, ID, AWS Region, subnet IDs, and security group IDs during cluster creation.
**Note**  
When your Amazon VPC and subnets support IPv6 in the [`VPCConfig`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateCluster.html#sagemaker-CreateCluster-request-VpcConfig) of the cluster or at the Instance group level using the `OverrideVPCConfig` attribute of [`ClusterInstanceGroupSpecification`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterInstanceGroupSpecification.html), network communications differ based on the cluster orchestration platform:  
Slurm-orchestrated clusters automatically configure nodes with dual IPv6 and IPv4 addresses, allowing immediate IPv6 network communications. No additional configuration is required beyond the `VPCConfig` IPv6 settings.
In EKS-orchestrated clusters, nodes receive dual-stack addressing, but pods can only use IPv6 when the Amazon EKS cluster is explicitly IPv6-enabled. You must create a new IPv6 Amazon EKS cluster - existing IPv4 Amazon EKS clusters cannot be converted to IPv6. For information about deploying an IPv6 Amazon EKS cluster, see [Amazon EKS IPv6 Cluster Deployment](https://docs.aws.amazon.com/eks/latest/userguide/deploy-ipv6-cluster.html#_deploy_an_ipv6_cluster_with_eksctl).
Additional resources for IPv6 configuration:  
For information about adding IPv6 support to your VPC, see to [IPv6 Support for VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-migrate-ipv6.html).
For information about creating a new IPv6-compatible VPC, see [Amazon VPC Creation Guide](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html).
To configure SageMaker HyperPod with a custom Amazon VPC, see [Custom Amazon VPC setup for SageMaker HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-prerequisites.html#sagemaker-hyperpod-prerequisites-optional-vpc).
+ Make sure that all resources are deployed in the same AWS Region as the SageMaker HyperPod cluster. Configure security group rules to allow inter-resource communication within the VPC. For example, when creating a VPC in `us-west-2`, provision subnets across one or more Availability Zones (such as `us-west-2a` or `us-west-2b`), and create a security group allowing intra-group traffic.
**Note**  
SageMaker HyperPod supports multi-Availability Zone deployment. For more information, see [Setting up SageMaker HyperPod clusters across multiple AZs](#sagemaker-hyperpod-prerequisites-multiple-availability-zones).
+ Establish Amazon Simple Storage Service (Amazon S3) connectivity for VPC-deployed SageMaker HyperPod instance groups by creating a VPC endpoint. Without internet access, instance groups cannot store or retrieve lifecycle scripts, training data, or model artifacts. We recommend that you create a custom IAM policy restricting Amazon S3 bucket access to the private VPC. For more information, see [Endpoints for Amazon S3](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-endpoints-s3.html) in the *AWS PrivateLink Guide*.
+ For HyperPod clusters using Elastic Fabric Adapter (EFA)-enabled instances, configure the security group to allow all inbound and outbound traffic to and from the security group itself. Specifically, avoid using `0.0.0.0/0` for outbound rules, as this may cause EFA health check failures. For more information about EFA security group preparation guidelines, see [Step 1: Prepare an EFA-enabled security group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-start.html#efa-start-security) in the *Amazon EC2 User Guide*.
+ Consider your subnet's Classless Inter-Domain Routing (CIDR) block size carefully before creating HyperPod clusters.
  + The subnet CIDR block size cannot be changed after creation. This is especially important when you use large accelerated instances like P5. Without sufficient block size, you must recreate your clusters when scaling up.
  + When choosing the appropriate subnet CIDR block size, consider these factors: your instance types, expected number of instances, and the number of IP addresses consumed by each instance.
  + For Slurm-orchestrated clusters, each P5 instance can create 32 IP addresses (one per network card). For EKS-orchestrated clusters, each P5 instance can create 81 IP addresses (50 from the primary card plus one from each of the remaining 31 cards). For detailed specifications, see [Network specifications ](https://docs.aws.amazon.com/ec2/latest/instancetypes/ac.html#ac_network) from *Amazon EC2 Instance Types Developer Guide*.
  + For examples of CloudFormation templates that specify the subnet CIDR block size, see the [HyperPod Slurm template](https://github.com/aws-samples/awsome-distributed-training/blob/main/1.architectures/5.sagemaker-hyperpod/sagemaker-hyperpod.yaml) and [HyperPod Amazon EKS template](https://github.com/aws-samples/awsome-distributed-training/blob/main/1.architectures/7.sagemaker-hyperpod-eks/cfn-templates/nested-stacks/private-subnet-stack.yaml) in the [awsome-distributed-training repository](https://github.com/aws-samples/awsome-distributed-training/tree/main).

## Setting up SageMaker HyperPod clusters across multiple AZs
<a name="sagemaker-hyperpod-prerequisites-multiple-availability-zones"></a>

You can configure your SageMaker HyperPod clusters across multiple Availability Zones (AZs) to improve reliability and availability.

**Note**  
Elastic Fabric Adapter (EFA) traffic cannot cross AZs or VPCs. This does not apply to normal IP traffic from the ENA device of an EFA interface. For more information, see [EFA limitations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html).
+ ** Default behavior **

  HyperPod deploys all cluster instances in a single Availability Zone. The VPC configuration determines the deployment AZ:
  + For Slurm-orchestrated clusters, VPC configuration is optional. When no VPC configuration is provided, HyperPod defaults to one subnet from the platform VPC. 
  + For EKS-orchestrated clusters, VPC configuration is required.
  + For both Slurm and EKS orchestrators, when [`VpcConfig`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VpcConfig.html) is provided, HyperPod selects a subnet from the provided `VpcConfig`'s subnet list. All instance groups inherit the subnet's AZ. 
**Note**  
Once you create a cluster, you cannot modify its `VpcConfig` settings.

  To learn more about configuring VPCs for HyperPod clusters, see the preceding section, [Setting up SageMaker HyperPod with a custom Amazon VPC](#sagemaker-hyperpod-prerequisites-optional-vpc).
+ ** Multi-AZ configuration **

  You can set up your HyperPod cluster across multiple AZs when creating a cluster or when adding a new instance group to an existing cluster. To configure multi-AZ deployments, you can override the default VPC settings of the cluster by specifying different subnets and security groups, potentially across different Availability Zones, for individual instance groups within your cluster. 

  SageMaker HyperPod API users can use the `OverrideVpcConfig` property within the [ClusterInstanceGroupSpecification](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterInstanceGroupSpecification.html) when working with the [`CreateCluster`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateCluster.html) or [`UpdateCluster`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateCluster.html) APIs.

  The `OverrideVpcConfig` field:
  + Cannot be modified after the instance group is created.
  + Is optional. If not specified, the cluster level [`VpcConfig`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VpcConfig.html) is used as default.
  + For Slurm-orchestrated clusters, can only be specified when cluster level `VpcConfig` is provided. If no `VpcConfig` is specified at cluster level, `OverrideVpcConfig` cannot be used for any instance group.
  + Contains two required fields:
    + `Subnets` - accepts between 1 and 16 subnet IDs
    + `SecurityGroupIds` - accepts between 1 and 5 security group IDs

  For more information about creating or updating a SageMaker HyperPod cluster using the SageMaker HyperPod console UI or the AWS CLI:
  + Slurm orchestration: See [Operating Slurm-orchestrated HyperPod clusters](sagemaker-hyperpod-operate-slurm.md).
  + EKS orchestration. See [Operating EKS-orchestrated HyperPod clusters](sagemaker-hyperpod-eks-operate.md).

**Note**  
When running workloads across multiple AZs, be aware that network communication between AZs introduces additional latency. Consider this impact when designing latency-sensitive applications.

## Setting up AWS Systems Manager and Run As for cluster user access control
<a name="sagemaker-hyperpod-prerequisites-ssm"></a>

[SageMaker HyperPod DLAMI](sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-hyperpod-ami) comes with [AWS Systems Manager](https://aws.amazon.com/systems-manager/) (SSM) out of the box to help you manage access to your SageMaker HyperPod cluster instance groups. This section describes how to create operating system (OS) users in your SageMaker HyperPod clusters and associate them with IAM users and roles. This is useful to authenticate SSM sessions using the credentials of the OS user account.

**Note**  
Granting users access to HyperPod cluster nodes allows them to install and operate user-managed software on the nodes. Ensure that you maintain the principle of least-privilege permissions for users.

### Enabling Run As in your AWS account
<a name="sagemaker-hyperpod-prerequisites-ssm-enable-runas"></a>

As an AWS account admin or a cloud administrator, you can manage access to SageMaker HyperPod clusters at an IAM role or user level by using the [Run As feature in SSM](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-preferences-run-as.html). With this feature, you can start each SSM session using the OS user associated to the IAM role or user.

To enable Run As in your AWS account, follow the steps in [Turn on Run As support for Linux and macOS managed nodes](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-preferences-run-as.html). If you already created OS users in your cluster, make sure that you associate them with IAM roles or users by tagging them as guided in **Option 2** of step 5 under **To turn on Run As support for Linux and macOS managed nodes**.

## (Optional) Setting up SageMaker HyperPod with Amazon FSx for Lustre
<a name="sagemaker-hyperpod-prerequisites-optional-fsx"></a>

To start using SageMaker HyperPod and mapping data paths between the cluster and your FSx for Lustre ﬁle system, select one of the AWS Regions supported by SageMaker HyperPod. After choosing the AWS Region you prefer, you also should determine which Availability Zone (AZ) to use. 

If you use SageMaker HyperPod compute nodes in AZs different from the AZs where your FSx for Lustre ﬁle system is set up within the same AWS Region, there might be communication and network overhead. We recommend that you to use the same physical AZ as the one for the SageMaker HyperPod service account to avoid any cross-AZ traffic between SageMaker HyperPod clusters and your FSx for Lustre ﬁle system. Also, make sure that you have configured it with your VPC. If you want to use Amazon FSx as the main file system for storage, you must configure SageMaker HyperPod clusters with your VPC.