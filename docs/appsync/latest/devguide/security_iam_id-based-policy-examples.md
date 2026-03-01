# Identity-based policies for AWS AppSync

By default, users and roles don't have permission to create or modify AWS AppSync
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by AWS AppSync, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for AWS AppSync](../../../service-authorization/latest/reference/list_awsappsync.md "../../../service-authorization/latest/reference/list_awsappsync.md") in the _Service Authorization Reference_.

To learn the best practices for creating and configuring IAM identity-based policies,
see [IAM policy best practices](best-practices.md#security_iam_service-with-iam-policy-best-practices "best-practices.md#security_iam_service-with-iam-policy-best-practices").

For
a list of IAM identity-based policies for AWS AppSync, see [AWS managed policies for AWS AppSync](security_iam_policy_list.md "security_iam_policy_list.md").

###### Topics

- [Using the AWS AppSync console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Allow users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Accessing one Amazon S3 bucket](#security_iam_id-based-policy-examples-access-one-bucket "#security_iam_id-based-policy-examples-access-one-bucket")
- [Viewing AWS AppSync widgets based on tags](#security_iam_id-based-policy-examples-view-widget-tags "#security_iam_id-based-policy-examples-view-widget-tags")
- [AWS managed policies for AWS AppSync](security_iam_policy_list.md "security_iam_policy_list.md")

## Using the AWS AppSync console

To access the AWS AppSync console, you must have a minimum set of permissions.
These permissions must allow you to list and view details about the AWS AppSync resources
in your AWS account. If you create an identity-based policy that is more restrictive
than the minimum required permissions, the console won't function as intended for
entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that they're trying to perform.

To ensure that
IAM
users and roles can still use the AWS AppSync console, also attach the
AWS AppSync `ConsoleAccess` or `ReadOnly` AWS managed policy to
the entities. For more information, see [Adding permissions to a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the
_IAM User Guide_.

## Allow users to view their own permissions

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user
identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ViewOwnUserInfo",
            "Effect": "Allow",
            "Action": [
                "iam:GetUserPolicy",
                "iam:ListGroupsForUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUser"
            ],
            "Resource": ["arn:aws:iam::*:user/${aws:username}"]
        },
        {
            "Sid": "NavigateInConsole",
            "Effect": "Allow",
            "Action": [
                "iam:GetGroupPolicy",
                "iam:GetPolicyVersion",
                "iam:GetPolicy",
                "iam:ListAttachedGroupPolicies",
                "iam:ListGroupPolicies",
                "iam:ListPolicyVersions",
                "iam:ListPolicies",
                "iam:ListUsers"
            ],
            "Resource": "*"
        }
    ]
}
```

## Accessing one Amazon S3 bucket

In this example, you want to grant an IAM user in your AWS account access to one
of your Amazon S3 buckets, `examplebucket`. You also want to allow the user to
add, update, and delete objects.

In addition to granting the `s3:PutObject`, `s3:GetObject`, and
`s3:DeleteObject` permissions to the user, the policy also grants the
`s3:ListAllMyBuckets`, `s3:GetBucketLocation`, and
`s3:ListBucket` permissions. These are the additional permissions required
by the console. Also, the `s3:PutObjectAcl` and the
`s3:GetObjectAcl` actions are required to be able to copy, cut, and paste
objects in the console. For an example walkthrough that grants permissions to users and
tests them using the console, see [An example
walkthrough: Using user policies to control access to your bucket](../../../AmazonS3/latest/userguide/walkthrough1.md "../../../AmazonS3/latest/userguide/walkthrough1.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"ListBucketsInConsole",
 "Effect":"Allow",
 "Action":[
 "s3:ListAllMyBuckets"
 ],
 "Resource":"arn:aws:s3:::*"
 },
 {
 "Sid":"ViewSpecificBucketInfo",
 "Effect":"Allow",
 "Action":[
 "s3:ListBucket",
 "s3:GetBucketLocation"
 ],
 "Resource":"arn:aws:s3:::examplebucket"
 },
 {
 "Sid":"ManageBucketContents",
 "Effect":"Allow",
 "Action":[
 "s3:PutObject",
 "s3:PutObjectAcl",
 "s3:GetObject",
 "s3:GetObjectAcl",
 "s3:DeleteObject"
 ],
 "Resource":"arn:aws:s3:::examplebucket/*"
 }
 ]
}`

```

## Viewing AWS AppSync `widgets` based on tags

You can use conditions in your identity-based policy to control access to AWS AppSync
resources based on tags. This example shows how you might create a policy that allows
viewing a `widget`. However, permission is granted only if the
`widget` tag `Owner` has the value of that user's
user name. This policy also grants the permissions necessary to complete this action on
the console.

You can attach this policy to the IAM users in your account. If a user named
`richard-roe` attempts to view an AWS AppSync
`widget`, the `widget` must be
tagged `Owner=richard-roe` or `owner=richard-roe`. Otherwise he is
denied access. The condition tag key `Owner` matches both `Owner`
and `owner` because condition key names are not case-sensitive. For more
information, see [IAM JSON policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.
