# Real-Time Audio-Video

AppStream 2.0 supports real-time audio-video (AV) by redirecting local webcam
video input to AppStream 2.0 streaming sessions. This capability enables your users
to use their local webcam for video and audio conferencing within an AppStream 2.0
streaming session. With real-time AV and support for real-time audio, your
users can collaborate by using familiar video and audio conferencing
applications without having to leave their AppStream 2.0 streaming session.

When a user starts a video conference from within an AppStream 2.0 streaming
session, AppStream 2.0 compresses the webcam video and microphone audio input
locally before transmitting this data over a secure channel to a streaming
instance. During their streaming sessions, users can enable audio and video
input by using the AppStream 2.0 toolbar. If users have more than one webcam (for
example, if they have a USB webcam that is connected to their local computer
and a built-in webcam), they can also choose which webcam to use during
their streaming session.

###### Note

For multi-session fleets, only in/out functionalities are accessible.
Video in (webcam support) is not yet available for multi-session
fleets.

To configure and test support for real-time AV, complete the following
steps.

###### Configure and test support for real-time AV

1.  Create a new image builder or connect to an existing image builder
    that meets the following requirements:

        * The image builder must run Windows Server 2016 or Windows
         Server 2019.
        * The image builder must use a version of the AppStream 2.0 agent
         released on or after June 1, 2021.
        * For AppStream 2.0 agents released on or after May 17, 2021,
         real-time AV is enabled by default. To create a streaming
         URL for testing, you can skip steps 3 through 6 and
         disconnect from the image builder. If you need to disable
         real-time AV, complete all of the steps, and disable webcam
         permissions in step 4.
        * The image builder must use a version of the AppStream 2.0 agent
         released on or after June 24, 2021 to support video when
         connecting using web browser access. For more information
         about supported web browsers, see [Web Browser Access](web-browser-user.md "web-browser-user.md").

    For information about how to create an image builder, see [Launch an Image Builder to Install and Configure Streaming Applications](tutorial-image-builder-create.md "tutorial-image-builder-create.md").

2.  Connect to the image builder that you want to use and sign in as
    Administrator. To connect to the image builder, do either of the
    following:
    - [Use the AppStream 2.0 console](managing-image-builders-connect-console.md "managing-image-builders-connect-console.md") (for web connections
      only)
    - [Create a streaming URL](managing-image-builders-connect-streaming-URL.md "managing-image-builders-connect-streaming-URL.md") (for web or AppStream 2.0 client
      connections)

    ###### Note

    If the image builder that you want to connect to is
    joined to an Active Directory domain and your
    organization requires smart card sign in, you must
    create a streaming URL and use the AppStream 2.0 client for the
    connection. For information about smart card sign in,
    see [Smart Cards](feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards "feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards").

3.  On the image builder, open Registry Editor. To do so, on the image
    builder desktop, in the search box on the taskbar, type
    `regedit`. Then, select the top result for
    **Registry Editor**.
4.  Under
    \*\*HKEY_LOCAL_MACHINE\SOFTWARE\Amazon\AppStream\*\*,
    create a new registry value that has the following type, name, and
    value data:
    - Registry value type: DWORD
    - Registry value name: WebcamPermission
    - Registry value data (Hexademical): 1 to enable or 0 to
      disable webcam permissions

5.  After you create the registry value, switch to **Template
    User** or to a domain account that does not have
    administrator permissions on the image builder. To switch to
    **Template User**, in the toolbar on the top
    right of the session window, choose **Admin
    Commands**, **Switch User**,
    **Template User**.
6.  Switch back to **Administrator**.
7.  Disconnect from the image builder and create a streaming URL for
    the image builder. To do so:
    1. Open the AppStream 2.0 console at
       [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
    2. In the navigation pane, choose
       **Images**, then choose **Image
       Builder**.
    3. Select the image builder from which you just disconnected,
       and choose **Actions**, **Create
       streaming URL**.
    4. Choose **Copy Link** and save the link to
       a secure and accessible location. You will use the link in
       the next step to connect to the image builder.

8.  Using the streaming URL that you just created, connect to the
    image builder by using the AppStream 2.0 client or web browser
    access.
9.  Test the real-time AV experience on the image builder by following
    the steps in [Video
    and Audio Conferencing](client-application-windows-how-to-use-local-webcam-user.md "client-application-windows-how-to-use-local-webcam-user.md").
10. After you verify that real-time AV is working as expected,
    disconnect from your streaming session, reconnect to the image
    builder and follow the necessary steps in Image Assistant to finish
    creating your image. For information about how to create an image,
    see [Tutorial: Create a Custom AppStream 2.0 Image by Using the
    AppStream 2.0 Console](tutorial-image-builder.md "tutorial-image-builder.md").
    After you finish configuring your image builder and creating an image that
    supports real-time AV, you can make this feature available to your users on
    AppStream 2.0 fleets. Ensure that version 1.1.257 or later of the AppStream 2.0 client is
    installed on your users' computers.

###### Note

To use real-time AV with the AppStream 2.0 client, your AppStream 2.0 base image and
agent version should be June 1, 2021 or later. We recommend using the
latest AppStream 2.0 client. For guidance that you can provide to your users to
help them use real-time AV, see [Video
and Audio Conferencing](client-application-windows-how-to-use-local-webcam-user.md "client-application-windows-how-to-use-local-webcam-user.md").

To use real-time AV with web browser access, your AppStream 2.0 image must
use a version of the AppStream 2.0 agent released on or after June 24, 2021.
For more information on supported web browsers, see [Web Browser Access](web-browser-user.md "web-browser-user.md").
