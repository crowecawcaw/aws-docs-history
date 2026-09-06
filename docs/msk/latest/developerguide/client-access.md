

# Connect to an Amazon MSK Provisioned cluster
<a name="client-access"></a>

By default, clients can access an MSK Provisioned cluster only if they're in the same VPC as the cluster. All communication between your Kafka clients and your MSK Provisioned cluster are private by default and your streaming data never traverses the internet. To connect to your MSK Provisioned cluster from a client that's in the same VPC as the cluster, make sure the cluster's security group has an inbound rule that accepts traffic from the client's security group. For information about setting up these rules, see [Security Group Rules](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#SecurityGroupRules). For an example of how to access a cluster from an Amazon EC2 instance that's in the same VPC as the cluster, see [Get started using Amazon MSK](getting-started.md).

**Note**  
KRaft metadata mode and MSK Express brokers can't have open monitoring and public access both enabled.

To connect to your MSK Provisioned cluster from a client that's outside the cluster's VPC, see [Access from within AWS but outside cluster's VPC](https://docs.aws.amazon.com/msk/latest/developerguide/aws-access.html).

**Topics**
+ [Turn on public access to an MSK Provisioned cluster](public-access.md)
+ [Access from within AWS but outside cluster's VPC](aws-access.md)