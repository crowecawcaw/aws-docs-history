

# IAM permissions reference
<a name="msk-replicator-iam-ref"></a>

The following table summarizes the IAM actions that the API caller (the IAM principal that calls `CreateReplicator` and other replicator APIs) needs. For complete policy examples, see [IAM permissions required to create an MSK Replicator](msk-replicator-create-iam-perms.md).


| Action | Description | 
| --- | --- | 
| `kafka:CreateReplicator` | Grants permission to create a replicator. | 
| `kafka:DescribeReplicator` | Grants permission to describe a replicator. | 
| `kafka:UpdateReplicationInfo` | Grants permission to update replication info of a replicator. | 
| `kafka:DeleteReplicator` | Grants permission to delete a replicator. | 
| `kafka:ListReplicators` | Grants permission to list replicators. | 
| `kafka:TagResource` | Grants permission to tag a replicator. Only needed if tags are provided during creation. | 
| `kafka:ListTagsForResource` | Grants permission to list tags for a replicator. | 
| `kafka:GetBootstrapBrokers` | Grants permission to retrieve bootstrap broker endpoints for the source and target clusters during replicator creation. | 
| `kafka:DescribeClusterV2` | Grants permission to describe the source and target clusters during replicator creation. | 
| `iam:PassRole` | Grants permission to pass the service execution role to `kafka.amazonaws.com`. | 
| `iam:CreateServiceLinkedRole` | Grants permission to create the `AWSServiceRoleForKafka*` service-linked role on first use. | 
| `ec2:DescribeSubnets`, `ec2:DescribeSecurityGroups`, `ec2:DescribeVpcs` | Grants permission to validate the VPC configuration provided to the replicator. | 

For service execution role permissions, see the [`AWSMSKReplicatorExecutionRole`](https://docs.aws.amazon.com/msk/latest/developerguide/security-iam-awsmanpol-AWSMSKReplicatorExecutionRole.html) managed policy. For SASL/SCRAM, mTLS, SASL/OAUTHBEARER (OAuth), and customer managed key scenarios, see [Additional SER permissions for SASL/SCRAM, mTLS, SASL/OAUTHBEARER, and customer managed keys](msk-replicator-ser-additional-perms.md).