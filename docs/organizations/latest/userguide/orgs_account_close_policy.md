# Protecting member accounts from

closure with AWS Organizations

To protect member accounts from accidental closure, create an IAM policy that specifies which accounts are exempt. This policy prevents closure of protected member accounts.

Create an IAM policy to deny account closure using one of these methods:

- Explicitly list protected accounts in the policy's `Resource` element using their ARNs.
- Tag individual accounts and use the `aws:ResourceTag` global condition key to prevent closure of tagged accounts.

###### Note

Service Control Policies (SCPs) don't affect IAM principals in the management account.

## Example IAM policies that

prevent member account closures

The following code examples show two different methods you can use to restrict
member accounts from closing their account.

Prevent member accounts with
tags from getting closed You can attach the following policy to an identity in your management account.
This policy prevents principals in the management account from closing any
member account that is tagged with the `aws:ResourceTag` tag global
condition key, the `AccountType` key and the `Critical`
tag value.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PreventCloseAccountForTaggedAccts",
            "Effect": "Deny",
            "Action": "organizations:CloseAccount",
            "Resource": "*",
            "Condition": {
                "StringEquals": {"aws:ResourceTag/AccountType": "Critical"}
            }
        }
    ]
}
```

Prevent member
accounts listed in this policy from getting closed You can attach the following policy to an identity in your management account.
This policy prevents principals in the management account from closing member
accounts explicitly specified in the `Resource` element.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PreventCloseAccount",
            "Effect": "Deny",
            "Action": "organizations:CloseAccount",
            "Resource": [
                "arn:aws:organizations::555555555555:account/o-12345abcdef/123456789012",
                "arn:aws:organizations::555555555555:account/o-12345abcdef/123456789014"
            ]
        }
    ]
}
```
