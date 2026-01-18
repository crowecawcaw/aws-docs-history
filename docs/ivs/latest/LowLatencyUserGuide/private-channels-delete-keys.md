# Delete IVS Playback Keys

Amazon IVS customers can delete playback keys from their accounts. Deleted keys will
remove the resource from the customer’s account; playback tokens signed with deleted
keys will not pass verification.

## Console Instructions

1. Open the [Amazon IVS console](https://console.aws.amazon.com/ivs "https://console.aws.amazon.com/ivs").
   Choose your channel’s region if you are not already on it.
2. In the left navigation menu, choose **Playback
   security > Playback keys**.
3. Choose the key(s) you want to delete.
4. Choose **Delete**. A **Delete playback key** dialog appears.
5. Choose **Delete playback key**.

## CLI Instructions

You can delete playback keys via the AWS CLI, if you have the key’s ARN. Amazon
IVS does not support batch deletes via the CLI.

```
aws ivs delete-playback-key-pair --arn arn:aws:ivs:us-west-2:991729659840:playback-key/3db9fc15-df57-4c02-b5a6-d4ee3448b8ad --region <aws-region>
```

You can omit `--region <aws-region>` if the region is in your local
AWS configuration file.

On success, there is no response. You can run the `get` command (below)
to verify that the key was deleted.

Here is an example error response:

```
An error occurred (ResourceNotFoundException) when calling the
DeletePlaybackKeyPair operation: ResourceNotFoundException:
```

## API Request

For usage information, see [DeletePlaybackKeyPair](../LowLatencyAPIReference/API_DeletePlaybackKeyPair.md "../LowLatencyAPIReference/API_DeletePlaybackKeyPair.md") in the _IVS Low-Latency
Streaming API Reference_.

```
POST /DeletePlaybackKeyPair HTTP/1.1
{
  "arn": "<playback key arn>"
}
```
