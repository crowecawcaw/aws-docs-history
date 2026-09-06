

# Troubleshoot AWS Secrets Manager replication
<a name="replicate-secrets_troubleshoot"></a>

AWS Secrets Manager replication might fail for various reasons. To check why a secret failed to replicate, you can do one of the following:
+ Call the `DescribeSecret` API operation
+ Review AWS CloudTrail events

When replication fails:
+ If there are no usable secret versions, Secrets Manager removes the secret from the replica Region.
+ If there are successfully replicated secret versions, they remain in the replica Region until you explicitly remove them using the `RemoveRegionsFromReplication` API operation.

The following sections describe some common reasons for replication failures.

## A secret with the same name exists in the selected Region
<a name="w2aac19c33c13"></a>

To resolve this issue, you can overwrite the duplicate name secret in the replica Region. Retry replication, and then in the **Retry replication** dialog box, choose **Overwrite**.

## No permissions available on the KMS key to complete the replication
<a name="w2aac19c33c15"></a>

Secrets Manager first decrypts the secret before re-encrypting with the new KMS key in the replica Region. If you don't have `kms:Decrypt` permission to the encryption key in the primary Region, you will encounter this error. To encrypt the replicated secret with a KMS key other than `aws/secretsmanager`, you need `kms:GenerateDataKey` and `kms:Encrypt` to the key. See [Permissions for the KMS key](security-encryption.md#security-encryption-authz).

## The KMS key is disabled or not found
<a name="w2aac19c33c17"></a>

If the encryption key in the primary Region is disabled or deleted, Secrets Manager can't replicate the secret. This error can occur even if you have changed the encryption key, if the secret has [custom labelled versions](whats-in-a-secret.md#term_version) that were encrypted with the disabled or deleted encryption key. For information about how Secrets Manager does encryption, see [Secret encryption and decryption in AWS Secrets Manager](security-encryption.md). To work around this issue, you can recreate the secret versions so that Secrets Manager encrypts them with the current encryption key. For more information, see [Change the encryption key for a secret](manage_update-encryption-key.md#manage_update-encryption-key_CLI). Then retry replication.

```
aws secretsmanager put-secret-value \
  --secret-id testDescriptionUpdate \
  --secret-string "SecretValue" \
  --version-stages "MyCustomLabel"
```

## You have not enabled the Region where the replication occurs
<a name="w2aac19c33c19"></a>

For information about how to enable a Region, see [Managing AWS Regions.](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html#rande-manage-enable) in the *AWS Account Management Reference Guide*.