

# AmazonRoute53RecoveryClusterReadOnlyAccess
<a name="AmazonRoute53RecoveryClusterReadOnlyAccess"></a>

**Description**: Provides read only access to Amazon Route 53 Recovery Cluster

`AmazonRoute53RecoveryClusterReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonRoute53RecoveryClusterReadOnlyAccess-how-to-use"></a>

You can attach `AmazonRoute53RecoveryClusterReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonRoute53RecoveryClusterReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: August 18, 2021, 17:36 UTC 
+ **Edited time:** April 01, 2022, 17:37 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonRoute53RecoveryClusterReadOnlyAccess`

## Policy version
<a name="AmazonRoute53RecoveryClusterReadOnlyAccess-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonRoute53RecoveryClusterReadOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "route53-recovery-cluster:GetRoutingControlState",
        "route53-recovery-cluster:ListRoutingControls"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonRoute53RecoveryClusterReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)