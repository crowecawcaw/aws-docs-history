

# Stop cross-account replication
<a name="cross-account-replicate-remove"></a>

Either account can stop cross-account replication at any time, and there is no required order between the two accounts:
+ The primary-account owner stops replication with [`DisassociateCrossAccountReplica`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_DisassociateCrossAccountReplica.html).
+ The replica-account owner stops replication with [`StopReplicationToReplica`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_StopReplicationToReplica.html).

When an account stops replication, Secrets Manager removes the replication information from that side. Calling [`DisassociateCrossAccountReplica`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_DisassociateCrossAccountReplica.html) on the primary secret removes the replica entry from the primary secret's list of replicas. Calling [`StopReplicationToReplica`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_StopReplicationToReplica.html) on the replica secret removes the cross-account primary information from the replica secret. `StopReplicationToReplica` also removes the system-managed resource policy named `cross-account-replication` that Secrets Manager attached to the replica secret during [`CreateSecret`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html). Because `StopReplicationToReplica` removes that managed policy, the caller must also have the `secretsmanager:DeleteResourcePolicy` permission. You can further qualify the delete permission with the `secretsmanager:PolicyName` condition key.

**Important**  
Secrets Manager blocks you from deleting a secret until that account has stopped replication from its own side. Before you delete the primary secret, run [`DisassociateCrossAccountReplica`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_DisassociateCrossAccountReplica.html) in the primary account. Before you delete the replica secret, run [`StopReplicationToReplica`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_StopReplicationToReplica.html) in the replica account.

## AWS CLI
<a name="cross-account-replicate-remove_CLI"></a>

**Example Stop replication from the primary account**  
The following [`DisassociateCrossAccountReplica`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_DisassociateCrossAccountReplica.html) example stops replication from the primary side.  

```
aws secretsmanager disassociate-cross-account-replica \
    --secret-id MyPrimarySecret \
    --cross-account-replica-arn arn:aws:secretsmanager:us-east-2:444455556666:secret:MyReplicaSecret-a1b2c3
```

```
{
    "ARN": "arn:aws:secretsmanager:us-east-2:111122223333:secret:MyPrimarySecret-a1b2c3",
    "CrossAccountReplicaARN": "arn:aws:secretsmanager:us-east-2:444455556666:secret:MyReplicaSecret-a1b2c3"
}
```

**Example Stop replication from the replica account**  
The following [`StopReplicationToReplica`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_StopReplicationToReplica.html) example stops replication from the replica side.  

```
aws secretsmanager stop-replication-to-replica \
    --secret-id MyReplicaSecret
```

```
{
    "ARN": "arn:aws:secretsmanager:us-east-2:444455556666:secret:MyReplicaSecret-a1b2c3"
}
```

## AWS SDK
<a name="cross-account-replicate-remove_SDK"></a>

To stop replication from the primary account, use the [`DisassociateCrossAccountReplica`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_DisassociateCrossAccountReplica.html) command. To stop replication from the replica account, use the [`StopReplicationToReplica`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_StopReplicationToReplica.html) command. For more information, see [AWS SDKs](asm_access.md#asm-sdks).