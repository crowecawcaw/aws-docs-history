

# Integrate in-app, web, video calling, and screen sharing natively into your application
<a name="config-com-widget2"></a>

To integrate Connect Customer in-app, web, video calling, and screen sharing with your application:

1. Use the Connect Customer [StartWebRTCContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartWebRTCContact.html) API to create the contact.

1. Then use the details returned by the API call to join the call using the Amazon Chime client library for [iOS](https://github.com/aws/amazon-chime-sdk-ios), [Android](https://github.com/aws/amazon-chime-sdk-android), or [JavaScript](https://github.com/aws/amazon-chime-sdk-js). 

For information about creating additional participants, see [Enable multi-user in-app, web, and video calling](enable-multiuser-inapp.md). 

See the following Github repository for sample applications: [amazon-connect-in-app-calling-examples](https://github.com/amazon-connect/amazon-connect-in-app-calling-examples). 

**Topics**
+ [How a client device initiates an in-app or web call](#diagram-option2)
+ [Get started](#diagram-option2-gs)
+ [Optional steps](#optional-steps)

## How a client device initiates an in-app or web call
<a name="diagram-option2"></a>

The following diagram shows the sequence of events for a client device (mobile application or browser) to initiate an in-app or web call.

![A conceptual diagram that shows how a client devices initiates a call.](http://docs.aws.amazon.com/connect/latest/adminguide/images/netra-gs-diagram.png)


1. Your customer uses the client application (website or application) to start an in-app or web call.

1. The client application (website or mobile application) or web server uses the Connect Customer [StartWebRTCContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartWebRTCContact.html) API to start the contact passing any attributes or context to Connect Customer.

1. The client application joins the call using the details returned from the [StartWebRTCContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartWebRTCContact.html) in step 2.

1. (Optional) Client uses the [CreateParticipantConnection](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_CreateParticipantConnection.html) API to receive a `ConnectionToken` that is used to send DTMF through the [SendMessage](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_SendMessage.html) API.

1. The contact reaches the flow and is routed based on the flow and placed in queue.

1. The agent accepts the contact.

1. (Optional) If video is enabled for customer and the agent, they are able to start their video.

1. (Optional - not shown in diagram) Additional participants can be added using the [CreateParticipant](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_CreateParticipant.html) and [CreateParticipantConnection](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_CreateParticipantConnection.html) APIs. 

## Get started
<a name="diagram-option2-gs"></a>

Following are the high level steps to get started:

1. Use the [StartWebRTCContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartWebRTCContact.html) API to create the contact. The API returns the details needed for the Amazon Chime SDK client to join the call.

1. Instantiate the Amazon Chime SDK client `MeetingSessionConfiguration` object using the configurations returned by [StartWebRTCContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartWebRTCContact.html).

1. Instantiate Amazon Chime SDK client `DefaultMeetingSession` with `MeetingSessionConfiguration`, which was created in step 2 to create a client meeting session. 
   + iOS

     ```
     let logger = ConsoleLogger(name: "logger") 
     let meetingSession = DefaultMeetingSession(
         configuration: meetingSessionConfig, 
         logger: logger
     )
     ```
   + Android

     ```
     val logger = ConsoleLogger()
     val meetingSession = DefaultMeetingSession(
         configuration = meetingSessionConfig,
         logger = logger,
         context = applicationContext
     )
     ```
   + JavaScript

     ```
     const logger = new ConsoleLogger('MeetingLogs', LogLevel.INFO);
     const deviceController = new DefaultDeviceController(logger);
     const configuration = new MeetingSessionConfiguration(
         meetingResponse, 
         attendeeResponse
     );
     const meetingSession = new DefaultMeetingSession(
         configuration, 
         logger, 
         deviceController
     );
     ```

1. Use the `meetingSession.audioVideo.start()` method to join the WebRTC contact with audio.
   + iOS/Android

     ```
     meetingSession.audioVideo.start()
     ```
   + JavaScript

     ```
     await meetingSession.audioVideo.start();
     ```

1. Use the `meetingSession.audioVideo.stop()` method to hangup the WebRTC contact.
   + iOS/Android

     ```
     meetingSession.audioVideo.stop()
     ```
   + JavaScript

     ```
     meetingSession.audioVideo.stop();
     ```

## Optional steps
<a name="optional-steps"></a>

For additional operations and comprehensive API documentation, refer to the platform-specific API overview guides:
+ **iOS**: [API Overview](https://aws.github.io/amazon-chime-sdk-ios/guides/api_overview.html)
+ **Android**: [API Overview](https://aws.github.io/amazon-chime-sdk-android/guides/api_overview.html)
+ **JavaScript**: [API Overview](https://github.com/aws/amazon-chime-sdk-js/blob/main/guides/03_API_Overview.md)

### Send DTMF tones
<a name="send-dtmf-tones"></a>

To send DTMF to the call, two Connect Customer Participant Service APIs are needed: [CreateParticipantConnection](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_CreateParticipantConnection.html) and [SendMessage](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_SendMessage.html) respectively.

**Note**  
`contentType` for the SendMessage API must be `audio/dtmf`.

1. Invoke [CreateParticipantConnection](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_CreateParticipantConnection.html) to retrieve `ConnectionToken`. (`ParticipantToken` is needed for calling this API. You can find it in the [StartWebRTCContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartWebRTCContact.html) response.)

1. With the `ConnectionToken`, call [SendMessage](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_SendMessage.html) for sending DTMF digits.

### Select audio devices
<a name="select-audio-devices"></a>

To select the audio input/output device, you can use the methods from the Amazon Chime SDK client for Android and iOS or the [native iOS capabilities](https://developer.apple.com/documentation/avkit/avroutepickerview) for iOS.

**iOS/Android**

```
meetingSession.audioVideo.listAudioDevices()
meetingSession.audioVideo.chooseAudioDevice(mediaDevice)
```

**JavaScript**

```
await meetingSession.audioVideo.listAudioInputDevices();
await meetingSession.audioVideo.listAudioOutputDevices();
await meetingSession.audioVideo.startAudioInput(device);
await meetingSession.audioVideo.chooseAudioOutput(deviceId);
```

### Mute and unmute audio
<a name="mute-unmute-audio"></a>

For mute and unmute, use `meetingSession.audioVideo.realtimeLocalMute()` and `meetingSession.audioVideo.realtimeLocalUnmute()`.

**iOS/Android**

```
meetingSession.audioVideo.realtimeLocalMute()
meetingSession.audioVideo.realtimeLocalUnmute()
```

**JavaScript**

```
meetingSession.audioVideo.realtimeMuteLocalAudio();
meetingSession.audioVideo.realtimeUnmuteLocalAudio();
```

### Start self video
<a name="start-self-video"></a>

To start self video, use the `meetingSession.audioVideo.startLocalVideo()`. See the client library API guides for more information on how to enumerate and choose specific devices.

**iOS/Android**

```
meetingSession.audioVideo.startLocalVideo()
```

**JavaScript**

```
meetingSession.audioVideo.startLocalVideoTile();
```

### Stop self video
<a name="stop-self-video"></a>

To stop self video, use the `meetingSession.audioVideo.stopLocalVideo()`.

**iOS/Android**

```
meetingSession.audioVideo.stopLocalVideo()
```

**JavaScript**

```
meetingSession.audioVideo.stopLocalVideoTile();
```

### Enable agent video
<a name="enable-agent-video"></a>

To allow receiving and loading video of the agent inside application, use the `meetingSession.audioVideo.startRemoteVideo()`. You will also need to implement video tile observers and bind video tiles to display views.

**iOS/Android**

```
meetingSession.audioVideo.startRemoteVideo()
// Implement VideoTileObserver to handle video tiles
meetingSession.audioVideo.addVideoTileObserver(observer)
// In videoTileDidAdd callback:
meetingSession.audioVideo.bindVideoView(videoView, tileId: tileState.tileId)
```

**JavaScript**

```
// Remote video is received automatically when available
// Implement AudioVideoObserver to handle video tiles
meetingSession.audioVideo.addObserver(observer);
// In videoTileDidUpdate callback:
meetingSession.audioVideo.bindVideoElement(tileId, videoElement);
```

Reference the platform-specific SDK guides for complete video tile implementation details.

### Disable agent video
<a name="disable-agent-video"></a>

To disallow receiving and loading video of the agent inside application, use the `meetingSession.audioVideo.stopRemoteVideo()`.

**iOS/Android**

```
meetingSession.audioVideo.stopRemoteVideo()
meetingSession.audioVideo.unbindVideoView(tileId)
```

**JavaScript**

```
meetingSession.audioVideo.unbindVideoElement(tileId);
```

### Use data messages
<a name="use-data-messages"></a>

You can use [data messages](https://github.com/aws/amazon-chime-sdk-js/blob/main/guides/03_API_Overview.md#9-send-and-receive-data-messages-optional) if you need to send any status from the agent side to the end user. For example, when customers are on hold, you can send a data message to the customer's application to display a message letting them know they are on hold and their video/screen sharing is still being sent, or you can turn off the video/screen share.

**iOS/Android**

```
meetingSession.audioVideo.realtimeSendDataMessage(topic, data, lifetimeMs)
meetingSession.audioVideo.addRealtimeDataMessageObserver(topic, observer)
```

**JavaScript**

```
meetingSession.audioVideo.realtimeSendDataMessage(topic, data, lifetimeMs);
meetingSession.audioVideo.realtimeSubscribeToReceiveDataMessage(topic, callback);
```

### Listen for stop events
<a name="listen-for-stop-events"></a>

You can listen for events when a Contact's participation ends through the `audioVideoDidStop` observer. Specific status codes might vary by platform.

#### Call reaches capacity
<a name="call-reaches-capacity"></a>

When more than 6 people attempt to join the call, additional participants will receive the following error and cannot join until others leave.
+ **iOS:** `MeetingSessionStatusCode.audioCallAtCapacity` or `MeetingSessionStatusCode.audioAuthenticationRejected`
+ **Android:** `MeetingSessionStatusCode.AudioCallAtCapacity` or `MeetingSessionStatusCode.AudioAuthenticationRejected`
+ **JavaScript:** `MeetingSessionStatusCode.AudioCallAtCapacity` or `MeetingSessionStatusCode.AudioAuthenticationRejected`

#### Participant removed from call
<a name="participant-removed-from-call"></a>

When a participant is removed from the call by the agent but the contact continues for other participants they will receive the following status code. Note that if the participant removal leads to the contact ending, they will receive either of this status or the contact end status.
+ **iOS:** `MeetingSessionStatusCode.audioServerHungup` or `MeetingSessionStatusCode.audioAuthenticationRejected`
+ **Android:** `MeetingSessionStatusCode.AudioServerHungup` or `MeetingSessionStatusCode.AudioAuthenticationRejected`
+ **JavaScript:** `MeetingSessionStatusCode.AudioAttendeeRemoved` or `MeetingSessionStatusCode.AudioAuthenticationRejected`

#### Contact ends
<a name="contact-ends"></a>

When the actual contact ends completely for all participants they will receive the following status code.
+ **iOS:** `MeetingSessionStatusCode.audioCallEnded`
+ **Android:** `MeetingSessionStatusCode.AudioCallEnded`
+ **JavaScript:** `MeetingSessionStatusCode.AudioCallEnded`