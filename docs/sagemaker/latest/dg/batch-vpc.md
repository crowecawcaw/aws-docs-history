# Give Batch Transform Jobs Access to Resources in Your

Amazon VPC

To control access to your data and batch transform jobs, we recommend that you create
a private Amazon VPC and configure it so that your jobs aren't accessible over the public
internet. You specify your private VPC configuration when you create a model by
specifying subnets and security groups. You then specify the same model when you create
a batch transform job. When you specify the subnets and security groups, SageMaker AI creates
_elastic network interfaces_ that are associated
with your security groups in one of the subnets. Network interfaces allow your model
containers to connect to resources in your VPC. For information about network
interfaces, see [Elastic Network Interfaces](../../../AmazonVPC/latest/UserGuide/VPC_ElasticNetworkInterfaces.md "../../../AmazonVPC/latest/UserGuide/VPC_ElasticNetworkInterfaces.md") in the _Amazon VPC User
Guide_.

This document explains how to add Amazon VPC configurations for batch transform
jobs.

## Configure a Batch Transform Job for Amazon VPC

Access

To specify subnets and security groups in your private VPC, use the `VpcConfig`
request parameter of the [`CreateModel`](../APIReference/API_CreateModel.md "../APIReference/API_CreateModel.md") API, or provide this information when you create a model in the
SageMaker AI console. Then specify the same model in the `ModelName` request parameter of the
[`CreateTransformJob`](../APIReference/API_CreateTransformJob.md "../APIReference/API_CreateTransformJob.md") API, or in the **Model name** field when
you create a transform job in the SageMaker AI console. SageMaker AI uses this information to create network
interfaces and attach them to your model containers. The network interfaces provide your model
containers with a network connection within your VPC that is not connected to the internet. They also
enable your transform job to connect to resources in your private VPC.

The following is an example of the `VpcConfig` parameter that you
include in your call to `CreateModel`:

```
VpcConfig: {
      "Subnets": [
          "subnet-0123456789abcdef0",
          "subnet-0123456789abcdef1",
          "subnet-0123456789abcdef2"
          ],
      "SecurityGroupIds": [
          "sg-0123456789abcdef0"
          ]
        }
```

