

# AmazonApplicationRecoveryControllerRegionSwitchPlanExecutionPolicy
<a name="AmazonApplicationRecoveryControllerRegionSwitchPlanExecutionPolicy"></a>

**Description**: Grants permissions to ARC Region switch for plan execution and plan evaluation.

`AmazonApplicationRecoveryControllerRegionSwitchPlanExecutionPolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonApplicationRecoveryControllerRegionSwitchPlanExecutionPolicy-how-to-use"></a>

You can attach `AmazonApplicationRecoveryControllerRegionSwitchPlanExecutionPolicy` to your users, groups, and roles.

## Policy details
<a name="AmazonApplicationRecoveryControllerRegionSwitchPlanExecutionPolicy-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 03, 2025, 19:34 UTC 
+ **Edited time:** March 05, 2026, 19:27 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonApplicationRecoveryControllerRegionSwitchPlanExecutionPolicy`

## Policy version
<a name="AmazonApplicationRecoveryControllerRegionSwitchPlanExecutionPolicy-version"></a>

**Policy version:** v4 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonApplicationRecoveryControllerRegionSwitchPlanExecutionPolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "arc-region-switch:GetPlan",
        "arc-region-switch:GetPlanExecution",
        "arc-region-switch:ListPlanExecutions"
      ],
      "Resource" : "*",
      "Sid" : "GetPlanAndExecutions"
    },
    {
      "Effect" : "Allow",
      "Action" : "iam:SimulatePrincipalPolicy",
      "Resource" : "arn:aws:iam::*:role/*",
      "Sid" : "PlanEvaluation"
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "cloudwatch:DescribeAlarms",
        "cloudwatch:DescribeAlarmHistory",
        "cloudwatch:GetMetricStatistics"
      ],
      "Resource" : "*",
      "Sid" : "CloudWatch"
    }
  ]
}
```

## Learn more
<a name="AmazonApplicationRecoveryControllerRegionSwitchPlanExecutionPolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)