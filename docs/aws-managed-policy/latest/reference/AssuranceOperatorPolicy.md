

# AssuranceOperatorPolicy
<a name="AssuranceOperatorPolicy"></a>

**Description**: Provides full access to AWS Assurance environments and read-only access to IAM Identity Center user details

`AssuranceOperatorPolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AssuranceOperatorPolicy-how-to-use"></a>

You can attach `AssuranceOperatorPolicy` to your users, groups, and roles.

## Policy details
<a name="AssuranceOperatorPolicy-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: October 21, 2026, 15:17 UTC 
+ **Edited time:** October 21, 2026, 15:17 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AssuranceOperatorPolicy`

## Policy version
<a name="AssuranceOperatorPolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AssuranceOperatorPolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AssuranceOperatorAccess",
      "Effect" : "Allow",
      "Action" : [
        "assurance:BatchGetComment",
        "assurance:BatchGetTask",
        "assurance:BatchGetControl",
        "assurance:Chat",
        "assurance:CreateComment",
        "assurance:CreateControl",
        "assurance:CreateControlGroup",
        "assurance:CreateFramework",
        "assurance:CreateProject",
        "assurance:DeleteComment",
        "assurance:DeleteControl",
        "assurance:DeleteControlGroup",
        "assurance:DeleteEvidence",
        "assurance:DeleteFramework",
        "assurance:DeleteProject",
        "assurance:DisableFramework",
        "assurance:DownloadEvidence",
        "assurance:EnableFramework",
        "assurance:GetAnnotation",
        "assurance:GetAssessment",
        "assurance:GetAssessmentReportContent",
        "assurance:GetAssessmentReportExport",
        "assurance:GetChatMessages",
        "assurance:GetComment",
        "assurance:GetControl",
        "assurance:GetControlGroup",
        "assurance:GetControlStatus",
        "assurance:GetEnvironment",
        "assurance:GetEvidence",
        "assurance:GetEvidenceContent",
        "assurance:GetFramework",
        "assurance:GetProject",
        "assurance:GetTask",
        "assurance:ListAssessmentAnnotations",
        "assurance:ListEvidenceAnnotations",
        "assurance:ListAssessmentJournalRecords",
        "assurance:ListAssessments",
        "assurance:ListAssessmentOutcomes",
        "assurance:ListChatSessions",
        "assurance:ListComments",
        "assurance:ListConnectionItems",
        "assurance:ListControls",
        "assurance:ListControlGroups",
        "assurance:ListDiscoveredResources",
        "assurance:ListEnabledFrameworks",
        "assurance:ListEnvironmentConnections",
        "assurance:ListEvidence",
        "assurance:ListFrameworks",
        "assurance:ListProjects",
        "assurance:ListResourcesForControl",
        "assurance:ListTagsForResource",
        "assurance:ListTaskHistory",
        "assurance:ListTasks",
        "assurance:PublishFramework",
        "assurance:PutControlStatusOverride",
        "assurance:PutEvidence",
        "assurance:StartAssessment",
        "assurance:StartAssessmentReportExport",
        "assurance:StartResourceDiscovery",
        "assurance:UpdateComment",
        "assurance:UpdateControl",
        "assurance:UpdateControlGroup",
        "assurance:UpdateEvidence",
        "assurance:UpdateFramework",
        "assurance:UpdateProject",
        "assurance:UpdateTask",
        "assurance:UploadEvidence"
      ],
      "Resource" : [
        "arn:aws:assurance:*:*:environment/*"
      ]
    },
    {
      "Sid" : "IDCUserAccess",
      "Effect" : "Allow",
      "Action" : "identitystore:DescribeUser",
      "Resource" : [
        "arn:aws:identitystore::*:identitystore/*",
        "arn:aws:identitystore:::user/*"
      ]
    }
  ]
}
```

## Learn more
<a name="AssuranceOperatorPolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)