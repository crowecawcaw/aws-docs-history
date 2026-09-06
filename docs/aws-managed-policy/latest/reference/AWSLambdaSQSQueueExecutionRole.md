

# AWSLambdaSQSQueueExecutionRole
<a name="AWSLambdaSQSQueueExecutionRole"></a>

**Description**: Provides receive message, delete message, and read attribute access to SQS queues, and write permissions to CloudWatch logs.

`AWSLambdaSQSQueueExecutionRole` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSLambdaSQSQueueExecutionRole-how-to-use"></a>

You can attach `AWSLambdaSQSQueueExecutionRole` to your users, groups, and roles.

## Policy details
<a name="AWSLambdaSQSQueueExecutionRole-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: June 14, 2018, 21:50 UTC 
+ **Edited time:** June 14, 2018, 21:50 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AWSLambdaSQSQueueExecutionRole`

## Policy version
<a name="AWSLambdaSQSQueueExecutionRole-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSLambdaSQSQueueExecutionRole-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "sqs:ReceiveMessage",
        "sqs:DeleteMessage",
        "sqs:GetQueueAttributes",
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
<a name="AWSLambdaSQSQueueExecutionRole-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)