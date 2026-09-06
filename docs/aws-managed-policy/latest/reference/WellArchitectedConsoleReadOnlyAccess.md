

# WellArchitectedConsoleReadOnlyAccess
<a name="WellArchitectedConsoleReadOnlyAccess"></a>

**Description**: Provides read-only access to AWS Well-Architected Tool via the AWS Management Console

`WellArchitectedConsoleReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="WellArchitectedConsoleReadOnlyAccess-how-to-use"></a>

You can attach `WellArchitectedConsoleReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="WellArchitectedConsoleReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 29, 2018, 18:21 UTC 
+ **Edited time:** July 09, 2026, 17:27 UTC
+ **ARN**: `arn:aws:iam::aws:policy/WellArchitectedConsoleReadOnlyAccess`

## Policy version
<a name="WellArchitectedConsoleReadOnlyAccess-version"></a>

**Policy version:** v3 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="WellArchitectedConsoleReadOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "wellarchitected:Get*",
        "wellarchitected:List*",
        "wellarchitected:ExportLens",
        "organizations:DescribeAccount",
        "organizations:ListAWSServiceAccessForOrganization",
        "organizations:ListDelegatedAdministrators",
        "organizations:ListRoots",
        "organizations:ListOrganizationalUnitsForParent",
        "organizations:ListAccountsForParent",
        "organizations:ListAccounts",
        "organizations:DescribeOrganization",
        "trustedadvisor:List*",
        "trustedadvisor:Get*"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="WellArchitectedConsoleReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)