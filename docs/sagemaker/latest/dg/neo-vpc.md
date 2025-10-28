# Give SageMaker AI Compilation Jobs Access to Resources in Your

Amazon VPC

###### Note

For compilation jobs, you can configure only subnets with a default tenancy VPC in
which your job runs on shared hardware. For more information on the tenancy
attribute for VPCs, see [Dedicated Instances](../../../AWSEC2/latest/UserGuide/dedicated-instance.md "../../../AWSEC2/latest/UserGuide/dedicated-instance.md").

## Configure a Compilation Job for Amazon VPC Access

To specify subnets and security groups in your private VPC, use the
`VpcConfig` request parameter of the [`CreateCompilationJob`](../APIReference/API_CreateCompilationJob.md "../APIReference/API_CreateCompilationJob.md") API, or provide this information when you
create a compilation job in the SageMaker AI console. SageMaker AI Neo uses this information to create
network interfaces and attach them to your compilation jobs. The network
interfaces provide compilation jobs with a network connection within your
VPC that is not connected to the internet. They also enable your compilation job to
connect to resources in your private VPC. The following is an example of the
`VpcConfig` parameter that you include in your call to `CreateCompilationJob`:

```
VpcConfig: {"Subnets": [
          "subnet-0123456789abcdef0",
          "subnet-0123456789abcdef1",
          "subnet-0123456789abcdef2"
          ],
      "SecurityGroupIds": [
          "sg-0123456789abcdef0"
          ]
        }
```

## Configure Your Private VPC for SageMaker AI Compilation

When configuring the private VPC for your SageMaker AI compilation jobs, use the following
guidelines. For information about setting up a VPC, see [Working
with VPCs and Subnets](../../../AmazonVPC/latest/UserGuide/working-with-vpcs.md "../../../AmazonVPC/latest/UserGuide/working-with-vpcs.md") in the _Amazon VPC User
Guide_.

###### Topics

- [Ensure That Subnets Have Enough IP Addresses](#neo-vpc-ip "#neo-vpc-ip")
- [Create an Amazon S3 VPC Endpoint](#neo-vpc-s3 "#neo-vpc-s3")
- [Use a Custom Endpoint Policy to Restrict
  Access to S3](#neo-vpc-policy "#neo-vpc-policy")
- [Configure Route Tables](#neo-vpc-route-table "#neo-vpc-route-table")
- [Configure the VPC Security Group](#neo-vpc-groups "#neo-vpc-groups")

### Ensure That Subnets Have Enough IP Addresses

Your VPC subnets should have at least two private IP addresses for each
instance in a compilation job. For more information, see [VPC and Subnet Sizing for IPv4](../../../AmazonVPC/latest/UserGuide/VPC_Subnets.md#vpc-sizing-ipv4 "../../../AmazonVPC/latest/UserGuide/VPC_Subnets.md#vpc-sizing-ipv4") in the _Amazon VPC User
Guide_.

### Create an Amazon S3 VPC Endpoint

If you configure your VPC to block access to the
internet, SageMaker Neo can't connect to the Amazon S3 buckets that contain your models
unless you create a VPC endpoint that allows access. By creating a VPC endpoint,
you allow your SageMaker Neo compilation jobs to access the buckets where you store your
data and model artifacts . We recommend that you also create a custom policy
that allows only requests from your private VPC to access to your S3 buckets.
For more information, see [Endpoints for Amazon S3](../../../AmazonVPC/latest/UserGuide/vpc-endpoints-s3.md "../../../AmazonVPC/latest/UserGuide/vpc-endpoints-s3.md").

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
   Access to S3](train-vpc.md#train-vpc-policy "train-vpc.md#train-vpc-policy").

### Use a Custom Endpoint Policy to Restrict

Access to S3

The default endpoint policy allows full access to S3 for any user or service
in your VPC. To further restrict access to S3, create a custom endpoint policy.
For more information, see [Using Endpoint Policies for Amazon S3](../../../vpc/latest/userguide/vpc-endpoints-s3.md#vpc-endpoints-policies-s3 "../../../vpc/latest/userguide/vpc-endpoints-s3.md#vpc-endpoints-policies-s3"). You can also use a bucket policy
to restrict access to your S3 buckets to only traffic that comes from your
Amazon VPC. For information, see [Using Amazon S3 Bucket Policies](../../../vpc/latest/userguide/vpc-endpoints-s3.md#vpc-endpoints-s3-bucket-policies "../../../vpc/latest/userguide/vpc-endpoints-s3.md#vpc-endpoints-s3-bucket-policies"). The following is a sample customized policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Principal": {
 "AWS": "*"
 },
 "Action": "s3:GetObject",
 "Resource": [
 "`arn:aws:s3:::your-sample-bucket`",
 "`arn:aws:s3:::your-sample-bucket/*`"
 ],
 "Condition": {
 "StringNotEquals": {
 "aws:SourceVpce": [
 "vpce-1a2b3c4d"
 ]
 }
 }
 }
 ]
}`

```

#### Add Permissions for Compilation Job Running

in a Amazon VPC to Custom IAM Policies

The `SageMakerFullAccess` managed policy includes the permissions that you
need to use models configured for Amazon VPC access with an endpoint. These
permissions allow SageMaker Neo to create an elastic network interface and attach
it to compilation job running in a Amazon VPC. If you use your own IAM policy, you must
add the following permissions to that policy to use models configured for Amazon VPC access.

JSON

```
`{"Version":"2012-10-17",
 "Statement": [
 {"Effect": "Allow",
 "Action": [
 "ec2:DescribeVpcEndpoints",
 "ec2:DescribeDhcpOptions",
 "ec2:DescribeVpcs",
 "ec2:DescribeSubnets",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DeleteNetworkInterfacePermission",
 "ec2:DeleteNetworkInterface",
 "ec2:CreateNetworkInterfacePermission",
 "ec2:CreateNetworkInterface",
 "ec2:ModifyNetworkInterfaceAttribute"
 ],
 "Resource": "*"
 }
 ]
}`

```

For more information about the `SageMakerFullAccess` managed policy, see
[AWS managed policy:
AmazonSageMakerFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSageMakerFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSageMakerFullAccess").

### Configure Route Tables

Use default DNS settings for your endpoint route table, so that standard Amazon S3
URLs (for example, `http://s3-aws-region.amazonaws.com/amzn-s3-demo-bucket`)
resolve. If you don't use default DNS settings, ensure that the URLs that you
use to specify the locations of the data in your compilation jobs resolve by
configuring the endpoint route tables. For information about VPC endpoint route
tables, see [Routing for Gateway Endpoints](../../../AmazonVPC/latest/UserGuide/vpce-gateway.md#vpc-endpoints-routing "../../../AmazonVPC/latest/UserGuide/vpce-gateway.md#vpc-endpoints-routing") in the _Amazon VPC User
Guide_.

### Configure the VPC Security Group

In your security group for the compilation job, you must allow outbound
communication to your Amazon S3 Amazon VPC endpoints and the subnet CIDR ranges used for the compilation job.
For information, see [Security Group Rules](../../../AmazonVPC/latest/UserGuide/VPC_SecurityGroups.md#SecurityGroupRules "../../../AmazonVPC/latest/UserGuide/VPC_SecurityGroups.md#SecurityGroupRules") and
[Control access to services with Amazon VPC endpoints](../../../AmazonVPC/latest/UserGuide/vpc-endpoints-access.md "../../../AmazonVPC/latest/UserGuide/vpc-endpoints-access.md").
