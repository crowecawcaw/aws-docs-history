

# Access AWS Secrets Manager secrets from a different account
<a name="auth-and-access_examples_cross"></a>

To allow users in one account to access secrets in another account (*cross-account access*), you must allow access both in a resource policy and in an identity policy. This is different than granting access to identities in the same account as the secret.

Cross-account permission is effective only for the following operations:
+ [CancelRotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CancelRotateSecret.html)
+ [DeleteResourcePolicy](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_DeleteResourcePolicy.html)
+ [DeleteSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_DeleteSecret.html)
+ [DescribeSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_DescribeSecret.html)
+ [GetRandomPassword](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetRandomPassword.html)
+ [GetResourcePolicy](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetResourcePolicy.html)
+ [GetSecretValue](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html)
+ [ListSecretVersionIds](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ListSecretVersionIds.html)
+ [PutResourcePolicy](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_PutResourcePolicy.html)
+ [PutSecretValue](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_PutSecretValue.html)
+ [RemoveRegionsFromReplication](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RemoveRegionsFromReplication.html)
+ [ReplicateSecretToRegions](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ReplicateSecretToRegions.html)
+ [RestoreSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RestoreSecret.html)
+ [RotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html)
+ [StopReplicationToReplica](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_StopReplicationToReplica.html)
+ [TagResource](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_TagResource.html)
+ [UntagResource](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_UntagResource.html)
+ [UpdateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_UpdateSecret.html)
+ [UpdateSecretVersionStage](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_UpdateSecretVersionStage.html)
+ [ValidateResourcePolicy](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ValidateResourcePolicy.html)

You can use the `BlockPublicPolicy` parameter with the [PutResourcePolicy](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_PutResourcePolicy.html) action to help protect your resources by preventing public access from being granted through the resource policies that are directly attached to your secrets. You can also use [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-preview-access) to verify cross-account access.

You must also allow the identity to use the KMS key that the secret is encrypted with. This is because you can't use the AWS managed key (`aws/secretsmanager`) for cross-account access. Instead, you must encrypt your secret with a KMS key that you create, and then attach a key policy to it. There is a charge for creating KMS keys. To change the encryption key for a secret, see [Modify an AWS Secrets Manager secret](manage_update-secret.md).

**Important**  
Resource-based policies granting `secretsmanager:PutResourcePolicy` permission gives principals, even those in other accounts, the ability to modify your resource-based policies. This permission lets principals escalate existing permissions like obtaining full administrative access to secrets. We recommend you apply the principle of [least privileged access](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) to your policies. For more information, see [Resource-based policies](auth-and-access_resource-policies.md).

The following example policies assume you have a secret and encryption key in *Account1*, and an identity in *Account2* that you want to allow to access the secret value.

**Step 1: Attach a resource policy to the secret in *Account1***
+ The following policy allows {{ApplicationRole}} in {{Account2}} to access the secret in {{Account1}}. To use this policy, see [Resource-based policies](auth-and-access_resource-policies.md).

------
#### [ JSON ]

****  

  ```
  {
      "Version":"2012-10-17",		 	 	 
      "Statement": [
          {
              "Effect": "Allow",
              "Principal": {
                  "AWS": "arn:aws:iam::{{111122223333}}:role/{{ApplicationRole}}"
              },
              "Action": "secretsmanager:GetSecretValue",
              "Resource": "*"
          }
      ]
  }
  ```

------

**Step 2: Add a statement to the key policy for the KMS key in *Account1***
+ The following key policy statement allows {{ApplicationRole}} in {{Account2}} to use the KMS key in {{Account1}} to decrypt the secret in {{Account1}}. To use this statement, add it to the key policy for your KMS key. For more information, see [Changing a key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying.html).

  ```
  {
    "Effect": "Allow",
    "Principal": {
      "AWS": "arn:aws:iam::{{Account2}}:role/{{ApplicationRole}}"
    },
    "Action": [
      "kms:Decrypt",
      "kms:DescribeKey"
    ],
    "Resource": "*"
  }
  ```

**Step 3: Attach an identity policy to the identity in *Account2***
+ The following policy allows {{ApplicationRole}} in {{Account2}} to access the secret in {{Account1}} and decrypt the secret value by using the encryption key which is also in {{Account1}}. To use this policy, see [Identity-based policies](auth-and-access_iam-policies.md). You can find the ARN for your secret in the Secrets Manager console on the secret details page under **Secret ARN**. Alternatively, you can call [`describe-secret`](https://docs.aws.amazon.com/cli/latest/reference/secretsmanager/describe-secret.html).

------
#### [ JSON ]

****  

  ```
  {
      "Version":"2012-10-17",		 	 	 
      "Statement": [
          {
              "Effect": "Allow",
              "Action": "secretsmanager:GetSecretValue",
              "Resource": "arn:aws:secretsmanager:{{us-east-1}}:{{123456789012}}:secret:{{secretName-AbCdEf}}"
          },
          {
              "Effect": "Allow",
              "Action": "kms:Decrypt",
              "Resource": "arn:aws:kms:{{us-east-1}}:{{123456789012}}:key/{{EncryptionKey}}"
          }
      ]
  }
  ```

------