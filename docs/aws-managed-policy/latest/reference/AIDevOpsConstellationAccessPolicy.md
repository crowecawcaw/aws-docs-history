

# AIDevOpsConstellationAccessPolicy
<a name="AIDevOpsConstellationAccessPolicy"></a>

**Description**: Provides permissions required by the AWS DevOps Agent to coordinate with AgentSpaces connected through Agent Space Constellation.

`AIDevOpsConstellationAccessPolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AIDevOpsConstellationAccessPolicy-how-to-use"></a>

You can attach `AIDevOpsConstellationAccessPolicy` to your users, groups, and roles.

## Policy details
<a name="AIDevOpsConstellationAccessPolicy-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: August 05, 2026, 16:27 UTC 
+ **Edited time:** August 05, 2026, 16:27 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AIDevOpsConstellationAccessPolicy`

## Policy version
<a name="AIDevOpsConstellationAccessPolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AIDevOpsConstellationAccessPolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "ConstellationCoordination",
      "Effect" : "Allow",
      "Action" : [
        "aidevops:GetAgentSpace",
        "aidevops:CreateBacklogTask",
        "aidevops:GetBacklogTask",
        "aidevops:ListBacklogTasks",
        "aidevops:GetAsset",
        "aidevops:GetAssetContent",
        "aidevops:GetAssetFile",
        "aidevops:ListAssets",
        "aidevops:ListAssetFiles",
        "aidevops:ListExecutions",
        "aidevops:ListJournalRecords"
      ],
      "Resource" : "arn:aws:aidevops:*:*:agentspace/*"
    }
  ]
}
```

## Learn more
<a name="AIDevOpsConstellationAccessPolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)