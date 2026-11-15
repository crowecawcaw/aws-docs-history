

# How Secrets Manager authorizes cross-account replication
<a name="cross-account-replicate-permissions"></a>

Every time Secrets Manager replicates a secret value, it decrypts the value with the primary secret's KMS key and re-encrypts it with the replica secret's KMS key. Secrets Manager needs an identity authorized for both operations. You choose the identity: a replication role that Secrets Manager assumes, or the caller's own identity through a forward access session (FAS). This topic explains both approaches.

## How replication is triggered
<a name="cross-account-replicate-permissions_trigger"></a>

Secrets Manager keeps the replica in sync by replicating each change to the primary secret value. For example, when you call [`PutSecretValue`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_PutSecretValue.html) on the primary secret, Secrets Manager creates the new version, moves the `AWSCURRENT` staging label to it, and then replicates the version to the replica. Replication is asynchronous and eventually consistent, so the replica might not reflect the latest value immediately. To follow progress, see [Monitor cross-account replication](cross-account-replicate-status.md).

## Replication performs two AWS KMS operations
<a name="cross-account-replicate-permissions_kms"></a>

To move a secret value from the primary to the replica, Secrets Manager performs the following two AWS KMS operations in order:

1. **Decrypt** – Secrets Manager calls `kms:Decrypt` with the primary secret's KMS key to decrypt the data key that protects the secret value.

1. **Encrypt** – Secrets Manager calls `kms:Encrypt` with the replica secret's KMS key to re-encrypt the data key for storage in the replica.

Because the two KMS keys are in different accounts, the replica key's key policy must grant the primary secret's account to call `kms:Encrypt`. You can scope this policy using the SecretARN encryption context to restrict use to the replica secret. For the key policy statement, see [Create a replica secret](cross-account-replicate-create.md). For more information about how Secrets Manager uses KMS keys and the encryption context during replication, see [AWS KMS keys for cross-account replication](security-encryption.md#security-encryption-cross-account).

**Important**  
An organization-level resource control policy (RCP) or service control policy (SCP) can block these AWS KMS operations, even if the identity and key policies allow them.

## Choose how Secrets Manager gets permissions
<a name="cross-account-replicate-permissions_choose"></a>

The difference between the two approaches is the identity that Secrets Manager uses to make the two AWS KMS calls.

### Replication role (recommended)
<a name="cross-account-replicate-permissions_choose_role"></a>

When you provide a replication role, Secrets Manager assumes that IAM role and uses it as the identity for both AWS KMS calls. Secrets Manager uses the role to call `kms:Decrypt` on the primary secret's KMS key and `kms:Encrypt` on the replica secret's KMS key. Because the role carries the cross-account permissions, individual callers of [`PutSecretValue`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_PutSecretValue.html) do not each need cross-account AWS KMS permissions. With this approach, the primary secret must use a customer managed KMS key.

For how to set up the role, its trust policy, and its permission policy, see [Set up the replication service role](#cross-account-replicate-permissions_role-policy).

### Forward access sessions
<a name="cross-account-replicate-permissions_choose_fas"></a>

A [forward access session](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_forward_access_sessions.html) (FAS) allows Secrets Manager to make downstream API calls using the permissions of the identity that triggered the operation. When you do not provide a replication role, Secrets Manager uses a forward access session: it makes the two AWS KMS calls under the identity that called the triggering operation, for example [`PutSecretValue`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_PutSecretValue.html).

**Note**  
With a forward access session, the initial replication is performed using the identity that called [`AssociateCrossAccountReplica`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_AssociateCrossAccountReplica.html).

With this approach, the triggering identity must hold both of the following permissions:
+ `kms:Decrypt` on the primary secret's KMS key. This key is in the same account as the caller, so the caller usually already holds this permission.
+ `kms:Encrypt` on the replica secret's KMS key. This key is in the replica account, so the caller needs cross-account permission to it. This is the requirement that FAS makes harder to satisfy.

If the triggering identity lacks either AWS KMS permission, replication cannot complete and the replication status becomes `Failed`. For how to read the status and recover, see [Monitor cross-account replication](cross-account-replicate-status.md).

The following identity policy allows a [`PutSecretValue`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_PutSecretValue.html) caller to use the cross-account `kms:Encrypt` permission it needs on the replica secret's KMS key. The statement is scoped with the SecretARN encryption context so that the identity can use the replica secret's KMS key only for the replica secret. Attach a policy like this to the identity that calls [`PutSecretValue`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_PutSecretValue.html) on the primary secret.

**Example Identity policy for a caller to encrypt under the replica secret's KMS key**  

```
{
  "Version": "2012-10-17",
  "Statement": [
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

## Recommendation
<a name="cross-account-replicate-permissions_recommendation"></a>

For most use cases, the replication role is the recommended approach. Secrets Manager assumes the role and uses it as the single identity for both AWS KMS calls, so you do not have to give every writer identity cross-account permission to the replica secret's KMS key. Forward access sessions can suit cases where the identities that change the primary secret already hold the cross-account `kms:Encrypt` permission on the replica secret's KMS key, and you prefer not to manage a replication role.

## Set up the replication service role
<a name="cross-account-replicate-permissions_role-policy"></a>

The service role must trust `secretsmanager.amazonaws.com`, and can be conditioned on `aws:SourceAccount` and `aws:SourceArn` to help prevent the confused deputy problem. Its permission policy must allow `kms:Decrypt` on the primary secret's KMS key (optionally with the SecretARN encryption context set to the primary secret ARN) and `kms:Encrypt` on the replica secret's KMS key (optionally with the SecretARN encryption context set to the replica secret ARN).

**Example Trust policy for the replication service role (representative example)**  

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "secretsmanager.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "111122223333"
        },
        "ArnEquals": {
          "aws:SourceArn": "arn:aws:secretsmanager:us-east-2:111122223333:secret:{{MyPrimarySecret}}-a1b2c3"
        }
      }
    }
  ]
}
```

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

The AWS managed key (`aws/secretsmanager`) does not support `kms:Decrypt` calls from a service role. You must use a customer managed key for the primary secret when you use a replication role. Add a statement like the following to your primary key's key policy to allow the replication role to decrypt the primary secret's data key.

**Example Primary key policy statement that allows the replication role to decrypt (representative example)**  

```
{
  "Sid": "AllowReplicationRoleDecrypt",
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/SecretsManagerCrossAccountReplicationRole"
  },
  "Action": "kms:Decrypt",
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "kms:EncryptionContext:SecretARN": "arn:aws:secretsmanager:us-east-2:111122223333:secret:{{MyPrimarySecret}}-a1b2c3"
    }
  }
}
```