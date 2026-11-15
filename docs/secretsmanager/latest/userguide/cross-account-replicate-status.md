

# Monitor cross-account replication
<a name="cross-account-replicate-status"></a>

Cross-account replication is asynchronous. To monitor progress, call [`DescribeSecret`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_DescribeSecret.html) periodically from either account and check the `ReplicationStatus` field.

## Replication status fields
<a name="cross-account-replicate-status_fields"></a>

The fields that [`DescribeSecret`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_DescribeSecret.html) returns depend on whether you describe the replica or the primary secret:
+ When you describe the *replica* secret, Secrets Manager returns `CrossAccountPrimary`, which contains `PrimarySecretARN`, `ReplicationStatus`, and `StatusMessage`.
+ When you describe the *primary* secret, Secrets Manager returns `CrossAccountReplicas`, a list in which each entry contains `ReplicaSecretARN`, `ReplicationRoleARN`, `ReplicationStatus`, and `StatusMessage`.

The `StatusMessage` field provides details when replication fails or stalls, for example, when a AWS KMS key permission is missing.

## Replication status values
<a name="cross-account-replicate-status_values"></a>

The `ReplicationStatus` field reports one of the following values:

Pending  
Secrets Manager has recorded the replication relationship but has not yet started copying the secret value. Only the replica secret shows this status.

InProgress  
Secrets Manager is copying the secret value from the primary to the replica.

InSync  
The replica holds the same secret value as the primary.

Failed  
Secrets Manager could not complete replication. See [Determine the cause of a failed replication](#cross-account-replicate-status_cause).

Detached  
One of the two accounts stopped replication, so the primary and replica secrets are no longer linked. For more information, see [Stop cross-account replication](cross-account-replicate-remove.md).

## Determine the cause of a failed replication
<a name="cross-account-replicate-status_cause"></a>

A `Failed` status means that Secrets Manager was unable to complete the replication. Review the `StatusMessage` to determine why replication failed; it contains additional information about the cause. The most common reasons for replication to fail are related to authorization. These failures are usually one of the following:
+ Secrets Manager does not have permission to call `kms:Decrypt` on the primary KMS key or `kms:Encrypt` on the replica KMS key.
+ Secrets Manager is unable to assume the replication role.

For AWS KMS failures, review the `StatusMessage` to identify the source of the failure. If you use a forward access session (FAS) instead of a replication role, verify that the caller's identity has the required `kms:Decrypt` and `kms:Encrypt` permissions. For more information about the permissions that replication requires, see [How Secrets Manager authorizes cross-account replication](cross-account-replicate-permissions.md).

### Example StatusMessage values
<a name="cross-account-replicate-status_statusmessage-examples"></a>

The following examples show common `StatusMessage` values for failed replications.

**Example kms:Decrypt denied on the primary secret's key**  

```
Replication failed: User: arn:aws:sts::111122223333:assumed-role/CrossAccountReplicationRole-1234567890123456789/SecretsManagerCrossAccountReplication-444455556666 is not authorized to perform: kms:Decrypt on resource: arn:aws:kms:us-west-2:111122223333:key/a8c8999a-a026-4df3-a42a-d0972222fe36 because no resource-based policy allows the kms:Decrypt action (Service: AWSKMS; Status Code: 400; Error Code: AccessDeniedException; Request ID: 12345678-1234-1234-1234-123456781234; Proxy: null)
```

**Example kms:Encrypt denied on the replica secret's key**  

```
Replication failed: User: arn:aws:sts::111122223333:assumed-role/CrossAccountReplicationRole-9876543210987654321/SecretsManagerCrossAccountReplication-444455556666 is not authorized to perform: kms:Encrypt on this resource because the resource does not exist in this Region, no resource-based policies allow access, or a resource-based policy explicitly denies access (Service: AWSKMS; Status Code: 400; Error Code: AccessDeniedException; Request ID: 87654321-4321-4321-4321-aaaabbbbcccc; Proxy: null)
```

**Example Unable to assume the replication role**  

```
Replication failed: Secrets Manager failed to assume role arn:aws:iam::111122223333:role/CrossAccountReplicationRole
```

## Recover from a failed replication
<a name="cross-account-replicate-status_failed"></a>

After you correct the permissions, the primary-account owner calls [`AssociateCrossAccountReplica`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_AssociateCrossAccountReplica.html) again for the same replica to retry replication. This call does not fix permissions; it only re-triggers the replication attempt. If permission issues remain, Secrets Manager will update the `StatusMessage`. When all permission issues are resolved, replication completes and the status changes to `InSync`.

**Example Retry a failed replication**  

```
aws secretsmanager associate-cross-account-replica \
    --secret-id MyPrimarySecret \
    --cross-account-replica-arn arn:aws:secretsmanager:us-east-2:444455556666:secret:MyReplicaSecret-a1b2c3 \
    --replication-role-arn arn:aws:iam::111122223333:role/SecretsManagerCrossAccountReplicationRole
```