# Retrieving thumbnails

programmatically

When the thumbnails feature is enabled, MediaLive generates thumbnails for the currently
active input in a channel that is running. For a standard channel, MediaLive generates two
thumbnails. For a single-pipeline channel, MediaLive generates one thumbnail.

You can use the AWS CLI to work with thumbnails
programmatically. The following information assumes that you are
familiar with the basics of using the AWS CLI. For information about
the basics, see the [AWS CLI Command Reference](../../../cli/latest/reference.md "../../../cli/latest/reference.md").

Use the `DescribeThumbnails` command. This command
is represented differently in different interfaces:

- In the AWS CLI, the command is
  `describe-thumbnails`.
- In the API, the command is represented by an
  `HTTP GET` on
  `describe-thumbnails/kmsKeyId`.
- In the AWS SDKs, the command is represented by
  constructs that are suitable to that SDK language.

###### To retrieve thumbnails using the AWS CLI

1. Make sure that you have [enabled thumbnails in the
   channel](thumbnails-enable.md "thumbnails-enable.md"), and make sure that the channel is
   running.
2. Enter this command:

**aws medialive describe-thumbnails
--channel-id `value`
--pipeline-id `value`
--thumbnail-type `value`**

Where:

`channel-id` is required.

`pipeline-id` is 0 or 1. If you want
thumbnails for both pipelines, enter the command
twice.

`thumbnail-type` is always
`CURRENT_ACTIVE`. This option is required,
even though it has only one value. 3. The response appears on the screen. For
example:

```
{
    "ThumbnailDetails": [
        {
            "PipelineId": "0",
            "Thumbnails": [
                {
                    "Body"`base64 string of the JPEG image`",
                    "ContentType": "image/jpeg",
                    "ThumbnailType": "CURRENT_ACTIVE",
                    "TimeStamp": "2023-07-15T21:01:11"
                }
            ]
        }
    ]
}
```

If thumbnails are disabled, the response looks like
this:

```
{
    "ThumbnailDetails": []
}
```
