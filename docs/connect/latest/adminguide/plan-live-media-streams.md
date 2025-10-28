# Plan for live media streaming from Amazon Connect to

Kinesis Video Streams

###### Important

If you want to use the audio streaming feature, you need to retain the streams
that are created by Amazon Connect. Don't delete them, unless you're going to stop using the
streaming feature.

You can send all audio to and from the customer to Kinesis Video Streams. Media streaming leverages
Kinesis Video Streams multi-track support so that what the customer says is on a separate track from
what the customer hears.

Audio sent to Kinesis uses a sampling rate of 8 kHz.

## Do you need to increase your service

quotas?

When you enable media streaming in Amazon Connect, one Kinesis video stream is used per active
call. We create new KVS streams as needed to handle concurrent streaming requests. We
automatically create additional streams as needed to keep pace with active calls,
unless your account reaches the [Kinesis Video Streams service
quota](../../../streams/latest/dev/service-sizes-and-limits.md "../../../streams/latest/dev/service-sizes-and-limits.md").

Contact Support to request an increase to **Number of
Streams**.

To request an increase to your service quota, in the AWS Support Center, choose
**Create Case** and then choose **Service Quota
Increase**.

###### Tip

We make sure that **PutMedia** requests always stay within
the 5 TPS quota. You don't need to request an increase.

## How long do you need to store audio?

Customer audio is stored in Kinesis for the time defined by your retention settings
in an Amazon Connect instance. For instructions for setting this value, see [Enable live media streaming in your Amazon Connect
instance](enable-live-media-streams.md "enable-live-media-streams.md").

## Do you need to change the audio

streams?

We recommend that you refrain from modifying the streams. Doing so can cause
unexpected behavior.

## Who requires IAM permissions to retrieve

data?

If your business is using IAM permissions, your AWS admin will need to grant
permissions to IAM roles which need to retrieve data from Kinesis Video Streams. They will need to
grant them full access permissions for Kinesis Video Streams and AWS Key Management Service.
