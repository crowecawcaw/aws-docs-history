

# AWSApplicationDiscoveryAgentlessCollectorAccess
<a name="AWSApplicationDiscoveryAgentlessCollectorAccess"></a>

**Description**: Allows Application Discovery Service Agentless Collectors to auto update, register, and communicate with Application Discovery Service

`AWSApplicationDiscoveryAgentlessCollectorAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSApplicationDiscoveryAgentlessCollectorAccess-how-to-use"></a>

You can attach `AWSApplicationDiscoveryAgentlessCollectorAccess` to your users, groups, and roles.

## Policy details
<a name="AWSApplicationDiscoveryAgentlessCollectorAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: August 16, 2022, 21:00 UTC 
+ **Edited time:** August 16, 2022, 21:00 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSApplicationDiscoveryAgentlessCollectorAccess`

## Policy version
<a name="AWSApplicationDiscoveryAgentlessCollectorAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSApplicationDiscoveryAgentlessCollectorAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "arsenal:RegisterOnPremisesAgent"
      ],
      "Resource" : "*"
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "ecr-public:DescribeImages"
      ],
      "Resource" : "arn:aws:ecr-public::446372222237:repository/6e5498e4-8c31-4f57-9991-13b4b992ff7b"
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "ecr-public:GetAuthorizationToken"
      ],
      "Resource" : "*"
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "mgh:GetHomeRegion"
      ],
      "Resource" : "*"
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "sts:GetServiceBearerToken"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSApplicationDiscoveryAgentlessCollectorAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)