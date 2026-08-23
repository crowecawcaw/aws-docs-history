# Example 2: Allow tagging a stream using aws:RequestTag

Using the `aws:RequestTag/tag-key` condition key, you can compare the tag key-value pair that's passed in your request with the tag pair specified in the IAM policy. For example, you can allow tagging a stream only if the request includes a specific tag.

## Using the AWS CLI

1. Create an [inline policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#inline-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#inline-policies") and add it to a role, as shown in the following example.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:TagResource"
      ],
      "Resource": "arn:aws:dynamodb:*:*:table/*/stream/*",
      "Condition": {
        "StringEquals": {
          "aws:RequestTag/CostCenter": "12345"
        }
      }
    }
  ]
}
```

2. Tag the stream with the required tag key-value pair.

```
aws dynamodb tag-resource \
  --resource-arn arn:aws:dynamodb:us-east-1:123456789012:table/myMusicTable/stream/2024-01-01T00:00:00.000 \
  --tags Key=CostCenter,Value=12345
```

## Behavior with and without Streams ABAC

Without Streams ABAC

If Streams ABAC isn't enabled for your AWS account, the tag conditions in the inline policy and the request aren't matched. The `TagResource` action returns an `AccessDeniedException`.

With Streams ABAC

If Streams ABAC is enabled for your AWS account, the tag request completes successfully. Because the tag key-value pair of `"CostCenter": "12345"` is present in the `TagResource` request, the inline policy allows the action.
