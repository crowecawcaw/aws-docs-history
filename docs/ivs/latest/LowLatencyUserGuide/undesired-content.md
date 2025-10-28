# Undesired Content and Viewers in IVS

Malicious users may try to re-stream undesired content (e.g., professional sports) on your
platform. This kind of streaming can dramatically increase the amount of live-streamed video
that your application is serving as well as the costs associated with it, without adding
value to your business. In addition to providing you with controls to stop active streams,
Amazon IVS provides resources to help detect and prevent this kind of behavior in the first
place.

## Detecting Undesired Content

### Anomaly Detection

You can detect and alert on the kind of anomalous spike in viewership that happens
when certain undesired content is being streamed. (Once you detect that a spike has
occurred, you can take the steps mentioned in [stop the stream and reset the stream
key](#undesired-content-stop-stream "#undesired-content-stop-stream"), as discussed below.)

Amazon CloudWatch allows you to create alarms which can send alerts under specific
circumstances; for example, when your viewership spikes. Amazon IVS automatically
reports concurrent views (CCV) metrics to Amazon CloudWatch for all your channels,
so you only need to set up an alarm. To set up an anomaly-detection alarm based on
CCV, follow these steps:

1. Open the Amazon CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. On the left navigation bar, select **Alarms**, then select **All
   alarms**.
3. On the top right of the page, select **Create
   alarm**.
4. Select **Select Metric**. Under _Metrics_, select **IVS**, then **All**, then select
   the checkbox next to **ConcurrentViews**.
5. On the lower right, select **Select metric**.
   A 4-step alarm-creation wizard opens.
6. Wizard: In **Step 1, Specify metric and
   conditions**, specify these settings:
   1. **Statistic** = **Maximum**
   2. **Period** = **1
      minute**
   3. **Threshold type** = **Anomaly Detection**
   4. **Whenever concurrent views is…** =
      **Greater than the band**
   5. **Anomaly detection threshold** =
      **3**

   This threshold value is an initial suggestion. You may want to
   select a different value depending on your typical traffic patterns
   and needs. Use a lower value to watch your metrics more closely; a
   higher value, to get fewer alarms. 6. Select **Next**.

7. Wizard: In **Step 2, Configuration actions**,
   choose an existing SNS topic or create a new one, to send email to an
   address you specify. To create a topic which sends an email, select
   **Create new topic**, provide a topic name,
   enter your email address, and select **Create
   topic**. Select **Next** to
   continue.
8. Wizard: In **Step 3, Add name and
   description**, add a name and optional description for the
   alarm, then select **Next**.
9. Wizard: In **Step 4, Preview and create**,
   verify that the information is correct, then select **Create alarm**.
10. Your alarm is created. If prompted, follow any instructions for confirming
    SNS subscriptions.

For more information, see:

1. [Monitoring Amazon IVS Low-Latency
   Streaming](stream-health.md "stream-health.md")
2. [Creating a CloudWatch alarm based on anomaly detection](../../../AmazonCloudWatch/latest/monitoring/Create_Anomaly_Detection_Alarm.md "../../../AmazonCloudWatch/latest/monitoring/Create_Anomaly_Detection_Alarm.md")

### Custom Content

Moderation

You can explore custom content-moderation solutions to detect undesired content
via image recognition. Amazon IVS provides the ability to [automatically record Amazon IVS live streams to Amazon
S3](record-to-s3.md "record-to-s3.md"), including the generation of thumbnail images for use in this kind of
solution.

Consider these additional detection and prevention techniques:

- The [Amazon IVS moderation with Amazon Rekognition](https://github.com/aws-samples/amazon-ivs-moderation-with-record-to-s3-web-demo/ "https://github.com/aws-samples/amazon-ivs-moderation-with-record-to-s3-web-demo/") demo showcases
  how to use IVS Auto-Record to S3 in conjunction with Amazon Rekognition to
  moderate live content.
- [Add Hive content moderation to your Amazon IVS video
  streams](https://aws.amazon.com/blogs/media/add-hive-content-moderation-to-your-amazon-ivs-video-streams/ "https://aws.amazon.com/blogs/media/add-hive-content-moderation-to-your-amazon-ivs-video-streams/")
- [Creating Safer Online Communities with AI/ML Content Moderation](https://dev.to/aws/creating-safer-online-communities-with-aiml-content-moderation-1bn "https://dev.to/aws/creating-safer-online-communities-with-aiml-content-moderation-1bn") is a blog post about using Amazon Rekognition within an IVS
  application.

## Preventing Undesired Content and

Viewers

### Stop the Stream and Reset the Stream

Key

If you detect that a channel is being used to stream undesired content, you can
use the Amazon IVS console to shut down the stream:

1. Open the [Amazon IVS
   console](https://console.aws.amazon.com/ivs "https://console.aws.amazon.com/ivs"). (You can also access the Amazon IVS console through the
   [AWS Management
   Console](https://console.aws.amazon.com "https://console.aws.amazon.com").)
2. If needed, from the navigation bar, use the **Select a
   Region** drop-down to choose the region in which the channel is
   hosted.
3. Select the channel on which the stream that you want to stop is
   running.
4. On the channel page, navigate down to the **Live
   Stream** section and select **Stop
   stream**.

Even after you stop the stream, the broadcaster can restart the stream on that
channel. To prevent this, reset the stream key; that prevents the broadcaster from
restarting a stream without first acquiring a new stream key. To reset the stream
key:

- While still on the channel page, navigate down to the **Stream configuration** section and select **Reset stream key**.

You also can stop a stream and reset (delete/create) the stream key
programmatically. See the [Amazon IVS Low-Latency
Streaming API Reference](../LowLatencyAPIReference/Welcome.md "../LowLatencyAPIReference/Welcome.md").

Depending on how your application issues stream keys, you may need to take further
measures to prevent any new stream keys from being acquired.

### Use Private Channels

In many cases, undesired content is streamed to a large audience outside of your
platform by simply embedding the playback URL in a third-party website. The best
solution to prevent this kind of behavior is Amazon IVS private channels. By using
private channels, you can restrict playback to viewers with valid playback tokens.
Playback tokens are used to validate the viewer within the playback application,
impeding viewership on unintended platforms. In addition, you can enable origin
enforcement, which prevents viewers from watching streams on websites that aren't
hosted on your domains. You can extend this protection to cover common streaming
applications by also enabling strict origin enforcement.

Note that you can get the protection of private channels and authentication
without forcing users to create and/or log in to formal accounts. Your playback
application can simply acquire a token anonymously behind the scenes. You’ll still
be able to take advantage of origin enforcement.

To learn more about private channels, see:

- [Setting Up
  Private Channels](private-channels.md "private-channels.md") in the _IVS Low-Latency
  Streaming User Guide_. Within that document, to learn more
  about origin enforcement, see [Generate and Sign IVS Playback Tokens](private-channels-generate-tokens.md "private-channels-generate-tokens.md").
- [Creating a Private Channel for Authorized Live Stream Playback with
  Amazon IVS](https://dev.to/aws/creating-a-private-channel-for-authorized-live-stream-playback-with-amazon-ivs-2mdl "https://dev.to/aws/creating-a-private-channel-for-authorized-live-stream-playback-with-amazon-ivs-2mdl") (blog post)

### Use Playback Restriction

Policies

If you do not want to use [private channels](#undesired-content-private-channels "#undesired-content-private-channels"), you can still benefit from some of the same
protections by leveraging playback restriction policies. These policies allow you to
enable features such as GeoBlocking and origin enforcement on public channels. You
create a playback restriction policy using the IVS console or API, then attach the
policy’s ARN to your channels.

#### Console Instructions (Playback

Restriction Policy)

1. Create a playback restriction policy
   1. [Open the Amazon
      IVS console](https://console.aws.amazon.com/ivs "https://console.aws.amazon.com/ivs"). On the left navigation pane, select
      **Playback security > Playback restriction
      policies**.
   2. Select **Create policy**.
   3. Optionally, name the policy.
   4. Optionally, toggle **Strict origin
      enforcement** (see note below).
   5. Specify **Allowed countries** and
      **Allowed origins**.
   6. Select **Create policy**.

2. Attach this policy to a new or existing channel
   1. Create a new channel or edit an existing channel.
   2. In the **Restrict playback section**
      (of the **Create channel** or **Update channel** window), select **Enable playback restriction**.
   3. From the **Playback restriction
      policy** drop-down list, select the policy you created
      in Step 1.
   4. Select **Create channel** (for a new
      channel) or **Save** (to update an
      existing channel).

**Note on strict origin enforcement:** This is an
optional setting that can be used to strengthen the origin restriction specified
with allowed origins. By default, the origin restriction applies only to the
multivariant playlist. If strict origin enforcement is enabled, the server will
enforce a requirement that the requesting origin matches the policy for all playback
requests (including multivariant playlist, variant playlist, and segments). This
means that all clients (including non-browser clients) will have to provide a valid
origin-request header with each request. Use the `setOrigin` method to
set the header in the IVS iOS and Android player SDKs. It is set automatically in
web browsers except iOS Safari. For iOS Safari, you need to add
`crossorigin="anonymous"` to the video element, to ensure that the
origin request header is sent. Example: `<video
 crossorigin="anonymous"></video>`.

**Note on mapping between IP addresses and
countries:** IVS determines the location of your users by using a
third-party database. The accuracy of the mapping between IP addresses and countries
varies by region. Based on recent tests, the overall accuracy is 99.8%. If IVS can't
determine a user's location, IVS serves the content that the user requested.

#### CLI Instructions (Playback Restriction

Policy)

1. Create a playback restriction policy. Here is an example. _For
   the `allowed-countries` and `allowed-origins`
   fields, replace the example values below with your actual values, or
   delete one or both fields, depending on your use case._

```
aws ivs create-playback-restriction-policy --name test-playback-restriction-policy --enable-strict-origin-enforcement --allowed-countries "US","JP" --allowed-origins "https://example1.com","https://*.example2.com"
```

This returns a new playback restriction policy. For its fields, see [PlaybackRestrictionPolicy](../LowLatencyAPIReference/API_PlaybackRestrictionPolicy.md "../LowLatencyAPIReference/API_PlaybackRestrictionPolicy.md") in the _IVS Low-Latency
Streaming API Reference_. 2. Attach the new policy to a channel. For an existing channel, run
`update-channel` and pass in the ARN of the playback
restriction policy created in the previous step:

```
aws ivs update-channel --arn "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh" --playback-restriction-policy-arn "arn:aws:ivs:us-west-2:123456789012:playback-restriction-policy/abcdABCDefgh"
```

For a new channel, include the
`--playback-restriction-policy-arn` statement during [channel creation.](create-channel-cli.md "create-channel-cli.md")
