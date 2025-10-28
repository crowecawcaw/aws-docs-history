# Auto-Record to Amazon S3

You have the option of enabling recording for a channel. If the auto-record to S3
feature is enabled, all streams on the channel are recorded and saved to an Amazon
S3 storage bucket that you own. Subsequently, the recording is available for
on-demand playback.

_Setting this up is an advanced option._ By
default, recording is disabled when a channel is created.

Before you can set up a channel for recording, you must create a _recording-configuration_. This is a resource which
specifies an Amazon S3 location where the recorded streams for the channel are
stored. You can create and manage recording configurations using the console or CLI;
both procedures are given below. After you create the recording configuration, you
associate it with a channel either when you create the channel (as described below)
or later, by updating an existing channel. (In the API, see [CreateChannel](../LowLatencyAPIReference/API_CreateChannel.md "../LowLatencyAPIReference/API_CreateChannel.md") and [UpdateChannel](../LowLatencyAPIReference/API_UpdateChannel.md "../LowLatencyAPIReference/API_UpdateChannel.md").) You can associate multiple channels with the same
recording configuration. You can delete a recording configuration that is no longer
associated with any channels.

Keep in mind the following constraints:

- You must own the S3 bucket. That is, the account that sets up a channel to
  be recorded must own the S3 bucket where recordings will be stored.
- The channel, recording configuration, and S3 location must be in the same
  AWS region. If you create channels in other regions and want to record them,
  you must also set up recording configurations and S3 buckets in those
  regions.
  Recording to your S3 bucket requires authorization with your AWS credentials. To
  give IVS the required access, an AWS IAM [Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") (SLR) is created automatically when the recording
  configuration is created: the SLR is limited to give IVS write permission only on
  the specific bucket.

Note that network issues between the streaming location and AWS or within AWS
could result in some data loss while recording your stream. In these cases, Amazon
IVS prioritizes the live stream over the recording. For redundancy, record locally
via your streaming tool.

For more information (including how to set up post-processing or VOD playback on
your recorded files), see [IVS Auto-Record to Amazon S3 | Low-Latency Streaming](record-to-s3.md "record-to-s3.md").

### How to Disable

Recording

To disable Amazon S3 recording on an existing channel:

- Console — On the details page for the relevant channel, in the
  **Record and store** streams
  section, choose **Disabled** and then
  choose **Save Channel**. This removes
  the recording configuration’s association with the channel; streams
  on that channel will no longer be recorded.
- CLI — Run the `update-channel` command and pass in the
  recording-configuration ARN as an empty string:

```
aws ivs update-channel --arn "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh" --recording-configuration-arn ""
```

This returns a channel object with an empty string for
`recordingConfigurationArn`, indicating that the
recording is disabled.
