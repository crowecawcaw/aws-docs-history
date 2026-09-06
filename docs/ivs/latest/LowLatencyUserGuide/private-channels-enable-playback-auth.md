

# Enable Playback Authorization on IVS Channels
<a name="private-channels-enable-playback-auth"></a>

A channel’s authorization requirement can be configured when the channel is created or later (using an update operation). Note that the steps are the same whether you want to enable or disable playback authorization.

Note that playback restriction policies (such as geo-blocking) cannot be used simultaneously with playback authorization. If playback authorization is enabled for a channel, any configured playback restriction policies will be ignored. To enforce geo-restrictions on a private channel, validate the user's location within your token generation logic before issuing a playback token.

## Console Instructions
<a name="private-channels-auth-console"></a>

To enable authorization when creating a channel:

1. Open the [Amazon IVS console](https://console.aws.amazon.com/ivs). Choose your channel’s region if you are not already on it.

1. In the **Get started** box (top right), choose **Create channel**.

1. On the **Channel create** page, choose **Custom configuration**.

1. In the **Playback authentication** section, turn on **Enable token-authentication requirement for video playback**.

1. Follow the rest of the prompts to create a channel. (See [Getting Started with IVS Low-Latency Streaming](getting-started.md).)

To enable authorization by updating an existing channel:

1. Open the [Amazon IVS console](https://console.aws.amazon.com/ivs). Choose your channel’s region if you are not already on it.

1. In the left navigation menu, choose **Channels**.

1. Choose the checkbox for the channel you want to update, then choose **Edit**. 

1. In the **Playback authentication** section, turn on **Enable token-authentication requirement for video playback**.

1. Click **Save changes**.

## CLI Instructions
<a name="private-channels-auth-cli"></a>

To enable authorization when creating a channel:

```
aws ivs create-channel --authorized --region <aws-region>
```

You can omit `--region <aws-region>` if the region is in your local AWS configuration file.

Here is an example response. Note that `authorized` is `true`.

```
{
    "streamKey": {
        "channelArn": "arn:aws:ivs:us-west-2:123456789:channel/fbc789c1-2c56-4ce6-a30a-d99275dc4481",
        "value": "sk_us-west-2_abcd1234efgh5678ijkl",
        "arn": "arn:aws:ivs:us-west-2:123456789:stream-key/62f15f1b-fe31-4127-b252-0666ac7f55a7",
        "tags": {}
    },
    "channel": {
        "name": "test-channel",
        "tags": {},
        "authorized": true,
        "latencyMode": "LOW",
        "ingestEndpoint": "jds34ksdg3las.global-contribute.live-video.net",
        "playbackUrl": "https://b37c565f6d79.us-west-2.playback.live-video.net/api/video/v1/aws.ivs.us-west-2.123456789.channel.oU4OKS4LA1Dz.m3u8",
        "arn": "arn:aws:ivs:us-west-2:123456789:channel/fbc789c1-2c56-4ce6-a30a-d99275dc4481"
    }
}
```

To enable authorization by updating an existing channel:

```
aws ivs update-channel --arn
arn:aws:ivs:us-west-2:693991300569:channel/742da049-fe9f-4f23-928e-c6753760a189 
--authorized
```

This is just an example; you must specify your own channel ARN after `--arn`. As when creating a channel, `authorized` is `true` in the update response.

## API Requests (Create and Update)
<a name="private-channels-auth-api"></a>

For usage information, see [CreateChannel](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_CreateChannel.html) and [UpdateChannel](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_UpdateChannel.html) in the *IVS Low-Latency Streaming API Reference*. 

```
POST /CreateChannel HTTP/1.1
{
  "name": "<your channel name>",
  "authorized": true
}
```

```
POST /UpdateChannel HTTP/1.1
{
  "arn": "<channel arn>",
  "authorized": true
}
```