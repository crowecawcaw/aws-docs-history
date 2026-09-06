

# CloudWatch-CrossAccountAccess
<a name="CloudWatch-CrossAccountAccess"></a>

**Description**: Allows CloudWatch to assume CloudWatch-CrossAccountSharing roles in remote accounts on behalf of the current account in order to display data cross-account, cross-region

`CloudWatch-CrossAccountAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="CloudWatch-CrossAccountAccess-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="CloudWatch-CrossAccountAccess-details"></a>
+ **Type**: Service-linked role policy 
+ **Creation time**: July 23, 2019, 09:59 UTC 
+ **Edited time:** July 23, 2019, 09:59 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/CloudWatch-CrossAccountAccess`

## Policy version
<a name="CloudWatch-CrossAccountAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="CloudWatch-CrossAccountAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Action" : [
        "sts:AssumeRole"
      ],
      "Resource" : [
        "arn:aws:iam::*:role/CloudWatch-CrossAccountSharing*"
      ],
      "Effect" : "Allow"
    }
  ]
}
```

## Learn more
<a name="CloudWatch-CrossAccountAccess-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)