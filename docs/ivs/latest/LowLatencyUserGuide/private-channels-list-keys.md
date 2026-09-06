

# List IVS Playback Keys
<a name="private-channels-list-keys"></a>

Amazon IVS customers can get a list of all of their playback-key resources at any time.

## Console Instructions
<a name="private-channels-list-console"></a>

1. Open the [Amazon IVS console](https://console.aws.amazon.com/ivs). Choose your channel’s region if you are not already on it.

1. In the left navigation menu, choose **Playback security > Playback keys**.

   All playback-key resources associated with your account are displayed. Deleted keys are not displayed, and there is no history of past keys.

## CLI Instructions
<a name="private-channels-list-cli"></a>

```
aws ivs list-playback-key-pairs --region <aws-region>
```

You can omit `--region <aws-region>` if the region is in your local AWS configuration file.

Example response:

```
{
    "keyPairs": [
        {
            "arn": "arn:aws:ivs:us-west-2:991729659840:playback-key/3db9fc15-df57-4c02-b5a6-d4ee3448b8ad",
            "fingerprint": "81:f3:8c:88:78:61:4e:bc:58:07:a3:ca:63:f5:72:08",
            "tags": {}
        },
        {
            "arn": "arn:aws:ivs:us-west-2:991729659840:playback-key/3ff88c71-b18e-415f-948b-18bbde605a97",
            "fingerprint": "a2:b5:b3:0b:be:8e:73:00:0e:ad:e9:bb:02:c9:81:9a",
            "tags": {}
        }
    ]
}
```

## API Request
<a name="private-channels-list-api"></a>

For usage information, see [ListPlaybackKeyPairs](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_ListPlaybackKeyPairs.html) in the *IVS Low-Latency Streaming API Reference*.

```
POST /ListPlaybackKeyPairs HTTP/1.1
{
   "maxResults": number,
   "nextToken": "string"
}
```