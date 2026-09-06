

# AWSApplicationAutoscalingEC2SpotFleetRequestPolicy
<a name="AWSApplicationAutoscalingEC2SpotFleetRequestPolicy"></a>

**Description**: Policy granting permissions to Application Auto Scaling to access EC2 Spot Fleet and CloudWatch.

`AWSApplicationAutoscalingEC2SpotFleetRequestPolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSApplicationAutoscalingEC2SpotFleetRequestPolicy-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="AWSApplicationAutoscalingEC2SpotFleetRequestPolicy-details"></a>
+ **Type**: Service-linked role policy 
+ **Creation time**: October 25, 2017, 18:23 UTC 
+ **Edited time:** October 25, 2017, 18:23 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/AWSApplicationAutoscalingEC2SpotFleetRequestPolicy`

## Policy version
<a name="AWSApplicationAutoscalingEC2SpotFleetRequestPolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSApplicationAutoscalingEC2SpotFleetRequestPolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "ec2:DescribeSpotFleetRequests",
        "ec2:ModifySpotFleetRequest",
        "cloudwatch:PutMetricAlarm",
        "cloudwatch:DescribeAlarms",
        "cloudwatch:DeleteAlarms"
      ],
      "Resource" : [
        "*"
      ]
    }
  ]
}
```

## Learn more
<a name="AWSApplicationAutoscalingEC2SpotFleetRequestPolicy-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)