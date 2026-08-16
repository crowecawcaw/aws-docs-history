# AIDevOpsConstellationAccessPolicy

**Description**: Provides permissions required by the AWS DevOps Agent to coordinate with AgentSpaces connected through Agent Space Constellation.

`AIDevOpsConstellationAccessPolicy` is an [AWS managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies").

## Using this policy

You can attach `AIDevOpsConstellationAccessPolicy` to your users, groups, and roles.

## Policy details

- **Type**: Service role policy
- **Creation time**: August 05, 2026, 16:27 UTC
- **Edited time:** August 05, 2026, 16:27 UTC
- **ARN**:
  `arn:aws:iam::aws:policy/service-role/AIDevOpsConstellationAccessPolicy`

## Policy version

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a
request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request.

## JSON policy document

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

- [Create a permission set using AWS managed policies in IAM Identity Center](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md")
- [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md")
- [Understand versioning for IAM policies](../../../IAM/latest/UserGuide/access_policies_managed-versioning.md "../../../IAM/latest/UserGuide/access_policies_managed-versioning.md")
- [Get started with AWS managed policies and move toward least-privilege permissions](../../../IAM/latest/UserGuide/best-practices.md#bp-use-aws-defined-policies "../../../IAM/latest/UserGuide/best-practices.md#bp-use-aws-defined-policies")
