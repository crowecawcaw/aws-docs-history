

# AWSCertificateManagerPrivateCAAuditor
<a name="AWSCertificateManagerPrivateCAAuditor"></a>

**Description**: Provides auditor access to AWS Certificate Manager Private Certificate Authority

`AWSCertificateManagerPrivateCAAuditor` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSCertificateManagerPrivateCAAuditor-how-to-use"></a>

You can attach `AWSCertificateManagerPrivateCAAuditor` to your users, groups, and roles.

## Policy details
<a name="AWSCertificateManagerPrivateCAAuditor-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: October 23, 2018, 16:51 UTC 
+ **Edited time:** August 17, 2020, 22:54 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSCertificateManagerPrivateCAAuditor`

## Policy version
<a name="AWSCertificateManagerPrivateCAAuditor-version"></a>

**Policy version:** v4 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSCertificateManagerPrivateCAAuditor-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "acm-pca:CreateCertificateAuthorityAuditReport",
        "acm-pca:DescribeCertificateAuthority",
        "acm-pca:DescribeCertificateAuthorityAuditReport",
        "acm-pca:GetCertificateAuthorityCsr",
        "acm-pca:GetCertificateAuthorityCertificate",
        "acm-pca:GetCertificate",
        "acm-pca:GetPolicy",
        "acm-pca:ListPermissions",
        "acm-pca:ListTags"
      ],
      "Resource" : "arn:aws:acm-pca:*:*:certificate-authority/*"
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "acm-pca:ListCertificateAuthorities"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSCertificateManagerPrivateCAAuditor-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)