

# AWSCloud9SSMInstanceProfile
<a name="AWSCloud9SSMInstanceProfile"></a>

**Description**: This policy will be used to attach a role on a InstanceProfile which will allow Cloud9 to use the SSM Session Manager to connect to the instance

`AWSCloud9SSMInstanceProfile` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSCloud9SSMInstanceProfile-how-to-use"></a>

You can attach `AWSCloud9SSMInstanceProfile` to your users, groups, and roles.

## Policy details
<a name="AWSCloud9SSMInstanceProfile-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: May 14, 2020, 11:40 UTC 
+ **Edited time:** May 14, 2020, 11:40 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSCloud9SSMInstanceProfile`

## Policy version
<a name="AWSCloud9SSMInstanceProfile-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSCloud9SSMInstanceProfile-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "ssmmessages:CreateControlChannel",
        "ssmmessages:CreateDataChannel",
        "ssmmessages:OpenControlChannel",
        "ssmmessages:OpenDataChannel",
        "ssm:UpdateInstanceInformation"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSCloud9SSMInstanceProfile-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)