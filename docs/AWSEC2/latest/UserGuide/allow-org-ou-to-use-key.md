# Allow organizations and OUs to use a KMS key

If you share an AMI that is backed by encrypted snapshots, you must also allow the
organizations or organizational units (OUs) to use the KMS keys that were used to
encrypt the snapshots.

###### Note

The encrypted snapshots must be encrypted with a _customer
managed_ key. You can’t share AMIs that are backed by snapshots
that are encrypted with the default AWS managed key.

To control access to the KMS key, in the [key policy](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") you can use
the [`aws:PrincipalOrgID`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalorgid "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalorgid") and [`aws:PrincipalOrgPaths`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalorgpaths "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalorgpaths") condition keys to allow only
specific principals permission to the specified actions. A principal can be a user,
IAM role, federated user, or AWS account root user.

The condition keys are used as follows:

- `aws:PrincipalOrgID` – Allows any principal belonging to the
  organization represented by the specified ID.
- `aws:PrincipalOrgPaths` – Allows any principal belonging to the OUs
  represented by the specified paths.
  To give an organization (including the OUs and accounts that belong to it) permission to
  use a KMS key, add the following statement to the key policy.

```
{
    "Sid": "Allow access for organization root",
    "Effect": "Allow",
    "Principal": "*",
    "Action": [
        "kms:Describe*",
        "kms:List*",
        "kms:Get*",
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:ReEncrypt*",
        "kms:GenerateDataKey*",
        "kms:CreateGrant"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "aws:PrincipalOrgID": "`o-123example`"
        }
    }
}
```

To give specific OUs (and the accounts that belong to it) permission to use a KMS key,
you can use a policy similar to the following example.

```
{
        "Sid": "Allow access for specific OUs and their descendants",
        "Effect": "Allow",
        "Principal": "*",
        "Action": [
            "kms:Describe*",
            "kms:List*",
            "kms:Get*",
            "kms:Encrypt",
            "kms:Decrypt",
            "kms:ReEncrypt*",
            "kms:GenerateDataKey*",
            "kms:CreateGrant"
        ],
        "Resource": "*",
        "Condition": {
            "StringEquals": {
                "aws:PrincipalOrgID": "`o-123example`"
            },
            "ForAnyValue:StringLike": {
                "aws:PrincipalOrgPaths": [
                    "`o-123example/r-ab12/ou-ab12-33333333/*`",
                    "`o-123example/r-ab12/ou-ab12-22222222/*`"
                ]
            }
        }
}
```

For more example condition statements, see [aws:PrincipalOrgID](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalorgid "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalorgid") and [aws:PrincipalOrgPaths](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalorgpaths "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalorgpaths") in the _IAM User Guide_.

For information about cross-account access, see [Allowing users in other accounts to use a KMS key](../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md "../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md") in the
_AWS Key Management Service Developer Guide_.
