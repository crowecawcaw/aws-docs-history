# Using ABAC with DynamoDB Streams

The following steps show how to set up permissions using ABAC for DynamoDB Streams. In this example scenario, you add tags to a DynamoDB stream and create an IAM role with a policy that includes tag-based conditions. Then, you test the allowed permissions on the DynamoDB stream by matching the tag conditions.

###### Topics

- [Step 1: Add tags to a DynamoDB stream](#abac-streams-step-1 "#abac-streams-step-1")
- [Step 2: Create an IAM role with a policy including tag-based conditions](#abac-streams-step-2 "#abac-streams-step-2")
- [Step 3: Test allowed permissions](#abac-streams-step-3 "#abac-streams-step-3")

## Step 1: Add tags to a DynamoDB stream

You can add tags to DynamoDB Streams using the AWS CLI or SDK. The following `tag-resource` CLI command adds a tag to a stream.

```
aws dynamodb tag-resource \
  --resource-arn arn:aws:dynamodb:us-east-1:123456789012:table/MusicTable/stream/2024-01-01T00:00:00.000 \
  --tags Key=environment,Value=staging
```

###### Note

To find your stream ARN, use the `describe-table` command and look for the `LatestStreamArn` field in the response.

## Step 2: Create an IAM role with a policy including tag-based conditions

Create an IAM policy using the `aws:ResourceTag/{{tag-key}}` condition key to compare the tag key-value pair that's specified in the IAM policy with the key-value pair that's attached to the stream. The following example policy allows users to get records and describe a stream if the stream contains the tag key-value pair: `"environment": "staging"`. If a stream doesn't have the specified tag key-value pair, these actions are denied.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:DescribeStream",
        "dynamodb:GetRecords",
        "dynamodb:GetShardIterator"
      ],
      "Resource": "arn:aws:dynamodb:*:*:table/*/stream/*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/environment": "staging"
        }
      }
    }
  ]
}
```

## Step 3: Test allowed permissions

1. Attach the IAM policy to a test user or role in your AWS account. Make sure that the IAM principal you use doesn't already have access to the DynamoDB stream through a different policy.
2. Make sure that your DynamoDB stream contains the `"environment"` tag key with a value of `"staging"`.
3. Perform the `dynamodb:DescribeStream` and `dynamodb:GetRecords` actions on the tagged stream. These actions succeed if the `"environment": "staging"` tag key-value pair is present.

If you perform these actions on a stream that doesn't have the `"environment": "staging"` tag key-value pair, your request fails with an `AccessDeniedException`.
