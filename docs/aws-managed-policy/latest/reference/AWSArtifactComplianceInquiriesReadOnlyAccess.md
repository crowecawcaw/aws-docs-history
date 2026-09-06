

# AWSArtifactComplianceInquiriesReadOnlyAccess
<a name="AWSArtifactComplianceInquiriesReadOnlyAccess"></a>

**Description**: Provides read-only access to Artifact Compliance Inquiry.

`AWSArtifactComplianceInquiriesReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSArtifactComplianceInquiriesReadOnlyAccess-how-to-use"></a>

You can attach `AWSArtifactComplianceInquiriesReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AWSArtifactComplianceInquiriesReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: June 30, 2026, 19:42 UTC 
+ **Edited time:** June 30, 2026, 19:42 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSArtifactComplianceInquiriesReadOnlyAccess`

## Policy version
<a name="AWSArtifactComplianceInquiriesReadOnlyAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSArtifactComplianceInquiriesReadOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "ListComplianceInquiryActions",
      "Effect" : "Allow",
      "Action" : [
        "artifact:ListComplianceInquiries"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "GetComplianceInquiryActions",
      "Effect" : "Allow",
      "Action" : [
        "artifact:GetComplianceInquiryMetadata",
        "artifact:ListComplianceInquiryQueries",
        "artifact:ExportComplianceInquiry"
      ],
      "Resource" : "arn:aws:artifact:*:*:compliance-inquiry/*"
    }
  ]
}
```

## Learn more
<a name="AWSArtifactComplianceInquiriesReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)