

# AWSElasticDisasterRecoveryCrossAccountReplicationPolicy
<a name="AWSElasticDisasterRecoveryCrossAccountReplicationPolicy"></a>

**Description**: This policy allows AWS Elastic Disaster Recovery (DRS) to support cross-account replication and cross-account failback.

`AWSElasticDisasterRecoveryCrossAccountReplicationPolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSElasticDisasterRecoveryCrossAccountReplicationPolicy-how-to-use"></a>

You can attach `AWSElasticDisasterRecoveryCrossAccountReplicationPolicy` to your users, groups, and roles.

## Policy details
<a name="AWSElasticDisasterRecoveryCrossAccountReplicationPolicy-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: May 14, 2023, 07:16 UTC 
+ **Edited time:** January 17, 2024, 13:19 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AWSElasticDisasterRecoveryCrossAccountReplicationPolicy`

## Policy version
<a name="AWSElasticDisasterRecoveryCrossAccountReplicationPolicy-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSElasticDisasterRecoveryCrossAccountReplicationPolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "CrossAccountPolicy1",
      "Effect" : "Allow",
      "Action" : [
        "ec2:DescribeVolumes",
        "ec2:DescribeVolumeAttribute",
        "ec2:DescribeInstances",
        "drs:DescribeSourceServers",
        "drs:DescribeReplicationConfigurationTemplates",
        "drs:CreateSourceServerForDrs"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "CrossAccountPolicy2",
      "Effect" : "Allow",
      "Action" : [
        "drs:TagResource"
      ],
      "Resource" : "arn:aws:drs:*:*:source-server/*",
      "Condition" : {
        "StringEquals" : {
          "drs:CreateAction" : "CreateSourceServerForDrs"
        }
      }
    }
  ]
}
```

## Learn more
<a name="AWSElasticDisasterRecoveryCrossAccountReplicationPolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)