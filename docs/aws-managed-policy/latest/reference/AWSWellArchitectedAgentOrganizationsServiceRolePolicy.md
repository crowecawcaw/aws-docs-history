

# AWSWellArchitectedAgentOrganizationsServiceRolePolicy
<a name="AWSWellArchitectedAgentOrganizationsServiceRolePolicy"></a>

**Description**: Allows AWS Well-Architected Agent to access organizational structure and delegated administrator information in AWS Organizations on your behalf

`AWSWellArchitectedAgentOrganizationsServiceRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSWellArchitectedAgentOrganizationsServiceRolePolicy-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="AWSWellArchitectedAgentOrganizationsServiceRolePolicy-details"></a>
+ **Type**: Service-linked role policy 
+ **Creation time**: September 15, 2026, 18:37 UTC 
+ **Edited time:** September 15, 2026, 18:37 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/AWSWellArchitectedAgentOrganizationsServiceRolePolicy`

## Policy version
<a name="AWSWellArchitectedAgentOrganizationsServiceRolePolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSWellArchitectedAgentOrganizationsServiceRolePolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "organizations:DescribeAccount",
        "organizations:DescribeOrganization",
        "organizations:DescribeOrganizationalUnit",
        "organizations:ListAccountsForParent",
        "organizations:ListAccounts",
        "organizations:ListAWSServiceAccessForOrganization",
        "organizations:ListChildren",
        "organizations:ListDelegatedAdministrators",
        "organizations:ListOrganizationalUnitsForParent",
        "organizations:ListParents",
        "organizations:ListRoots"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSWellArchitectedAgentOrganizationsServiceRolePolicy-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)