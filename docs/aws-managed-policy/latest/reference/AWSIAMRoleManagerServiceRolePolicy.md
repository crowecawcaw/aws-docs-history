

# AWSIAMRoleManagerServiceRolePolicy
<a name="AWSIAMRoleManagerServiceRolePolicy"></a>

**Description**: Allows IAM Role Manager to manage resources in your account on your behalf.

`AWSIAMRoleManagerServiceRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSIAMRoleManagerServiceRolePolicy-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="AWSIAMRoleManagerServiceRolePolicy-details"></a>
+ **Type**: Service-linked role policy 
+ **Creation time**: July 15, 2026, 23:57 UTC 
+ **Edited time:** August 05, 2026, 19:42 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/AWSIAMRoleManagerServiceRolePolicy`

## Policy version
<a name="AWSIAMRoleManagerServiceRolePolicy-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSIAMRoleManagerServiceRolePolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "ManageServiceLinkedAnalyzer",
      "Effect" : "Allow",
      "Action" : [
        "access-analyzer:CreateServiceLinkedAnalyzer",
        "access-analyzer:DeleteServiceLinkedAnalyzer"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "CreateAccessAnalyzerServiceLinkedRole",
      "Effect" : "Allow",
      "Action" : "iam:CreateServiceLinkedRole",
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "iam:AWSServiceName" : "access-analyzer.amazonaws.com"
        }
      }
    }
  ]
}
```

## Learn more
<a name="AWSIAMRoleManagerServiceRolePolicy-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)