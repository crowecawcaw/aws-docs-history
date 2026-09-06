

# AWSElasticDisasterRecoveryNetworkReplicationPolicy
<a name="AWSElasticDisasterRecoveryNetworkReplicationPolicy"></a>

**Description**: This policy allows AWS Elastic Disaster Recovery (DRS) to support network replication.

`AWSElasticDisasterRecoveryNetworkReplicationPolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSElasticDisasterRecoveryNetworkReplicationPolicy-how-to-use"></a>

You can attach `AWSElasticDisasterRecoveryNetworkReplicationPolicy` to your users, groups, and roles.

## Policy details
<a name="AWSElasticDisasterRecoveryNetworkReplicationPolicy-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: June 11, 2023, 12:36 UTC 
+ **Edited time:** January 02, 2024, 13:25 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AWSElasticDisasterRecoveryNetworkReplicationPolicy`

## Policy version
<a name="AWSElasticDisasterRecoveryNetworkReplicationPolicy-version"></a>

**Policy version:** v4 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSElasticDisasterRecoveryNetworkReplicationPolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "DRSNetworkReplicationPolicy1",
      "Effect" : "Allow",
      "Action" : [
        "ec2:DescribeVpcAttribute",
        "ec2:DescribeInternetGateways",
        "ec2:DescribeVpcs",
        "ec2:DescribeSubnets",
        "ec2:DescribeNetworkAcls",
        "ec2:DescribeSecurityGroups",
        "ec2:DescribeRouteTables",
        "ec2:DescribeAvailabilityZones",
        "ec2:DescribeDhcpOptions",
        "ec2:DescribeInstances",
        "ec2:DescribeManagedPrefixLists",
        "ec2:GetManagedPrefixListEntries",
        "ec2:GetManagedPrefixListAssociations"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSElasticDisasterRecoveryNetworkReplicationPolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)