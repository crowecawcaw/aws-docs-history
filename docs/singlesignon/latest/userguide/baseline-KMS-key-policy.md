# Baseline KMS key and IAM policy statements

The baseline KMS key and identity-based policies provided here serve as a foundation for
common requirements. We also recommend that you review [Advanced KMS key policy statements](advanced-kms-policy.md "advanced-kms-policy.md") that provide more granular access controls, such as
ensuring the KMS key is accessible only to a specific IAM Identity Center instance or AWS
managed application. Before using advanced KMS key policy statements, review the [Considerations for
choosing baseline vs. advanced KMS key policy statements](considerations-for-customer-managed-kms-keys-advanced.md#kms-policy-considerations-advanced-vs-baseline "considerations-for-customer-managed-kms-keys-advanced.md#kms-policy-considerations-advanced-vs-baseline").

The following sections provide baseline policy statements for each use case. Expand the
sections that match your use cases, and copy the KMS key policy statements. Then, return to [Step 2: Prepare KMS key policy
statements](identity-center-customer-managed-keys.md#choose-kms-key-policy-statements "identity-center-customer-managed-keys.md#choose-kms-key-policy-statements").

Use the following KMS key policy statement template in [Step 2: Prepare KMS key policy
statements](identity-center-customer-managed-keys.md#choose-kms-key-policy-statements "identity-center-customer-managed-keys.md#choose-kms-key-policy-statements") to allow IAM Identity Center, its associated
Identity Store, and IAM Identity Center administrators to use the KMS key.

- In the Principal element for administrator policy statements, specify the AWS
  account principals of the IAM Identity Center's
  administration accounts, which are the AWS organization management account and the
  delegated administration account, using
  the format "arn:aws:iam::111122223333:root".
- In the PrincipalArn element, replace the example ARNs with the IAM Identity Center
  administrators' IAM roles.

You can specify either:

    + Specific IAM role ARN:



    `"arn:aws:iam::111122223333:role/aws-reserved/sso.amazonaws.com/ap-southeast-2/AWSReservedSSO_permsetname_12345678"`
    + Wildcard pattern (recommended):



    `"arn:aws:iam::111122223333:role/aws-reserved/sso.amazonaws.com/ap-southeast-2/AWSReservedSSO_permsetname_*"`

Using the wildcard (`*`) prevents access loss if the permission set
is deleted and recreated, as Identity Center generates new unique identifiers for
recreated permission sets. For an example implementation, see [Custom trust policy example](referencingpermissionsets.md#custom-trust-policy-example "referencingpermissionsets.md#custom-trust-policy-example")
.

- In the SourceAccount element, specify the IAM Identity Center account ID.
- Identity Store has its own service principal, `identitystore.amazonaws.com`,
  which must be allowed to use the KMS key.
- These policy statements allow your IAM Identity Center instances in a specific AWS account
  to use the KMS key. To restrict access to a specific IAM Identity Center instance,
  see [Advanced KMS key policy statements](advanced-kms-policy.md "advanced-kms-policy.md"). You
  can have only one IAM Identity Center instance for each AWS account.
  KMS key policy statements

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowIAMIdentityCenterAdminToUseTheKMSKeyViaIdentityCenter",
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "arn:aws:iam::111122223333:root",
          "arn:aws:iam::444455556666:root"
        ]
      },
      "Action": [
        "kms:Decrypt",
        "kms:Encrypt",
        "kms:GenerateDataKeyWithoutPlaintext"
      ],
      "Resource": "*",
      "Condition": {
        "ArnLike": {
          "aws:PrincipalArn": [
            "arn:aws:iam::111122223333:role/aws-reserved/sso.amazonaws.com/us-east-1/AWSReservedSSO_Admin_*",
            "arn:aws:iam::444455556666:role/aws-reserved/sso.amazonaws.com/us-east-1/AWSReservedSSO_DelegatedAdmin_*"
          ]
        },
        "StringLike": {
          "kms:EncryptionContext:aws:sso:instance-arn": "*",
          "kms:ViaService": "sso.*.amazonaws.com"
        }
      }
    },
    {
      "Sid": "AllowIAMIdentityCenterAdminToUseTheKMSKeyViaIdentityStore",
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "arn:aws:iam::111122223333:root",
          "arn:aws:iam::444455556666:root"
        ]
      },
      "Action": [
        "kms:Decrypt",
        "kms:Encrypt",
        "kms:GenerateDataKeyWithoutPlaintext"
      ],
      "Resource": "*",
      "Condition": {
        "ArnLike": {
          "aws:PrincipalArn": [
            "arn:aws:iam::111122223333:role/aws-reserved/sso.amazonaws.com/us-east-1/AWSReservedSSO_Admin_*",
            "arn:aws:iam::444455556666:role/aws-reserved/sso.amazonaws.com/us-east-1/AWSReservedSSO_DelegatedAdmin_*"
          ]
        },
        "StringLike": {
          "kms:EncryptionContext:aws:identitystore:identitystore-arn": "*",
          "kms:ViaService": "identitystore.*.amazonaws.com"
        }
      }
    },
    {
      "Sid": "AllowIAMIdentityCenterAdminToDescribeTheKMSKey",
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "arn:aws:iam::111122223333:root",
          "arn:aws:iam::444455556666:root"
        ]
      },
      "Action": "kms:DescribeKey",
      "Resource": "*",
      "Condition": {
        "ArnLike": {
          "aws:PrincipalArn": [
            "arn:aws:iam::111122223333:role/aws-reserved/sso.amazonaws.com/us-east-1/AWSReservedSSO_Admin_*",
            "arn:aws:iam::444455556666:role/aws-reserved/sso.amazonaws.com/us-east-1/AWSReservedSSO_DelegatedAdmin_*"
          ]
        }
      }
    },
    {
      "Sid": "AllowIAMIdentityCenterToUseTheKMSKey",
      "Effect": "Allow",
      "Principal": {
        "Service": "sso.amazonaws.com"
      },
      "Action": [
        "kms:Decrypt",
        "kms:ReEncryptTo",
        "kms:ReEncryptFrom",
        "kms:GenerateDataKeyWithoutPlaintext"
      ],
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "kms:EncryptionContext:aws:sso:instance-arn": "*"
        },
        "StringEquals": {
          "aws:SourceAccount": "111122223333"
        }
      }
    },
    {
      "Sid": "AllowIdentityStoreToUseTheKMSKey",
      "Effect": "Allow",
      "Principal": {
        "Service": "identitystore.amazonaws.com"
      },
      "Action": [
        "kms:Decrypt",
        "kms:ReEncryptTo",
        "kms:ReEncryptFrom",
        "kms:GenerateDataKeyWithoutPlaintext"
      ],
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "kms:EncryptionContext:aws:identitystore:identitystore-arn": "*"
        },
        "StringEquals": {
          "aws:SourceAccount": "111122223333"
        }
      }
    },
    {
      "Sid": "AllowIAMIdentityCenterAndIdentityStoreToDescribeKMSKey",
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "identitystore.amazonaws.com",
          "sso.amazonaws.com"
        ]
      },
      "Action": "kms:DescribeKey",
      "Resource": "*"
    }
  ]
}
```

Use the following IAM policy statement template in [Step 4: Configure IAM policies for
cross-account use of the KMS key](identity-center-customer-managed-keys.md#configure-iam-policies-kms-key "identity-center-customer-managed-keys.md#configure-iam-policies-kms-key") to allow IAM Identity Center
administrators to use the KMS key.

- Replace the example key ARN in the `Resource` element with your
  actual KMS key ARN. For help finding the values of the referenced identifiers, see [Where to find the required identifiers](identity-center-customer-managed-keys.md#find-the-required-identifiers "identity-center-customer-managed-keys.md#find-the-required-identifiers").
- These IAM policy statements grant KMS key access to the IAM principal but don't
  restrict which AWS service can make the request. The KMS key policy typically
  provides these service restrictions. However, you can add encryption context to this
  IAM policy to limit usage to a specific Identity Center instance. For details, refer
  to [Advanced KMS key policy statements](advanced-kms-policy.md "advanced-kms-policy.md").
  IAM Policy statements required for delegated administrators of IAM Identity Center

```
{
  "Version": "2012-10-17",
  "Statement": [{
      "Sid": "IAMPolicyToAllowIAMIdentityCenterAdminToUseKMSkey",
      "Effect": "Allow",
      "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:DescribeKey"
      ],
      "Resource": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
    },
    {
      "Sid": "IAMPolicyToAllowIAMIdentityCenterAdminToListKeyAliases",
      "Effect": "Allow",
      "Action": "kms:ListAliases",
      "Resource": "*"
    }
  ]
}
```

###### Note

Some AWS managed applications cannot be used with IAM Identity Center configured
with a customer managed KMS key. For more information, see [AWS
managed applications that work with IAM Identity Center](awsapps-that-work-with-identity-center.md "awsapps-that-work-with-identity-center.md").

Use the following KMS key policy statement template in [Step 2: Prepare KMS key policy
statements](identity-center-customer-managed-keys.md#choose-kms-key-policy-statements "identity-center-customer-managed-keys.md#choose-kms-key-policy-statements") to allow both AWS managed
applications and their administrators to use the KMS key.

- Insert your AWS Organizations ID in the PrincipalOrgID and SourceOrgId conditions. For
  help finding the values of the referenced identifiers, see [Where to find the required identifiers](identity-center-customer-managed-keys.md#find-the-required-identifiers "identity-center-customer-managed-keys.md#find-the-required-identifiers").
- These policy statements allow any of your AWS managed applications and any IAM
  principals (application administrators) in the AWS organization to use kms:Decrypt
  using IAM Identity Center and Identity Store. To restrict these policy statements to specific
  AWS managed applications, accounts, or IAM Identity Center instances, see [Advanced KMS key policy statements](advanced-kms-policy.md "advanced-kms-policy.md").

You can restrict access to specific application administrators by replacing `*` with specific IAM principals. To protect against IAM role name changes when
permission sets are recreated, use the approach in the [Custom trust policy example](referencingpermissionsets.md#custom-trust-policy-example "referencingpermissionsets.md#custom-trust-policy-example").
For more information, see [Considerations for
choosing baseline vs. advanced KMS key policy statements](considerations-for-customer-managed-kms-keys-advanced.md#kms-policy-considerations-advanced-vs-baseline "considerations-for-customer-managed-kms-keys-advanced.md#kms-policy-considerations-advanced-vs-baseline").
KMS key policy statements

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowAppAdminsInTheSameOrganizationToUseTheKMSKeyViaIdentityCenter",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:PrincipalOrgID": "o-a1b2c3d4e5"
        },
        "StringLike": {
          "kms:ViaService": "sso.*.amazonaws.com",
          "kms:EncryptionContext:aws:sso:instance-arn": "*"
        }
      }
    },
    {
      "Sid": "AllowAppAdminsInTheSameOrganizationToUseTheKMSKeyViaIdentityStore",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:PrincipalOrgID": "o-a1b2c3d4e5"
        },
        "StringLike": {
          "kms:ViaService": "identitystore.*.amazonaws.com",
          "kms:EncryptionContext:aws:identitystore:identitystore-arn": "*"
        }
      }
    },
    {
      "Sid": "AllowManagedAppsToUseTheKMSKeyViaIdentityCenter",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "kms:ViaService": "sso.*.amazonaws.com",
          "kms:EncryptionContext:aws:sso:instance-arn": "*"
        },
        "Bool": {
          "aws:PrincipalIsAWSService": "true"
        },
        "StringEquals": {
          "aws:SourceOrgID": "o-a1b2c3d4e5"
        }
      }
    },
    {
      "Sid": "AllowManagedAppsToUseTheKMSKeyViaIdentityStore",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "kms:ViaService": "identitystore.*.amazonaws.com",
          "kms:EncryptionContext:aws:identitystore:identitystore-arn": "*"
        },
        "Bool": {
          "aws:PrincipalIsAWSService": "true"
        },
        "StringEquals": {
          "aws:SourceOrgID": "o-a1b2c3d4e5"
        }
      }
    }
  ]
}
```

