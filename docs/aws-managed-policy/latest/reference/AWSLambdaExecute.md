

# AWSLambdaExecute
<a name="AWSLambdaExecute"></a>

**Important**  
The `AWSLambdaExecute` managed policy is on the path to deprecation, and no longer recommended for use with AWS Lambda. Instead, use [`AWSLambdaBasicExecutionRole`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaBasicExecutionRole.html). When the IAM service eventually deprecates the policy, you won't be able to attach it to a role. However, you can attach an existing role to a resource even if that role uses the deprecated policy.

**Description**: Provides Put, Get access to S3 and full access to CloudWatch Logs.

`AWSLambdaExecute` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSLambdaExecute-how-to-use"></a>

You can attach `AWSLambdaExecute` to your users, groups, and roles.

## Policy details
<a name="AWSLambdaExecute-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: February 06, 2015, 18:40 UTC 
+ **Edited time:** February 06, 2015, 18:40 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSLambdaExecute`

## Policy version
<a name="AWSLambdaExecute-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSLambdaExecute-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "logs:*"
      ],
      "Resource" : "arn:aws:logs:*:*:*"
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource" : "arn:aws:s3:::*"
    }
  ]
}
```

## Learn more
<a name="AWSLambdaExecute-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)