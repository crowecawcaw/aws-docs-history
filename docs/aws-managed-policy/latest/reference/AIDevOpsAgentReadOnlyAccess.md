

# AIDevOpsAgentReadOnlyAccess
<a name="AIDevOpsAgentReadOnlyAccess"></a>

**Description**: Provides read only access to Amazon DevOps Agent via the AWS Management Console

`AIDevOpsAgentReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AIDevOpsAgentReadOnlyAccess-how-to-use"></a>

You can attach `AIDevOpsAgentReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AIDevOpsAgentReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: March 26, 2026, 03:42 UTC 
+ **Edited time:** June 11, 2026, 00:57 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AIDevOpsAgentReadOnlyAccess`

## Policy version
<a name="AIDevOpsAgentReadOnlyAccess-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AIDevOpsAgentReadOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AIDevOpsAgentReadOnlyAccess",
      "Effect" : "Allow",
      "Action" : [
        "aidevops:DescribePrivateConnection",
        "aidevops:DescribeServices",
        "aidevops:Get*",
        "aidevops:List*",
        "aidevops:SearchServiceAccessibleResource"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AIDevOpsAgentReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)