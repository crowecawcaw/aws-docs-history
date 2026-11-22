

# AWSNetworkFirewallIGWServiceRolePolicy

**Description**: Allows AWS Network Firewall to manage resources required for IGW Firewall on your behalf. Example of such resources include elastic IP addresses for network address translation.

`AWSNetworkFirewallIGWServiceRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSNetworkFirewallIGWServiceRolePolicy-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="AWSNetworkFirewallIGWServiceRolePolicy-details"></a>
+ **Type**: Service-linked role policy 
+ **Creation time**: November 11, 2026, 19:57 UTC 
+ **Edited time:** November 11, 2026, 19:57 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/AWSNetworkFirewallIGWServiceRolePolicy`

## Policy version
<a name="AWSNetworkFirewallIGWServiceRolePolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSNetworkFirewallIGWServiceRolePolicy-json"></a>

```json
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "ec2:DescribeVpcs",
        "ec2:DescribeInstances",
        "ec2:DescribeNetworkInterfaces",
        "ec2:DescribeInternetGateways"
      ],
      "Resource" : "*"
    },
    {
      "Effect" : "Allow",
      "Action" : "acm:DescribeCertificate",
      "Resource" : "*"
    },
    {
      "Effect" : "Allow",
      "Action" : "resource-groups:ListGroupResources",
      "Resource" : "*"
    },
    {
      "Effect" : "Allow",
      "Action" : "tag:GetResources",
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "aws:CalledViaLast" : "resource-groups.amazonaws.com"
        }
      }
    },
    {
      "Sid" : "EIPManagementForNATIPScaling",
      "Effect" : "Allow",
      "Action" : [
        "ec2:AllocateAddress",
        "ec2:DisassociateAddress",
        "ec2:DescribeAddresses",
        "ec2:AssociateAddress"
      ],
      "Resource" : "*"
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "ecs:ListContainerInstances",
        "ecs:ListTasks",
        "ecs:DescribeTasks",
        "ecs:DescribeContainerInstances"
      ],
      "Resource" : [
        "arn:aws:ecs:*:*:cluster/*",
        "arn:aws:ecs:*:*:container-instance/*/*",
        "arn:aws:ecs:*:*:task/*/*"
      ]
    }
  ]
}
```

## Learn more
<a name="AWSNetworkFirewallIGWServiceRolePolicy-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)