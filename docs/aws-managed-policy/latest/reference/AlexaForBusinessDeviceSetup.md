

# AlexaForBusinessDeviceSetup
<a name="AlexaForBusinessDeviceSetup"></a>

**Description**: Provide device setup access to AlexaForBusiness services

`AlexaForBusinessDeviceSetup` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AlexaForBusinessDeviceSetup-how-to-use"></a>

You can attach `AlexaForBusinessDeviceSetup` to your users, groups, and roles.

## Policy details
<a name="AlexaForBusinessDeviceSetup-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 30, 2017, 16:47 UTC 
+ **Edited time:** May 20, 2019, 21:05 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AlexaForBusinessDeviceSetup`

## Policy version
<a name="AlexaForBusinessDeviceSetup-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AlexaForBusinessDeviceSetup-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "a4b:RegisterDevice",
        "a4b:CompleteRegistration",
        "a4b:SearchDevices",
        "a4b:SearchNetworkProfiles",
        "a4b:GetNetworkProfile",
        "a4b:PutDeviceSetupEvents"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "A4bDeviceSetupAccess",
      "Effect" : "Allow",
      "Action" : [
        "secretsmanager:GetSecretValue"
      ],
      "Resource" : "arn:aws:secretsmanager:*:*:secret:A4BNetworkProfile*"
    }
  ]
}
```

## Learn more
<a name="AlexaForBusinessDeviceSetup-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)