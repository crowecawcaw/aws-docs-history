# Network prerequisites for Aurora MySQL database activity streams

In the following section, you can find how to configure your virtual private cloud (VPC) for
use with database activity streams.

###### Note

Aurora MySQL network prerequisites are applicable to the following engine versions:

- Aurora MySQL version 2, up to 2.11.3
- Aurora MySQL version 2.12.0
- Aurora MySQL version 3, up to 3.04.2

###### Topics

- [Prerequisites for AWS KMS endpoints](#DBActivityStreams.Prereqs.KMS "#DBActivityStreams.Prereqs.KMS")
- [Prerequisites for public availability](#DBActivityStreams.Prereqs.Public "#DBActivityStreams.Prereqs.Public")
- [Prerequisites for private availability](#DBActivityStreams.Prereqs.Private "#DBActivityStreams.Prereqs.Private")

## Prerequisites for AWS KMS endpoints

Instances in an Aurora MySQL cluster that use activity streams must be able to access AWS KMS endpoints. Make sure
this requirement is satisfied before enabling database activity streams for your Aurora MySQL cluster. If the Aurora
cluster is publicly available, this requirement is satisfied automatically.

###### Important

If the Aurora MySQL DB cluster can't access the AWS KMS endpoint, the activity stream stops. In that case,
Aurora notifies you about this issue using RDS Events.

## Prerequisites for public availability

For an Aurora DB cluster to be public, it must meet the following requirements:

- **Publicly Accessible** is **Yes** in the AWS Management Console cluster details
  page.
- The DB cluster is in an Amazon VPC public subnet. For more information about publicly accessible DB instances, see
  [Working with a DB cluster in a VPC](USER_VPC.md "USER_VPC.md").
  For more information about public Amazon VPC subnets, see [Your VPC and
  Subnets](../../../vpc/latest/userguide/VPC_Subnets.md "../../../vpc/latest/userguide/VPC_Subnets.md").

## Prerequisites for private availability

If your Aurora DB cluster is in a VPC public subnet and isn't publicly accessible, it's private. To keep
your cluster private and use it with database activity streams, you have the following options:

- Configure Network Address Translation (NAT) in your VPC. For more information, see [NAT Gateways](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md").
- Create an AWS KMS endpoint in your VPC. This option is recommended because it's easier to configure.

###### To create an AWS KMS endpoint in your VPC

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Endpoints**.
3. Choose **Create Endpoint**.

The **Create Endpoint** page appears. 4. Do the following:

    * In **Service category**, choose **AWS services**.
    * In **Service Name**, choose
     **com.amazonaws.`region`.kms**, where
     `region` is the AWS Region where your cluster is located.
    * For **VPC**, choose the VPC where your cluster is located.

5. Choose **Create Endpoint**.

For more information about configuring VPC endpoints, see [VPC
Endpoints](../../../vpc/latest/userguide/vpc-endpoints.md "../../../vpc/latest/userguide/vpc-endpoints.md").
