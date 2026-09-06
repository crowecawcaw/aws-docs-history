

# AWSSecurityIncidentResponseCaseFullAccess
<a name="AWSSecurityIncidentResponseCaseFullAccess"></a>

**Description**: Policy provides customers with Read and Write permissions to case resources that are created through the Security Incident Response service.

`AWSSecurityIncidentResponseCaseFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSSecurityIncidentResponseCaseFullAccess-how-to-use"></a>

You can attach `AWSSecurityIncidentResponseCaseFullAccess` to your users, groups, and roles.

## Policy details
<a name="AWSSecurityIncidentResponseCaseFullAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: December 01, 2024, 23:21 UTC 
+ **Edited time:** April 22, 2026, 15:57 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSSecurityIncidentResponseCaseFullAccess`

## Policy version
<a name="AWSSecurityIncidentResponseCaseFullAccess-version"></a>

**Policy version:** v4 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSSecurityIncidentResponseCaseFullAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "SecurityIRCaseFullAccess",
      "Effect" : "Allow",
      "Action" : [
        "security-ir:GetCase",
        "security-ir:ListCases",
        "security-ir:GetCaseAttachmentDownloadUrl",
        "security-ir:ListComments",
        "security-ir:ListCaseEdits",
        "security-ir:CreateCase",
        "security-ir:UpdateCase",
        "security-ir:CloseCase",
        "security-ir:UpdateCaseStatus",
        "security-ir:UpdateResolverType",
        "security-ir:GetCaseAttachmentUploadUrl",
        "security-ir:CreateCaseComment",
        "security-ir:UpdateCaseComment",
        "security-ir:SendFeedback",
        "security-ir:ListInvestigations"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "SecurityIRCaseTagFullAccess",
      "Effect" : "Allow",
      "Action" : [
        "security-ir:ListTagsForResource",
        "security-ir:TagResource",
        "security-ir:UntagResource"
      ],
      "Resource" : "arn:aws:security-ir:*:*:case/*"
    }
  ]
}
```

## Learn more
<a name="AWSSecurityIncidentResponseCaseFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)