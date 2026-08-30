# Granting Lambda function access to AWS services

When you [use an AWS service to invoke your function](lambda-services.md "lambda-services.md"), you grant
permission in a statement on a resource-based policy. You can apply the statement to the entire function, or limit the statement to a single version or alias.

###### Note

When you add a trigger to your function with the Lambda console, the console updates the function's
resource-based policy to allow the service to invoke it. To grant permissions to other accounts or services that
aren't available in the Lambda console, you can use the AWS CLI.

We recommend using `put-resource-policy` to define a full JSON policy. With `put-resource-policy`, you can add deny statements,
use the full range of IAM condition keys, and manage all permissions in a single document.
You can also use `add-permission` to add individual statements for simple use cases.

###### Important

Using `put-resource-policy` replaces any existing resource-based policy on the resource. If the resource
already has permissions defined with `add-permission`, `put-resource-policy` overwrites them.
Use `get-resource-policy` to retrieve the existing policy before making changes.

## Using a full JSON policy (recommended)

The following example policy grants Amazon Simple Notification Service permission to invoke a function named `my-function`,
but only for a specific topic. It also denies invocations from a particular topic.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "allow-sns-my-topic",
            "Effect": "Allow",
            "Principal": {
                "Service": "sns.amazonaws.com"
            },
            "Action": "lambda:InvokeFunction",
            "Resource": "arn:aws:lambda:us-east-2:123456789012:function:my-function",
            "Condition": {
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:sns:us-east-2:123456789012:my-topic"
                }
            }
        },
        {
            "Sid": "deny-sns-other-topic",
            "Effect": "Deny",
            "Principal": {
                "Service": "sns.amazonaws.com"
            },
            "Action": "lambda:InvokeFunction",
            "Resource": [
                "arn:aws:lambda:us-east-2:123456789012:function:my-function",
                "arn:aws:lambda:us-east-2:123456789012:function:my-function:*"
            ],
            "Condition": {
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:sns:us-east-2:123456789012:restricted-topic"
                }
            }
        }
    ]
}
```

Save the policy to a file named `policy.json` and apply it with `put-resource-policy`:

```
`aws lambda put-resource-policy \
 --resource-arn arn:aws:lambda:`us-east-2`:`123456789012`:function:`my-function` \
 --policy file://policy.json`
```

For Amazon S3, the source is a bucket whose ARN doesn't include an account ID. It's possible that you could delete a bucket and
another account could create a bucket with the same name. Use the `aws:SourceAccount` condition key to ensure that
only resources in your account can invoke the function:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "allow-s3",
            "Effect": "Allow",
            "Principal": {
                "Service": "s3.amazonaws.com"
            },
            "Action": "lambda:InvokeFunction",
            "Resource": "arn:aws:lambda:us-east-2:123456789012:function:my-function",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "123456789012"
                },
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:s3:::my-bucket"
                }
            }
        }
    ]
}
```

## Using add-permission

For simple use cases, you can use `add-permission` to add individual statements. The following command grants
Amazon Simple Notification Service permission to invoke a function named `my-function`:

```
`aws lambda add-permission \
 --function-name my-function \
 --action lambda:InvokeFunction \
 --statement-id sns \
 --principal sns.amazonaws.com \
 --output text`
```

You should see the following output:

```
{"Sid":"sns","Effect":"Allow","Principal":{"Service":"sns.amazonaws.com"},"Action":"lambda:InvokeFunction","Resource":"arn:aws:lambda:us-east-2:123456789012:function:my-function"}
```

###### Note

If you call `add-permission` after `put-resource-policy`, the new statement appends to the existing JSON policy.

To restrict invocations to a specific resource, use the `source-arn` option:

```
`aws lambda add-permission \
 --function-name my-function \
 --action lambda:InvokeFunction \
 --statement-id sns-my-topic \
 --principal sns.amazonaws.com \
 --source-arn arn:aws:sns:`us-east-2:123456789012:my-topic``
```

For Amazon S3, use the `source-account` option with your account ID:

```
`aws lambda add-permission \
 --function-name my-function \
 --action lambda:InvokeFunction \
 --statement-id s3-account \
 --principal s3.amazonaws.com \
 --source-arn arn:aws:s3:::`amzn-s3-demo-bucket` \
 --source-account `123456789012``
```
