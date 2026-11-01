

# Route53PrivateHealthChecksServiceRolePolicy
<a name="Route53PrivateHealthChecksServiceRolePolicy"></a>

**Description**: Allows Amazon Route 53 health checks to describe subnets in your VPC. Helps Amazon Route 53 health checks determine whether IPv6 should be enabled for a customer's resource.

`Route53PrivateHealthChecksServiceRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="Route53PrivateHealthChecksServiceRolePolicy-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="Route53PrivateHealthChecksServiceRolePolicy-details"></a>
+ **Type**: Service-linked role policy 
+ **Creation time**: October 30, 2026, 20:07 UTC 
+ **Edited time:** October 30, 2026, 20:07 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/Route53PrivateHealthChecksServiceRolePolicy`

## Policy version
<a name="Route53PrivateHealthChecksServiceRolePolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="Route53PrivateHealthChecksServiceRolePolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : "ec2:CreateNetworkInterface",
      "Condition" : {
        "StringLike" : {
          "aws:RequestTag/Name" : "healthchecksource-*"
        },
        "ForAllValues:StringEquals" : {
          "aws:TagKeys" : [
            "Name"
          ]
        }
      },
      "Resource" : "arn:aws:ec2:*:*:network-interface/*"
    },
    {
      "Effect" : "Allow",
      "Action" : "ec2:CreateNetworkInterface",
      "Resource" : [
        "arn:aws:ec2:*:*:security-group/*",
        "arn:aws:ec2:*:*:subnet/*"
      ]
    },
    {
      "Effect" : "Allow",
      "Action" : "ec2:CreateTags",
      "Condition" : {
        "StringEquals" : {
          "ec2:CreateAction" : "CreateNetworkInterface"
        },
        "StringLike" : {
          "aws:RequestTag/Name" : "healthchecksource-*"
        }
      },
      "Resource" : "arn:aws:ec2:*:*:network-interface/*"
    },
    {
      "Effect" : "Allow",
      "Action" : "ec2:DeleteNetworkInterface",
      "Condition" : {
        "StringLike" : {
          "ec2:ResourceTag/Name" : "healthchecksource-*"
        }
      },
      "Resource" : "arn:aws:ec2:*:*:network-interface/*"
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "ec2:DescribeNetworkInterfaces",
        "ec2:DescribeSecurityGroups",
        "ec2:DescribeVpcs",
        "ec2:DescribeSubnets"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="Route53PrivateHealthChecksServiceRolePolicy-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)