

# AWSMigrationHubOrchestratorInstanceRolePolicy
<a name="AWSMigrationHubOrchestratorInstanceRolePolicy"></a>

**Description**: This policy needs to be attached for SAP and MGN migrated instance for our service to orchestrate instances by downloading scripts from S3 and to fetch secret values inside EC2 instance.

`AWSMigrationHubOrchestratorInstanceRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSMigrationHubOrchestratorInstanceRolePolicy-how-to-use"></a>

You can attach `AWSMigrationHubOrchestratorInstanceRolePolicy` to your users, groups, and roles.

## Policy details
<a name="AWSMigrationHubOrchestratorInstanceRolePolicy-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: April 20, 2022, 02:43 UTC 
+ **Edited time:** April 20, 2022, 02:43 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSMigrationHubOrchestratorInstanceRolePolicy`

## Policy version
<a name="AWSMigrationHubOrchestratorInstanceRolePolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSMigrationHubOrchestratorInstanceRolePolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "secretsmanager:GetSecretValue"
      ],
      "Resource" : "arn:aws:secretsmanager:*:*:secret:migrationhub-orchestrator-*"
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "s3:GetObject"
      ],
      "Resource" : [
        "arn:aws:s3:::migrationhub-orchestrator-*",
        "arn:aws:s3:::aws-migrationhub-orchestrator-*/*"
      ]
    }
  ]
}
```

## Learn more
<a name="AWSMigrationHubOrchestratorInstanceRolePolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)