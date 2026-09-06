

# Get Information about IVS Playback Keys
<a name="private-channels-get-info"></a>

Amazon IVS customers can get information about their playback key resources. It is important to note that the associated private key will not be available, even in the case that the playback key was created by Amazon IVS via the console.

## Console Instructions
<a name="private-channels-info-console"></a>

1. Open the [Amazon IVS console](https://console.aws.amazon.com/ivs). Choose your channel’s region if you are not already on it.

1. In the left navigation menu, choose **Playback security > Playback keys**.

1. Choose the key you want to get more details about and choose **View details**.

## CLI Instructions
<a name="private-channels-info-cli"></a>

```
aws ivs get-playback-key-pair --arn arn:aws:ivs:us-west-2:991729659840:playback-key/3db9fc15-df57-4c02-b5a6-d4ee3448b8ad --region <aws-region>
```

You can omit `--region <aws-region>` if the region is in your local AWS configuration file.

Example response:

```
{
    "keyPair": {
        "arn": "arn:aws:ivs:us-west-2:991729659840:playback-key/3ff88c71-b18e-415f-948b-18bbde605a97",
        "fingerprint": "a2:b5:b3:0b:be:8e:73:00:0e:ad:e9:bb:02:c9:81:9a",
        "tags": {}
    }
}
```

## API Request
<a name="private-channels-info-api"></a>

For usage information, see [GetPlaybackKeyPair](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_GetPlaybackKeyPair.html) in the *IVS Low-Latency Streaming API Reference*. 

```
POST /GetPlaybackKeyPair HTTP/1.1
{
   "arn": "<playback key arn>"
}
```