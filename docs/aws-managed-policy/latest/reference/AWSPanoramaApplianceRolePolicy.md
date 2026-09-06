

# AWSPanoramaApplianceRolePolicy
<a name="AWSPanoramaApplianceRolePolicy"></a>

**Description**: Allows AWS IoT software on an AWS Panorama Appliance to upload logs to Amazon CloudWatch.

`AWSPanoramaApplianceRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSPanoramaApplianceRolePolicy-how-to-use"></a>

You can attach `AWSPanoramaApplianceRolePolicy` to your users, groups, and roles.

## Policy details
<a name="AWSPanoramaApplianceRolePolicy-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: December 01, 2020, 13:13 UTC 
+ **Edited time:** December 01, 2020, 13:13 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AWSPanoramaApplianceRolePolicy`

## Policy version
<a name="AWSPanoramaApplianceRolePolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSPanoramaApplianceRolePolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "PanoramaDeviceCreateLogStream",
      "Effect" : "Allow",
      "Action" : [
        "logs:CreateLogStream",
        "logs:DescribeLogStreams",
        "logs:PutLogEvents"
      ],
      "Resource" : "arn:aws:logs:*:*:log-group:/aws/panorama_device*:log-stream:*"
    },
    {
      "Sid" : "PanoramaDeviceCreateLogGroup",
      "Effect" : "Allow",
      "Action" : "logs:CreateLogGroup",
      "Resource" : "arn:aws:logs:*:*:log-group:/aws/panorama_device*"
    }
  ]
}
```

## Learn more
<a name="AWSPanoramaApplianceRolePolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)