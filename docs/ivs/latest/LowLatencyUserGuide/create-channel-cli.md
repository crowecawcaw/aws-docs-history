# CLI Instructions for Creating an IVS

Channel

Creating a channel with the AWS CLI is an advanced option and requires that you
first download and configure the CLI on your machine. For details, see the [AWS
Command Line Interface User Guide](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md").

Follow one of the two procedures below, depending on whether you want to create a
channel with or without recording enabled.

## Create a

Channel without Recording

1. Run the `create-channel` command and pass in an optional
   name:

```
aws ivs create-channel --name test-channel
```

2. This returns a new channel:

```
{
   "channel": {
      "arn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh",
      "authorized": false,
      "ingestEndpoint": "a1b2c3d4e5f6.global-contribute.live-video.net",
      "insecureIngest": false,
      "latencyMode": "LOW",
      "name": "channel-live",
      "playbackRestrictionPolicyArn": "arn:aws:ivs:us-west-2:123456789012:playback-restriction-policy/abcdABCDefgh",
      "playbackUrl": "https://a1b2c3d4e5f6.us-west-2.playback.live-video.net/api/video/v1/us-west-2.123456789012.channel.abcdEFGH.m3u8",
      "recordingConfigurationArn": "none",
      "srt": {
         "endpoint": "a1b2c3d4e5f6.srt.live-video.net",
         "passphrase: "ZU5A3yrjGAkghUNDr0c5NXBhsPrjlmtcKMNBluh7oImwJQ3ijeyClvMKxlpPcGAMziICJ",
      },
      "tags": {},
      "type": "STANDARD"
   },
   "streamKey": {
      "arn": "arn:aws:ivs:us-west-2:123456789012:stream-key/g1H2I3j4k5L6",
      "channelArn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh",
      "tags": {},
      "value": "sk_us-west-2_abcdABCDefgh_567890abcdef"
   }
}
```

3. **Important**: Note the
   `ingestEndpoint`, `streamKey value`, and
   `playbackUrl`. You will use these to set up streaming and
   playback.

## Create a Channel

with Recording

**Prerequisite:** Before starting this procedure,
create an Amazon S3 bucket and note its ARN. See [Getting Started with
Amazon S3](../../../AmazonS3/latest/userguide/GetStartedWithS3.md "../../../AmazonS3/latest/userguide/GetStartedWithS3.md"). The S3 bucket must be in the same region where you will
create a recording configuration; see the known issue in Step 1 below.

Then follow these steps to create the channel:

1. Run the `create-recording-configuration` command and pass
   in the ARN of an existing Amazon S3 bucket:

```
aws ivs create-recording-configuration --name configuration-1 --destination-configuration s3={bucketName=test-bucket}
```

Optionally, pass the `thumbnail-configuration` parameter to
manually set the thumbnail-recording mode and thumbnail interval:

```
aws ivs create-recording-configuration --name configuration-1 --destination-configuration s3={bucketName=s3_bucket_name} --thumbnail-configuration recordingMode="INTERVAL",targetIntervalSeconds=60
```

Optionally, pass the `recording-reconnect-window-seconds`
parameter to enable merge fragmented streams functionality:

```
aws ivs create-recording-configuration --name configuration-1 --destination-configuration s3={bucketName=test-bucket} --recording-reconnect-window-seconds 60
```

**Known issue:** In the us-east-1 region,
if you use the AWS CLI to create a recording configuration, it returns
success even if the S3 bucket is in a different region. In this case,
the `state` of the recording configuration is
`CREATE_FAILED` (instead of `ACTIVE`). (In
other regions, the CLI correctly returns failure if the bucket is in a
different region.)

**Workaround:** Ensure that your S3
bucket is in the same region as the recording configuration. If you
create a recording configuration in a different region as your S3
bucket, delete that recording configuration and create a new one with an
S3 bucket from the correct region. 2. This returns a new recording configuration with a unique ARN. The
state of the recording configuration is `CREATING`,
indicating that it is in the process of being created.

```
{
   "recordingConfiguration": {
      "arn": "arn:aws:ivs:us-west-2:123456789012:recording-configuration/mhndauNaO1te",
      "name": "configuration-1",
      "destinationConfiguration": {
         "s3": {
            "bucketName": "s3_bucket_name"
         }
      },
      "recordingReconnectWindowSeconds": 60,
      "state": "CREATING",
      "tags": {},
      "thumbnailConfiguration": {
         "recordingMode": "INTERVAL",
         "targetIntervalSeconds": 60
      }
   }
}
```

3. Typically, creation of the recording configuration takes a few
   seconds, but it can be up to 20 seconds. To check that the recording
   configuration has been created,run the
   `get-recording-configuration` command:

```
aws ivs get-recording-configuration --arn "arn:aws:ivs:us-west-2:123456789012:recording-configuration/mhndauNaO1te"
```

4. This returns a response indicating that the recording configuration
   was created (`state` is `ACTIVE`):

```
{
   "recordingConfiguration": {
      "arn": "arn:aws:ivs:us-west-2:123456789012:recording-configuration/mhndauNaO1te",
      "name": "configuration-1",
      "destinationConfiguration": {
         "s3": {
            "bucketName": "s3_bucket_name"
         }
      },
      "recordingReconnectWindowSeconds": 60,
      "state": "ACTIVE",
      "tags": {},
      "thumbnailConfiguration": {
         "recordingMode": "INTERVAL",
         "targetIntervalSeconds": 60
      }
   }
}
```

5. To create a channel and enable recording on it, run the
   `create-channel` command and pass in the
   recording-configuration ARN:

```
aws ivs create-channel --name channel-live --recording-configuration-arn  "arn:aws:ivs:us-west-2:123456789012:recording-configuration/mhndauNaO1te"
```

Alternately, to enable recording on an existing channel, run the
`update-channel` command and pass in the
recording-configuration ARN:

```
aws ivs update-channel --arn "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh" --recording-configuration-arn "arn:aws:ivs:us-west-2:123456789012:recording-configuration/mhndauNaO1te"
```

6. This returns a channel object with a non-"none" value for
   `recordingConfigurationArn`, indicating that recording is
   enabled. (The response below is from `create-channel`. The
   `update-channel` response does not include the
   `streamKey` object.)

```
{
   "channel": {
      "arn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh",
      "authorized": false,
      "ingestEndpoint": "a1b2c3d4e5f6.global-contribute.live-video.net",
      "insecureIngest": false,
      "latencyMode": "LOW",
      "name": "channel-live",
      "playbackUrl": "https://a1b2c3d4e5f6.us-west-2.playback.live-video.net/api/video/v1/us-west-2.123456789012.channel.abcdEFGH.m3u8",
      "recordingConfigurationArn": "arn:aws:ivs:us-west-2:123456789012:recording-configuration/mhndauNaO1te",
      "srt": {
         "endpoint": "a1b2c3d4e5f6.srt.live-video.net",
         "passphrase: "ZU5A3yrjGAkghUNDr0c5NXBhsPrjlmtcKMNBluh7oImwJQ3ijeyClvMKxlpPcGAMziICJ",
      },
      "tags": {},
      "type": "STANDARD"
   },
   "streamKey": {
      "arn": "arn:aws:ivs:us-west-2:123456789012:stream-key/g1H2I3j4k5L6",
      "channelArn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh",
      "tags": {},
      "value": "sk_us-west-2_abcdABCDefgh_567890abcdef"
   }
}
```

7. **Important**: Note the
   `ingestEndpoint`, `streamKey value`, and
   `playbackUrl`. You will use these to set up streaming and
   playback.
