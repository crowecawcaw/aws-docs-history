

# Amazon VPC options when you launch a cluster
<a name="emr-clusters-in-a-vpc"></a>



When you launch an Amazon EMR cluster within a VPC, you can launch it within either a public, private, or shared subnet. There are slight but notable differences in configuration, depending on the subnet type you choose for a cluster.

## Public subnets
<a name="emr-vpc-public-subnet"></a>

EMR clusters in a public subnet require a connected internet gateway. This is because Amazon EMR clusters must access AWS services and Amazon EMR. If a service, such as Amazon S3, provides the ability to create a VPC endpoint, you can access those services using the endpoint instead of accessing a public endpoint through an internet gateway. Additionally, Amazon EMR cannot communicate with clusters in public subnets through a network address translation (NAT) device. An internet gateway is required for this purpose but you can still use a NAT instance or gateway for other traffic in more complex scenarios.

All instances in a cluster connect to Amazon S3 through either a VPC endpoint or internet gateway. Other AWS services which do not currently support VPC endpoints use only an internet gateway.

If you have additional AWS resources that you do not want connected to the internet gateway, you can launch those components in a private subnet that you create within your VPC. 

Clusters running in a public subnet use two security groups: one for the primary node and another for core and task nodes. For more information, see [Control network traffic with security groups for your Amazon EMR cluster](emr-security-groups.md).

The following diagram shows how an Amazon EMR cluster runs in a VPC using a public subnet. The cluster is able to connect to other AWS resources, such as Amazon S3 buckets, through the internet gateway.

![Cluster on a VPC](http://docs.aws.amazon.com/emr/latest/ManagementGuide/images/vpc_default_v3a.png)


The following diagram shows how to set up a VPC so that a cluster in the VPC can access resources in your own network, such as an Oracle database.

![Set up a VPC and cluster to access local VPN resources](http://docs.aws.amazon.com/emr/latest/ManagementGuide/images/vpc_withVPN_v3a.png)


## Private subnets
<a name="emr-vpc-private-subnet"></a>

A private subnet lets you launch AWS resources without requiring the subnet to have an attached internet gateway. Amazon EMR supports launching clusters in private subnets with release versions 4.2.0 or later.

**Note**  
When you set up an Amazon EMR cluster in a private subnet, we recommend that you also set up [VPC endpoints for Amazon S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html). If your EMR cluster is in a private subnet without VPC endpoints for Amazon S3, you will incur additional NAT gateway charges that are associated with S3 traffic because the traffic between your EMR cluster and S3 will not stay within your VPC.

Private subnets differ from public subnets in the following ways:
+ For Amazon EMR 8.0.0 and later and Amazon EMR Spark 8.0.0 and later, Amazon EMR provisions a VPC endpoint in your VPC to enable the Amazon EMR cluster to communicate with the Amazon EMR service. You must either provide `ec2:CreateVpcEndpoint` and `ec2:ModifyVpcEndpoint` permissions on your service role for Amazon EMR or create this VPC endpoint manually before launching a cluster. The name of the VPC endpoint service is `aws.api.{{region}}.emr-service-cell01`. For an example scoped-down policy with tags, see [Service role for Amazon EMR (EMR role)](emr-iam-role.md).
+ To access AWS services that do not provide a VPC endpoint, you still must use a NAT instance or an internet gateway. To configure NAT gateways, see [NAT Gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) in the *Amazon VPC User Guide*.
+ At a minimum, you must provide a route to Amazon S3 for the buckets required by Amazon EMR. For more information, see [Sample policies for private subnets that access Amazon S3](private-subnet-iampolicy.md)
+ If you use EMRFS features, you need to have an Amazon S3 VPC endpoint and a route from your private subnet to DynamoDB.
+ You cannot change a subnet with an existing Amazon EMR cluster from public to private or vice versa. To locate an Amazon EMR cluster within a private subnet, the cluster must be started in that private subnet. 

Amazon EMR creates and uses different default security groups for the clusters in a private subnet: ElasticMapReduce-Primary-Private, ElasticMapReduce-Core-Private, and ElasticMapReduce-ServiceAccess. For more information, see [Control network traffic with security groups for your Amazon EMR cluster](emr-security-groups.md).

For a complete listing of NACLs of your cluster, choose **Security groups for Primary** and **Security groups for Core & Task** on the Amazon EMR console **Cluster Details** page.

The following image shows how an Amazon EMR cluster is configured within a private subnet. The only communication outside the subnet is to Amazon EMR. 

![Launch an Amazon EMR cluster in a private subnet](http://docs.aws.amazon.com/emr/latest/ManagementGuide/images/vpc_with_private_subnet_v4.png)


The following image shows a sample configuration for an Amazon EMR cluster within a private subnet connected to a NAT instance that is residing in a public subnet.

![Private subnet with NAT](http://docs.aws.amazon.com/emr/latest/ManagementGuide/images/vpc_private_subnet_nat_v4.png)


## Shared subnets
<a name="emr-vpc-shared-subnet"></a>

VPC sharing allows customers to share subnets with other AWS accounts within the same AWS Organization. You can launch Amazon EMR clusters into both public shared and private shared subnets, with the following caveats.

The subnet owner must share a subnet with you before you can launch an Amazon EMR cluster into it. However, shared subnets can later be unshared. For more information, see [Working with Shared VPCs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-sharing.html). When a cluster is launched into a shared subnet and that shared subnet is then unshared, you can observe specific behaviors based on the state of the Amazon EMR cluster when the subnet is unshared.
+ Subnet is unshared *before* the cluster is successfully launched - If the owner stops sharing the Amazon VPC or subnet while the participant is launching a cluster, the cluster could fail to start or be partially initialized without provisioning all requested instances. 
+ Subnet is unshared *after* the cluster is successfully launched - When the owner stops sharing a subnet or Amazon VPC with the participant, the participant's clusters will not be able to resize to add new instances or to replace unhealthy instances.

When you launch an Amazon EMR cluster, multiple security groups are created. In a shared subnet, the subnet participant controls these security groups. The subnet owner can see these security groups but cannot perform any actions on them. If the subnet owner wants to remove or modify the security group, the participant that created the security group must take the action.

## Control VPC permissions with IAM
<a name="emr-iam-on-vpc"></a>

By default, all users can see all of the subnets for the account, and any user can launch a cluster in any subnet. 

When you launch a cluster into a VPC, you can use AWS Identity and Access Management (IAM) to control access to clusters and restrict actions using policies, just as you would with clusters launched into Amazon EC2 Classic. For more information about IAM, see [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/). 

You can also use IAM to control who can create and administer subnets. For example, you can create an IAM role to administer subnets, and a second role that can launch clusters but cannot modify Amazon VPC settings. For more information about administering policies and actions in Amazon EC2 and Amazon VPC, see [IAM Policies for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html) in the *Amazon EC2 User Guide*. 