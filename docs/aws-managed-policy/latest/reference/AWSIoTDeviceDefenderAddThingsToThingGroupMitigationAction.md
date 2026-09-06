

# AWSIoTDeviceDefenderAddThingsToThingGroupMitigationAction
<a name="AWSIoTDeviceDefenderAddThingsToThingGroupMitigationAction"></a>

**Description**: Provides write access to IoT thing groups and read access to IoT Certificates for execution of ADD\_THINGS\_TO\_THING\_GROUP mitigation action

`AWSIoTDeviceDefenderAddThingsToThingGroupMitigationAction` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSIoTDeviceDefenderAddThingsToThingGroupMitigationAction-how-to-use"></a>

You can attach `AWSIoTDeviceDefenderAddThingsToThingGroupMitigationAction` to your users, groups, and roles.

## Policy details
<a name="AWSIoTDeviceDefenderAddThingsToThingGroupMitigationAction-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: August 07, 2019, 17:55 UTC 
+ **Edited time:** August 07, 2019, 17:55 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AWSIoTDeviceDefenderAddThingsToThingGroupMitigationAction`

## Policy version
<a name="AWSIoTDeviceDefenderAddThingsToThingGroupMitigationAction-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSIoTDeviceDefenderAddThingsToThingGroupMitigationAction-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "iot:ListPrincipalThings",
        "iot:AddThingToThingGroup"
      ],
      "Resource" : [
        "*"
      ]
    }
  ]
}
```

## Learn more
<a name="AWSIoTDeviceDefenderAddThingsToThingGroupMitigationAction-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)