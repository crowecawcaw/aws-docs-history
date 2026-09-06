

# AWSSecurityIncidentResponseReadOnlyAccess
<a name="AWSSecurityIncidentResponseReadOnlyAccess"></a>

**Description**: Policy provides customers with Read-only permissions to all resources associated to the Security Incident Response service. Permission includes access to GetCaseAttachmentDownloadUrl as well for the ability to get case attachment download URLs.

`AWSSecurityIncidentResponseReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSSecurityIncidentResponseReadOnlyAccess-how-to-use"></a>

You can attach `AWSSecurityIncidentResponseReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AWSSecurityIncidentResponseReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: December 01, 2024, 23:06 UTC 
+ **Edited time:** April 22, 2026, 16:12 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSSecurityIncidentResponseReadOnlyAccess`

## Policy version
<a name="AWSSecurityIncidentResponseReadOnlyAccess-version"></a>

**Policy version:** v4 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSSecurityIncidentResponseReadOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "SecurityIRReadAccess",
      "Effect" : "Allow",
      "Action" : [
        "security-ir:BatchGetMemberAccountDetails",
        "security-ir:GetMembership",
        "security-ir:ListMemberships",
        "security-ir:GetCase",
        "security-ir:ListCases",
        "security-ir:GetCaseAttachmentDownloadUrl",
        "security-ir:ListComments",
        "security-ir:ListCaseEdits",
        "security-ir:ListTagsForResource",
        "security-ir:ListInvestigations"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSSecurityIncidentResponseReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)