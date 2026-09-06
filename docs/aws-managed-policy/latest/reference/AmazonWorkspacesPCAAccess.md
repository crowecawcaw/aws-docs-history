

# AmazonWorkspacesPCAAccess
<a name="AmazonWorkspacesPCAAccess"></a>

**Description**: This managed policy provides full administrative access to AWS Certificate Manager Private CA resources in your AWS account for certificate-based authentication.

`AmazonWorkspacesPCAAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonWorkspacesPCAAccess-how-to-use"></a>

You can attach `AmazonWorkspacesPCAAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonWorkspacesPCAAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 08, 2022, 00:25 UTC 
+ **Edited time:** November 08, 2022, 00:25 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonWorkspacesPCAAccess`

## Policy version
<a name="AmazonWorkspacesPCAAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonWorkspacesPCAAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "acm-pca:IssueCertificate",
        "acm-pca:GetCertificate",
        "acm-pca:DescribeCertificateAuthority"
      ],
      "Resource" : "arn:*:acm-pca:*:*:*",
      "Condition" : {
        "StringLike" : {
          "aws:ResourceTag/euc-private-ca" : "*"
        }
      }
    }
  ]
}
```

## Learn more
<a name="AmazonWorkspacesPCAAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)