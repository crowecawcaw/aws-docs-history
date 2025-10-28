# Example SCPs for AWS Resource Access Manager

###### Topics

- [Preventing external sharing](#example_ram_1 "#example_ram_1")
- [Restrict resource sharing to specific account IDs](#example_ram_2 "#example_ram_2")
- [Prevent sharing with organizations or
  organizational units (OUs)](#example_ram_3 "#example_ram_3")
- [Allow sharing with only specified IAM users
  and roles](#example_ram_4 "#example_ram_4")

## Preventing external sharing

The following example SCP prevents users from creating resource shares that allow
sharing with IAM users and roles that aren't part of the organization.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Deny",
            "Action": [
                "ram:CreateResourceShare",
                "ram:UpdateResourceShare"
            ],
            "Resource": "*",
            "Condition": {
                "Bool": {
                    "ram:RequestedAllowsExternalPrincipals": "true"
                }
            }
        }
    ]
}
```

## Restrict resource sharing to specific account IDs

The following SCP allows accounts `111111111111` and
`222222222222` to create resource shares that share prefix lists, and to
associate prefix lists with existing resource shares.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "OnlyNamedAccountsCanSharePrefixLists",
            "Effect": "Deny",
            "Action": [
                "ram:AssociateResourceShare",
                "ram:CreateResourceShare"
            ],
            "Resource": "*",
            "Condition": {
                "StringNotEquals": {
                    "aws:PrincipalAccount": [
                        "111111111111",
                        "222222222222"
                    ]
                },
                "StringEquals": {
                    "ram:RequestedResourceType": "ec2:PrefixList"
                }
            }
        }
    ]
}
```

## Prevent sharing with organizations or

organizational units (OUs)

The following SCP prevents users from creating resource shares that share resources
with an organization or OUs.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Deny",
            "Action": [
                "ram:CreateResourceShare",
                "ram:AssociateResourceShare"
            ],
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringLike": {
                    "ram:Principal": [
                        "arn:aws:organizations::*:organization/*",
                        "arn:aws:organizations::*:ou/*"
                    ]
                }
            }
        }
    ]
}
```

## Allow sharing with only specified IAM users

and roles

The following example SCP allows users to share resources with
_only_ organization `o-12345abcdef`, organizational
unit `ou-98765fedcba`, and account `111111111111`.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ram:AssociateResourceShare",
                "ram:CreateResourceShare"
            ],
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "ram:Principal": [
                        "arn:aws:organizations::123456789012:organization/o-12345abcdef",
                        "arn:aws:organizations::123456789012:ou/o-12345abcdef/ou-98765fedcba",
                        "111111111111"
                    ]
                }
            }
        }
    ]
}
```
