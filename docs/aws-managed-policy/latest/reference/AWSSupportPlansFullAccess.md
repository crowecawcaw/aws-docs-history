

# AWSSupportPlansFullAccess
<a name="AWSSupportPlansFullAccess"></a>

**Description**: Provides full access to supportplans.

`AWSSupportPlansFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSSupportPlansFullAccess-how-to-use"></a>

You can attach `AWSSupportPlansFullAccess` to your users, groups, and roles.

## Policy details
<a name="AWSSupportPlansFullAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: September 27, 2022, 18:19 UTC 
+ **Edited time:** August 24, 2026, 18:27 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSSupportPlansFullAccess`

## Policy version
<a name="AWSSupportPlansFullAccess-version"></a>

**Policy version:** v4 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSSupportPlansFullAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "supportplans:GetSupportPlan",
        "supportplans:GetSupportPlanUpdateStatus",
        "supportplans:ListSupportPlanModifiers",
        "supportplans:StartSupportPlanUpdate",
        "supportplans:CreateSupportPlanSchedule",
        "supportplans:AcceptSupportAgreement",
        "supportplans:CancelSupportAgreement",
        "supportplans:CreateSupportAgreement",
        "supportplans:GetSupportAgreement",
        "supportplans:ListSupportAgreements",
        "supportplans:ListSupportAgreementRevisions",
        "supportplans:RejectSupportAgreement",
        "supportplans:UpdateSupportAgreement"
      ],
      "Resource" : "*"
    },
    {
      "Effect" : "Allow",
      "Action" : "iam:CreateServiceLinkedRole",
      "Resource" : "arn:aws:iam::*:role/aws-service-role/supportplans.amazonaws.com/AWSServiceRoleForSupportPlans",
      "Condition" : {
        "StringEquals" : {
          "iam:AWSServiceName" : "supportplans.amazonaws.com"
        }
      }
    },
    {
      "Effect" : "Allow",
      "Action" : "iam:GetRole",
      "Resource" : "arn:aws:iam::*:role/aws-service-role/supportplans.amazonaws.com/AWSServiceRoleForSupportPlans"
    }
  ]
}
```

## Learn more
<a name="AWSSupportPlansFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)