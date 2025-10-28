# Embedding Metadata within a Video Stream

Amazon Interactive Video Service (IVS) timed metadata provides a way to embed metadata in
an Amazon IVS stream. It ensures that all your viewers receive the metadata at the same time
in the video stream, regardless of stream latency or geographic location.

## What is Timed Metadata?

_Timed_ metadata is metadata with timestamps. It can
be inserted into a stream programmatically, using the IVS API or the IVS broadcast SDK. When Amazon IVS
processes a stream, the timed metadata is synchronized with the audio and video frames.
During playback, all viewers of the stream get the metadata at the same time relative to
the stream. The timecode serves as a cue point, which can be used to trigger an action
based on the data, such as the following:

- Updating player statistics for a sports stream.
- Sending product details for a live shopping stream.
- Sending questions for a live quiz stream.

Amazon IVS timed metadata uses ID3 tags embedded in the video segments. As a result,
they are available in the recorded video.

## Setting Up IAM Permissions

**Prerequisite:** Before proceeding, you should have
stepped through [Getting Started with IVS Low-Latency Streaming](getting-started.md "getting-started.md") (including creating
an IAM user and setting up permissions).

Next, you must give your IAM user permission to use timed metadata. Follow these
steps:

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Users**, then
   choose the desired user (the user name you specified when you created an AWS
   account).
3. In the user **Summary** window, on the **Permissions** tab, choose **Add
   inline policy** (on the right side).
4. On the **JSON** tab, paste in this blob:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ivs:PutMetadata"
 ],
 "Resource": "arn:aws:ivs:*:*:channel/*"
 }
 ]
}`

```

5. Still in the **Create Policy** window, choose
   **Review Policy**. Give the policy a **Name**, then choose **Create
   Policy**.
6. You’re returned to the user **Summary** window,
   showing your new policy name.

## Inserting Timed Metadata

You can insert timed metadata only into an active stream on a specified
channel.

### Using the AWS CLI

