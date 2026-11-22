

# Create a replica secret

To enable cross-account replication, the replica-account owner creates a new replica secret in the replica account. Secrets Manager creates the replica with no secret value and initializes its permissions so that the primary-account owner can associate it with a primary secret. The replica's value stays empty until the primary-account owner starts replication.

You must encrypt the replica secret with a customer managed KMS key. The AWS managed key `aws/secretsmanager` does not support cross-account access.

After you create the replica secret, the primary-account owner associates it with the primary secret to start replication. For more information, see [Associate the replica with a primary secret](cross-account-replicate-associate.md).

## Steps to create a replica secret
<a name="cross-account-replicate-create_CLI"></a>

1. **Create the customer managed key.** In the replica account and AWS Region, create a symmetric encryption KMS key. Create a key policy that gives the replica account permissions to create a new secret. For more information, see [Permissions for the KMS key](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security-encryption.html#security-encryption-authz). You add the cross-account encryption permissions to this KMS key after you have the replica secret's ARN. For more information about creating keys, see [Creating keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) in the *AWS Key Management Service Developer Guide*.

1. **Create the replica secret.** In the replica account, run [`CreateSecret`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html). Set `CrossAccountPrimaryARN` to the ARN of the primary secret and `KmsKeyId` to the ARN of the replica customer managed KMS key.  
**Example Create a replica secret**  

   ```
   aws secretsmanager create-secret \
       --name MyReplicaSecret \
       --cross-account-primary-arn arn:aws:secretsmanager:us-east-2:111122223333:secret:MyPrimarySecret-a1b2c3 \
       --kms-key-id arn:aws:kms:us-east-2:444455556666:key/{{replica-key-id}}
   ```

   Until the primary secret replicates its first value, calling [`GetSecretValue`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html) on the replica returns `ResourceNotFoundException`. Secrets Manager does not support write operations on a replica secret, such as [`PutSecretValue`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_PutSecretValue.html). For the full list, see [Operations not supported on a replica secret](#cross-account-replicate-create_blocked).
**Note**  
When you create the replica secret, Secrets Manager attaches a system-managed resource policy named `cross-account-replication` to it. This managed policy is read-only and coexists with any resource policy you set on the replica.

   Because creating the replica attaches a managed resource policy, the caller needs `secretsmanager:PutResourcePolicy` on the new secret. The caller also needs the AWS KMS permissions to use the replica secret's KMS key.

1. **Update the replica key policy.** Now that the replica secret ARN exists, update the *key policy* of the replica KMS key to authorize the primary account to call `kms:Encrypt`. Adjust the principal and conditions to match your security requirements.

   To restrict the key's use further, you can optionally scope the statement with the [SecretARN encryption context](security-encryption.md#security-encryption-encryption-context) set to the replica secret ARN. With this condition, the primary account can use the key only when it replicates to this replica secret.  
**Example Replica key policy statement for cross-account replication**  <a name="cross-account-replicate-create_keypolicy-example"></a>

   ```
   {
     "Sid": "AllowCrossAccountReplication",
     "Effect": "Allow",
     "Principal": "*",
     "Action": "kms:Encrypt",
     "Resource": "*",
     "Condition": {
       "StringEquals": {
         "kms:CallerAccount": "111122223333",
         "kms:EncryptionContext:SecretARN": "arn:aws:secretsmanager:us-east-2:444455556666:secret:{{MyReplicaSecret}}-a1b2c3"
       }
     }
   }
   ```

   For more information about how Secrets Manager uses KMS keys and the encryption context for cross-account replication, see [AWS KMS keys for cross-account replication](security-encryption.md#security-encryption-cross-account).

## System-managed resource policy for the replica secret
<a name="cross-account-replicate-create_resource-policy"></a>

When you create the replica secret, Secrets Manager creates a system-managed resource policy that allows the primary secret's owner to set up replication to this replica secret. You can't edit this policy directly. Secrets Manager removes it when you call `StopReplicationToReplica`. You can override the policy and explicitly deny `secretsmanager:AcceptCrossAccountReplication`, but doing so prevents the primary account from replicating to this replica.

**Example system-managed resource policy on the replica secret**  

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "CrossAccountReplication",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::111122223333:root" },
      "Action": "secretsmanager:AcceptCrossAccountReplication",
      "Resource": "*",
      "Condition": {
        "ForAnyValue:StringEquals": { "aws:InvokedBy": "secretsmanager.amazonaws.com" },
        "ArnEquals": { "secretsmanager:CrossAccountPrimaryARN": "arn:aws:secretsmanager:us-east-2:111122223333:secret:MyPrimarySecret-a1b2c3" }
      }
    }
  ]
}
```

## Operations not supported on a replica secret
<a name="cross-account-replicate-create_blocked"></a>

While a secret is a cross-account replica, Secrets Manager does not support the following operations on it. If you call one of the following operations on a replica secret, the request returns `InvalidRequestException`:
+ `PutSecretValue`
+ `UpdateSecret`
+ `DeleteSecret` – To delete a replica, first call `StopReplicationToReplica` to promote it to a standalone secret, and then call `DeleteSecret`.
+ `RotateSecret`
+ `CancelRotateSecret`
+ `UpdateSecretVersionStage`
+ `ReplicateSecretToRegions`
+ `RemoveRegionsFromReplication`

Operations that remain available on a replica secret include `GetSecretValue`, `DescribeSecret`, the resource-policy operations (`GetResourcePolicy`, `PutResourcePolicy`, and `DeleteResourcePolicy`), tag operations, and `StopReplicationToReplica`.

## AWS SDK
<a name="cross-account-replicate-create_SDK"></a>

To create a replica secret, use the [`CreateSecret`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html) command with the `CrossAccountPrimaryARN` and `KmsKeyId` parameters. For more information, see [AWS SDKs](asm_access.md#asm-sdks).