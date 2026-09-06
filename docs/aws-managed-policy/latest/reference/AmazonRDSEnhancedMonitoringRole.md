

# AmazonRDSEnhancedMonitoringRole
<a name="AmazonRDSEnhancedMonitoringRole"></a>

**Description**: Provides access to Cloudwatch for RDS Enhanced Monitoring

`AmazonRDSEnhancedMonitoringRole` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonRDSEnhancedMonitoringRole-how-to-use"></a>

You can attach `AmazonRDSEnhancedMonitoringRole` to your users, groups, and roles.

## Policy details
<a name="AmazonRDSEnhancedMonitoringRole-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: November 11, 2015, 19:58 UTC 
+ **Edited time:** November 11, 2015, 19:58 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AmazonRDSEnhancedMonitoringRole`

## Policy version
<a name="AmazonRDSEnhancedMonitoringRole-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonRDSEnhancedMonitoringRole-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "EnableCreationAndManagementOfRDSCloudwatchLogGroups",
      "Effect" : "Allow",
      "Action" : [
        "logs:CreateLogGroup",
        "logs:PutRetentionPolicy"
      ],
      "Resource" : [
        "arn:aws:logs:*:*:log-group:RDS*"
      ]
    },
    {
      "Sid" : "EnableCreationAndManagementOfRDSCloudwatchLogStreams",
      "Effect" : "Allow",
      "Action" : [
        "logs:CreateLogStream",
        "logs:PutLogEvents",
        "logs:DescribeLogStreams",
        "logs:GetLogEvents"
      ],
      "Resource" : [
        "arn:aws:logs:*:*:log-group:RDS*:log-stream:*"
      ]
    }
  ]
}
```

## Learn more
<a name="AmazonRDSEnhancedMonitoringRole-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)