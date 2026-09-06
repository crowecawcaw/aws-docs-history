

# AmazonDetectiveMemberAccess
<a name="AmazonDetectiveMemberAccess"></a>

**Description**: Provides member access to Amazon Detective service and scoped access to the console UI dependencies.

`AmazonDetectiveMemberAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonDetectiveMemberAccess-how-to-use"></a>

You can attach `AmazonDetectiveMemberAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonDetectiveMemberAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: January 17, 2023, 15:16 UTC 
+ **Edited time:** January 17, 2023, 15:16 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonDetectiveMemberAccess`

## Policy version
<a name="AmazonDetectiveMemberAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonDetectiveMemberAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "detective:AcceptInvitation",
        "detective:BatchGetMembershipDatasources",
        "detective:DisassociateMembership",
        "detective:GetFreeTrialEligibility",
        "detective:GetPricingInformation",
        "detective:GetUsageInformation",
        "detective:ListInvitations",
        "detective:RejectInvitation"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonDetectiveMemberAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)