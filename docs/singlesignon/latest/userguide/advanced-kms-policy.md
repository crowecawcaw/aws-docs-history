# Advanced KMS key policy statements

Use advanced KMS key policy statements to implement more granular access controls for your customer managed KMS key. These policies build on the [Baseline KMS key and IAM policy statements](baseline-KMS-key-policy.md "baseline-KMS-key-policy.md") by adding encryption context conditions and service-specific restrictions. Before deciding whether to use advanced KMS key policy statements, make sure to review the pertinent considerations.

## Using encryption context to restrict access

You can restrict KMS key usage to a specific IAM Identity Center instance by specifying an encryption context condition in your key policy statements. The baseline key policy statements already include this context with a generic value. Replace the "\*" wildcard with a specific Identity Center instance ARN and Identity Store ARN to ensure the key works only with your intended instance. You can also add the same encryption context conditions to the IAM policy configured for cross-account use of the KMS key.

Identity Center

```

"StringEquals": {
    "kms:EncryptionContext:aws:sso:instance-arn": "arn:aws:sso:::instance/ssoins-1234567890abcdef"
}

```

Identity Store

```

"StringEquals": {
    "kms:EncryptionContext:aws:identitystore:identitystore-arn": "arn:aws:identitystore::111122223333:identitystore/d-1234567890"
}

```

If you need help finding these identifiers, see [Find the required identifiers](identity-center-customer-managed-keys.md#insert-the-required-identifiers "identity-center-customer-managed-keys.md#insert-the-required-identifiers").

###### Note

You can use a customer managed KMS key only with an organization instance of IAM Identity Center. The customer managed key must be located in the AWS organization's management account, which helps ensure the key is used with a single IAM Identity Center instance. However, the encryption context mechanism provides an independent technical safeguard of single-instance usage. You can also use the `aws:SourceArn` condition key in the KMS key policy statements intended for the Identity Center and Identity Store service principals.

### Considerations for implementing encryption context conditions

Before implementing encryption context conditions, review these requirements:

- **DescribeKey action.** The encryption context cannot be applied to the "kms:DescribeKey" action, which can be used by IAM Identity Center administrators. When configuring your KMS key policy, exclude the encryption context for this specific action to ensure proper operations of your IAM Identity Center instance.
- **New instance setup.** If you're enabling a new IAM Identity Center instance with a customer managed KMS key, see [Considerations for customer managed KMS keys and advanced KMS key policies](considerations-for-customer-managed-kms-keys-advanced.md "considerations-for-customer-managed-kms-keys-advanced.md").
- **Identity source changes.** When changing your identity source to or from Active Directory, the encryption context requires special attention. See [Considerations for changing
  your identity source](manage-your-identity-source-considerations.md "manage-your-identity-source-considerations.md").

## Policy templates

Choose from these advanced policy templates based on your security requirements. Balance granular access controls with the administrative overhead they introduce.

Topics covered here:

- [KMS policy statements for read-only use of a specific IAM Identity Center instance](#kms-policy-statements-for-read-only-use-of-a-specific-iam-identity-center-instance "#kms-policy-statements-for-read-only-use-of-a-specific-iam-identity-center-instance"). This section demonstrates the use of the encryption context for read-only access to IAM Identity Center.
- [Refined KMS key policy statements for use of AWS managed applications](#refined-kms-key-policy-statements-for-use-of-aws-managed-applications "#refined-kms-key-policy-statements-for-use-of-aws-managed-applications"). This section demonstrates how to refine the KMS key policies for AWS managed applications using the encryption context and application information, such as the application service principal, application ARN and AWS account ID.

## KMS policy statements for read-only use of a specific IAM Identity Center instance

This policy allows [security auditors](../../../aws-managed-policy/latest/reference/SecurityAudit.md "../../../aws-managed-policy/latest/reference/SecurityAudit.md") and other personnel who need only read access to IAM Identity Center to use the KMS key.

To use this policy:

1. Replace the example read-only administrator IAM principals with your actual administrator IAM principals
2. Replace the example IAM Identity Center instance ARN with your actual instance ARN
3. Replace the example Identity Store ARN with your actual Identity Store ARN
4. If using [delegated administration](delegated-admin.md "delegated-admin.md"), see [Step 4: Configure IAM policies for cross-account use of the KMS key](identity-center-customer-managed-keys.md#configure-iam-policies-kms-key "identity-center-customer-managed-keys.md#configure-iam-policies-kms-key")

If you need help finding the values of these identifiers, see [Find the required identifiers](identity-center-customer-managed-keys.md#insert-the-required-identifiers "identity-center-customer-managed-keys.md#insert-the-required-identifiers").

Once you have updated the template with your values, return to [Step 2: Prepare KMS key policy statements](identity-center-customer-managed-keys.md#choose-kms-key-policy-statements "identity-center-customer-managed-keys.md#choose-kms-key-policy-statements") to prepare additional KMS key policy statements, as needed.

The kms:Decrypt action alone does not restrict access to read-only operations. The IAM policy must enforce read-only access on IAM Identity Center service APIs.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowReadOnlyAccessToIdentityCenterAPI",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/MyAdminRole"
      },
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "kms:EncryptionContext:aws:sso:instance-arn": "arn:aws:sso:::instance/ssoins-1234567890abcdef",
          "kms:ViaService": "sso.*.amazonaws.com"
        }
      }
    },
    {
      "Sid": "AllowReadOnlyAccessToIdentityStoreAPI",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/MyAdminRole"
      },
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "kms:ViaService": "identitystore.*.amazonaws.com",
          "kms:EncryptionContext:aws:identitystore:identitystore-arn": "arn:aws:identitystore::111122223333:identitystore/d-1234567890"
        }
      }
    }
  ]
}
```

## Refined KMS key policy statements for use of AWS managed applications

These policy templates provide more granular control over which AWS managed applications can use your KMS key.

###### Note

Some AWS managed applications cannot be used with IAM Identity Center configured with a customer managed KMS key. See [AWS managed applications that you can use with IAM Identity Center](awsapps-that-work-with-identity-center.md "awsapps-that-work-with-identity-center.md").

The [Baseline KMS key and IAM policy statements for use of AWS managed applications](baseline-KMS-key-policy.md#baseline-kms-key-policy-statements-for-use-of-aws-managed-applications "baseline-KMS-key-policy.md#baseline-kms-key-policy-statements-for-use-of-aws-managed-applications") allow any AWS managed application from any account in the same AWS organization to use the KMS key. Use these refined policies to restrict access by:

- Application service principal
- Application instance ARNs
- AWS account IDs
- Encryption context for specific IAM Identity Center instances

###### Note

A service principal is a unique identifier for an AWS service, typically formatted as servicename.amazonaws.com (for example, elasticmapreduce.amazonaws.com for Amazon EMR).

### Restrict by account

This KMS key policy statement template allows an AWS managed application in specific AWS accounts to use the KMS key using a specific IAM Identity Center instance.

To use this policy:

1. Replace the example service principal with your actual application service principal
2. Replace the example account IDs with the actual account IDs where your AWS managed applications are deployed
3. Replace the example Identity Store ARN with your actual Identity Store ARN
4. Replace the example IAM Identity Center instance ARN with your actual instance ARN

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowServiceInSpecificAccountsToUseTheKMSKeyViaIdentityCenter",
      "Effect": "Allow",
      "Principal": {
        "Service": "myapp.amazonaws.com"
      },
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": [
            "111122223333",
            "444455556666"
          ]
        },
        "StringLike": {
          "kms:ViaService": "sso.*.amazonaws.com",
          "kms:EncryptionContext:aws:sso:instance-arn": "arn:aws:sso:::instance/ssoins-1234567890abcdef"
        },
        "Bool": {
          "aws:PrincipalIsAWSService": "true"
        }
      }
    },
    {
      "Sid": "AllowServiceInSpecificAccountsToUseTheKMSKeyViaIdentityStore",
      "Effect": "Allow",
      "Principal": {
        "Service": "myapp.amazonaws.com"
      },
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": [
            "111122223333",
            "444455556666"
          ]
        },
        "StringLike": {
          "kms:ViaService": "identitystore.*.amazonaws.com",
          "kms:EncryptionContext:aws:identitystore:identitystore-arn": "arn:aws:identitystore::111122223333:identitystore/d-1234567890"
        },
        "Bool": {
          "aws:PrincipalIsAWSService": "true"
        }
      }
    }
  ]
}
```

