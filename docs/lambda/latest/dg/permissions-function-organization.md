# Granting function access to an organization

To grant permissions to all accounts in an [AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md") organization,
we recommend using `put-resource-policy` to create a full JSON policy with the `aws:PrincipalOrgID` condition key.

###### Important

Using `put-resource-policy` replaces any existing resource-based policy on the resource. If the resource
already has permissions defined with `add-permission`, `put-resource-policy` overwrites them.
Use `get-resource-policy` to retrieve the existing policy before making changes.

## Using a full JSON policy (recommended)

The following example policy grants invoke access to all AWS accounts in organization `o-a1b2c3d4e5f`:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "org-access",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "lambda:InvokeFunction",
            "Resource": "arn:aws:lambda:us-east-2:123456789012:function:my-function",
            "Condition": {
                "StringEquals": {
                    "aws:PrincipalOrgID": "o-a1b2c3d4e5f"
                }
            }
        }
    ]
}
```

Save the policy to a file named `policy.json` and apply it:

```
`aws lambda put-resource-policy \
 --resource-arn arn:aws:lambda:`us-east-2`:`123456789012`:function:`my-function` \
 --policy file://policy.json`
```

With a full JSON policy, you can also deny access to specific accounts within an organization:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "allow-org",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "lambda:InvokeFunction",
            "Resource": "arn:aws:lambda:us-east-2:123456789012:function:my-function",
            "Condition": {
                "StringEquals": {
                    "aws:PrincipalOrgID": "o-a1b2c3d4e5f"
                }
            }
        },
        {
            "Sid": "deny-specific-account",
            "Effect": "Deny",
            "Principal": {
                "AWS": "arn:aws:iam::999888777666:root"
            },
            "Action": "lambda:InvokeFunction",
            "Resource": [
                "arn:aws:lambda:us-east-2:123456789012:function:my-function",
                "arn:aws:lambda:us-east-2:123456789012:function:my-function:*"
            ]
        }
    ]
}
```

## Using add-permission

For simple use cases, you can use `add-permission` with the `principal-org-id` option.
The following command grants invocation access to all users in organization `o-a1b2c3d4e5f`:

```
`aws lambda add-permission \
 --function-name my-function \
 --statement-id org-access \
 --action lambda:InvokeFunction \
 --principal * \
 --principal-org-id o-a1b2c3d4e5f`
```

###### Note

In this command, `Principal` is `*`. This means that all users in the organization
`o-a1b2c3d4e5f` get function invocation permissions. If you specify an AWS account or role as the
`Principal`, then only that principal gets function invocation permissions, but only if they are
also part of the `o-a1b2c3d4e5f` organization.

For more information, see [aws:PrincipalOrgID](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalorgid "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalorgid") in the _IAM user guide_.
