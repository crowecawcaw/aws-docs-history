# Managing secrets and resource

policies

When you [configure a third-party
speech provider](configure-third-party-speech-providers.md "configure-third-party-speech-providers.md"), you will need to create a secret in Secrets Manager that contains the speech
provider's API key. Creating the secret is a two step process:

- Create the secret containing the API key. For instructions, see [Create an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md").
- Configure the necessary permissions:

      + Attach a resource-based policy to the secret.
      + Attach a resource-based policy to the KMS key (not the API key) associated
       with the secret. The KMS key protects the API key in the secret.

  These policies allow Amazon Connect to access to the API key within the secret. Note that you
  cannot use the default `aws/secretsmanager` KMS key; you will have to
  create a new key or use an existing customer-managed key. For more information about
  how KMS keys secure secrets, see [Secret encryption
  and decryption in Secrets Manager](../../../secretsmanager/latest/userguide/security-encryption.md "../../../secretsmanager/latest/userguide/security-encryption.md").
  Make sure that the resource-based policy for the secret includes the
  `aws:SourceAccount` and `aws:SourceArn` confused deputy conditions
  (see [The confused
  deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md")) and that the resource-based policy for the KMS key includes the
  `kms:EncryptionContext:SecretARN` condition. This will ensure that Amazon Connect can
  only access your API key secret in context of a single specific instance, and can only access
  your KMS key in context of both that instance and the specific secret.

## Example of a resource-based

policy for Secrets Manager secrets

The following is an example of a resource-based policy that you can attach to your
secret.

```

{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "connect.amazonaws.com"
        ]
      },
      "Action": "secretsmanager:GetSecretValue",
      "Resource": "*",
      "Condition": {
        "ArnLike": {
          "aws:sourceArn": "///the ARN of your Amazon Connect instance///"
        },
        "StringEquals": {
          "aws:sourceAccount": "///Your account ID///"
        }
      }
    }
  ]
}

```

## Example of a resource-based policy for

AWS KMS keys

The following is an example of a resource-based policy that you can attach to your
KMS key.

```

{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "connect.amazonaws.com"
        ]
      },
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "ArnLike": {
          "aws:sourceArn": "///the ARN of your Amazon Connect instance///"
        },
        "StringEquals": {
          "aws:sourceAccount": "///Your account ID///",
          "kms:EncryptionContext:SecretARN": "///the ARN of your secrets manager secret///"
        }
      }
    }
  ]
}

```

## Attaching a resource-based

policy to your Secrets Manager secret

To attach a resource-based policy to your secret, go to the Secrets Manager console
within the AWS Management Console, navigate to your secret, choose **Edit
Permissions** or **Resource Permissions** and then add or
modify the resource policy directly on the page so that it looks similar to the [example](#example-resource-policy-secrets-manager "#example-resource-policy-secrets-manager"). You can also attach
the resource policy through the AWS CLI's `put-resource-policy` command, or
programmatically using the [PutResourcePolicy](../../../secretsmanager/latest/apireference/API_PutResourcePolicy.md "../../../secretsmanager/latest/apireference/API_PutResourcePolicy.md") API operation.

## Attaching a resource-based policy to

your KMS key

To attach a resource-based policy to your KMS key, go to the AWS Key Management Service console within
the AWS Management Console, navigate to your KMS key and edit your key policy to look like the [example](#example-resource-policy-kms-keys "#example-resource-policy-kms-keys"). You can also update the key
through the AWS CLI's `put-key-policy` command, or programmatically using the
[PutKeyPolicy](../../../kms/latest/APIReference/API_PutKeyPolicy.md "../../../kms/latest/APIReference/API_PutKeyPolicy.md") API operation.

## Rotating API keys

We recommend rotating API keys at least every 90 days to minimize the risk of
compromise, and to maintain a well-practiced key rotation process for emergency
situations.

To rotate an API key, you must rotate the secret in which it is contained. See [Rotate Secrets Manager secrets](../../../secretsmanager/latest/userguide/rotating-secrets.md "../../../secretsmanager/latest/userguide/rotating-secrets.md") in the _Secrets Manager User Guide_ for more
information on how to rotate secrets. When you rotate an API key, it is recommended that
you wait for the previous key's usage to drop to zero before revoking the old API key to
ensure that ongoing requests are not impacted.
