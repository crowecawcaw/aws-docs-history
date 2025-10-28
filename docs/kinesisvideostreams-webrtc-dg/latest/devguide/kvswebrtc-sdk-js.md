# Amazon Kinesis Video Streams with WebRTC SDK in JavaScript for web applications

You can find the Kinesis Video Streams with WebRTC SDK in JavaScript for web applications and its
corresponding samples in [GitHub](https://github.com/awslabs/amazon-kinesis-video-streams-webrtc-sdk-js "https://github.com/awslabs/amazon-kinesis-video-streams-webrtc-sdk-js").

###### Topics

- [Install the SDK](#install-sdk-js "#install-sdk-js")
- [WebRTC JavaScript SDK documentation](#docs-sdk-js "#docs-sdk-js")
- [Use the sample application](#build-sdk-js "#build-sdk-js")
- [Edit the sample application](#run-sdk-js "#run-sdk-js")

## Install the SDK

Whether and how you install the Kinesis Video Streams with WebRTC SDK in JavaScript depends on whether the
code executes in `Node.js` modules or browser scripts.

NodeJS module
The preferred way to install the Kinesis Video Streams with WebRTC SDK in JavaScript for Node.js is to use [npm, the Node.js package manager](https://www.npmjs.com/ "https://www.npmjs.com/").

The package is hosted at [https://www.npmjs.com/package/amazon-kinesis-video-streams-webrtc](https://www.npmjs.com/package/amazon-kinesis-video-streams-webrtc?activeTab=readme "https://www.npmjs.com/package/amazon-kinesis-video-streams-webrtc?activeTab=readme").

To install this SDK in your `Node.js` project, use the terminal to navigate to
the same directory as your project’s `package.json`:

Type the following:

```
npm install amazon-kinesis-video-streams-webrtc
```

You can import the SDK classes like typical Node.js modules:

```
// JavaScript
const SignalingClient = require('amazon-kinesis-video-streams-webrtc').SignalingClient;
// TypeScript
import { SignalingClient } from 'amazon-kinesis-video-streams-webrtc';
```

Browser
You don't have to install the SDK to use it in browser scripts. You can load the hosted
SDK package directly from AWS with a script in your HTML pages.

To use the SDK in the browser, add the following script element to your HTML
pages:

```
<script src="https://unpkg.com/amazon-kinesis-video-streams-webrtc/dist/kvs-webrtc.min.js"></script>
```

After the SDK loads in your page, the SDK is available from the global variable
`KVSWebRTC` (or `window.KVSWebRTC`).

For example, `window.KVSWebRTC.SignalingClient`.

## WebRTC JavaScript SDK documentation

The documentation for the SDK methods are on the GitHub readme, under [Documentation](https://github.com/awslabs/amazon-kinesis-video-streams-webrtc-sdk-js?tab=readme-ov-file#documentation "https://github.com/awslabs/amazon-kinesis-video-streams-webrtc-sdk-js?tab=readme-ov-file#documentation").

In the [Usage](https://github.com/awslabs/amazon-kinesis-video-streams-webrtc-sdk-js?tab=readme-ov-file#usage "https://github.com/awslabs/amazon-kinesis-video-streams-webrtc-sdk-js?tab=readme-ov-file#usage") section, there is additional information for integrating this SDK along with the
AWS SDK for JavaScript to build a web-based viewer application.

See the `examples` directory for an example of a complete application, including both a master and viewer role.

## Use the sample application

Kinesis Video Streams with WebRTC also hosts a sample application that you can use to either create a new
signaling channel or connect to an existing channel and use it as a master or viewer.

The Kinesis Video Streams with WebRTC sample application is located in [GitHub](https://awslabs.github.io/amazon-kinesis-video-streams-webrtc-sdk-js/examples/index.html "https://awslabs.github.io/amazon-kinesis-video-streams-webrtc-sdk-js/examples/index.html").

The code for the sample application is in the `examples` directory.

###### Topics

- [Stream peer-to-peer from the sample application to the
  AWS Management Console](#sdk-js-stream-console "#sdk-js-stream-console")
- [Stream peer-to-peer from the sample application to the
  sample application](#sdk-js-stream-test "#sdk-js-stream-test")
- [Stream peer-to-peer with WebRTC Ingestion from the sample page to the sample page](#sdk-js-stream-ingestion "#sdk-js-stream-ingestion")

### Stream peer-to-peer from the sample application to the

AWS Management Console

1. Open the [Kinesis Video Streams with WebRTC sample application](https://awslabs.github.io/amazon-kinesis-video-streams-webrtc-sdk-js/examples/index.html "https://awslabs.github.io/amazon-kinesis-video-streams-webrtc-sdk-js/examples/index.html") and complete the following:
   - AWS Region. For example, `us-west-2`.
   - The AWS access key and the secret key for your IAM user or role. Leave the session
     token blank if you are using long-term AWS credentials.
   - The name of the signaling channel to which you want to connect.

   If you want to connect to a new signaling channel, choose **Create
   Channel** to create a signaling channel with the value provided in the box.

   ###### Note

   Your signaling channel name must be unique for the current account and region. You can
   use letters, numbers, underscores (\_), and hyphens (-), but not spaces.
   - Whether you want to send audio, video, or both.
   - WebRTC Ingestion and Storage. Expand the node and choose one of the following:
     - Select **Automatically determine ingestion mode**.
     - Make sure **Automatically determine ingestion mode** isn't selected
       and set the manual override to **OFF**.

     ###### Note

     **Automatically determine ingestion mode** has the application call the
     [DescribeMediaStorageConfiguration](../../../kinesisvideostreams/latest/dg/API_DescribeMediaStorageConfiguration.md "../../../kinesisvideostreams/latest/dg/API_DescribeMediaStorageConfiguration.md") API to determine which mode to run in
     (Peer-to-peer or WebRTC ingestion). This additional API call adds a small amount to the
     startup time.

     If you know ahead of time which mode this signaling channel is running in, use the
     manual override to skip this API call.

   - ICE candidate generation. Leave `STUN`/`TURN` selected and leave
     `Trickle ICE` enabled.

2. Choose **Start Master** to connect to the signaling channel.

Allow access to your camera and/or microphone, if needed. 3. Open the [Kinesis Video Streams console](https://console.aws.amazon.com/kinesisvideo/home/ "https://console.aws.amazon.com/kinesisvideo/home/") in the AWS Management Console.

Make sure the correct region is selected. 4. In the left navigation, select **[signaling channels](https://console.aws.amazon.com/kinesisvideo/home#/signalingChannels/ "https://console.aws.amazon.com/kinesisvideo/home#/signalingChannels/")**.

Select the name of the signaling channel above. Use the search bar, if needed. 5. Expand the **Media playback viewer** section. 6. Choose the **play** button on the video player. This joins the WebRTC session
as a `viewer`.

The media that is being sent on the demo page should display in the AWS Management Console.

### Stream peer-to-peer from the sample application to the

sample application

1. Open the [Kinesis Video Streams with WebRTC sample application](https://awslabs.github.io/amazon-kinesis-video-streams-webrtc-sdk-js/examples/index.html "https://awslabs.github.io/amazon-kinesis-video-streams-webrtc-sdk-js/examples/index.html") and complete the following information:
   - AWS Region. For example, `us-west-2`.
   - The AWS access key and the secret key for your IAM user or role. Leave the session
     token blank if you are using long-term AWS credentials.
   - The name of the signaling channel to which you want to connect.

   If you want to connect to a new signaling channel, choose **Create
   Channel** to create a signaling channel with the value provided in the box.

   ###### Note

   Your signaling channel name must be unique for the current account and region. You can
   use letters, numbers, underscores (\_), and hyphens (-), but not spaces.
   - Whether you want to send audio, video, or both.
   - WebRTC Ingestion and Storage. Expand the node and choose one of the following:
     - Select **Automatically determine ingestion mode**.
     - Make sure **Automatically determine ingestion mode** isn't selected
       and set the manual override to **OFF**.

     ###### Note

     **Automatically determine ingestion mode** has the application call
     the [DescribeMediaStorageConfiguration](../../../kinesisvideostreams/latest/dg/API_DescribeMediaStorageConfiguration.md "../../../kinesisvideostreams/latest/dg/API_DescribeMediaStorageConfiguration.md") API to determine which mode to run in
     (Peer-to-peer or WebRTC ingestion). This additional API call adds a small amount to the
     startup time.

     If you know ahead of time which mode this signaling channel is running in, use the
     manual override to skip this API call.

   - ICE candidate generation. Leave `STUN`/`TURN` selected and leave
     `Trickle ICE` enabled.

2. Choose **Start Master** to connect to the signaling channel as the
   `master` role.

Allow access to your camera and/or microphone, if needed. 3. Open another browser tab and open the [Kinesis Video Streams with WebRTC sample application](https://awslabs.github.io/amazon-kinesis-video-streams-webrtc-sdk-js/examples/index.html "https://awslabs.github.io/amazon-kinesis-video-streams-webrtc-sdk-js/examples/index.html"). All of the information from the previous run
should load. 4. Scroll down and choose **Start Viewer** to connect to the signaling
channel as the `viewer` role.

You should see the media being exchanged between the `master` and
`viewer`.

### Stream peer-to-peer with WebRTC Ingestion from the sample page to the sample page

1. Follow [Ingest media from a browser](ingest-media.md#ingest-browser "ingest-media.md#ingest-browser") to connect a master participant and make sure it is connected to the storage session.
2. Follow [Add viewers to the ingestion session](ingest-media.md#ingest-add-viewers "ingest-media.md#ingest-add-viewers") to add viewer participants.

Viewer participants will connect to and receive media from the storage session. They can send optional audio back to the storage session.

The storage session handles mixing the media received from master and viewer participants and sending it to the appropriate destinations. 3. You can view and consume ingested media through [Kinesis Video Streams playback](../../../kinesisvideostreams/latest/dg/how-playback.md "../../../kinesisvideostreams/latest/dg/how-playback.md").

## Edit the sample application

To edit the SDK and sample application for development purposes, follow the instructions
below.

**Prerequisite**

NodeJS version 16+

###### Note

We recommend downloading the latest long term support (LTS) version from
[https://nodejs.org/en/download](https://nodejs.org/en/download "https://nodejs.org/en/download").

###### Edit the sample application

1. Download the Kinesis Video Streams with WebRTC SDK in JavaScript.

Type the following in the terminal:

```
git clone https://github.com/awslabs/amazon-kinesis-video-streams-webrtc-sdk-js.git
```

2. Navigate to the directory with the package.json file. The file is located in the
   repository's root directory.

Type the following in the terminal:

```
cd amazon-kinesis-video-streams-webrtc-sdk-js
```

3. Install dependencies.

Type the following [npm CLI](https://docs.npmjs.com/cli/v10/commands "https://docs.npmjs.com/cli/v10/commands")
command in the terminal:

```
npm install
```

4. Start the web server to start serving web pages.

Type the following [npm CLI](https://docs.npmjs.com/cli/v10/commands "https://docs.npmjs.com/cli/v10/commands")
command in the terminal:

```
npm run develop
```

5. In your browser, visit [http://localhost:3001/](http://localhost:3001/ "http://localhost:3001/").

You can make edits to the web page by editing the files in the `examples`
directory.
