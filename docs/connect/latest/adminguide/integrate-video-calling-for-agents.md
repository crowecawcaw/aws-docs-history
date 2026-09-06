

# Integrate video calling and screen sharing into your custom agent desktop by using Connect Customer Streams JS
<a name="integrate-video-calling-for-agents"></a>

This topic is for developers. For custom agent desktops, you need to make changes to support video calling and screen sharing. Following are high level steps.

**Note**  
If you embed the CCP directly into your custom agent application make sure `allowFramedVideoCall` is set to true when you initiate the CCP using [Connect Customer Streams JS](https://github.com/aws/amazon-connect-streams).

1. Use [Connect Customer Streams JS](https://github.com/aws/amazon-connect-streams) to check if the incoming contact is an WebRTC contact. Use contact subtype `"connect:WebRTC"`, as shown in the following code example:

   `contact.getContactSubtype() === "connect:WebRTC"`

1. You can retrieve the customer display name by using the name field in ` contact contact.getName()`.

## Add support for video
<a name="support-video"></a>

Complete the following steps to add support for video handling when your customers have it enabled.

1. To check whether a contact has video capability:

   ```
   // Return true if any connection has video send capability
   contact.hasVideoRTCCapabilities()
   
   // Return true if the agent connection has video send capability
   contact.canAgentSendVideo()
   
   // Return true if other non-agent connection has video send capability
   contact.canAgentReceiveVideo()
   ```

1. To check on whether the agent has video permission to handle video call:

   `agent.getPermissions().includes('videoContact');`

1. To accept a video call, the contact must have video capability and the agent must have video permission.

   ```
   function shouldRenderVideoUI() {
       return contact.getContactSubtype() === "connect:WebRTC" &&
       contact.hasVideoRTCCapabilities() &&
       agent.getPermissions().includes('videoContact');
   }
   ```

1. To join a video session, call `getVideoConnectionInfo`:

   ```
   if (shouldRenderVideoUI()) {
      const response = await
      contact.getAgentConnection().getVideoConnectionInfo();
   }
   ```

1. To build a video UI and join a video meeting session, see:
   + [Amazon Chime SDK for JavaScript](https://github.com/aws/amazon-chime-sdk-js) on GitHub 
   + [Amazon Chime SDK React Components Library](https://github.com/aws/amazon-chime-sdk-component-library-react) on GitHub

1. For simplicity, the following code snippets use examples from the Amazon Chime SDK React Components Library.

   ```
   import { MeetingSessionConfiguration } from "amazon-chime-sdk-js";
   import {
     useMeetingStatus,
     useMeetingManager,
     MeetingStatus,
     DeviceLabels,
     useLocalAudioOutput
   } from 'amazon-chime-sdk-component-library-react';
   
   const App = () => (
     <MeetingProvider>
       <MyVideoManager />
     </MeetingProvider>
   );
   
   const MyVideoManager = () => {
       const meetingManager = useMeetingManager();
       if (shouldRenderVideoUI()) {
           const response = await contact.getAgentConnection().getVideoConnectionInfo();
           const configuration = new MeetingSessionConfiguration(
               response.meeting, response.attendee);
           await meetingManager.join(configuration, { deviceLabels: DeviceLabels.Video });
           await meetingManager.start();
       }
       
       function endContact() {
           meetingManager.leave();
       }
   }
   ```

1. To render the video grid, use the [VideoTileGrid](https://aws.github.io/amazon-chime-sdk-component-library-react/?path=/docs/sdk-components-videotilegrid--page) from the Amazon Chime SDK React Components Library or customize the UI behavior using [RemoteVideoTileProvider](https://aws.github.io/amazon-chime-sdk-component-library-react/?path=/docs/sdk-providers-remotevideotileprovider--page). 

1. To render a video preview, you can use [VideoPreview](https://aws.github.io/amazon-chime-sdk-component-library-react/?path=/docs/sdk-components-previewvideo--page) and [CameraSelection](https://aws.github.io/amazon-chime-sdk-component-library-react/?path=/docs/sdk-components-deviceselection-camera-cameraselection--page) components. To choose or change a camera video, you can use `meetingManager.selectVideoInputDevice` or `meetingManager.startVideoInput `if the meeting is in progress.

   ```
   const meetingManager = useMeetingManager();
   const { isVideoEnabled } = useLocalVideo();
   if (isVideoEnabled) {
       await meetingManager.startVideoInputDevice(current);
    } else {
       meetingManager.selectVideoInputDevice(current);
   }
   ```

1. To implement background blur, see [useBackgroundBlur](https://aws.github.io/amazon-chime-sdk-component-library-react/?path=/docs/sdk-hooks-usebackgroundblur--page). 

1. For sample code on how to build a custom video experience, see this Amazon Chime SDK sample: [Amazon Chime React Meeting demo](https://github.com/aws-samples/amazon-chime-sdk/tree/main/apps/meeting). 

## Add support for screen sharing
<a name="support-screen-sharing"></a>

**Note**  
If you use the out-of-box CCP directly in your custom agent application make sure `allowFramedScreenSharing` and `allowFramedScreenSharingPopUp` are set to true when you initiate the CCP using [Connect Customer Streams JS](https://github.com/aws/amazon-connect-streams).   
Setting `allowFramedScreenSharing` to true enables the screen sharing button on only one CCP in one window or tab. Setting `allowFramedScreenSharingPopUp` to true launches the screen sharing app in a separate window when the agent chooses the screen sharing button. For more detail, see the [Connect Customer Streams JS](https://github.com/aws/amazon-connect-streams) documentation.

Complete the following steps to enable screen sharing on your custom agent desktops. 

1. Check whether a contact has screen sharing capability. 

   ```
   // Return true if any connection has screen sharing send capability
   contact.hasScreenShareCapability()
   
   // Return true if the agent connection has screen sharing send capability
   contact.canAgentSendScreenShare()
   
   // Return true if customer connection has screen sharing send capability
   contact.canCustomerSendScreenShare()
   ```

1. Check whether the agent has video permission.

   ```
   agent.getPermissions().includes('videoContact');
   ```

1. Check whether the agent can initiate a screen sharing session for the eligible contact.

   ```
   fun canStartScreenSharingSession() {
       return contactgetContactSubtype() === "connect:WebRTC" &&
       contact.hasScreenShareCapability() &&
       agent.getPermissions().includes('videoContact');
   }
   ```

1. Call `startScreenSharing` to initiate the screen sharing session. This adds `ScreenSharingActivated` to the contact, enabling you to search for it in the [contact record](ctr-data-model.md). 

   ```
   contact.startScreenSharing();
   ```

1. Call `getVideoConnectionInfo` to join the session. You can skip the step if the agent has joined the video session to handle video.

   ```
   if (canStartScreenSharingSession) {
       contact.startScreenSharing();
       const response = await
       contact.getAgentConnection().getVideoConnectionInfo();
   }
   ```

1. Join the session by using the Amazon Chime SDK React Components Library. For a code snippet, see step 6 in [Add support for video](#support-video).

1. Use the same [VideoTileGrid](https://aws.github.io/amazon-chime-sdk-component-library-react/?path=/docs/sdk-components-videotilegrid--page) from the Amazon Chime SDK React Components to render screen sharing video tile. For more information, see [useContentShareState](https://aws.github.io/amazon-chime-sdk-component-library-react/?path=/docs/sdk-hooks-usecontentsharestate--page) and [useContentShareControls](https://aws.github.io/amazon-chime-sdk-component-library-react/?path=/docs/sdk-hooks-usecontentsharecontrols--page) 

1. Call `stopScreenSharing` when end the session.

   ```
   contact.stopScreenSharing();
   ```

1. You can receive events for the screen sharing activity by subscribing the following callbacks:

   ```
   initScreenSharingListeners() {
       this.contact.onScreenSharingStarted(() => {
           // Screen sharing session started
       });
   
       this.contact.onScreenSharingStopped(() => {
           // Screen sharing session ended
       });
   
       this.contact.onScreenSharingError((error) => {
           // Screen sharing session error occurred
       });
     }
   }
   ```