### Restrict by application instance

This KMS key policy statement template allows a specific AWS managed application instance to use the KMS key using a specific IAM Identity Center instance.

To use this policy:

1. Replace the example service principal with your actual application service principal
2. Replace the example application ARN with your actual application instance ARN
3. Replace the example Identity Store ARN with your actual Identity Store ARN
4. Replace the example IAM Identity Center instance ARN with your actual instance ARN

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowSpecificAppInstanceToUseTheKMSKeyViaIdentityCenter",
      "Effect": "Allow",
      "Principal": {
        "Service": "myapp.amazonaws.com"
      },
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:SourceARN": "arn:aws:myapp:us-east-1:111122223333:application/my-application"
        },
        "StringLike": {
          "kms:ViaService": "sso.*.amazonaws.com",
          "kms:EncryptionContext:aws:sso:instance-arn": "arn:aws:sso:::instance/ssoins-1234567890abcdef"
        },
        "Bool": {
          "aws:PrincipalIsAWSService": "true"
        }
      }
    },
    {
      "Sid": "AllowSpecificAppInstanceToUseTheKMSKeyViaIdentityStore",
      "Effect": "Allow",
      "Principal": {
        "Service": "myapp.amazonaws.com"
      },
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:SourceARN": "arn:aws:myapp:us-east-1:111122223333:application/my-application"
        },
        "StringLike": {
          "kms:ViaService": "identitystore.*.amazonaws.com",
          "kms:EncryptionContext:aws:identitystore:identitystore-arn": "arn:aws:identitystore::111122223333:identitystore/d-1234567890"
        },
        "Bool": {
          "aws:PrincipalIsAWSService": "true"
        }
      }
    }
  ]
}
```
