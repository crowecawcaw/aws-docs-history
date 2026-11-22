

# CloudWatchOmniDevOpsAgentInvestigationServiceRolePolicy

**Description**: Grants Amazon CloudWatch permissions to read your CloudWatch integrations, context graph and intelligence configuration, to create, monitor and request mitigation plans for AWS DevOps Agent investigation tasks, and to read the topology of the investigation's agent space, in your account.

`CloudWatchOmniDevOpsAgentInvestigationServiceRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="CloudWatchOmniDevOpsAgentInvestigationServiceRolePolicy-how-to-use"></a>

You can attach `CloudWatchOmniDevOpsAgentInvestigationServiceRolePolicy` to your users, groups, and roles.

## Policy details
<a name="CloudWatchOmniDevOpsAgentInvestigationServiceRolePolicy-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: November 19, 2026, 02:47 UTC 
+ **Edited time:** November 19, 2026, 02:47 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/CloudWatchOmniDevOpsAgentInvestigationServiceRolePolicy`

## Policy version
<a name="CloudWatchOmniDevOpsAgentInvestigationServiceRolePolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="CloudWatchOmniDevOpsAgentInvestigationServiceRolePolicy-json"></a>

```json
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "DevOpsAgentInvestigation",
      "Effect" : "Allow",
      "Action" : [
        "aidevops:CreateBacklogTask",
        "aidevops:ListBacklogTasks",
        "aidevops:GetBacklogTask",
        "aidevops:UpdateBacklogTask",
        "aidevops:ListJournalRecords",
        "aidevops:ListExecutions",
        "aidevops:DiscoverTopology"
      ],
      "Resource" : "arn:aws:aidevops:*:*:agentspace/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    }
  ]
}
```

## Learn more
<a name="CloudWatchOmniDevOpsAgentInvestigationServiceRolePolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)