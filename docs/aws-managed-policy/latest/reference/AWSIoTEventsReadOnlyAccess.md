

# AWSIoTEventsReadOnlyAccess
<a name="AWSIoTEventsReadOnlyAccess"></a>

**Description**: Provides read only access to IoT Events.

`AWSIoTEventsReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSIoTEventsReadOnlyAccess-how-to-use"></a>

You can attach `AWSIoTEventsReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AWSIoTEventsReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: January 10, 2019, 22:50 UTC 
+ **Edited time:** September 23, 2019, 17:22 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSIoTEventsReadOnlyAccess`

## Policy version
<a name="AWSIoTEventsReadOnlyAccess-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSIoTEventsReadOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "iotevents:Describe*",
        "iotevents:List*"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSIoTEventsReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)