

# AWSOrganizationsReadOnlyAccess
<a name="AWSOrganizationsReadOnlyAccess"></a>

**Description**: Provides read-only access to AWS Organizations.

`AWSOrganizationsReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSOrganizationsReadOnlyAccess-how-to-use"></a>

You can attach `AWSOrganizationsReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AWSOrganizationsReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 06, 2018, 20:32 UTC 
+ **Edited time:** June 07, 2024, 21:32 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSOrganizationsReadOnlyAccess`

## Policy version
<a name="AWSOrganizationsReadOnlyAccess-version"></a>

**Policy version:** v6 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSOrganizationsReadOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AWSOrganizationsReadOnly",
      "Effect" : "Allow",
      "Action" : [
        "organizations:Describe*",
        "organizations:List*"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "AWSOrganizationsReadOnlyAccount",
      "Effect" : "Allow",
      "Action" : [
        "account:GetAlternateContact",
        "account:GetContactInformation",
        "account:ListRegions",
        "account:GetRegionOptStatus",
        "account:GetPrimaryEmail"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSOrganizationsReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)