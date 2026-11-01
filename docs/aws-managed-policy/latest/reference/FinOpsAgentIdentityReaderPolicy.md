

# FinOpsAgentIdentityReaderPolicy
<a name="FinOpsAgentIdentityReaderPolicy"></a>

**Description**: Provides permissions required by AWS FinOps Agent to read IAM Identity Center user and group information and check group membership for agent access

`FinOpsAgentIdentityReaderPolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="FinOpsAgentIdentityReaderPolicy-how-to-use"></a>

You can attach `FinOpsAgentIdentityReaderPolicy` to your users, groups, and roles.

## Policy details
<a name="FinOpsAgentIdentityReaderPolicy-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: October 29, 2026, 17:17 UTC 
+ **Edited time:** October 29, 2026, 17:17 UTC
+ **ARN**: `arn:aws:iam::aws:policy/FinOpsAgentIdentityReaderPolicy`

## Policy version
<a name="FinOpsAgentIdentityReaderPolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="FinOpsAgentIdentityReaderPolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "FinOpsAgentIdentityStoreReads",
      "Effect" : "Allow",
      "Action" : [
        "identitystore:DescribeUser",
        "identitystore:DescribeGroup",
        "identitystore:IsMemberInGroups"
      ],
      "Resource" : [
        "arn:aws:identitystore::*:identitystore/*",
        "arn:aws:identitystore:::user/*",
        "arn:aws:identitystore:::group/*"
      ]
    }
  ]
}
```

## Learn more
<a name="FinOpsAgentIdentityReaderPolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)