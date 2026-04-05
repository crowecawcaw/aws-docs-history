# Delete tags from a stream processor

###### Note

Amazon Rekognition Streaming Video Analysis will no longer be
open to new customers starting April 30, 2026. If you would like to use Streaming Video Analysis, sign up prior to
that date. Existing customers for accounts that have used this feature within the last 12 months can continue
to use the service as normal. For more information, see
[Rekognition Streaming Video Analysis availability change](rekognition-streaming-video-analysis-availability-change.md "rekognition-streaming-video-analysis-availability-change.md").

You can identify, organize, search for, and filter Amazon Rekognition stream processors by using tags. Each tag is a label consisting of a
user-defined key and value.

To remove one or more tags from a stream processor, use the `UntagResource` operation. Specify the ARN of the model (`ResourceArn`) and the tag keys (`Tag-Keys`) that you want to remove.

```
aws rekognition untag-resource --resource-arn resource-arn \
                --tag-keys '["key1","key2"]'
```

Alternatively, you can specify tag-keys in this format:

```
--tag-keys key1,key2
```
