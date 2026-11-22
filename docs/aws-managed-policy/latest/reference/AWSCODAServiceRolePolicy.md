

# AWSCODAServiceRolePolicy

**Description**: Allows AWS CODA to monitor the deployment of delegations on your behalf.

`AWSCODAServiceRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSCODAServiceRolePolicy-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="AWSCODAServiceRolePolicy-details"></a>
+ **Type**: Service-linked role policy 
+ **Creation time**: November 10, 2026, 20:07 UTC 
+ **Edited time:** November 10, 2026, 20:07 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/AWSCODAServiceRolePolicy`

## Policy version
<a name="AWSCODAServiceRolePolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSCODAServiceRolePolicy-json"></a>

```json
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "cloudformation:DescribeStacks",
        "cloudformation:DescribeStackSet",
        "cloudformation:DescribeStackSetOperation",
        "cloudformation:DescribeStackInstance",
        "cloudformation:ListStackSetOperations",
        "cloudformation:ListStackInstances"
      ],
      "Resource" : [
        "arn:aws:cloudformation:*:*:stack/coda-*/*",
        "arn:aws:cloudformation:*:*:stackset/coda-*:*"
      ]
    },
    {
      "Effect" : "Allow",
      "Action" : "organizations:DescribeAccount",
      "Resource" : "arn:aws:organizations::*:account/o-*/*"
    },
    {
      "Effect" : "Allow",
      "Action" : "organizations:DescribeOrganizationalUnit",
      "Resource" : "arn:aws:organizations::*:ou/o-*/ou-*"
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "organizations:DescribeOrganization",
        "organizations:ListAccounts",
        "organizations:ListAccountsForParent",
        "organizations:ListChildren",
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
<a name="AWSCODAServiceRolePolicy-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)