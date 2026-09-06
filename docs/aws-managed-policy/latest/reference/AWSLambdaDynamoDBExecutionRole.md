

# AWSLambdaDynamoDBExecutionRole
<a name="AWSLambdaDynamoDBExecutionRole"></a>

**Description**: Provides list and read access to DynamoDB streams and write permissions to CloudWatch logs.

`AWSLambdaDynamoDBExecutionRole` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSLambdaDynamoDBExecutionRole-how-to-use"></a>

You can attach `AWSLambdaDynamoDBExecutionRole` to your users, groups, and roles.

## Policy details
<a name="AWSLambdaDynamoDBExecutionRole-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: April 09, 2015, 15:09 UTC 
+ **Edited time:** April 09, 2015, 15:09 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AWSLambdaDynamoDBExecutionRole`

## Policy version
<a name="AWSLambdaDynamoDBExecutionRole-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSLambdaDynamoDBExecutionRole-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "dynamodb:DescribeStream",
        "dynamodb:GetRecords",
        "dynamodb:GetShardIterator",
        "dynamodb:ListStreams",
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSLambdaDynamoDBExecutionRole-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)