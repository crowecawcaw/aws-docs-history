

# Associate the replica with a primary secret

After the replica-account owner creates the replica secret, the primary-account owner associates the replica with the primary secret to start replication. For how to create the replica secret, see [Create a replica secret](cross-account-replicate-create.md).

## How association works
<a name="cross-account-replicate-associate_how"></a>

The primary-account owner runs [`AssociateCrossAccountReplica`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_AssociateCrossAccountReplica.html) with `SecretId` for the primary secret and `CrossAccountReplicaARN` for the replica secret.

During association, Secrets Manager does the following:
+ Performs dry-run AWS KMS permission checks on both the primary and replica secret's KMS keys.
+ Sets up the replication metadata for both the primary and replica secrets.
+ Triggers the replication process to start replicating data from the primary secret to the replica secret.

### AcceptCrossAccountReplication
<a name="cross-account-replicate-associate_accept"></a>

`AcceptCrossAccountReplication` is an internal-only operation that Secrets Manager calls within `AssociateCrossAccountReplica`. This operation acts on the replica secret using the identity of the `AssociateCrossAccountReplica` caller.

The `AcceptCrossAccountReplication` call performs the dry-run `kms:Encrypt` check on the replica secret's KMS key and updates the replica secret's replication metadata. Only after `AcceptCrossAccountReplication` succeeds does `AssociateCrossAccountReplica` update the replication metadata on the primary secret.

## Permissions to associate a replica
<a name="cross-account-replicate-associate_permissions"></a>

The identity that associates the replica needs the following permissions:
+ `secretsmanager:AssociateCrossAccountReplica` on the primary secret.
+ `secretsmanager:GetSecretValue` on the primary secret.
+ `secretsmanager:AcceptCrossAccountReplication` on the replica secret.
+ `kms:Decrypt` on the primary secret's KMS key.
+ `kms:Encrypt` on the replica secret's KMS key (cross-account).

If you pass a replication role with `ReplicationRoleARN`, the caller also needs `iam:PassRole` for that role.

## Permissions for replication
<a name="cross-account-replicate-associate_permissions-for-replication"></a>

To satisfy the cross-account `kms:Encrypt` permission without giving every caller cross-account access to the replica key, we recommend a replication role. Secrets Manager assumes the role and uses it as the single identity for the encryption-key operations. For the two approaches Secrets Manager can use, see [How Secrets Manager authorizes cross-account replication](cross-account-replicate-permissions.md).

## Replica restriction
<a name="cross-account-replicate-associate_restriction"></a>

The replica restriction is a parameter of the `AssociateCrossAccountReplica` operation. This parameter controls whether Secrets Manager blocks replication to a replica secret outside your AWS organization.

By default, the replica restriction is `SameOrg`, which requires both accounts to be in the same AWS organization. To allow replication outside your AWS organization, set the restriction to `NoRestriction`.

Secrets Manager enforces the replica restriction only during the initial association. Calling [`AssociateCrossAccountReplica`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_AssociateCrossAccountReplica.html) again with a different restriction value does not change an existing association.

If the replica account does not meet the restriction, Secrets Manager returns an `AccessDeniedException` on the internal `AcceptCrossAccountReplication` call.

## AWS CLI
<a name="cross-account-replicate-associate_CLI"></a>

From the primary account, run [`AssociateCrossAccountReplica`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_AssociateCrossAccountReplica.html).

**Example Associate the replica with the primary secret**  

```
aws secretsmanager associate-cross-account-replica \
    --secret-id MyPrimarySecret \
    --cross-account-replica-arn arn:aws:secretsmanager:us-east-2:444455556666:secret:MyReplicaSecret-a1b2c3 \
    --replication-role-arn arn:aws:iam::111122223333:role/SecretsManagerCrossAccountReplicationRole
```

```
{
    "ARN": "arn:aws:secretsmanager:us-east-2:111122223333:secret:MyPrimarySecret-a1b2c3",
    "CrossAccountReplicaARN": "arn:aws:secretsmanager:us-east-2:444455556666:secret:MyReplicaSecret-a1b2c3",
    "ReplicationStatus": "InProgress"
}
```

**Example Replica restriction denies a replica outside the AWS organization**  

```
aws secretsmanager associate-cross-account-replica \
    --secret-id MyPrimarySecret \
    --cross-account-replica-arn arn:aws:secretsmanager:us-east-2:555555555555:secret:MyReplicaSecret-a1b2c3 \
    --replica-restriction SameOrg
```

```
An error occurred (AccessDeniedException) when calling the AssociateCrossAccountReplica operation: User: arn:aws:sts::111122223333:assumed-role/Admin/secretsmanager-Test is not authorized to perform: secretsmanager:AcceptCrossAccountReplication on resource: arn:aws:secretsmanager:us-east-2:555555555555:secret:MyReplicaSecret-a1b2c3 with an explicit deny in a resource-based policy
```

To replicate to an account outside your AWS organization, add `--replica-restriction NoRestriction`.

Replication is asynchronous. Call [`DescribeSecret`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_DescribeSecret.html) periodically and check the `ReplicationStatus` field until it shows `InSync`.

**Example Check the replication status**  

```
aws secretsmanager describe-secret \
    --secret-id MyPrimarySecret
```

```
{
    "ARN": "arn:aws:secretsmanager:us-east-2:111122223333:secret:MyPrimarySecret-a1b2c3",
    "Name": "MyPrimarySecret",
    "KmsKeyId": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
    "LastChangedDate": 1793805184.669,
    "LastAccessedDate": 1793664000.0,
    "VersionIdsToStages": {
        "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111": [
            "AWSCURRENT"
        ],
        "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222": [
            "AWSPREVIOUS"
        ]
    },
    "CreatedDate": 1793314703.348,
    "CrossAccountReplicas": [
        {
            "ReplicaSecretARN": "arn:aws:secretsmanager:us-east-2:444455556666:secret:MyReplicaSecret-a1b2c3",
            "ReplicationRoleARN": "arn:aws:iam::111122223333:role/SecretsManagerCrossAccountReplicationRole",
            "ReplicationStatus": "InSync"
        }
    ]
}
```

For more information about the replication status fields, see [Monitor cross-account replication](cross-account-replicate-status.md).

## AWS SDK
<a name="cross-account-replicate-associate_SDK"></a>

To associate the replica with the primary secret, use the [`AssociateCrossAccountReplica`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_AssociateCrossAccountReplica.html) command. For more information, see [AWS SDKs](asm_access.md#asm-sdks).