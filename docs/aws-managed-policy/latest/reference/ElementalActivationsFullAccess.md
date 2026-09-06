

# ElementalActivationsFullAccess
<a name="ElementalActivationsFullAccess"></a>

**Description**: Full access to view and take action on Elemental Appliances and Software purchased assets

`ElementalActivationsFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="ElementalActivationsFullAccess-how-to-use"></a>

You can attach `ElementalActivationsFullAccess` to your users, groups, and roles.

## Policy details
<a name="ElementalActivationsFullAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: June 04, 2020, 21:00 UTC 
+ **Edited time:** June 04, 2020, 21:00 UTC
+ **ARN**: `arn:aws:iam::aws:policy/ElementalActivationsFullAccess`

## Policy version
<a name="ElementalActivationsFullAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="ElementalActivationsFullAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "elemental-activations:*"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="ElementalActivationsFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)