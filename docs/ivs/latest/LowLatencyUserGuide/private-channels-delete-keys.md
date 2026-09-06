

# Delete IVS Playback Keys
<a name="private-channels-delete-keys"></a>

Amazon IVS customers can delete playback keys from their accounts. Deleted keys will remove the resource from the customer’s account; playback tokens signed with deleted keys will not pass verification.

## Console Instructions
<a name="private-channels-delete-console"></a>

1. Open the [Amazon IVS console](https://console.aws.amazon.com/ivs). Choose your channel’s region if you are not already on it.

1. In the left navigation menu, choose **Playback security > Playback keys**.

1. Choose the key(s) you want to delete. 

1. Choose **Delete**. A **Delete playback key** dialog appears.

1. Choose **Delete playback key**.

## CLI Instructions
<a name="private-channels-delete-cli"></a>

You can delete playback keys via the AWS CLI, if you have the key’s ARN. Amazon IVS does not support batch deletes via the CLI. 

```
aws ivs delete-playback-key-pair --arn arn:aws:ivs:us-west-2:991729659840:playback-key/3db9fc15-df57-4c02-b5a6-d4ee3448b8ad --region <aws-region>
```

You can omit `--region <aws-region>` if the region is in your local AWS configuration file.

On success, there is no response. You can run the `get` command (below) to verify that the key was deleted.

Here is an example error response:

```
An error occurred (ResourceNotFoundException) when calling the 
DeletePlaybackKeyPair operation: ResourceNotFoundException:
```

## API Request
<a name="private-channels-delete-api"></a>

For usage information, see [DeletePlaybackKeyPair](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_DeletePlaybackKeyPair.html) in the *IVS Low-Latency Streaming API Reference*. 

```
POST /DeletePlaybackKeyPair HTTP/1.1
{
  "arn": "<playback key arn>"
}
```