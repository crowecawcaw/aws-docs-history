# List tags in a stream processor

###### Note

Amazon Rekognition Streaming Video Analysis will no longer be
open to new customers starting April 30, 2026. If you would like to use Streaming Video Analysis, sign up prior to
that date. Existing customers for accounts that have used this feature within the last 12 months can continue
to use the service as normal. For more information, see
[Rekognition Streaming Video Analysis availability change](rekognition-streaming-video-analysis-availability-change.md "rekognition-streaming-video-analysis-availability-change.md").

You can identify, organize, search for, and filter Amazon Rekognition stream processors by using tags. Each tag is a label consisting of a
user-defined key and value.

To list the tags attached to a stream processor, use the `ListTagsForResource` operation and specify the ARN of the stream processor (`ResourceArn`).
The response is a map of tag keys and values that are attached to the specified stream processor.

```
aws rekognition list-tags-for-resource --resource-arn resource-arn

```

The output displays a list of tags attached to the stream processor:

```

{
    "Tags": {
        "Dept": "Engineering",
        "Name": "Ana Silva Carolina",
        "Role": "Developer"
    }
}

```
