

# AmazonMachineLearningCreateOnlyAccess
<a name="AmazonMachineLearningCreateOnlyAccess"></a>

**Description**: Provides create access for non-prediction Amazon Machine Learning resources.

`AmazonMachineLearningCreateOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonMachineLearningCreateOnlyAccess-how-to-use"></a>

You can attach `AmazonMachineLearningCreateOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonMachineLearningCreateOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: April 09, 2015, 17:18 UTC 
+ **Edited time:** June 29, 2016, 20:55 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonMachineLearningCreateOnlyAccess`

## Policy version
<a name="AmazonMachineLearningCreateOnlyAccess-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonMachineLearningCreateOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "machinelearning:Add*",
        "machinelearning:Create*",
        "machinelearning:Delete*",
        "machinelearning:Describe*",
        "machinelearning:Get*"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonMachineLearningCreateOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)