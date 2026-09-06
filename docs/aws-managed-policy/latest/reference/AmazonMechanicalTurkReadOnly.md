

# AmazonMechanicalTurkReadOnly
<a name="AmazonMechanicalTurkReadOnly"></a>

**Description**: Provides access to read only APIs in Amazon Mechanical Turk.

`AmazonMechanicalTurkReadOnly` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonMechanicalTurkReadOnly-how-to-use"></a>

You can attach `AmazonMechanicalTurkReadOnly` to your users, groups, and roles.

## Policy details
<a name="AmazonMechanicalTurkReadOnly-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: December 11, 2015, 19:08 UTC 
+ **Edited time:** September 25, 2019, 21:06 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonMechanicalTurkReadOnly`

## Policy version
<a name="AmazonMechanicalTurkReadOnly-version"></a>

**Policy version:** v3 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonMechanicalTurkReadOnly-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "mechanicalturk:Get*",
        "mechanicalturk:List*"
      ],
      "Resource" : [
        "*"
      ]
    }
  ]
}
```

## Learn more
<a name="AmazonMechanicalTurkReadOnly-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)