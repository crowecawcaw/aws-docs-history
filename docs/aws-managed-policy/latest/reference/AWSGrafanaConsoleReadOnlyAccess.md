

# AWSGrafanaConsoleReadOnlyAccess
<a name="AWSGrafanaConsoleReadOnlyAccess"></a>

**Description**: Access to read only operations in Amazon Grafana.

`AWSGrafanaConsoleReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSGrafanaConsoleReadOnlyAccess-how-to-use"></a>

You can attach `AWSGrafanaConsoleReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AWSGrafanaConsoleReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: February 23, 2021, 00:10 UTC 
+ **Edited time:** February 15, 2022, 22:30 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSGrafanaConsoleReadOnlyAccess`

## Policy version
<a name="AWSGrafanaConsoleReadOnlyAccess-version"></a>

**Policy version:** v3 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSGrafanaConsoleReadOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AWSGrafanaConsoleReadOnlyAccess",
      "Effect" : "Allow",
      "Action" : [
        "grafana:Describe*",
        "grafana:List*"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSGrafanaConsoleReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)