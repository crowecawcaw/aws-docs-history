# Change the encryption key for an AWS Secrets Manager secret

Secrets Manager uses [envelope encryption](security-encryption.md "security-encryption.md") with AWS KMS keys and data keys to protect each secret value. For each secret, you can choose which KMS key to use. You can use the
AWS managed key **aws/secretsmanager**, or you can use a customer managed key. For most cases, we recommend using **aws/secretsmanager**, and there is no cost for using it. If you need to access the secret from another AWS account, or if you want to use your own KMS key so that you can rotate it or apply a key policy to it, use a customer managed key. You must have [Permissions for the KMS key](security-encryption.md#security-encryption-authz "security-encryption.md#security-encryption-authz"). For information about the costs of using a customer managed key, see [Pricing](intro.md#asm_pricing "intro.md#asm_pricing").

You can change the encryption key for your secret. For example, if you want to [access the secret from another account](auth-and-access_examples_cross.md "auth-and-access_examples_cross.md"), and the secret is currently encrypted using the AWS managed key `aws/secretsmanager`, you can switch to a customer managed key.

###### Tip

If you want to rotate your customer managed key, we recommend using AWS KMS automatic key rotation. For more information, see [Rotating AWS KMS keys](../../../kms/latest/developerguide/rotate-keys.md "../../../kms/latest/developerguide/rotate-keys.md").

When you change the encryption key, Secrets Manager re-encrypts `AWSCURRENT`, `AWSPENDING`, and `AWSPREVIOUS` versions with the new key. To avoid locking you out of the secret, Secrets Manager keeps all existing versions encrypted with the previous key. That means you can decrypt `AWSCURRENT`, `AWSPENDING`, and `AWSPREVIOUS` versions with the previous key or the new key. If you don't have `kms:Decrypt` permission to the previous key, when you change the encryption key, Secrets Manager can't decrypt the secret versions to re-encrypt them. In this case, the existing versions are not re-encrypted.

To make it so `AWSCURRENT` can only be decrypted by the new encryption key, create a new version of the secret with the new key. Then to be able to decrypt the `AWSCURRENT` secret version, you must have permission to the new key.

If you deactivate the previous encryption key, you will not be able to decrypt any secret versions except `AWSCURRENT`, `AWSPENDING`, and `AWSPREVIOUS`. If you have other labelled secret versions that you want to retain access to, you need to recreate those versions with the new encryption key using the [AWS CLI](#manage_update-encryption-key_CLI "#manage_update-encryption-key_CLI").

###### To change the encryption key for a secret (console)

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
2. From the list of secrets, choose your secret.
3. On the secret details page, in the **Secrets details** section,
   choose **Actions**, and then choose **Edit encryption
   key**.

## AWS CLI

If you change the encryption key for a secret and then deactivate the previous encryption key, you will not be able to decrypt any secret versions except `AWSCURRENT`, `AWSPENDING`, and `AWSPREVIOUS`. If you have other labelled secret versions that you want to retain access to, you need to recreate those versions with the new encryption key using the AWS CLI.

###### To change the encryption key for a secret (AWS CLI)

1. The following [`update-secret`](../../../cli/latest/reference/secretsmanager/update-secret.md "../../../cli/latest/reference/secretsmanager/update-secret.md") example updates the KMS key used to encrypt the secret value. The KMS key must be in the same region as the secret.

```
aws secretsmanager update-secret \
      --secret-id MyTestSecret \
      --kms-key-id arn:aws:kms:us-west-2:123456789012:key/EXAMPLE1-90ab-cdef-fedc-ba987EXAMPLE
```

2. (Optional) If you have secret versions that have custom labels, to re-encrypt them using the new key, you must recreate those versions.

When you enter commands in a command shell, there is a risk of the command
history being accessed or utilities having access to your command parameters. See [Mitigate the risks of using the AWS CLI
to store your AWS Secrets Manager secrets](security_cli-exposure-risks.md "security_cli-exposure-risks.md").

    1. Get the value of the secret version.



    ```
    aws secretsmanager get-secret-value \
          --secret-id MyTestSecret \
          --version-stage MyCustomLabel
    ```

    Make a note of the secret value.
    2. Create a new version with that value.



    ```
    aws secretsmanager put-secret-value \
        --secret-id testDescriptionUpdate \
        --secret-string "SecretValue" \
        --version-stages "MyCustomLabel"
    ```