For testing, the easiest way to add timed metadata is with the AWS CLI. Using the
AWS CLI requires that you first download and configure the CLI on your machine. You
may have already done that when you stepped through [Getting Started with IVS Low-Latency Streaming](getting-started.md "getting-started.md");
if not, do it now. For details, see the [AWS
Command Line Interface User Guide](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md").

Once you have the CLI:

1. Run the `put-metadata` command and pass in the channel ARN and
   your metadata:

```
aws ivs put-metadata --channel-arn <your-channel-arn> --metadata <your-metadata>
```

For example:

```
aws ivs put-metadata --channel-arn arn:aws:ivs:us-west-2:465369119046:channel/GbiYJna5hFoC --metadata '{"question": "What does IVS stand for?", "correctIndex": 0, "answers": ["interactive video service", "interesting video service", "ingenious video service"]}'
```

2. Amazon IVS checks whether the stream is live. If the stream is not live,
   you get an error; otherwise, the CLI returns without an error and the
   metadata (text blob) is inserted into the stream. This happens as soon as
   possible. There is no guarantee as to when this occurs; however, all viewers
   see the metadata at the same point in the stream.

### Using the Amazon IVS API

To programmatically insert timed metadata, use the [PutMetadata](../LowLatencyAPIReference/API_PutMetadata.md "../LowLatencyAPIReference/API_PutMetadata.md") API operation.

Here is an example HTTP request:

```
POST /PutMetadata HTTP/1.1
{
    "channelArn": "my_channel",
    "metadata": "{\"question\": \"What does IVS stand for?\", \"correctIndex\": 0, \"answers\": [\"interactive video service\", \"interesting video service\", \"ingenious video service\"]}"
}
```

### Using the IVS Broadcast SDK

You can insert timed metadata inband using the IVS broadcast SDK. This may be useful to synchronize the metadata with the audio and video content.

- Android — In the `BroadcastSession` class, use `sendTimedMetadata`.
- iOS — In the `IVSBroadcastSession` class, use `sendTimedMetadata`.

## Consuming Timed Metadata

Use the Amazon IVS Player to consume timed metadata embedded in a video stream. See
[IVS Player SDK](player.md "player.md") and the rest of the Player
documentation.

Below are example snippets that print any metadata received to the console using the
Amazon IVS Player SDK. An event is triggered whenever playback reaches a segment with
embedded metadata. (The event is `TEXT_METADATA_CUE` for Web,
`onCue()` for Android, and `player(_:didOutputCue:)` for iOS.)
You can use this event to initiate functionality within your client application, such as
updating an interactive widget. This event is triggered for both live and recorded
content.

**Amazon IVS Player SDK for Web:**

```
const player = IVSPlayer.create();
player.addEventListener(IVSPlayer.PlayerEventType.TEXT_METADATA_CUE,
    function (cue) {
  console.log('Timed metadata: ', cue.text);
});
```

**Amazon IVS Player SDK for Android:**

```
@Override
public void onCue(@NonNull Cue cue) {
  if(cue instanceof TextMetadataCue) {
    Log.i("Timed Metadata: ", ((TextMetadataCue)cue).text);
  }
}
```

**Amazon IVS Player SDK for iOS:**

```
func player(_ player: IVSPlayer, didOutputCue cue: IVSCue) {
  if let textMetadataCue = cue as? IVSTextMetadataCue {
    print("Timed Metadata: \(textMetadataCue.text)")
  }
}
```

**Note:** Timed metadata is supported for iOS Safari and
iOS Chrome in Player 1.3.0 and later.

### Consuming SEI Data

When IVS real-time stages are recorded with individual participant recording enabled, SEI (Supplemental
Enhancement Information) payloads are retained and published as `IVSPlayer.PlayerEventType.SEI` events.
Below is an example snippet that prints out SEI data to the console when using the IVS web player SDK:

```
const player = IVSPlayer.create();
player.addEventListener(IVSPlayer.MetadataEventType.SEI, (event) => {
  const data = new TextDecoder().decode(event.data);
  const message = JSON.parse(data);
  console.log(message);
});
```

**Note:** For more information about SEI, see
[Supplemental Enhancement Information (SEI)](../RealTimeUserGuide/web-publish-subscribe.md#web-publish-subscribe-sei-attributes "../RealTimeUserGuide/web-publish-subscribe.md#web-publish-subscribe-sei-attributes") in the
_IVS Web Broadcast SDK Guide_ for real-time streaming.

### Sample Demo: Quiz App

Code samples of an interactive quiz app are available on GitHub. We use JSON via
timed metadata to populate a quiz UI to display questions and answers. The answers
are selectable and reveal whether the selection is correct.

| Amazon IVS Player SDK Platform | Repo of Samples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Web                            | [https://github.com/aws-samples/amazon-ivs-basic-web-sample](https://github.com/aws-samples/amazon-ivs-basic-web-sample "https://github.com/aws-samples/amazon-ivs-basic-web-sample")Within this repo, see the [quiz demo](https://github.com/aws-samples/amazon-ivs-basic-web-sample/tree/master/simple-quiz "https://github.com/aws-samples/amazon-ivs-basic-web-sample/tree/master/simple-quiz") (and [live demo](https://codepen.io/amazon-ivs/pen/XWmjEKN "https://codepen.io/amazon-ivs/pen/XWmjEKN")). |
| Android                        | [https://github.com/aws-samples/amazon-ivs-player-android-sample](https://github.com/aws-samples/amazon-ivs-player-android-sample "https://github.com/aws-samples/amazon-ivs-player-android-sample")Within this repo, see the [quiz demo](https://github.com/aws-samples/amazon-ivs-player-android-sample/tree/master/quizdemo "https://github.com/aws-samples/amazon-ivs-player-android-sample/tree/master/quizdemo").                                                                                       |
| iOS                            | [https://github.com/aws-samples/amazon-ivs-player-ios-sample](https://github.com/aws-samples/amazon-ivs-player-ios-sample "https://github.com/aws-samples/amazon-ivs-player-ios-sample")Within this repo, see the [quiz demo](https://github.com/aws-samples/amazon-ivs-player-ios-sample/tree/master/QuizDemo "https://github.com/aws-samples/amazon-ivs-player-ios-sample/tree/master/QuizDemo").                                                                                                           | ## Viewing Timed Metadata If desired, you can view the timed metadata embedded in your live stream, in the console: 1. Open the [Amazon IVS console](https://console.aws.amazon.com/ivs "https://console.aws.amazon.com/ivs"). 2. In the top left, choose the hamburger icon to open the navigation pane, then choose **Live channels**. 3. Choose the channel whose stream you want to view, to go to a details page for that channel. The live stream is playing in the **Live stream** section of the page. 4. At the bottom of the window, choose **Timed Metadata**. While the player is playing, as each timed-metadata event is received, its value and time received are displayed. ## For More Information See [Using Amazon Interactive Video Service Timed Metadata](https://aws.amazon.com/blogs/media/part-1-using-amazon-interactive-video-service-timed-metadata/ "https://aws.amazon.com/blogs/media/part-1-using-amazon-interactive-video-service-timed-metadata/"), the first of a two-part blog series on using Amazon IVS timed metadata. |
