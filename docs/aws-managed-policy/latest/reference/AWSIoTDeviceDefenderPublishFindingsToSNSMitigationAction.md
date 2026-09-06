

# AWSIoTDeviceDefenderPublishFindingsToSNSMitigationAction
<a name="AWSIoTDeviceDefenderPublishFindingsToSNSMitigationAction"></a>

**Description**: Provides messages publish access to SNS topic for execution of PUBLISH\_FINDING\_TO\_SNS mitigation action

`AWSIoTDeviceDefenderPublishFindingsToSNSMitigationAction` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSIoTDeviceDefenderPublishFindingsToSNSMitigationAction-how-to-use"></a>

You can attach `AWSIoTDeviceDefenderPublishFindingsToSNSMitigationAction` to your users, groups, and roles.

## Policy details
<a name="AWSIoTDeviceDefenderPublishFindingsToSNSMitigationAction-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: August 07, 2019, 17:04 UTC 
+ **Edited time:** August 07, 2019, 17:04 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AWSIoTDeviceDefenderPublishFindingsToSNSMitigationAction`

## Policy version
<a name="AWSIoTDeviceDefenderPublishFindingsToSNSMitigationAction-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSIoTDeviceDefenderPublishFindingsToSNSMitigationAction-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "sns:Publish"
      ],
      "Resource" : [
        "*"
      ]
    }
  ]
}
```

## Learn more
<a name="AWSIoTDeviceDefenderPublishFindingsToSNSMitigationAction-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)