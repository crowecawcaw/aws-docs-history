

# Prerequisites
<a name="msk-replicator-prerequisites"></a>

Before you create an MSK Replicator, ensure that you have the following prerequisites in place.

## IAM permissions required to create an MSK Replicator
<a name="msk-replicator-prereq-iam"></a>

Before creating an MSK Replicator, ensure your IAM role has the required permissions. For the full policy examples, see [IAM permissions required to create an MSK Replicator](msk-replicator-create-iam-perms.md).

## Networking prerequisites
<a name="msk-replicator-prereq-networking"></a>

Depending on whether you are setting up cross-region or same-region replication, the networking requirements differ.
+ **Cross-region replication (CRR)** – The source cluster must have multi-VPC private connectivity turned on for IAM access control. You must also attach a resource-based permissions policy to the source cluster. See [Prepare source and target clusters](msk-replicator-prepare-clusters.md).
+ **Same-region replication (SRR)** – Multi-VPC private connectivity is not required. However, you must configure security groups so that the Replicator can reach both the source and target clusters on port 9098 (the IAM access control port).

For both CRR and SRR, ensure that your network ACLs are not blocking the connection between the MSK Replicator and your source and target clusters.