

# AmazonNimbleStudio-LaunchProfileWorker
<a name="AmazonNimbleStudio-LaunchProfileWorker"></a>

**Description**: This policy grants access to resources needed by Nimble Studio Launch Profile workers. Attach this policy to EC2 instances created by Nimble Studio Builder.

`AmazonNimbleStudio-LaunchProfileWorker` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonNimbleStudio-LaunchProfileWorker-how-to-use"></a>

You can attach `AmazonNimbleStudio-LaunchProfileWorker` to your users, groups, and roles.

## Policy details
<a name="AmazonNimbleStudio-LaunchProfileWorker-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: April 28, 2021, 04:47 UTC 
+ **Edited time:** April 28, 2021, 04:47 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonNimbleStudio-LaunchProfileWorker`

## Policy version
<a name="AmazonNimbleStudio-LaunchProfileWorker-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonNimbleStudio-LaunchProfileWorker-json"></a>

```
{
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "ec2:DescribeNetworkInterfaces",
        "ec2:DescribeSecurityGroups",
        "fsx:DescribeFileSystems",
        "ds:DescribeDirectories"
      ],
      "Resource" : [
        "*"
      ],
      "Condition" : {
        "StringEquals" : {
          "aws:CalledViaLast" : "nimble.amazonaws.com"
        }
      },
      "Sid" : "GetLaunchProfileInitializationDependencies"
    }
  ],
  "Version" : "2012-10-17"
}
```

## Learn more
<a name="AmazonNimbleStudio-LaunchProfileWorker-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)