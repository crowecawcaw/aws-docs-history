# Enabling and retrieving

thumbnails programmatically

You can use the AWS CLI to work with thumbnails programmatically. The following
information assumes that you are familiar with the basics of using the AWS CLI. For
information about the basics, see the [AWS CLI Command Reference](../../../cli/latest/reference.md "../../../cli/latest/reference.md").

You enable thumbnails separately in each flow. You can enable thumbnails when you
first create a flow or you can enable them in an existing flow.

After thumbnails are active, MediaConnect automatically starts to generate them whenever the
flow is active. It generates one thumbnail at most once every second. (For more
information about the generation rate, see [How thumbnails are generated](monitor-with-thumbnails.md#thumbnails-how-generated "monitor-with-thumbnails.md#thumbnails-how-generated").)
You can retrieve the most recently generated thumbnail.

## Enabling thumbnails

Use the `CreateFlow` or `UpdateFlow` command. This command
is represented differently in different interfaces:

- In the AWS CLI, the commands are `create-flow` or
  `update-flow`.
- In the API, the command is an `HTTP POST` on
  `CreateFlow` or by an `HTTP PUT` on
  `UpdateFlow`.
- In the AWS SDKs, the command is represented by constructs that are
  suitable to that SDK language.

**To enable thumbnails using the AWS CLI**

Enter the `create-flow` or `update-flow` command. This
example illustrates the `update-flow` command. Replace the ARN with your
ARN.

```
aws mediaconnect update-flow
--flow-arn `arn:aws:mediaconnect:`us-east-1`:`111122223333`:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:AwardsShow`
--source-monitoring-config ThumbnailState=ENABLED
```

## Retrieving thumbnails

To retrieve thumbnails with the AWS CLI, use the
`DescribeFlowSourceThumbnail` command. This command is represented
differently in different interfaces:

- In the AWS CLI, the command is
  `describe-flow-source-thumbnail`.
- In the API, the command is an `HTTP GET` on
  `Source-thumbnail`.
- In the AWS SDKs, the command is represented by constructs that are
  suitable to that SDK language.

**To retrieve thumbnails using the AWS CLI**

Enter the `describe-flow-source-thumbnail` command. Replace the ARN
with your ARN.

```

aws mediaconnect describe-flow-source-thumbnail
--flow-arn `arn:aws:mediaconnect:`us-east-1`:`111122223333`:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:AwardsShow`

```

**The response**

The request results in a status code and a response.

- **Status code 200**: The request was processed
  successfully. This typically means that the response includes the flow source
  thumbnail in base64 encoding.

However, in some cases, MediaConnect might return a 200 status code even when a
thumbnail couldn't be retrieved. In these situations, the response includes an
error message explaining why the thumbnail couldn't be generated:

    + `ThumbnailDecodeError`: The video source doesn't meet [the
     requirements](thumbnails-specifications.md#thumbnails-source-video-requirements "thumbnails-specifications.md#thumbnails-source-video-requirements"), or there is no ingress traffic on the flow.
     Therefore, MediaConnect can't generate a thumbnail.
    + `ThumbnailGenerationInProgress`: The thumbnail is still being
     generated. Wait a few seconds and try again.
    + `ThumbnailSuppressed`: Typically this error occurs because
     the CPU and memory required to process the flow is currently high. If
     MediaConnect generated thumbnails now, the flow handling would slow down. Try
     again after a few seconds. If the problem persists, see the information
     in [Requirements for the flow](thumbnails-specifications.md#thumbnails-flow-requirements "thumbnails-specifications.md#thumbnails-flow-requirements").

- **Status code 202**: The request is valid, but
  MediaConnect is still preparing the flow. As a result, a thumbnail can't be generated
  yet. Wait a few seconds and try again.
- **Status code 4xx:** The request isn't valid.
- **Status code 5xx**: The request is valid but
  MediaConnect couldn't fulfill the request.
