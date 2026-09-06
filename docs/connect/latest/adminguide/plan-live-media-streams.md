

# Plan for live media streaming from Connect Customer to Kinesis Video Streams
<a name="plan-live-media-streams"></a>

**Important**  
If you want to use the audio streaming feature, you need to retain the streams that are created by Connect Customer. Don't delete them, unless you're going to stop using the streaming feature.

You can send all audio to and from the customer to Kinesis Video Streams. Media streaming uses Kinesis Video Streams multi-track support so that what the customer says is on a separate track from what the customer hears. 

Audio sent to Kinesis uses a sampling rate of 8 kHz.

## Do you need to increase your service quotas?
<a name="create-streams-service-limit"></a>

When you enable media streaming in Connect Customer, one Kinesis video stream is used per active call. We create new KVS streams as needed to handle concurrent streaming requests. We automatically create additional streams as needed to keep pace with active calls, unless your account reaches the [Kinesis Video Streams service quota](https://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html).

Contact Support to request an increase to **Number of Streams**.

To request an increase to your service quota, in the AWS Support Center, choose **Create Case** and then choose **Service Quota Increase**.

**Tip**  
We make sure that **PutMedia** requests always stay within the 5 TPS quota. You don't need to request an increase.

## How long do you need to store audio?
<a name="storing-audio-streams"></a>

Customer audio is stored in Kinesis for the time defined by your retention settings in a Connect Customer instance. For instructions for setting this value, see [Enable live media streaming in your Connect Customer instance](enable-live-media-streams.md).

## Do you need to change the audio streams?
<a name="changing-audio-streams"></a>

We recommend that you refrain from modifying the streams. Doing so can cause unexpected behavior.

## Who requires IAM permissions to retrieve data?
<a name="perms-audio-streams"></a>

If your business is using IAM permissions, your AWS admin will need to grant permissions to IAM roles which need to retrieve data from Kinesis Video Streams. They will need to grant them full access permissions for Kinesis Video Streams and AWS Key Management Service. 