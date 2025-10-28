# Promote a replica secret to a standalone secret in AWS Secrets Manager

A replica secret is a secret that is replicated from a primary in another AWS Region. It
has the same secret value and metadata as the primary, but it can be encrypted with a
different KMS key. A replica secret can't be updated independently from its primary
secret, except for its encryption key. Promoting a replica secret disconnects the replica
secret from the primary secret and makes the replica secret a standalone secret. Changes to
the primary secret won't replicate to the standalone secret.

You might want to promote a replica secret to a standalone secret as a disaster recovery
solution if the primary secret becomes unavailable. Or you might want to promote a replica
to a standalone secret if you want to turn on rotation for the replica.

If you promote a replica, be sure to update the corresponding applications to use the
standalone secret.

Secrets Manager generates a CloudTrail log entry when you promote a secret. For more information, see [Log AWS Secrets Manager events with AWS CloudTrail](monitoring-cloudtrail.md "monitoring-cloudtrail.md").

###### To promote a replica secret (console)

1. Log in to the Secrets Manager at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
2. Navigate to the replica region.
3. On the **Secrets** page, choose the replica secret.
4. On the replica secret details page, choose **Promote to standalone
   secret**.
5. In the **Promote replica to standalone secret** dialog box, enter the Region and then choose **Promote replica**.

## AWS CLI

###### Example Promote a replica secret to a primary

The following [`stop-replication-to-replica`](../../../cli/latest/reference/secretsmanager/stop-replication-to-replica.md "../../../cli/latest/reference/secretsmanager/stop-replication-to-replica.md") example removes the link between a replica secret to the primary. The replica secret is promoted to a primary secret in the replica region. You must call [`stop-replication-to-replica`](../../../cli/latest/reference/secretsmanager/stop-replication-to-replica.md "../../../cli/latest/reference/secretsmanager/stop-replication-to-replica.md") from within the replica region.

```
aws secretsmanager stop-replication-to-replica \
    --secret-id MyTestSecret
```

## AWS SDK

To promote a replica to a standalone secret, use the [`StopReplicationToReplica`](../apireference/API_StopReplicationToReplica.md "../apireference/API_StopReplicationToReplica.md") command. You must call this
command from the replica secret Region. For more information, see [AWS SDKs](asm_access.md#asm-sdks "asm_access.md#asm-sdks").
