

# ContinuumThreatsServiceRolePolicy

**Description**: Allows AWS Continuum Threats to collect security telemetry from the account on your behalf, by managing an AWS CloudTrail service-linked channel and an AWS Config service-linked configuration recorder, and creating the AWS Config service-linked role if it does not exist.

`ContinuumThreatsServiceRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="ContinuumThreatsServiceRolePolicy-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="ContinuumThreatsServiceRolePolicy-details"></a>
+ **Type**: Service-linked role policy 
+ **Creation time**: November 13, 2026, 17:27 UTC 
+ **Edited time:** November 13, 2026, 17:27 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/ContinuumThreatsServiceRolePolicy`

## Policy version
<a name="ContinuumThreatsServiceRolePolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="ContinuumThreatsServiceRolePolicy-json"></a>

```json
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "ManageServiceLinkedChannel",
      "Effect" : "Allow",
      "Action" : [
        "cloudtrail:CreateServiceLinkedChannel",
        "cloudtrail:UpdateServiceLinkedChannel",
        "cloudtrail:GetServiceLinkedChannel",
        "cloudtrail:DeleteServiceLinkedChannel"
      ],
      "Resource" : "arn:aws:cloudtrail:*:*:channel/aws-service-channel/continuumthreats/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "PutServiceLinkedConfigurationRecorder",
      "Effect" : "Allow",
      "Action" : "config:PutServiceLinkedConfigurationRecorder",
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "config:ConfigurationRecorderServicePrincipal" : "threats.continuum.amazonaws.com"
        }
      }
    },
    {
      "Sid" : "ManageServiceLinkedConfigurationRecorder",
      "Effect" : "Allow",
      "Action" : [
        "config:DeleteServiceLinkedConfigurationRecorder",
        "config:DescribeConfigurationRecorderStatus"
      ],
      "Resource" : "arn:aws:config:*:*:configuration-recorder/AWSConfigurationRecorderFor*/*",
      "Condition" : {
        "StringEquals" : {
          "config:ConfigurationRecorderServicePrincipal" : "threats.continuum.amazonaws.com",
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "CreateConfigServiceLinkedRole",
      "Effect" : "Allow",
      "Action" : "iam:CreateServiceLinkedRole",
      "Resource" : "arn:aws:iam::*:role/aws-service-role/config.amazonaws.com/AWSServiceRoleForConfig",
      "Condition" : {
        "StringEquals" : {
          "iam:AWSServiceName" : "config.amazonaws.com",
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    }
  ]
}
```

## Learn more
<a name="ContinuumThreatsServiceRolePolicy-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)