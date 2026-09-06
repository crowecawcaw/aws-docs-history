

# Ec2ImageBuilderCrossAccountDistributionAccess
<a name="Ec2ImageBuilderCrossAccountDistributionAccess"></a>

**Description**: Permissions need by EC2 Image Builder to perform a cross account distribution.

`Ec2ImageBuilderCrossAccountDistributionAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="Ec2ImageBuilderCrossAccountDistributionAccess-how-to-use"></a>

You can attach `Ec2ImageBuilderCrossAccountDistributionAccess` to your users, groups, and roles.

## Policy details
<a name="Ec2ImageBuilderCrossAccountDistributionAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: September 30, 2020, 19:22 UTC 
+ **Edited time:** September 30, 2020, 19:22 UTC
+ **ARN**: `arn:aws:iam::aws:policy/Ec2ImageBuilderCrossAccountDistributionAccess`

## Policy version
<a name="Ec2ImageBuilderCrossAccountDistributionAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="Ec2ImageBuilderCrossAccountDistributionAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : "ec2:CreateTags",
      "Resource" : "arn:aws:ec2:*::image/*"
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "ec2:DescribeImages",
        "ec2:CopyImage",
        "ec2:ModifyImageAttribute"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="Ec2ImageBuilderCrossAccountDistributionAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)