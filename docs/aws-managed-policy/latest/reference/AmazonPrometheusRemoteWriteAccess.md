

# AmazonPrometheusRemoteWriteAccess
<a name="AmazonPrometheusRemoteWriteAccess"></a>

**Description**: Grants write only access to AWS Managed Prometheus workspaces

`AmazonPrometheusRemoteWriteAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonPrometheusRemoteWriteAccess-how-to-use"></a>

You can attach `AmazonPrometheusRemoteWriteAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonPrometheusRemoteWriteAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: December 19, 2020, 01:04 UTC 
+ **Edited time:** December 19, 2020, 01:04 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonPrometheusRemoteWriteAccess`

## Policy version
<a name="AmazonPrometheusRemoteWriteAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonPrometheusRemoteWriteAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Action" : [
        "aps:RemoteWrite"
      ],
      "Effect" : "Allow",
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonPrometheusRemoteWriteAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)