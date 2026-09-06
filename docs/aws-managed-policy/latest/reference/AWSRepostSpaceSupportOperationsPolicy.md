

# AWSRepostSpaceSupportOperationsPolicy
<a name="AWSRepostSpaceSupportOperationsPolicy"></a>

**Description**: This policy allows the re:Post Space service to create, manage, and resolve Support cases that are created through the Space application.

`AWSRepostSpaceSupportOperationsPolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSRepostSpaceSupportOperationsPolicy-how-to-use"></a>

You can attach `AWSRepostSpaceSupportOperationsPolicy` to your users, groups, and roles.

## Policy details
<a name="AWSRepostSpaceSupportOperationsPolicy-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 26, 2023, 21:52 UTC 
+ **Edited time:** November 26, 2023, 21:52 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSRepostSpaceSupportOperationsPolicy`

## Policy version
<a name="AWSRepostSpaceSupportOperationsPolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSRepostSpaceSupportOperationsPolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "RepostSpaceSupportOperations",
      "Effect" : "Allow",
      "Action" : [
        "support:AddAttachmentsToSet",
        "support:AddCommunicationToCase",
        "support:CreateCase",
        "support:DescribeCases",
        "support:DescribeCommunications",
        "support:ResolveCase"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSRepostSpaceSupportOperationsPolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)