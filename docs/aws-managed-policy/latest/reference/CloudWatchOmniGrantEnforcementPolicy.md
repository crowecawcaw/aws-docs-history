

# CloudWatchOmniGrantEnforcementPolicy

**Description**: Denies CloudWatch Omni actions that are not allowed by an access grant in the space.

`CloudWatchOmniGrantEnforcementPolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="CloudWatchOmniGrantEnforcementPolicy-how-to-use"></a>

You can attach `CloudWatchOmniGrantEnforcementPolicy` to your users, groups, and roles.

## Policy details
<a name="CloudWatchOmniGrantEnforcementPolicy-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 19, 2026, 03:17 UTC 
+ **Edited time:** November 19, 2026, 03:17 UTC
+ **ARN**: `arn:aws:iam::aws:policy/CloudWatchOmniGrantEnforcementPolicy`

## Policy version
<a name="CloudWatchOmniGrantEnforcementPolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="CloudWatchOmniGrantEnforcementPolicy-json"></a>

```json
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "RequireOmniAccessGrant",
      "Effect" : "Deny",
      "Action" : [
        "cloudwatch:StartTelemetryQuerySession",
        "cloudwatch:List*",
        "cloudwatch:GetTelemetryQueryResults",
        "cloudwatch:StopTelemetryQuery",
        "cloudwatch:StopTelemetryQuerySession",
        "cloudwatch:GetRecords",
        "cloudwatch:GetContextGraph",
        "cloudwatch:GetAlert",
        "cloudwatch:GetIntelligenceConfiguration",
        "cloudwatch:GetSpace"
      ],
      "Resource" : "*",
      "Condition" : {
        "StringNotEquals" : {
          "cloudwatch:HasAccessGrant" : "true"
        }
      }
    }
  ]
}
```

## Learn more
<a name="CloudWatchOmniGrantEnforcementPolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)