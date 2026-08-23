# Example 1: Allow stream read access using aws:ResourceTag

Using the `aws:ResourceTag/tag-key` condition key, you can compare the tag key-value pair specified in an IAM policy with the key-value pair attached to a DynamoDB stream. For example, you can allow stream `GetRecords` operations if the tag conditions match.

## Using the AWS CLI

1. Create a table with a stream enabled and add a tag.

```
aws dynamodb create-table \
  --table-name myMusicTable \
  --attribute-definitions AttributeName=id,AttributeType=S \
  --key-schema AttributeName=id,KeyType=HASH \
  --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
  --stream-specification StreamEnabled=true,StreamViewType=NEW_AND_OLD_IMAGES \
  --region us-east-1
```

2. Add a tag to the stream. First, get the stream ARN from the table description.

```
STREAM_ARN=$(aws dynamodb describe-table \
  --table-name myMusicTable \
  --query "Table.LatestStreamArn" \
  --output text \
  --region us-east-1)

aws dynamodb tag-resource \
  --resource-arn $STREAM_ARN \
  --tags Key=Team,Value=Analytics \
  --region us-east-1
```

3. Create an [inline policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#inline-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#inline-policies") and add it to a role, as shown in the following example.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:DescribeStream",
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

This policy allows the `DescribeStream` and `GetRecords` operations when the stream's tag matches the key "Team" and value "Analytics" specified in the policy. 4. Assume the role with the policy described in Step 3. 5. Use the `describe-stream` AWS CLI command on the stream.

```
aws dynamodb describe-stream \
  --stream-arn $STREAM_ARN \
  --region us-east-1
```

## Behavior with and without Streams ABAC

Without Streams ABAC

If Streams ABAC isn't enabled for your AWS account, the tag conditions in the IAM policy and the DynamoDB stream aren't matched. The `DescribeStream` action returns an `AccessDeniedException` because no policy allows the action without matching tag conditions.

With Streams ABAC

If Streams ABAC is enabled for your AWS account, the `DescribeStream` action completes successfully. This is because the inline policy allows the action when the tag conditions in the IAM policy and the stream match.
