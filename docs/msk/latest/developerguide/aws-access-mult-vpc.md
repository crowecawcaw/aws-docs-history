# Amazon MSK multi-VPC private connectivity in a single Region

Multi-VPC private connectivity (powered by [AWS PrivateLink](../../../vpc/latest/privatelink/what-is-privatelink.md "../../../vpc/latest/privatelink/what-is-privatelink.md")) for Amazon Managed Streaming for Apache Kafka (Amazon MSK) clusters is a feature that enables you to more quickly connect Kafka clients hosted in different Virtual Private Clouds (VPCs) and AWS accounts to an Amazon MSK cluster.

Multi-VPC private connectivity is a managed solution that simplifies the networking infrastructure for multi-VPC and cross-account connectivity. Clients can connect to the Amazon MSK cluster over PrivateLink while keeping all traffic within the AWS network. Multi-VPC private connectivity for Amazon MSK clusters is available in all AWS Regions where Amazon MSK is available.

###### Topics

- [What is multi-VPC private connectivity?](#mvpc-what-is "#mvpc-what-is")
- [Benefits of multi-VPC private connectivity](#mvpc-benefits "#mvpc-benefits")
- [Requirements and limitations for multi-VPC private connectivity](#mvpc-requirements "#mvpc-requirements")
- [Get started using multi-VPC private connectivity](mvpc-getting-started.md "mvpc-getting-started.md")
- [Update the authorization schemes on a cluster](mvpc-cross-account-update-authschemes.md "mvpc-cross-account-update-authschemes.md")
- [Reject a managed VPC connection to an Amazon MSK cluster](mvpc-cross-account-reject-connection.md "mvpc-cross-account-reject-connection.md")
- [Delete a managed VPC connection to an Amazon MSK cluster](mvpc-cross-account-delete-connection.md "mvpc-cross-account-delete-connection.md")
- [Permissions for multi-VPC private connectivity](mvpc-cross-account-permissions.md "mvpc-cross-account-permissions.md")

## What is multi-VPC private connectivity?

Multi-VPC private connectivity for Amazon MSK is a connectivity option that enables
you to connect Apache Kafka clients that are hosted in different Virtual Private
Clouds (VPCs) and AWS accounts to a MSK cluster.

Amazon MSK simplifies cross-account access with [cluster policies](mvpc-cluster-owner-action-policy.md "mvpc-cluster-owner-action-policy.md"). These policies allow the cluster owner to grant permissions for other AWS accounts to establish private connectivity to the MSK cluster.

## Benefits of multi-VPC private connectivity

Multi-VPC private connectivity has several advantages over [other connectivity solutions](aws-access.md "aws-access.md"):

- It automates operational management of the AWS PrivateLink connectivity solution.
- It allows overlapping IPs across connecting VPCs, eliminating the need to maintain non-overlapping IPs, complex peering, and routing tables associated with other VPC connectivity solutions.

You use a cluster policy for your MSK cluster to define which AWS accounts have permissions to set up cross-account private connectivity to your MSK cluster. The cross-account admin can delegate permissions to appropriate roles or users. When used with IAM client authentication, you can also use the cluster policy to define Kafka data plane permissions on a granular basis for the connecting clients.

## Requirements and limitations for multi-VPC private connectivity

Note these MSK cluster requirements for running multi-VPC private connectivity:

- Multi-VPC private connectivity is supported only on Apache Kafka 2.7.1 or higher. Make sure that any clients that you use with the MSK cluster are running Apache Kafka versions that are compatible with the cluster.
- Multi-VPC private connectivity supports auth types IAM, TLS and SASL/SCRAM. Unauthenticated clusters can't use multi-VPC private connectivity.
- If you are using the SASL/SCRAM or mTLS access-control methods, you must set Apache Kafka ACLs for your cluster. First, set the Apache Kafka ACLs for your cluster. Then, update the cluster's configuration to have the property `allow.everyone.if.no.acl.found` set to false for the cluster. For information about how to update the configuration of a cluster, see [Broker configuration
  operations](msk-configuration-operations.md "msk-configuration-operations.md"). If you are using IAM access control and want to apply authorization policies or update your authorization policies, see [IAM access control](iam-access-control.md "iam-access-control.md"). For information about Apache Kafka ACLs, see [Apache Kafka ACLs](msk-acls.md "msk-acls.md").
- Multi-VPC private connectivity doesn’t support the t3.small instance type.
- Multi-VPC private connectivity isn’t supported across AWS Regions, only on AWS accounts within the same Region.
- To set up multi-VPC private connectivity, you must have the same number of client subnets as cluster subnets. You must also make sure that [Availability Zone IDs](../../../ram/latest/userguide/working-with-az-ids.md "../../../ram/latest/userguide/working-with-az-ids.md") are same for the client subnet and cluster subnet.
- Amazon MSK doesn't support multi-VPC private connectivity to Zookeeper nodes.
