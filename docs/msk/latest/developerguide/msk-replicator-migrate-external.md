# Migrate from non-MSK Apache Kafka clusters to Amazon MSK Provisioned

You can use MSK Replicator to migrate Apache Kafka workloads from self-managed environments to Amazon MSK Provisioned clusters. MSK Replicator supports data migration from Kafka deployments (Kafka version 2.8.1 or later) that have SASL/SCRAM, mutual TLS (mTLS), or SASL/OAUTHBEARER (OAuth) authentication enabled.

###### Note

SASL/SCRAM, mTLS, or SASL/OAUTHBEARER authentication is required only for MSK Replicator to connect to your self-managed Kafka cluster. Your client applications can continue using their existing authentication mechanisms.

###### Prerequisites

Before you begin, ensure you have the following:

1. Source Apache Kafka cluster running version 2.8.1 or later
2. SASL/SCRAM, mTLS, or SASL/OAUTHBEARER authentication enabled on source cluster
3. SSL encryption configured on source cluster
4. Network connectivity via AWS Site-to-Site VPN or AWS Direct Connect
5. VPC subnets configured for Secrets Manager access
   For detailed instructions, see [Set up prerequisites for MSK Replicator with self-managed Apache Kafka clusters](msk-replicator-external-prereqs.md "msk-replicator-external-prereqs.md").

###### Step 1: Create an Amazon MSK Provisioned cluster

Create an MSK Provisioned cluster with IAM authentication enabled. Minimum three brokers across three AZs. See [Prepare the target cluster](msk-replicator-prepare-clusters.md#msk-replicator-prepare-target "msk-replicator-prepare-clusters.md#msk-replicator-prepare-target").

###### Step 2: Create an IAM execution role

Attach the `AWSMSKReplicatorExecutionRole` managed policy and configure the trust policy for `kafka.amazonaws.com`. Add inline permissions for AWS Secrets Manager (and AWS KMS if your secrets are CMK-encrypted) per [Additional SER permissions for SASL/SCRAM, mTLS, SASL/OAUTHBEARER, and customer managed keys](msk-replicator-ser-additional-perms.md "msk-replicator-ser-additional-perms.md"). See [Set up prerequisites for MSK Replicator with self-managed Apache Kafka clusters](msk-replicator-external-prereqs.md "msk-replicator-external-prereqs.md").

###### Step 3: Configure SASL/SCRAM, mTLS, or SASL/OAUTHBEARER, and SSL on self-managed cluster

Configure authentication on your self-managed cluster. For SASL/SCRAM, create a dedicated SCRAM user with the required ACL permissions. For mTLS, configure an SSL listener with client certificate authentication. For SASL/OAUTHBEARER, configure your brokers for OAUTHBEARER and register the identity provider (IDP) that vends access tokens. Configure SSL certificates. See [Set up prerequisites for MSK Replicator with self-managed Apache Kafka clusters](msk-replicator-external-prereqs.md "msk-replicator-external-prereqs.md").

###### Step 4: Store credentials in AWS Secrets Manager

Create a secret with the appropriate key-value pairs for your authentication type. For SASL/SCRAM, include `username`, `password`, and `certificate` fields. For mTLS, include `certificate` and `privateKey` fields (and optionally `privateKeyPassword` for encrypted private keys). For SASL/OAUTHBEARER using the client credentials mechanism, include `client_id` and `client_secret` fields. See [Set up prerequisites for MSK Replicator with self-managed Apache Kafka clusters](msk-replicator-external-prereqs.md "msk-replicator-external-prereqs.md").

###### Step 5: Create the Replicator

Use `CreateReplicator` API with `EARLIEST` starting position, Identical topic name replication, and `synchroniseConsumerGroupOffsets` set to `true`. The IAM principal that calls `CreateReplicator` must have the API caller permissions described in [IAM permissions required to create an MSK Replicator](msk-replicator-create-iam-perms.md "msk-replicator-create-iam-perms.md"). If you plan to set up bidirectional replication for rollback capability (Step 6), also set `consumerGroupOffsetSyncMode` to `ENHANCED` on both the forward and reverse Replicators. Allow approximately 30 minutes for the Replicator to reach RUNNING status. See [CreateReplicator API examples for self-managed Kafka clusters](msk-replicator-external-api-examples.md "msk-replicator-external-api-examples.md").

###### Step 6: (Optional) Set up bidirectional replication

Create a reverse Replicator from the MSK Provisioned cluster back to the self-managed cluster for rollback capabilities. Identify both clusters in the reverse Replicator exactly as you identified them in the forward Replicator. See [Bidirectional replication example](msk-replicator-external-api-examples.md#msk-replicator-external-bidirectional "msk-replicator-external-api-examples.md#msk-replicator-external-bidirectional").

###### Step 7: Monitor replication progress

Monitor the following metrics:

- `MessageLag` (should reach 0)
- `ReplicationLatency`
- `ConsumerGroupOffsetSyncFailure` (should be 0)
- `ConsumerGroupCount`
- `OffsetLag (MSK Cluster)` and `OffsetLag (Non-MSK Cluster)`
  For more information, see [Monitor replication](msk-replicator-monitor.md "msk-replicator-monitor.md").

###### Step 8: Migrate applications

Follow these steps to migrate your applications:

1. Stop producers writing to self-managed cluster
2. Reconfigure producers to MSK Provisioned cluster with IAM authentication
3. Monitor `MessageLag` until it reaches 0
4. Stop consumers on self-managed cluster
5. Reconfigure consumers to MSK Provisioned cluster

###### Step 9: (Optional) Roll back to self-managed cluster

If bidirectional replication was configured, you can reverse the migration steps to roll back to the self-managed cluster. The reverse Replicator (MSK Provisioned → External) will have been keeping the self-managed cluster in sync, so consumers can be redirected back without data loss.
