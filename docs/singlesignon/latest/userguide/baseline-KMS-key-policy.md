

# Baseline KMS key policy
<a name="baseline-KMS-key-policy"></a>

The following KMS key policy covers the most common deployment scenario: an IAM Identity Center instance with delegated administrators and AWS managed applications, including AWS Control Tower, SSO to Amazon EC2 instances, and custom workflows. Use this policy as your starting point when creating a customer managed KMS key for IAM Identity Center. If you need more granular access controls, such as restricting the key to a specific IAM Identity Center instance or application, see [Advanced KMS key policy statements](advanced-kms-policy.md). Please note if using a multi-Region key, the same policy should be used across all replicas to help ensure consistent authorization.

To use this policy, replace the following placeholder values with your own:
+ `{{111122223333}}` — The AWS account ID of your IAM Identity Center instance (the AWS Organizations management account).
+ `{{444455556666}}` — The AWS account ID of your delegated administration account. If you don't use delegated administration, remove this principal.

 Since AWS IAM Identity Center requires that the KMS key be in the same AWS Account as the service, the following statements use the `${aws:ResourceOrgID}` and `${aws:ResourceAccount}` variables instead of literal values. You can replace these variables with your AWS Organization ID and AWS Account ID if you prefer to do so.

```
{
  "Version": "2012-10-17", 		 	 	 
  "Statement": [
    {
      "Sid": "AllowIdentityCenterAdminAccounts",
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "arn:aws:iam::{{111122223333}}:root",
          "arn:aws:iam::{{444455556666}}:root"
        ]
      },
      "Action": "kms:*",
      "Resource": "*"
    },
    {
      "Sid": "AllowIdentityCenterAndIdentityStoreToDescribeKey",
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "identitystore.amazonaws.com",
          "sso.amazonaws.com"
        ]
      },
      "Action": "kms:DescribeKey",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "${aws:ResourceAccount}"
        }
      }
    },
    {
      "Sid": "AllowIdentityCenterAndIdentityStoreToUseKey",
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "identitystore.amazonaws.com",
          "sso.amazonaws.com"
        ]
      },
      "Action": [
        "kms:Decrypt",
        "kms:ReEncryptTo",
        "kms:ReEncryptFrom",
        "kms:GenerateDataKeyWithoutPlaintext"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "${aws:ResourceAccount}"
        },
        "ForAnyValue:StringEquals": {
          "kms:EncryptionContextKeys": [
            "aws:sso:instance-arn",
            "aws:identitystore:identitystore-arn"
          ]
        }
      }
    },
    {
      "Sid": "AllowOrgPrincipalsViaIdentityCenterAndIdentityStore",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:PrincipalOrgID": "${aws:ResourceOrgID}"
        },
        "StringLike": {
          "kms:ViaService": [
            "sso.*.amazonaws.com",
            "identitystore.*.amazonaws.com"
          ]
        },
        "ForAnyValue:StringEquals": {
          "kms:EncryptionContextKeys": [
            "aws:sso:instance-arn",
            "aws:identitystore:identitystore-arn"
          ]
        }
      }
    },
    {
      "Sid": "AllowManagedApps",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "Bool": {
          "aws:PrincipalIsAWSService": "true"
        },
        "StringEquals": {
          "aws:SourceOrgID": "${aws:ResourceOrgID}"
        },
        "StringLike": {
          "kms:ViaService": [
            "identitystore.*.amazonaws.com",
            "sso.*.amazonaws.com"
          ]
        },
        "ForAnyValue:StringEquals": {
          "kms:EncryptionContextKeys": [
            "aws:sso:instance-arn",
            "aws:identitystore:identitystore-arn"
          ]
        }
      }
    }
  ]
}
```

This policy contains five statements. The following table describes what each statement does.


| Statement | Purpose | 
| --- | --- | 
| AllowIdentityCenterAdminAccounts | Grants full KMS key permissions to the IAM Identity Center management account and the delegated administration account. This includes key management actions such as modifying the key policy and scheduling key deletion. Administrators in these accounts can manage and use the key if they have the required permissions in their identity-based policies. | 
| AllowIdentityCenterAndIdentityStoreToDescribeKey | Allows the IAM Identity Center and Identity Store service principals to retrieve key metadata. This is required for service operations that validate the key without performing encryption or decryption. The aws:SourceAccount condition helps ensure only your IAM Identity Center instance can use your KMS key. | 
| AllowIdentityCenterAndIdentityStoreToUseKey | Allows the IAM Identity Center and Identity Store service principals to use the key for encryption operations such as encrypting, decrypting, and re-encrypting data. The aws:SourceAccount condition helps ensure only your IAM Identity Center instance can use your KMS key. | 
| AllowOrgPrincipalsViaIdentityCenterAndIdentityStore | Allows IAM principals in your AWS Organization to decrypt data through the IAM Identity Center and Identity Store services. This covers application administrators who interact with IAM Identity Center-integrated AWS services using Forward Access Sessions (FAS). | 
| AllowManagedApps | Allows AWS managed applications to decrypt data protected by your KMS key through IAM Identity Center and Identity Store. | 

Use the following IAM policy statement in [Step 4: Configure IAM policies for cross-account use of the KMS key](identity-center-customer-managed-keys.md#configure-iam-policies-kms-key) to allow delegated administrators to use the KMS key through IAM Identity Center service APIs. Replace the example key ARN with your actual KMS key ARN. The wildcard region in the example accommodates all replicas of a multi-Region KMS key.

For cross-account use cases other than IAM Identity Center administration, such as SSO to Amazon EC2 instances or administration of AWS managed applications, scope `AllowCrossAccountKMSKeyUse` down to `kms:Decrypt` only and remove the `AllowListKMSKeyAliases` statement.

```
{
  "Version": "2012-10-17", 		 	 	 
  "Statement": [
    {
      "Sid": "AllowCrossAccountKMSKeyUse",
      "Effect": "Allow",
      "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:DescribeKey"
      ],
      "Resource": [
        "arn:aws:kms:{{*}}:{{111122223333}}:key/{{mrk-1234abcd-12ab-34cd-56ef-1234567890ab}}"
      ]
    },
    {
      "Sid": "AllowListKMSKeyAliases",
      "Effect": "Allow",
      "Action": "kms:ListAliases",
      "Resource": "*"
    }
  ]
}
```