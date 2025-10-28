# Give SageMaker AI Training Jobs Access to Resources in Your

Amazon VPC

###### Note

For training jobs, you can configure only subnets with a default tenancy VPC in
which your instance runs on shared hardware. For more information on the tenancy
attribute for VPCs, see [Dedicated Instances](../../../AWSEC2/latest/UserGuide/dedicated-instance.md "../../../AWSEC2/latest/UserGuide/dedicated-instance.md").

## Configure a Training Job for Amazon VPC Access

To control access to your training jobs, run them in an Amazon VPC with private subnets that don’t have internet access.

You configure the training job to run in the VPC by specifying its subnets and security group IDs. You don’t need to specify the subnet for the container of the training job.
Amazon SageMaker AI automatically pulls the training container image from Amazon ECR.

When you create a training job, you can specify the subnets and security groups in your VPC using the Amazon SageMaker AI console
or the API.

To use the API, you specify the subnets and security group IDs in the `VpcConfig` parameter of the [CreateTrainingJob](../APIReference/API_CreateTrainingJob.md "../APIReference/API_CreateTrainingJob.md") operation. SageMaker AI uses the subnet and security group details to create the network interfaces and attaches them to the training containers.
The network interfaces provide the training containers with a network connection within your VPC. This allows the training job to connect to resources that exist in your VPC.

The following is an example of the `VpcConfig` parameter that you
include in your call to the `CreateTrainingJob` operation:

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

## Configure Your Private VPC for SageMaker AI Training

When configuring the private VPC for your SageMaker AI training jobs, use the following
guidelines. For information about setting up a VPC, see [Working
with VPCs and Subnets](../../../AmazonVPC/latest/UserGuide/working-with-vpcs.md "../../../AmazonVPC/latest/UserGuide/working-with-vpcs.md") in the _Amazon VPC User
Guide_.

###### Topics

