

# ElementalActivationsGenerateLicenses
<a name="ElementalActivationsGenerateLicenses"></a>

**Description**: Access to view purchased assets and generate software licenses for pending activations

`ElementalActivationsGenerateLicenses` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="ElementalActivationsGenerateLicenses-how-to-use"></a>

You can attach `ElementalActivationsGenerateLicenses` to your users, groups, and roles.

## Policy details
<a name="ElementalActivationsGenerateLicenses-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: August 28, 2020, 18:28 UTC 
+ **Edited time:** August 28, 2020, 18:28 UTC
+ **ARN**: `arn:aws:iam::aws:policy/ElementalActivationsGenerateLicenses`

## Policy version
<a name="ElementalActivationsGenerateLicenses-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="ElementalActivationsGenerateLicenses-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "elemental-activations:Get*",
        "elemental-activations:GenerateLicenses",
        "elemental-activations:StartFileUpload",
        "elemental-activations:CompleteFileUpload"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="ElementalActivationsGenerateLicenses-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)