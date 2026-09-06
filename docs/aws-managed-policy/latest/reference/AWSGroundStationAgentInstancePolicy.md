

# AWSGroundStationAgentInstancePolicy
<a name="AWSGroundStationAgentInstancePolicy"></a>

**Description**: Provides the Dataflow Endpoint Instance permissions to use the AWS Ground Station Agent

`AWSGroundStationAgentInstancePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSGroundStationAgentInstancePolicy-how-to-use"></a>

You can attach `AWSGroundStationAgentInstancePolicy` to your users, groups, and roles.

## Policy details
<a name="AWSGroundStationAgentInstancePolicy-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: March 29, 2023, 15:23 UTC 
+ **Edited time:** February 12, 2026, 18:02 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSGroundStationAgentInstancePolicy`

## Policy version
<a name="AWSGroundStationAgentInstancePolicy-version"></a>

**Policy version:** v4 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSGroundStationAgentInstancePolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "groundstation:RegisterAgent",
        "groundstation:UpdateAgentStatus",
        "groundstation:GetAgentConfiguration",
        "groundstation:GetAgentTaskResponseUrl"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSGroundStationAgentInstancePolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)