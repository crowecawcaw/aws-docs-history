

# Permissions for cross-account replication

Cross-account replication is a two-party process, so each account owner needs permission for the operations they run. For an overview of the feature, see [Cross-account replication](cross-account-replicate-secrets.md). For how Secrets Manager obtains the encryption-key permissions it needs during replication, and the choice between a replication role and forward access sessions, see [How Secrets Manager authorizes cross-account replication](cross-account-replicate-permissions.md).
+ To create the replica secret, the replica-account owner needs `secretsmanager:CreateSecret` and `secretsmanager:PutResourcePolicy`. Secrets Manager attaches a managed resource policy named `cross-account-replication` to the replica when you create it, which is why `secretsmanager:PutResourcePolicy` is required.
+ To stop replication, the replica-account owner needs `secretsmanager:StopReplicationToReplica` and `secretsmanager:DeleteResourcePolicy`. Secrets Manager removes the managed resource policy when you stop replication, which is why `secretsmanager:DeleteResourcePolicy` is required.
+ To associate a replica, the primary-account owner needs `secretsmanager:AssociateCrossAccountReplica` and `secretsmanager:GetSecretValue` on the primary secret, `secretsmanager:AcceptCrossAccountReplication` on the replica secret, `kms:Decrypt` on the primary secret's KMS key, and `kms:Encrypt` on the replica secret's KMS key. To authorize the association with a replication service role, the primary-account owner also needs `iam:PassRole` for that role.
+ To disassociate a replica, the primary-account owner needs `secretsmanager:DisassociateCrossAccountReplica` on the primary secret.

The AWS KMS permissions required for cross-account replication are the same permissions that Secrets Manager requires for any secret encrypted with a customer managed key. For more information, see [Permissions for the KMS key](security-encryption.md#security-encryption-authz).

## Replication service role
<a name="auth-and-access_cross-account-replication_role"></a>

We recommend that you authorize the association with a *replication service role* in the primary account, which you pass with the `ReplicationRoleARN` parameter. The service role lets Secrets Manager decrypt the primary secret value and encrypt it under the replica KMS key on your behalf. The role trusts `secretsmanager.amazonaws.com`, conditioned on `aws:SourceAccount` and `aws:SourceArn` to help prevent the confused deputy problem, and its permission policy allows `kms:Decrypt` on the primary secret's key and `kms:Encrypt` on the replica secret's key, each scoped by the [SecretARN encryption context](security-encryption.md#security-encryption-encryption-context).

**Example Permission policy for the replication service role (representative example)**  

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DecryptPrimarySecretKey",
      "Effect": "Allow",
      "Action": "kms:Decrypt",
      "Resource": "arn:aws:kms:us-east-2:111122223333:key/{{primary-key-id}}",
      "Condition": {
        "StringEquals": {
          "kms:EncryptionContext:SecretARN": "arn:aws:secretsmanager:us-east-2:111122223333:secret:{{MyPrimarySecret}}-a1b2c3"
        }
      }
    },
    {
      "Sid": "EncryptReplicaSecretKey",
      "Effect": "Allow",
      "Action": "kms:Encrypt",
      "Resource": "arn:aws:kms:us-east-2:444455556666:key/{{replica-key-id}}",
      "Condition": {
        "StringEquals": {
          "kms:EncryptionContext:SecretARN": "arn:aws:secretsmanager:us-east-2:444455556666:secret:{{MyReplicaSecret}}-a1b2c3"
        }
      }
    }
  ]
}
```

For the trust policy and the matching replica key policy statement, see [How Secrets Manager authorizes cross-account replication](cross-account-replicate-permissions.md).

## Replica restriction
<a name="auth-and-access_cross-account-replication_restriction"></a>

When the primary-account owner associates a replica, the replica restriction controls which accounts can receive the replica. By default, the restriction is `SameOrg`, which requires the replica account to be in the same AWS organization as the primary account. This safeguard helps prevent a secret from being replicated to an unexpected account. To replicate a secret to an account outside your AWS organization, the primary-account owner must explicitly set the restriction to `NoRestriction` with `ReplicaRestriction`.