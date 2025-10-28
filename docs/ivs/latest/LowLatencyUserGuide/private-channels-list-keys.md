# List IVS Playback Keys

Amazon IVS customers can get a list of all of their playback-key resources at any
time.

## Console Instructions

1. Open the [Amazon IVS console](https://console.aws.amazon.com/ivs "https://console.aws.amazon.com/ivs").
   Choose your channel’s region if you are not already on it.
2. In the left navigation menu, choose **Playback
   security > Playback keys**.

All playback-key resources associated with your account are displayed.
Deleted keys are not displayed, and there is no history of past keys.

## CLI Instructions

```
aws ivs list-playback-key-pairs --region <aws-region>
```

You can omit `--region <aws-region>` if the region is in your local
AWS configuration file.

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

For usage information, see [ListPlaybackKeyPairs](../LowLatencyAPIReference/API_ListPlaybackKeyPairs.md "../LowLatencyAPIReference/API_ListPlaybackKeyPairs.md") in the _IVS Low-Latency
Streaming API Reference_.

```
POST /ListPlaybackKeyPairs HTTP/1.1
{
   "maxResults": number,
   "nextToken": "string"
}
```
