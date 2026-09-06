

# ResourceGroupsServiceRolePolicy
<a name="ResourceGroupsServiceRolePolicy"></a>

**Description**: Allows AWS Resource Groups to query the AWS services that own your resources to keep the group up-to-date

`ResourceGroupsServiceRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="ResourceGroupsServiceRolePolicy-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="ResourceGroupsServiceRolePolicy-details"></a>
+ **Type**: Service-linked role policy 
+ **Creation time**: January 05, 2023, 16:57 UTC 
+ **Edited time:** January 05, 2023, 16:57 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/ResourceGroupsServiceRolePolicy`

## Policy version
<a name="ResourceGroupsServiceRolePolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="ResourceGroupsServiceRolePolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "tag:GetResources",
        "cloudformation:DescribeStacks",
        "cloudformation:ListStackResources"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="ResourceGroupsServiceRolePolicy-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)