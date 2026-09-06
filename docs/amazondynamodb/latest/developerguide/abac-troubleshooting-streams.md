

# Troubleshooting common ABAC errors for DynamoDB Streams
<a name="abac-troubleshooting-streams"></a>

If you receive an `AccessDeniedException` or your tag-based conditions don't behave as expected after you enable ABAC for DynamoDB Streams, use this topic to diagnose and resolve the most common causes.

## Service-specific condition keys in policies result in an error
<a name="abac-troubleshooting-streams-service-specific-keys"></a>

Service-specific condition keys aren't considered as valid condition keys. If you've used such keys in your policies, these keys result in an error. You must replace the service-specific condition keys with an appropriate condition key to implement ABAC for DynamoDB Streams.

For example, say that you've used the `dynamodb:ResourceTag` condition key in a policy that performs the `GetRecords` request on a stream. The request fails with an `AccessDeniedException`. The following example shows the erroneous policy with the `dynamodb:ResourceTag` condition key.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:GetRecords"
      ],
      "Resource": "arn:aws:dynamodb:*:*:table/*/stream/*",
      "Condition": {
        "StringEquals": {
          "dynamodb:ResourceTag/Team": "Analytics"
        }
      }
    }
  ]
}
```

To fix this issue, replace the `dynamodb:ResourceTag` condition key with `aws:ResourceTag`, as shown in the following example.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:GetRecords"
      ],
      "Resource": "arn:aws:dynamodb:*:*:table/*/stream/*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/Team": "Analytics"
        }
      }
    }
  ]
}
```

## Streams ABAC is enabled but tag conditions are not evaluated
<a name="abac-troubleshooting-streams-not-evaluated"></a>

If you recently enabled Streams ABAC, the change might not have propagated yet. Updating the status of Streams ABAC is an asynchronous operation. Wait a few minutes and retry your request.

## Unable to tag a stream after parent table is deleted
<a name="abac-troubleshooting-streams-tag-deleted-table"></a>

After a parent table is deleted, the stream continues to exist for 24 hours before being removed. During this 24-hour window, you can manage stream tags using the CLI or SDK commands (`tag-resource`, `untag-resource`, and `list-tags-of-resource`) with the stream ARN. You can't use the console or CloudFormation to modify tags on a stream whose parent table no longer exists.

If you receive an error when attempting to tag through the console, use the CLI instead:

```
aws dynamodb tag-resource \
  --resource-arn arn:aws:dynamodb:us-east-1:123456789012:table/DeletedTable/stream/2024-01-01T00:00:00.000 \
  --tags Key=environment,Value=production
```

To verify existing tags on the stream with parent table deleted:

```
aws dynamodb list-tags-of-resource \
  --resource-arn arn:aws:dynamodb:us-east-1:123456789012:table/DeletedTable/stream/2024-01-01T00:00:00.000
```

If you receive a `ResourceNotFoundException`, the 24-hour retention period has expired and the stream no longer exists.

## Unable to opt out of Streams ABAC
<a name="abac-troubleshooting-streams-unable-opt-out"></a>

You can opt out of Streams ABAC yourself only if the following are true:
+ You used the self-service way of opting in through the DynamoDB console.
+ You're opting out within seven calendar days of opting in.

If Streams ABAC was enabled for your account through Support, you won't be able to opt out through the DynamoDB console. To opt out, contact Support.

## CloudFormation deployments fail when tagging streams
<a name="abac-troubleshooting-streams-cfn-tagging"></a>

CloudFormation deployments that create or update a table with a stream might fail if the IAM role is missing required permissions. Specifically, the role must have `dynamodb:TagResource` and `dynamodb:UntagResource` permissions for stream resources. This applies to both `AWS::DynamoDB::Table` and `AWS::DynamoDB::GlobalTable` resource types, and affects both explicit stream tags and inherited stack-level tags.

To resolve this, update your CloudFormation service role's IAM policy to include stream tagging permissions:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:TagResource",
        "dynamodb:UntagResource"
      ],
      "Resource": [
        "arn:aws:dynamodb:*:*:table/*/stream/*"
      ]
    }
  ]
}
```