If you are creating a model using the `CreateModel` API operation, the
IAM execution role that you use to create your model must include the permissions
described in [CreateModel API: Execution Role
Permissions](sagemaker-roles.md#sagemaker-roles-createmodel-perms "sagemaker-roles.md#sagemaker-roles-createmodel-perms"), including the following
permissions required for a private VPC.

When creating a model in the console, if you select **Create a new
role** in the **Model Settings** section, the [AmazonSageMakerFullAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonSageMakerFullAccess$jsonEditor "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonSageMakerFullAccess$jsonEditor") policy used to create the role already
contains these permissions. If you select **Enter a custom IAM role
ARN** or **Use existing role**, the role ARN that you
specify must have an execution policy attached with the following permissions.

```
{
            "Effect": "Allow",
            "Action": [
            "ec2:CreateNetworkInterface",
            "ec2:CreateNetworkInterfacePermission",
            "ec2:DeleteNetworkInterface",
            "ec2:DeleteNetworkInterfacePermission",
            "ec2:DescribeNetworkInterfaces",
            "ec2:DescribeVpcs",
            "ec2:DescribeDhcpOptions",
            "ec2:DescribeSubnets",
            "ec2:DescribeSecurityGroups"
```

## Configure Your Private VPC for SageMaker AI Batch

Transform

When configuring the private VPC for your SageMaker AI batch transform jobs, use the
following guidelines. For information about setting up a VPC, see [Working
with VPCs and Subnets](../../../AmazonVPC/latest/UserGuide/working-with-vpcs.md "../../../AmazonVPC/latest/UserGuide/working-with-vpcs.md") in the _Amazon VPC User
Guide_.

###### Topics

- [Ensure That Subnets Have Enough IP Addresses](#batch-vpc-ip "#batch-vpc-ip")
- [Create an Amazon S3 VPC Endpoint](#batch-vpc-s3 "#batch-vpc-s3")
- [Use a Custom Endpoint Policy to Restrict
  Access to S3](#batch-vpc-policy "#batch-vpc-policy")
- [Configure Route Tables](#batch-vpc-route-table "#batch-vpc-route-table")
- [Configure the VPC Security Group](#batch-vpc-groups "#batch-vpc-groups")
- [Connect to Resources Outside Your VPC](#batch-vpc-nat "#batch-vpc-nat")

### Ensure That Subnets Have Enough IP Addresses

Your VPC subnets should have at least two private IP addresses for each
instance in a transform job. For more information, see [VPC and Subnet Sizing for IPv4](../../../AmazonVPC/latest/UserGuide/VPC_Subnets.md#vpc-sizing-ipv4 "../../../AmazonVPC/latest/UserGuide/VPC_Subnets.md#vpc-sizing-ipv4") in the _Amazon VPC User
Guide_.

### Create an Amazon S3 VPC Endpoint

If you configure your VPC so that model containers don't have access to the
internet, they can't connect to the Amazon S3 buckets that contain your data unless
you create a VPC endpoint that allows access. By creating a VPC endpoint, you
allow your model containers to access the buckets where you store your data and
model artifacts . We recommend that you also create a custom policy that allows
only requests from your private VPC to access to your S3 buckets. For more
information, see [Endpoints for Amazon S3](../../../AmazonVPC/latest/UserGuide/vpc-endpoints-s3.md "../../../AmazonVPC/latest/UserGuide/vpc-endpoints-s3.md").

###### To create an S3 VPC endpoint:

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Endpoints**, then
   choose **Create Endpoint**
3. For **Service Name**, choose
   **com.amazonaws.`region`.s3**,
   where `region` is the name of the region where
   your VPC resides.
4. For **VPC**, choose the VPC you want to use for this
   endpoint.
5. For **Configure route tables**, select the route
   tables to be used by the endpoint. The VPC service automatically adds a
   route to each route table you select that points any S3 traffic to the
   new endpoint.
6. For **Policy**, choose **Full
   Access** to allow full access to the S3 service by any user
   or service within the VPC. Choose **Custom** to
   restrict access further. For information, see [Use a Custom Endpoint Policy to Restrict
   Access to S3](#batch-vpc-policy "#batch-vpc-policy").

### Use a Custom Endpoint Policy to Restrict

Access to S3

The default endpoint policy allows full access to S3 for any user or service
in your VPC. To further restrict access to S3, create a custom endpoint policy.
For more information, see [Using Endpoint Policies for Amazon S3](../../../vpc/latest/userguide/vpc-endpoints-s3.md#vpc-endpoints-policies-s3 "../../../vpc/latest/userguide/vpc-endpoints-s3.md#vpc-endpoints-policies-s3"). You can also use a bucket policy
to restrict access to your S3 buckets to only traffic that comes from your
Amazon VPC. For information, see [Using Amazon S3 Bucket Policies](../../../vpc/latest/userguide/vpc-endpoints-s3.md#vpc-endpoints-s3-bucket-policies "../../../vpc/latest/userguide/vpc-endpoints-s3.md#vpc-endpoints-s3-bucket-policies").

#### Restrict Package Installation on

the Model Container

The default endpoint policy allows users to install packages from the Amazon Linux
and Amazon Linux 2 repositories on the training container. If you don't want users
to install packages from that repository, create a custom endpoint policy
that explicitly denies access to the Amazon Linux and Amazon Linux 2 repositories. The
following is an example of a policy that denies access to these
repositories:

```
{
    "Statement": [
      {
        "Sid": "AmazonLinuxAMIRepositoryAccess",
        "Principal": "*",
        "Action": [
            "s3:GetObject"
        ],
        "Effect": "Deny",
        "Resource": [
            "arn:aws:s3:::packages.*.amazonaws.com/*",
            "arn:aws:s3:::repo.*.amazonaws.com/*"
        ]
      }
    ]
}

{
    "Statement": [
        { "Sid": "AmazonLinux2AMIRepositoryAccess",
          "Principal": "*",
          "Action": [
              "s3:GetObject"
              ],
          "Effect": "Deny",
          "Resource": [
              "arn:aws:s3:::amazonlinux.*.amazonaws.com/*"
              ]
         }
    ]
}
```

### Configure Route Tables

Use default DNS settings for your endpoint route table, so that standard Amazon S3
URLs (for example, `http://s3-aws-region.amazonaws.com/amzn-s3-demo-bucket`)
resolve. If you don't use default DNS settings, ensure that the URLs that you
use to specify the locations of the data in your batch transform jobs resolve by
configuring the endpoint route tables. For information about VPC endpoint route
tables, see [Routing for Gateway Endpoints](../../../AmazonVPC/latest/UserGuide/vpce-gateway.md#vpc-endpoints-routing "../../../AmazonVPC/latest/UserGuide/vpce-gateway.md#vpc-endpoints-routing") in the _Amazon VPC User
Guide_.

### Configure the VPC Security Group

In distributed batch transform, you must allow communication between the
different containers in the same batch transform job. To do that, configure a
rule for your security group that allows inbound and outbound connections between members of
the same security group. Members of the same security group should be able to communicate
with each other across all ports. For more information, see [Security Group Rules](../../../AmazonVPC/latest/UserGuide/VPC_SecurityGroups.md#SecurityGroupRules "../../../AmazonVPC/latest/UserGuide/VPC_SecurityGroups.md#SecurityGroupRules").

### Connect to Resources Outside Your VPC

If you configure your VPC so that it doesn't have internet access, batch
transform jobs that use that VPC do not have access to resources outside your
VPC. If your batch transform job needs access to resources outside your VPC,
provide access with one of the following options:

- If your batch transform job needs access to an AWS service that
  supports interface VPC endpoints, create an endpoint to connect to that
  service. For a list of services that support interface endpoints, see
  [VPC Endpoints](../../../AmazonVPC/latest/UserGuide/vpc-endpoints.md "../../../AmazonVPC/latest/UserGuide/vpc-endpoints.md") in the _Amazon VPC User Guide_. For information about creating an
  interface VPC endpoint, see [Interface VPC Endpoints (AWS PrivateLink)](../../../AmazonVPC/latest/UserGuide/vpce-interface.md "../../../AmazonVPC/latest/UserGuide/vpce-interface.md") in the _Amazon VPC User Guide_.
- If your batch transform job needs access to an AWS service that
  doesn't support interface VPC endpoints or to a resource outside of
  AWS, create a NAT gateway and configure your security groups to allow
  outbound connections. For information about setting up a NAT gateway for
  your VPC, see [Scenario 2: VPC with Public and Private Subnets (NAT)](../../../AmazonVPC/latest/UserGuide/VPC_Scenario2.md "../../../AmazonVPC/latest/UserGuide/VPC_Scenario2.md") in
  the _Amazon Virtual Private Cloud User Guide_.
