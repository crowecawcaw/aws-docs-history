# Using attribute-based access control with DynamoDB Streams

DynamoDB Streams supports attribute-based access control (ABAC), the same authorization strategy described in [Using resource-based policies for DynamoDB](attribute-based-access-control.md "attribute-based-access-control.md"). With DynamoDB Streams ABAC, you attach tags to your streams and use tag-based conditions in your IAM policies to control access to them.

Stream resources do not inherit tags from their parent table, and you can manage tags on streams independently. You can add up to 50 tags for each DynamoDB stream. The maximum size supported for all the tags on a stream is 10 KB. For more information about tagging DynamoDB resources and tagging restrictions, see [Adding tags and labels to resources in DynamoDB](Tagging.md "Tagging.md") and [Tagging restrictions in DynamoDB](Tagging.md#TaggingRestrictions "Tagging.md#TaggingRestrictions").

You can use the [aws:ResourceTag](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag") condition key to allow or deny access to a stream based on the tags that are attached to that stream. For example, the following policy allows the `GetRecords` action on any stream that includes the tag key `environment` with the value `production`.

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
          "aws:ResourceTag/environment": "production"
        }
      }
    }
  ]
}
```

###### Topics

- [Condition keys to implement ABAC with DynamoDB Streams](#condition-keys-implement-abac-streams "#condition-keys-implement-abac-streams")
- [Considerations for using ABAC with DynamoDB Streams](#abac-considerations-streams "#abac-considerations-streams")
- [Enabling ABAC for DynamoDB Streams](abac-enable-streams.md "abac-enable-streams.md")
- [Using ABAC with DynamoDB Streams](abac-implementation-streams.md "abac-implementation-streams.md")
- [Examples for using ABAC with DynamoDB Streams](abac-examples-streams.md "abac-examples-streams.md")
- [Troubleshooting common ABAC errors for DynamoDB Streams](abac-troubleshooting-streams.md "abac-troubleshooting-streams.md")

## Condition keys to implement ABAC with DynamoDB Streams

DynamoDB Streams ABAC uses the same condition keys as DynamoDB tables: `aws:ResourceTag/tag-key`, `aws:RequestTag/tag-key`, and `aws:TagKeys`. For a description of each condition key, see [Condition keys to implement ABAC with DynamoDB](attribute-based-access-control.md#condition-keys-implement-abac "attribute-based-access-control.md#condition-keys-implement-abac"). The following behavior is specific to DynamoDB Streams:

- The condition keys apply to the DynamoDB Streams APIs that operate on a stream, including [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md"), `UntagResource`, and read APIs such as `GetRecords`.
- When DynamoDB Streams ABAC is not enabled for your account, `aws:ResourceTag` conditions are evaluated as if no tags are attached to the stream resource.

## Considerations for using ABAC with DynamoDB Streams

When you use ABAC with DynamoDB Streams, the following considerations apply:

- ABAC for DynamoDB Streams is separate from ABAC for DynamoDB tables. Enabling ABAC for tables does not automatically enable it for streams in your account. You must enable each independently.
- You can tag or untag a stream after its parent table is deleted, using the CLI or SDK `tag-resource`, `untag-resource`, and `list-tags-of-resource` commands on the stream ARN. The stream continues to exist for 24 hours after table deletion before being removed. This capability is not available through the Console or CloudFormation after table deletion.
- If you use CloudFormation to manage your DynamoDB resources, make sure your service role has `dynamodb:TagResource`, `dynamodb:UntagResource` and `dynamodb:ListTagsOfResource` permissions for stream resources.