Use the following IAM policy statement template in [Step 4: Configure IAM policies for
cross-account use of the KMS key](identity-center-customer-managed-keys.md#configure-iam-policies-kms-key "identity-center-customer-managed-keys.md#configure-iam-policies-kms-key") to allow administrators of AWS
managed applications to use the KMS key from a member account.

- Replace the example ARN in the Resource element with your actual KMS key ARN.
  For help finding the values of the referenced identifiers, see [Where to find the required identifiers](identity-center-customer-managed-keys.md#find-the-required-identifiers "identity-center-customer-managed-keys.md#find-the-required-identifiers").
- Some AWS managed applications require you to configure permissions for IAM
  Identity Center service APIs. Before you configure a customer managed key in IAM
  Identity Center, verify that these permissions also allow use of the KMS key. For
  specific KMS key permission requirements, see the documentation for each AWS
  managed application you have deployed.
  IAM policy statements required for administrators of AWS managed applications:

```
{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "AllowIAMIdentityCenterAdminToUseTheKMSKeyViaIdentityCenterAndIdentityStore",
    "Effect": "Allow",
    "Action": "kms:Decrypt",
    "Resource": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
    "Condition": {
      "StringLike": {
        "kms:ViaService": [
          "sso.*.amazonaws.com",
          "identitystore.*.amazonaws.com"
        ]
      }
    }
  }]
}
```

Use the following KMS key statement templates in [Step 2: Prepare KMS key policy
statements](identity-center-customer-managed-keys.md#choose-kms-key-policy-statements "identity-center-customer-managed-keys.md#choose-kms-key-policy-statements") to allow AWS Control Tower
administrators to use the KMS key.

- In the Principal element, specify the IAM principals used for access to the
  IAM Identity Center service APIs. For more information about IAM principals, see [Specifying
  a principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md") in the _IAM User Guide_.
- These policy statements allow AWS Control Tower administrators to use the KMS
  key through any of your IAM Identity Center instances. However, AWS Control Tower
  restricts access to the organization instance of IAM Identity Center in the same
  AWS organization. Because of this restriction, there is no practical benefit to
  further restricting the KMS key to a specific IAM Identity Center instance as
  described in [Advanced KMS key policy statements](advanced-kms-policy.md "advanced-kms-policy.md")
  .
- To help protect against IAM role name changes when permission sets are
  recreated, use the approach described in the [Custom trust policy example](referencingpermissionsets.md#custom-trust-policy-example "referencingpermissionsets.md#custom-trust-policy-example")
  .
  KMS key policy statement:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowControlTowerAdminRoleToUseTheKMSKeyViaIdentityCenter",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/AWSControlTowerExecution"
      },
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "kms:EncryptionContext:aws:sso:instance-arn": "*",
          "kms:ViaService": "sso.*.amazonaws.com"
        }
      }
    },
    {
      "Sid": "AllowControlTowerAdminRoleToUseTheKMSKeyViaIdentityStore",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/AWSControlTowerExecution"
      },
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "kms:ViaService": "identitystore.*.amazonaws.com",
          "kms:EncryptionContext:aws:identitystore:identitystore-arn": "*"
        }
      }
    }
  ]
}
```

AWS Control Tower does not support delegated administration and, therefore, you don't need to
configure an IAM policy for its administrators.

Use the following KMS key policy statement template in [Step 2: Prepare KMS key policy
statements](identity-center-customer-managed-keys.md#choose-kms-key-policy-statements "identity-center-customer-managed-keys.md#choose-kms-key-policy-statements") to allow users of single sign-on
(SSO) to Amazon EC2 instances to use the KMS key across accounts.

- Specify the IAM principals used for access to IAM Identity Center in the
  Principal field. For more information about IAM principals, see [Specifying
  a principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md") in the _IAM User Guide_.
- This policy statement allows any of your IAM Identity Center instances to use
  the KMS key. To restrict access to a specific IAM Identity Center instance, see [Advanced KMS key policy statements](advanced-kms-policy.md "advanced-kms-policy.md").
- To help protect against IAM role name changes when permission sets are
  recreated, use the approach described in Custom
  trust policy example.
  KMS key policy statement

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowIAMIdentityCenterPermissionSetRoleToUseTheKMSKeyViaIdentityCenter",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/aws-reserved/sso.amazonaws.com/us-east-1/AWSReservedSSO_MyPermissionSet_1a2b3c4d5e6f7g8h"
      },
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "kms:EncryptionContext:aws:sso:instance-arn": "*",
          "kms:ViaService": "sso.*.amazonaws.com"
        }
      }
    },
    {
      "Sid": "AllowIAMIdentityCenterPermissionSetRoleToUseTheKMSKeyViaIdentityStore",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/aws-reserved/sso.amazonaws.com/us-east-1/AWSReservedSSO_MyPermissionSet_1a2b3c4d5e6f7g8h"
      },
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "kms:ViaService": "identitystore.*.amazonaws.com",
          "kms:EncryptionContext:aws:identitystore:identitystore-arn": "*"
        }
      }
    }
  ]
}
```

