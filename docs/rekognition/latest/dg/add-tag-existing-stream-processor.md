# Add tags to an existing stream processor

###### Note

Amazon Rekognition Streaming Video Analysis will no longer be
open to new customers starting April 30, 2026. If you would like to use Streaming Video Analysis, sign up prior to
that date. Existing customers for accounts that have used this feature within the last 12 months can continue
to use the service as normal. For more information, see
[Rekognition Streaming Video Analysis availability change](rekognition-streaming-video-analysis-availability-change.md "rekognition-streaming-video-analysis-availability-change.md").

You can identify, organize, search for, and filter Amazon Rekognition stream processors by using tags. Each tag is a label consisting of a
user-defined key and value.

To add one or more tags to an existing stream processor, use the `TagResource` operation.
Specify the stream processor's Amazon Resource Name (ARN) (`ResourceArn`) and the tags (`Tags`) that you want to add. The following example shows how to add two tags.

```
aws rekognition tag-resource --resource-arn resource-arn \
                --tags '{"key1":"value1","key2":"value2"}'

```

###### Note

If you do not know the stream processor's Amazon Resource Name, you can use the `DescribeStreamProcessor` operation.
