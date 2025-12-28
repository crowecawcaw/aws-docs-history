# Enabling network

communication from Amazon Aurora to other AWS services

To use certain other AWS services with Amazon Aurora, the network configuration of
your Aurora DB cluster must allow outbound connections to endpoints for those services.
The following operations require this network configuration.

- Invoking AWS Lambda functions. To learn about this feature, see
  [Invoking a Lambda function with an Aurora MySQL native function](AuroraMySQL.Integrating.md "AuroraMySQL.Integrating.md").
- Accessing files from Amazon S3. To learn about this feature, see
  [Loading data into an Amazon Aurora MySQL DB cluster from
  text files in an Amazon S3 bucket](AuroraMySQL.Integrating.md "AuroraMySQL.Integrating.md")
  and [Saving data from an Amazon Aurora MySQL DB cluster into text files in an Amazon S3
  bucket](AuroraMySQL.Integrating.md "AuroraMySQL.Integrating.md").
- Accessing AWS KMS endpoints. AWS KMS access is required to use database activity streams with Aurora MySQL. To learn about
  this feature, see [Monitoring Amazon Aurora with Database Activity
  Streams](DBActivityStreams.md "DBActivityStreams.md").
- Accessing SageMaker AI endpoints. SageMaker AI access is required to use SageMaker AI machine learning with Aurora MySQL. To learn about
  this feature, see [Using Amazon Aurora machine learning with Aurora MySQL](mysql-ml.md "mysql-ml.md").
  Aurora returns the following error messages if it can't connect to a service
  endpoint.

```
ERROR 1871 (HY000): S3 API returned error: Network Connection
```

```
ERROR 1873 (HY000): Lambda API returned error: Network Connection. Unable to connect to endpoint
```

```
ERROR 1815 (HY000): Internal error: Unable to initialize S3Stream
```

For database activity streams using Aurora MySQL, the activity stream stops functioning if the DB cluster can't access
the AWS KMS endpoint. Aurora notifies you about this issue using RDS Events.

If you encounter these messages while using the corresponding AWS services,
check if your Aurora DB cluster is public or private. If your Aurora DB cluster
is private, you must configure it to enable connections.

For an Aurora DB cluster to be public, it must be marked as publicly accessible. If you
look at the details for the DB cluster in the AWS Management Console, **Publicly
Accessible** is **Yes** if this is the case. The DB
cluster must also be in an Amazon VPC public subnet. For more information about publicly
accessible DB instances, see [Working with a DB cluster in a VPC](USER_VPC.md "USER_VPC.md"). For more information about
public Amazon VPC subnets, see [Your VPC and
subnets](../../../vpc/latest/userguide/VPC_Subnets.md "../../../vpc/latest/userguide/VPC_Subnets.md").

If your Aurora DB cluster isn't publicly accessible and in a VPC public subnet, it is private. You might have a DB
cluster that is private and want to use one of the features that requires this network configuration. If so, configure the
cluster so that it can connect to Internet addresses through Network Address Translation (NAT). As an alternative for Amazon S3,
Amazon SageMaker AI, and AWS Lambda, you can instead configure the VPC to have a VPC endpoint for the other service associated with the
DB cluster's route table, see [Working with a DB cluster in a VPC](USER_VPC.md "USER_VPC.md"). For more information about configuring NAT in your VPC, see [NAT gateways](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md"). For more information about configuring VPC endpoints, see
[VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints.md "../../../vpc/latest/userguide/vpc-endpoints.md"). You can also create an S3 gateway endpoint to access your S3 bucket.
For more information, see [Gateway endpoints for Amazon S3](../../../vpc/latest/privatelink/vpc-endpoints-s3.md "../../../vpc/latest/privatelink/vpc-endpoints-s3.md").

You might also have to open the ephemeral ports for your network access control lists (ACLs) in the outbound rules for
your VPC security group. For more information on ephemeral ports for network ACLs, see [Ephemeral ports](../../../vpc/latest/userguide/vpc-network-acls.md#nacl-ephemeral-ports "../../../vpc/latest/userguide/vpc-network-acls.md#nacl-ephemeral-ports") in the _Amazon Virtual Private Cloud
User Guide_.
