

# AWSConfigRoleForOrganizations
<a name="AWSConfigRoleForOrganizations"></a>

**Description**: Allows AWS Config to call read-only AWS Organizations APIs

`AWSConfigRoleForOrganizations` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSConfigRoleForOrganizations-how-to-use"></a>

You can attach `AWSConfigRoleForOrganizations` to your users, groups, and roles.

## Policy details
<a name="AWSConfigRoleForOrganizations-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: March 19, 2018, 22:53 UTC 
+ **Edited time:** November 24, 2020, 20:19 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AWSConfigRoleForOrganizations`

## Policy version
<a name="AWSConfigRoleForOrganizations-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSConfigRoleForOrganizations-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "organizations:ListAccounts",
        "organizations:DescribeOrganization",
        "organizations:ListAWSServiceAccessForOrganization",
        "organizations:ListDelegatedAdministrators"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSConfigRoleForOrganizations-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)