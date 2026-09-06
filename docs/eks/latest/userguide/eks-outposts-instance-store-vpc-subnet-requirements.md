

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create a VPC and subnets for Amazon EKS local clusters on AWS Outposts configured with EC2 instance store
<a name="eks-outposts-instance-store-vpc-subnet-requirements"></a>

When you create a local cluster, you specify a VPC and at least one private subnet that runs on Outposts. This topic provides an overview of the VPC and subnet requirements for your local cluster.

**Note**  
If your Outpost is configured with Amazon EBS instead of EC2 instance store, the architecture described in this topic isn’t available for your Outpost. Outposts configured with EBS will continue to use the existing local clusters implementation. For more information, see [Create a VPC and subnets for Amazon EKS clusters on AWS Outposts](eks-outposts-vpc-subnet-requirements.md).  
If you are interested in creating a local cluster on an EBS-backed Outpost using the updated local clusters architecture, contact your AWS account team.

## VPC requirements
<a name="eks-outposts-instance-store-vpc-requirements"></a>
+ The VPC must have enough IP addresses for the local cluster, any nodes, and other Kubernetes resources that you want to create. You can associate additional CIDR blocks with your VPC before or after you create your cluster. It can take up to 1 hour for a newly associated CIDR block to be recognized.
+ The VPC must have DNS hostname and DNS resolution support. Otherwise, nodes can’t register to your cluster. For more information, see [DNS attributes for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html) in the *Amazon VPC User Guide*.
+ To access your local cluster over your local network, the VPC must be associated with your Outpost’s local gateway route table. For more information, see [VPC associations](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-local-gateways.html#vpc-associations) in the * AWS Outposts User Guide*.

## Subnet requirements
<a name="eks-outposts-instance-store-subnet-requirements"></a>

When you create a local cluster, you specify at least one private subnet on your Outpost. Amazon EKS creates three cross-account elastic network interfaces in the subnets that you specify. These network interfaces enable communication between your cluster and your VPC.

The subnets that you specify must meet the following requirements:
+ All subnets must be on the same logical Outpost.
+ All subnets must be in the same VPC.
+ All subnets must be in the Availability Zone to which the Outpost is homed.
+ Each subnet must have at least 3 available IP addresses for the Amazon EKS cross-account elastic network interfaces.
+ The subnets must use IP address-based naming. Amazon EC2 [resource-based naming](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html#instance-naming-rbn) isn’t supported by Amazon EKS.
+ The subnets must have a route to the Outpost rack’s [local gateway](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-local-gateways.html) to access the Kubernetes API server over your local network. If the subnets don’t have a route to the local gateway, you must communicate with the Kubernetes API server from within the VPC.
+ The subnets can’t reside in the following Availability Zones.


|  AWS Region | Region name | Disallowed Availability Zone IDs | 
| --- | --- | --- | 
|  `us-east-1`  | US East (N. Virginia) |  `use1-az3`  | 
|  `us-west-1`  | US West (N. California) |  `usw1-az2`  | 
|  `ca-central-1`  | Canada (Central) |  `cac1-az3`  | 

## Subnet access to AWS services
<a name="eks-outposts-instance-store-subnet-access"></a>

Local clusters need connectivity to the AWS Region for cluster management operations, `etcd` backups, and control plane updates. In a disconnected state, the local cluster can continue to operate, but the cluster management operations that Amazon EKS can take are limited. For more information, see [Prepare local Amazon EKS clusters on AWS Outposts configured with EC2 instance store for network disconnects](eks-outposts-instance-store-network-disconnects.md).