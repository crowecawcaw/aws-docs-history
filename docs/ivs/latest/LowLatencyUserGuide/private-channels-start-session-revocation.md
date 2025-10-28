# Revoke IVS Viewer

Sessions

Amazon IVS customers can revoke the viewer session associated with an auth token, to
prevent and stop playback using that token. An example use case is transitioning a
public stream to a private stream in which only a subset of the public stream viewers
can continue watching.

For information on the `viewer-id` field mentioned in the instructions
below, see the "Token Schema" under [Generate and Sign IVS Playback
Tokens](private-channels-generate-tokens.md "private-channels-generate-tokens.md").

## CLI Instructions

You can revoke the viewer session via the AWS CLI, if you have the channel ARN and
the viewer ID.

```
aws ivs start-viewer-session-revocation --channel-arn arn:aws:ivs:us-west-2:991729659840:channel/abcdABCDefgh --viewer-id UDbh1u6M8nrOoarrzuKe --region <aws-region>
```

An optional input, `--viewer-session-versions-less-than-or-equal-to
 <version>` lets you specify a filter for which versions of the viewer
session to revoke at once.

You can omit `--region <aws-region>` if the region is in your local
AWS configuration file.

On success, there is no response.

Here is an example error response:

```
An error occurred (ValidationException) when calling the StartViewerSessionRevocation operation: ValidationException:
```

## API Request

For usage information, see [StartViewerSessionRevocation](../LowLatencyAPIReference/API_StartViewerSessionRevocation.md "../LowLatencyAPIReference/API_StartViewerSessionRevocation.md")
in the _IVS Low-Latency Streaming API Reference_.

```
POST /StartViewerSessionRevocation HTTP/1.1
{
  "channelArn": <channel ARN>,
  "viewerId": <viewer ID>,
  "viewerSessionVersionsLessThanOrEqualTo": <version>
}
```

There also is a [BatchStartViewerSessionRevocation](../LowLatencyAPIReference/API_BatchStartViewerSessionRevocation.md "../LowLatencyAPIReference/API_BatchStartViewerSessionRevocation.md")
operation.
