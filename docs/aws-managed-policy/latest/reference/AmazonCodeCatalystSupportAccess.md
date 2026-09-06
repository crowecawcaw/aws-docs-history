

# AmazonCodeCatalystSupportAccess
<a name="AmazonCodeCatalystSupportAccess"></a>

**Description**: Allows Amazon CodeCatalyst to create, update, and resolve AWS Support cases on your behalf.

`AmazonCodeCatalystSupportAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonCodeCatalystSupportAccess-how-to-use"></a>

You can attach `AmazonCodeCatalystSupportAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonCodeCatalystSupportAccess-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: April 20, 2023, 12:34 UTC 
+ **Edited time:** April 20, 2023, 12:34 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AmazonCodeCatalystSupportAccess`

## Policy version
<a name="AmazonCodeCatalystSupportAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonCodeCatalystSupportAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "support:DescribeAttachment",
        "support:DescribeCaseAttributes",
        "support:DescribeCases",
        "support:DescribeCommunications",
        "support:DescribeIssueTypes",
        "support:DescribeServices",
        "support:DescribeSeverityLevels",
        "support:DescribeSupportLevel",
        "support:SearchForCases",
        "support:AddAttachmentsToSet",
        "support:AddCommunicationToCase",
        "support:CreateCase",
        "support:InitiateCallForCase",
        "support:InitiateChatForCase",
        "support:PutCaseAttributes",
        "support:RateCaseCommunication",
        "support:ResolveCase"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonCodeCatalystSupportAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)