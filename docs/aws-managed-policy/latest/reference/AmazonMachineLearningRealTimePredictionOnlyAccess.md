

# AmazonMachineLearningRealTimePredictionOnlyAccess
<a name="AmazonMachineLearningRealTimePredictionOnlyAccess"></a>

**Description**: Grants users permission to request Amazon Machine Learning real-time predictions.

`AmazonMachineLearningRealTimePredictionOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonMachineLearningRealTimePredictionOnlyAccess-how-to-use"></a>

You can attach `AmazonMachineLearningRealTimePredictionOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonMachineLearningRealTimePredictionOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: April 09, 2015, 17:44 UTC 
+ **Edited time:** April 09, 2015, 17:44 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonMachineLearningRealTimePredictionOnlyAccess`

## Policy version
<a name="AmazonMachineLearningRealTimePredictionOnlyAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonMachineLearningRealTimePredictionOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "machinelearning:Predict"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonMachineLearningRealTimePredictionOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)