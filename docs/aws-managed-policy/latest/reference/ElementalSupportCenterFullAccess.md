

# ElementalSupportCenterFullAccess
<a name="ElementalSupportCenterFullAccess"></a>

**Description**: Full access to view and take action on Elemental Appliance and Software support cases and product support content

`ElementalSupportCenterFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="ElementalSupportCenterFullAccess-how-to-use"></a>

You can attach `ElementalSupportCenterFullAccess` to your users, groups, and roles.

## Policy details
<a name="ElementalSupportCenterFullAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 25, 2020, 18:08 UTC 
+ **Edited time:** February 05, 2021, 21:02 UTC
+ **ARN**: `arn:aws:iam::aws:policy/ElementalSupportCenterFullAccess`

## Policy version
<a name="ElementalSupportCenterFullAccess-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="ElementalSupportCenterFullAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "elemental-support-cases:*",
        "elemental-support-content:*",
        "elemental-activations:CompleteAccountRegistration"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="ElementalSupportCenterFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)