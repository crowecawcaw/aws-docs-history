

# AmazonGuardDutyReadOnlyAccess
<a name="AmazonGuardDutyReadOnlyAccess"></a>

**Description**: Provides read only access to Amazon GuardDuty resources

`AmazonGuardDutyReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonGuardDutyReadOnlyAccess-how-to-use"></a>

You can attach `AmazonGuardDutyReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonGuardDutyReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 28, 2017, 22:29 UTC 
+ **Edited time:** November 16, 2023, 23:07 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonGuardDutyReadOnlyAccess`

## Policy version
<a name="AmazonGuardDutyReadOnlyAccess-version"></a>

**Policy version:** v4 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonGuardDutyReadOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "guardduty:Describe*",
        "guardduty:Get*",
        "guardduty:List*"
      ],
      "Resource" : "*"
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "organizations:ListDelegatedAdministrators",
        "organizations:ListAWSServiceAccessForOrganization",
        "organizations:DescribeOrganizationalUnit",
        "organizations:DescribeAccount",
        "organizations:DescribeOrganization",
        "organizations:ListAccounts"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonGuardDutyReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)