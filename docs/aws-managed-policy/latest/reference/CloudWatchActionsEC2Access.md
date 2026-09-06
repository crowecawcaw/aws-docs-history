

# CloudWatchActionsEC2Access
<a name="CloudWatchActionsEC2Access"></a>

**Description**: Provides read-only access to CloudWatch alarms and metrics as well as EC2 metadata. Provides access to Stop, Terminate and Reboot EC2 instances.

`CloudWatchActionsEC2Access` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="CloudWatchActionsEC2Access-how-to-use"></a>

You can attach `CloudWatchActionsEC2Access` to your users, groups, and roles.

## Policy details
<a name="CloudWatchActionsEC2Access-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: July 07, 2015, 00:00 UTC 
+ **Edited time:** July 07, 2015, 00:00 UTC
+ **ARN**: `arn:aws:iam::aws:policy/CloudWatchActionsEC2Access`

## Policy version
<a name="CloudWatchActionsEC2Access-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="CloudWatchActionsEC2Access-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "cloudwatch:Describe*",
        "ec2:Describe*",
        "ec2:RebootInstances",
        "ec2:StopInstances",
        "ec2:TerminateInstances"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="CloudWatchActionsEC2Access-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)