Use the following IAM policy statement template in [Step 4: Configure IAM policies for
cross-account use of the KMS key](identity-center-customer-managed-keys.md#configure-iam-policies-kms-key "identity-center-customer-managed-keys.md#configure-iam-policies-kms-key") to allow SSO to EC2 instances to use
the KMS key.

Attach the IAM policy statement to the existing permission set in IAM Identity
Center that you are using to allow SSO access to Amazon EC2 instances. For IAM policy
examples, see [Remote
Desktop Protocol connections](../../../systems-manager/latest/userguide/fleet-manager-remote-desktop-connections.md#rdp-iam-policy-examples "../../../systems-manager/latest/userguide/fleet-manager-remote-desktop-connections.md#rdp-iam-policy-examples") in the _AWS Systems Manager User Guide_
.

- Replace the example ARN in the Resource element with your actual KMS key ARN.
  For help finding the values of the referenced identifiers, see [Where to find the required identifiers](identity-center-customer-managed-keys.md#find-the-required-identifiers "identity-center-customer-managed-keys.md#find-the-required-identifiers").
  Permission set IAM policy:

```
{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "IAMPolicyToAllowKMSKeyUseViaIdentityCenterAndIdentityStore",
    "Effect": "Allow",
    "Action": "kms:Decrypt",
    "Resource": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
    "Condition": {
      "StringLike": {
        "kms:ViaService": [
          "sso.*.amazonaws.com",
          "identitystore.*.amazonaws.com"
        ]
      }
    }
  }]
}
```

Use the following KMS key policy statement templates in [Step 2: Prepare KMS key policy
statements](identity-center-customer-managed-keys.md#choose-kms-key-policy-statements "identity-center-customer-managed-keys.md#choose-kms-key-policy-statements") to allow custom workflows, such as
customer managed applications, in the AWS Organizations management account or delegated
administration account to use the KMS key. Note that SAML federation into customer
managed applications does not require KMS key permissions.

- In the Principal element, specify the IAM principals used to access IAM Identity Center
  service APIs. For more information about IAM principals, see [Specifying
  a principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md") in the _IAM User Guide_.
- These policy statements allow your workflow to use the KMS key through any of
  your IAM Identity Center instances. To restrict access to a specific IAM Identity
  Center instance, see [Advanced KMS key policy statements](advanced-kms-policy.md "advanced-kms-policy.md").
- To help protect against IAM role name changes when permission sets are
  recreated, use the approach described in the [Custom trust policy example](referencingpermissionsets.md#custom-trust-policy-example "referencingpermissionsets.md#custom-trust-policy-example")
  .
  KMS key policy statement:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowCustomWorkflowToUseTheKMSKeyViaIdentityCenter",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/MyCustomWorkflowRole"
      },
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "kms:EncryptionContext:aws:sso:instance-arn": "*",
          "kms:ViaService": "sso.*.amazonaws.com"
        }
      }
    },
    {
      "Sid": "AllowCustomWorkflowToUseTheKMSKeyViaIdentityStore",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/MyCustomWorkflowRole"
      },
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "kms:ViaService": "identitystore.*.amazonaws.com",
          "kms:EncryptionContext:aws:identitystore:identitystore-arn": "*"
        }
      }
    }
  ]
}
```

Use the following IAM policy statement template in [Step 4: Configure IAM policies for
cross-account use of the KMS key](identity-center-customer-managed-keys.md#configure-iam-policies-kms-key "identity-center-customer-managed-keys.md#configure-iam-policies-kms-key") to allow the IAM principal
associated with the custom workflow to use the KMS key across accounts. Add the IAM
policy statement to the IAM principal.

- Replace the example ARN in the Resource element with your actual KMS key ARN.
  For help finding the values of the referenced identifiers, see [Where to find the required identifiers](identity-center-customer-managed-keys.md#find-the-required-identifiers "identity-center-customer-managed-keys.md#find-the-required-identifiers").
  IAM policy statement (required only for cross-account use):

```
{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "AllowCustomWorkflowToUseTheKMSKeyViaIdentityCenterAndIdentityStore",
    "Effect": "Allow",
    "Action": "kms:Decrypt",
    "Resource": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
    "Condition": {
      "StringLike": {
        "kms:ViaService": [
          "sso.*.amazonaws.com",
          "identitystore.*.amazonaws.com"
        ]
      }
    }
  }]
}
```

## Examples of KMS key policy

statements for common use cases

### IAM Identity Center with delegated

administrators and AWS managed applications

This section contains example KMS key policy statements that you can use for an
IAM Identity Center instance that has delegated administrators and AWS managed applications.

###### Important

The KMS key policy statements assume that your IAM Identity Center instance is not used in any
other use cases that require KMS key permissions. To confirm, you can review all [use cases](identity-center-customer-managed-keys.md#identify-use-cases "identity-center-customer-managed-keys.md#identify-use-cases"). Also, to confirm if your AWS
managed applications require additional configuration, see [Additional configuration in some
AWS managed applications](identity-center-customer-managed-keys.md#additional-config-in-some-aws-apps "identity-center-customer-managed-keys.md#additional-config-in-some-aws-apps")

Copy the KMS key policy statements below the table and add them to your KMS key
policy. This example uses the following example values:

- `111122223333` - Account ID of the IAM Identity Center instance
- `444455556666` - Delegated administration account ID
- `o-a1b2c3d4e5` - AWS organization ID
- `arn:aws:iam::111122223333:role/aws-reserved/sso.amazonaws.com/us-east-1/AWSReservedSSO_Admin_*`

* A wildcard pattern of an IAM Identity Center administrator's IAM role provisioned from the
  permission set `Admin`. Such a role contains the Region code of
  the primary Region (us-east-1 in this example).

- `arn:aws:iam::444455556666:role/aws-reserved/sso.amazonaws.com/us-east-1/AWSReservedSSO_DelegatedAdmin_*`

* A wildcard pattern of an IAM Identity Center delegated administrator's IAM role provisioned from the
  permission set `DelegatedAdmin`. Such a role contains the
  Region code of the primary Region (us-east-1 in this example).

If the IAM role was not generated from a permission set, the IAM role will look like
a regular one such as `arn:aws:iam::`111122223333`:role/`idcadmin``.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowIAMIdentityCenterAdminToUseTheKMSKeyViaIdentityCenter",
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "arn:aws:iam::`111122223333`:root",
          "arn:aws:iam::`444455556666`:root"
        ]
      },
      "Action": [
        "kms:Decrypt",
        "kms:Encrypt",
        "kms:GenerateDataKeyWithoutPlaintext"
      ],
      "Resource": "*",
      "Condition": {
        "ArnLike": {
          "aws:PrincipalArn": [
            "`arn:aws:iam::111122223333:role/aws-reserved/sso.amazonaws.com/us-east-1/AWSReservedSSO_Admin_*`",
            "`arn:aws:iam::444455556666:role/aws-reserved/sso.amazonaws.com/us-east-1/AWSReservedSSO_DelegatedAdmin_*`"
          ]
        },
        "StringLike": {
          "kms:EncryptionContext:aws:sso:instance-arn": "*",
          "kms:ViaService": "sso.*.amazonaws.com"
        }
      }
    },
    {
      "Sid": "AllowIAMIdentityCenterAdminToUseTheKMSKeyViaIdentityStore",
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "arn:aws:iam::`111122223333`:root",
          "arn:aws:iam::`444455556666`:root"
        ]
      },
      "Action": [
        "kms:Decrypt",
        "kms:Encrypt",
        "kms:GenerateDataKeyWithoutPlaintext"
      ],
      "Resource": "*",
      "Condition": {
        "ArnLike": {
          "aws:PrincipalArn": [
            "`arn:aws:iam::111122223333:role/aws-reserved/sso.amazonaws.com/us-east-1/AWSReservedSSO_Admin_*`",
            "`arn:aws:iam::444455556666:role/aws-reserved/sso.amazonaws.com/us-east-1/AWSReservedSSO_DelegatedAdmin_*`"
          ]
        },
        "StringLike": {
          "kms:EncryptionContext:aws:identitystore:identitystore-arn": "*",
          "kms:ViaService": "identitystore.*.amazonaws.com"
        }
      }
    },
    {
      "Sid": "AllowIAMIdentityCenterAdminToDescribeTheKMSKey",
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "arn:aws:iam::`111122223333`:root",
          "arn:aws:iam::`444455556666`:root"
        ]
      },
      "Action": "kms:DescribeKey",
      "Resource": "*",
      "Condition": {
        "ArnLike": {
          "aws:PrincipalArn": [
            "`arn:aws:iam::111122223333:role/aws-reserved/sso.amazonaws.com/us-east-1/AWSReservedSSO_Admin_*`",
            "`arn:aws:iam::444455556666:role/aws-reserved/sso.amazonaws.com/us-east-1/AWSReservedSSO_DelegatedAdmin_*`"
          ]
        }
      }
    },
    {
      "Sid": "AllowIAMIdentityCenterToUseTheKMSKey",
      "Effect": "Allow",
      "Principal": {
        "Service": "sso.amazonaws.com"
      },
      "Action": [
        "kms:Decrypt",
        "kms:ReEncryptTo",
        "kms:ReEncryptFrom",
        "kms:GenerateDataKeyWithoutPlaintext"
      ],
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "kms:EncryptionContext:aws:sso:instance-arn": "*"
        },
        "StringEquals": {
          "aws:SourceAccount": "`111122223333`"
        }
      }
    },
    {
      "Sid": "AllowIdentityStoreToUseTheKMSKey",
      "Effect": "Allow",
      "Principal": {
        "Service": "identitystore.amazonaws.com"
      },
      "Action": [
        "kms:Decrypt",
        "kms:ReEncryptTo",
        "kms:ReEncryptFrom",
        "kms:GenerateDataKeyWithoutPlaintext"
      ],
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "kms:EncryptionContext:aws:identitystore:identitystore-arn": "*"
        },
        "StringEquals": {
          "aws:SourceAccount": "`111122223333`"
        }
      }
    },
    {
      "Sid": "AllowIAMIdentityCenterAndIdentityStoreToDescribeKMSKey",
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "identitystore.amazonaws.com",
          "sso.amazonaws.com"
        ]
      },
      "Action": "kms:DescribeKey",
      "Resource": "*"
    },

   {
      "Sid": "AllowAppAdminsInTheSameOrganizationToUseTheKMSKeyViaIdentityCenter",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:PrincipalOrgID": "`o-a1b2c3d4e5`"
        },
        "StringLike": {
          "kms:ViaService": "sso.*.amazonaws.com",
          "kms:EncryptionContext:aws:sso:instance-arn": "*"
        }
      }
    },
    {
      "Sid": "AllowAppAdminsInTheSameOrganizationToUseTheKMSKeyViaIdentityStore",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:PrincipalOrgID": "`o-a1b2c3d4e5`"
        },
        "StringLike": {
          "kms:ViaService": "identitystore.*.amazonaws.com",
          "kms:EncryptionContext:aws:identitystore:identitystore-arn": "*"
        }
      }
    },
    {
      "Sid": "AllowManagedAppsToUseTheKMSKeyViaIdentityCenter",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "kms:ViaService": "sso.*.amazonaws.com",
          "kms:EncryptionContext:aws:sso:instance-arn": "*"
        },
        "Bool": {
          "aws:PrincipalIsAWSService": "true"
        },
        "StringEquals": {
          "aws:SourceOrgID": "`o-a1b2c3d4e5`"
        }
      }
    },
    {
      "Sid": "AllowManagedAppsToUseTheKMSKeyViaIdentityStore",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "kms:ViaService": "identitystore.*.amazonaws.com",
          "kms:EncryptionContext:aws:identitystore:identitystore-arn": "*"
        },
        "Bool": {
          "aws:PrincipalIsAWSService": "true"
        },
        "StringEquals": {
          "aws:SourceOrgID": "`o-a1b2c3d4e5`"
        }
      }
    }
  ]
}

```
