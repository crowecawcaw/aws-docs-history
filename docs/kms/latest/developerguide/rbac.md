# RBAC for AWS KMS

Role-based access control (RBAC) is an authorization strategy that only provides
users with the permissions required to perform their job duties, and nothing more.
AWS KMS supports RBAC by allowing you to control access to your keys by specifying
granular permissions on key usage within [key
policies](key-policies.md "key-policies.md"). Key policies specify a resource, action, effect, principal, and
optional conditions to grant access to keys.

To implement RBAC in AWS KMS, we recommend separating the permissions for key users
and key administrators.

Key users
The following key policy example allows the
`ExampleUserRole` IAM role to use the KMS key.

```
{
            "Sid": "Allow use of the key",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::111122223333:role/ExampleUserRole"
            },
            "Action": [
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:ReEncrypt*",
                "kms:GenerateDataKey*",
                "kms:DescribeKey"
            ],
            "Resource": "*"
  }
```

Your key users might need fewer permissions than the user in this
example. Only assign the permissions that the user needs. Use the
following questions to help you further refine permissions.

- Which IAM principals (roles or users) need access to the
  key?
- Which actions does each principal need to perform with the
  key? For example, does the principal only need Encrypt and Sign
  permissions?
- Is the user a human or an AWS service? If it's an AWS
  service, you can use the [condition key](conditions-kms.md#conditions-kms-via-service "conditions-kms.md#conditions-kms-via-service") to
  restrict key usage to a specific AWS service.

Key administrators

The following key policy example allows the
`ExampleAdminRole` IAM role to administer the
KMS key.

```
{
            "Sid": "Allow access for Key Administrators",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::111122223333:role/ExampleAdminRole"
            },
            "Action": [
                "kms:Create*",
                "kms:Describe*",
                "kms:Enable*",
                "kms:List*",
                "kms:Put*",
                "kms:Update*",
                "kms:Revoke*",
                "kms:Disable*",
                "kms:Get*",
                "kms:Delete*",
                "kms:TagResource",
                "kms:UntagResource",
                "kms:ScheduleKeyDeletion",
                "kms:CancelKeyDeletion"
            ],
            "Resource": "*"
    }
```

Your key administrators might need fewer permissions than the
administrator in this example. Only assign the permissions that your key
administrators need.

Only give users the permissions they need to fulfill their roles. A user's
permissions might vary depending on whether the key is used in test or production
environments. If you use less restrictive permissions in certain non-production
environments, implement a process to test the policies before they're released to
production.

###### Learn more

- [IAM identities (users, user groups,
  and roles)](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md")
- [Types of access control](../../../prescriptive-guidance/latest/saas-multitenant-api-access-authorization/access-control-types.md "../../../prescriptive-guidance/latest/saas-multitenant-api-access-authorization/access-control-types.md")