- [Ensure That Subnets Have Enough IP Addresses](#train-vpc-ip "#train-vpc-ip")
- [Create an Amazon S3 VPC Endpoint](#train-vpc-s3 "#train-vpc-s3")
- [Use a Custom Endpoint Policy to Restrict
  Access to S3](#train-vpc-policy "#train-vpc-policy")
- [Configure Route Tables](#train-vpc-route-table "#train-vpc-route-table")
- [Configure the VPC Security Group](#train-vpc-groups "#train-vpc-groups")
- [Connect to Resources Outside Your VPC](#train-vpc-nat "#train-vpc-nat")
- [Monitor Amazon SageMaker Training Jobs with CloudWatch Logs and Metrics](#train-vpc-cloudwatch "#train-vpc-cloudwatch")

### Ensure That Subnets Have Enough IP Addresses

Training instances that _don't use_ an Elastic Fabric Adapter (EFA) should have at least 2 private IP addresses.
Training instances that use an EFA should have at least 5 private IP addresses. For more information, see [Multiple IP addresses](../../../AWSEC2/latest/UserGuide/MultipleIP.md "../../../AWSEC2/latest/UserGuide/MultipleIP.md") in the Amazon EC2 User Guide.

Your VPC subnets should have at least two private IP addresses for each
instance in a training job. For more information, see [VPC and Subnet Sizing for IPv4](../../../AmazonVPC/latest/UserGuide/VPC_Subnets.md#vpc-sizing-ipv4 "../../../AmazonVPC/latest/UserGuide/VPC_Subnets.md#vpc-sizing-ipv4") in the _Amazon VPC User
Guide_.

### Create an Amazon S3 VPC Endpoint

If you configure your VPC so that training containers don't have access to the
internet, they can't connect to the Amazon S3 buckets that contain your training data
unless you create a VPC endpoint that allows access. By creating a VPC endpoint,
you allow your training containers to access the buckets where you store your
data and model artifacts. We recommend that you also create a custom policy that
allows only requests from your private VPC to access to your S3 buckets. For
more information, see [Endpoints for Amazon S3](../../../AmazonVPC/latest/UserGuide/vpc-endpoints-s3.md "../../../AmazonVPC/latest/UserGuide/vpc-endpoints-s3.md").

###### To create an S3 VPC endpoint:

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Endpoints**, then
   choose **Create Endpoint**
3. For **Service Name**, search for
   **com.amazonaws.`region`.s3**,
   where `region` is the name of the region where
   your VPC resides.
4. Choose the **Gateway** type.
5. For **VPC**, choose the VPC you want to use for this
   endpoint.
6. For **Configure route tables**, select the route
   tables to be used by the endpoint. The VPC service automatically adds a
   route to each route table you select that points any S3 traffic to the
   new endpoint.
7. For **Policy**, choose **Full
   Access** to allow full access to the S3 service by any user
   or service within the VPC. Choose **Custom** to
   restrict access further. For information, see [Use a Custom Endpoint Policy to Restrict
   Access to S3](#train-vpc-policy "#train-vpc-policy").

### Use a Custom Endpoint Policy to Restrict

Access to S3

The default endpoint policy allows full access to S3 for any user or service
in your VPC. To further restrict access to S3, create a custom endpoint policy.
For more information, see [Using Endpoint Policies for Amazon S3](../../../vpc/latest/userguide/vpc-endpoints-s3.md#vpc-endpoints-policies-s3 "../../../vpc/latest/userguide/vpc-endpoints-s3.md#vpc-endpoints-policies-s3"). You can also use a bucket policy
to restrict access to your S3 buckets to only traffic that comes from your
Amazon VPC. For information, see [Using Amazon S3 Bucket Policies](../../../vpc/latest/userguide/vpc-endpoints-s3.md#vpc-endpoints-s3-bucket-policies "../../../vpc/latest/userguide/vpc-endpoints-s3.md#vpc-endpoints-s3-bucket-policies").

#### Restrict Package Installation on

the Training Container

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
use to specify the locations of the data in your training jobs resolve by
configuring the endpoint route tables. For information about VPC endpoint route
tables, see [Routing for Gateway Endpoints](../../../AmazonVPC/latest/UserGuide/vpce-gateway.md#vpc-endpoints-routing "../../../AmazonVPC/latest/UserGuide/vpce-gateway.md#vpc-endpoints-routing") in the _Amazon VPC User
Guide_.

### Configure the VPC Security Group

In distributed training, you must allow communication between the different
containers in the same training job. To do that, configure a rule for your
security group that allows inbound connections between members of the same
security group. For EFA-enabled instances, ensure that both inbound and outbound
connections allow all traffic from the same security group. For information, see
[Security Group Rules](../../../AmazonVPC/latest/UserGuide/VPC_SecurityGroups.md#SecurityGroupRules "../../../AmazonVPC/latest/UserGuide/VPC_SecurityGroups.md#SecurityGroupRules") in the _Amazon Virtual Private Cloud User
Guide_.

### Connect to Resources Outside Your VPC

If you configure your VPC so that it doesn't have internet access, training
jobs that use that VPC do not have access to resources outside your VPC. If your
training job needs access to resources outside your VPC, provide access with one
of the following options:

- If your training job needs access to an AWS service that supports
  interface VPC endpoints, create an endpoint to connect to that service.
  For a list of services that support interface endpoints, see [VPC Endpoints](../../../AmazonVPC/latest/UserGuide/vpc-endpoints.md "../../../AmazonVPC/latest/UserGuide/vpc-endpoints.md") in the _Amazon Virtual Private Cloud User
  Guide_. For information about creating an interface VPC
  endpoint, see [Interface VPC Endpoints (AWS PrivateLink)](../../../AmazonVPC/latest/UserGuide/vpce-interface.md "../../../AmazonVPC/latest/UserGuide/vpce-interface.md") in the
  _Amazon Virtual Private Cloud User Guide_.
- If your training job needs access to an AWS service that doesn't
  support interface VPC endpoints or to a resource outside of AWS,
  create a NAT gateway and configure your security groups to allow
  outbound connections. For information about setting up a NAT gateway for
  your VPC, see [Scenario 2: VPC with Public and Private Subnets (NAT)](../../../AmazonVPC/latest/UserGuide/VPC_Scenario2.md "../../../AmazonVPC/latest/UserGuide/VPC_Scenario2.md") in
  the _Amazon Virtual Private Cloud User Guide_.

### Monitor Amazon SageMaker Training Jobs with CloudWatch Logs and Metrics

Amazon SageMaker AI provides Amazon CloudWatch logs and metrics to monitor training jobs. CloudWatch provides CPU, GPU, memory, GPU memory, and disk metrics, and event logging.
For more information about monitoring Amazon SageMaker training jobs, see [Amazon SageMaker AI metrics in Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md") and [SageMaker AI job metrics](monitoring-cloudwatch.md#cloudwatch-metrics-jobs "monitoring-cloudwatch.md#cloudwatch-metrics-jobs").
