# Give SageMaker AI Processing Jobs Access to Resources in Your

Amazon VPC

To control access to your data and processing jobs, create a Amazon VPC with private subnets.
For information about creating and configuring a VPC, see [Get
Started With Amazon VPC](../../../AmazonVPC/latest/UserGuide/vpc-getting-started.md "../../../AmazonVPC/latest/UserGuide/vpc-getting-started.md") in the _Amazon VPC User Guide_.

You can monitor all network traffic in and out of
your processing containers by using VPC flow logs. For more information, see [VPC Flow
Logs](../../../AmazonVPC/latest/UserGuide/flow-logs.md "../../../AmazonVPC/latest/UserGuide/flow-logs.md") in the _Amazon VPC User Guide_.

This document explains how to add Amazon VPC configurations for processing jobs.

## Configure a Processing Job for Amazon VPC

Access

You configure the processing job by specifying the subnets and security group IDs within the VPC.
You don’t need to specify the subnet for the processing container. Amazon SageMaker AI automatically pulls the processing container from Amazon ECR.
For more information about processing containers, see [Data transformation
workloads with SageMaker Processing](processing-job.md "processing-job.md").

When creating a processing job, you can specify subnets and security groups in your VPC using either the SageMaker AI console or the API.

To use the API, you specify the subnets and security group IDs in the `NetworkConfig.VpcConfig` parameter of the [CreateProcessingJob](../APIReference/API_CreateProcessingJob.md "../APIReference/API_CreateProcessingJob.md") operation. SageMaker AI uses the subnet and security group details to create the network interfaces and attaches them to the processing containers.
The network interfaces provide the processing containers with a network connection within your VPC. This allows the processing job to connect to resources that exist in your VPC.

The following is an example of the `VpcConfig` parameter that you
include in your call to the `CreateProcessingJob` operation:

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

## Configure Your Private VPC for SageMaker AI

Processing

When configuring the private VPC for your SageMaker AI processing jobs, use the following
guidelines. For information about setting up a VPC, see [Working
with VPCs and Subnets](../../../AmazonVPC/latest/UserGuide/working-with-vpcs.md "../../../AmazonVPC/latest/UserGuide/working-with-vpcs.md") in the _Amazon VPC User
Guide_.

###### Topics

- [Ensure That Subnets Have Enough IP Addresses](#process-vpc-ip "#process-vpc-ip")
- [Create an Amazon S3 VPC Endpoint](#process-vpc-s3 "#process-vpc-s3")
- [Use a Custom Endpoint Policy to Restrict
  Access to S3](#process-vpc-policy "#process-vpc-policy")
- [Configure Route Tables](#process-vpc-route-table "#process-vpc-route-table")
- [Configure the VPC Security Group](#process-vpc-groups "#process-vpc-groups")
- [Connect to Resources Outside Your VPC](#process-vpc-nat "#process-vpc-nat")
- [Monitor Amazon SageMaker Processing Jobs with CloudWatch Logs and Metrics](#process-vpc-cloudwatch "#process-vpc-cloudwatch")

### Ensure That Subnets Have Enough IP Addresses

Your VPC subnets should have at least two private IP addresses for each
instance in a processing job. For more information, see [VPC and Subnet Sizing for IPv4](../../../AmazonVPC/latest/UserGuide/VPC_Subnets.md#vpc-sizing-ipv4 "../../../AmazonVPC/latest/UserGuide/VPC_Subnets.md#vpc-sizing-ipv4") in the _Amazon VPC User
Guide_.

### Create an Amazon S3 VPC Endpoint

If you configure your VPC so that processing containers don't have access to
the internet, they can't connect to the Amazon S3 buckets that contain your data
unless you create a VPC endpoint that allows access. By creating a VPC endpoint,
you allow your processing containers to access the buckets where you store your
data. We recommend that you also create a custom policy that allows only
requests from your private VPC to access to your S3 buckets. For more
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
   Access to S3](#process-vpc-policy "#process-vpc-policy").

### Use a Custom Endpoint Policy to Restrict

Access to S3

The default endpoint policy allows full access to S3 for any user or service
in your VPC. To further restrict access to S3, create a custom endpoint policy.
For more information, see [Using Endpoint Policies for Amazon S3](../../../vpc/latest/userguide/vpc-endpoints-s3.md#vpc-endpoints-policies-s3 "../../../vpc/latest/userguide/vpc-endpoints-s3.md#vpc-endpoints-policies-s3"). You can also use a bucket policy
to restrict access to your S3 buckets to only traffic that comes from your
Amazon VPC. For information, see [Using Amazon S3 Bucket Policies](../../../vpc/latest/userguide/vpc-endpoints-s3.md#vpc-endpoints-s3-bucket-policies "../../../vpc/latest/userguide/vpc-endpoints-s3.md#vpc-endpoints-s3-bucket-policies").

#### Restrict Package Installation on

the Processing Container

The default endpoint policy allows users to install packages from the Amazon Linux
and Amazon Linux 2 repositories on the processing container. If you don't want users
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
use to specify the locations of the data in your processing jobs resolve by
configuring the endpoint route tables. For information about VPC endpoint route
tables, see [Routing for Gateway Endpoints](../../../AmazonVPC/latest/UserGuide/vpce-gateway.md#vpc-endpoints-routing "../../../AmazonVPC/latest/UserGuide/vpce-gateway.md#vpc-endpoints-routing") in the _Amazon VPC User
Guide_.

### Configure the VPC Security Group

In distributed processing, you must allow communication between the different
containers in the same processing job. To do that, configure a rule for your
security group that allows inbound connections between members of the same
security group. For more information, see [Security Group Rules](../../../AmazonVPC/latest/UserGuide/VPC_SecurityGroups.md#SecurityGroupRules "../../../AmazonVPC/latest/UserGuide/VPC_SecurityGroups.md#SecurityGroupRules").

### Connect to Resources Outside Your VPC

If you're connecting your models to resources outside the VPC that they're running in, do one
of the following:

- **Connect to other AWS services** – If your model needs access to an AWS service that supports interface Amazon VPC endpoints, create an endpoint to connect to that service.
  For a list of services that support interface endpoints, see [AWS services that integrate with AWS PrivateLink](../../../vpc/latest/privatelink/aws-services-privatelink-support.md "../../../vpc/latest/privatelink/aws-services-privatelink-support.md") in the AWS PrivateLink User Guide.
  For information about creating an interface VPC endpoint, see [Access an AWS service using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") in the AWS PrivateLink User Guide.
- **Connect to resources over the internet** – If your models are running on instances in an Amazon VPC that does not have a subnet with access to the internet, the models won't have access to resources on the internet. If your model needs access to an AWS service that doesn't support interface VPC endpoints,
  or to a resource outside of AWS, ensure that you are running your models in a private subnet that has access to the internet using a public NAT gateway in a public subnet.
  After you have your models running in the private subnet, configure your security groups and network access control lists (NACLs) to allow outbound connections from the private subnet to the public NAT gateway in the public subnet.
  For information, see [NAT gateways](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") in the Amazon VPC User Guide.

### Monitor Amazon SageMaker Processing Jobs with CloudWatch Logs and Metrics

Amazon SageMaker AI provides Amazon CloudWatch logs and metrics to monitor training jobs. CloudWatch provides CPU, GPU, memory, GPU memory, and disk metrics, and event logging.
For more information about monitoring Amazon SageMaker processing jobs, see [Amazon SageMaker AI metrics in Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md") and [SageMaker AI job metrics](monitoring-cloudwatch.md#cloudwatch-metrics-jobs "monitoring-cloudwatch.md#cloudwatch-metrics-jobs").
