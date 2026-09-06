

# AWSArtifactComplianceInquiriesFullAccess
<a name="AWSArtifactComplianceInquiriesFullAccess"></a>

**Description**: Provides full access to the Artifact Compliance Inquiry.

`AWSArtifactComplianceInquiriesFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSArtifactComplianceInquiriesFullAccess-how-to-use"></a>

You can attach `AWSArtifactComplianceInquiriesFullAccess` to your users, groups, and roles.

## Policy details
<a name="AWSArtifactComplianceInquiriesFullAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: June 30, 2026, 19:27 UTC 
+ **Edited time:** July 23, 2026, 20:12 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSArtifactComplianceInquiriesFullAccess`

## Policy version
<a name="AWSArtifactComplianceInquiriesFullAccess-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSArtifactComplianceInquiriesFullAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "ListAndCreateComplianceInquiryActions",
      "Effect" : "Allow",
      "Action" : [
        "artifact:ListComplianceInquiries",
        "artifact:CreateComplianceInquiry"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "ComplianceInquiryActions",
      "Effect" : "Allow",
      "Action" : [
        "artifact:ListComplianceInquiryQueries",
        "artifact:GetComplianceInquiryMetadata",
        "artifact:ExportComplianceInquiry",
        "artifact:PutComplianceInquiryFeedback"
      ],
      "Resource" : "arn:aws:artifact:*:*:compliance-inquiry/*"
    }
  ]
}
```

## Learn more
<a name="AWSArtifactComplianceInquiriesFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)