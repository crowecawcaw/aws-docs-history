# Using a remote access session in AWS Device Farm

For information about performing interactive testing of Android and iOS apps through remote access sessions,
see [Sessions](sessions.md "sessions.md").

- [Prerequisites](#how-to-use-session-prerequisites "#how-to-use-session-prerequisites")
- [Use a session in the Device Farm console](#how-to-use-session-console "#how-to-use-session-console")
- [Next steps](#how-to-use-session-next-steps "#how-to-use-session-next-steps")
- [Tips and tricks](#how-to-use-session-tips "#how-to-use-session-tips")

## Prerequisites

- Create a session. Follow the instructions in [Creating a session](how-to-create-session.md "how-to-create-session.md"), and then return to this page.

## Use a session in the Device Farm console

As soon as the device that you requested for a remote access session becomes available, the console
displays the device screen. The session has a maximum length of 150 minutes. The time remaining in the
session appears in the **Time Left** field near the device name.

### Installing an application

To install an application on the session device, in **Install applications**, select
**Choose File**, and then choose the .apk file (Android) or the .ipa file (iOS)
that you want to install. Applications that you run in a remote access session don't require any test
instrumentation or provisioning.

###### Note

When you upload an app, there's sometimes a delay before the app is available.
A confirmation message will appear to let you know if the app was successfully installed or not.

### Controlling the device

You can interact with the device displayed in the console as you would the actual physical device, by
using your mouse or a comparable device for touch and the device's on-screen keyboard. For Android
devices, there are buttons in **View controls** that function like the
**Home** and **Back** buttons on an Android device. For iOS
devices, there is a **Home** button that functions like the home button on an iOS
device. You can also switch between applications running on the device by choosing **Recent
Apps**.

### Switching between portrait

and landscape mode

You can also switch between portrait (vertical) and landscape (horizontal) mode for the devices that
you're using.

## Next steps

Device Farm continues the session until you stop it manually or the 150-minute time limit is reached. To end the
session, choose **Stop Session**. After the session stops, you can access the video that
was captured and the logs that were generated. For more information, see [Retrieving session results](how-to-access-session-results.md "how-to-access-session-results.md").

## Tips and tricks

You might experience performance issues with the remote access session in some AWS Regions. This is due,
in part, to latency in some Regions. If you experience performance issues, give the remote access session a
chance to catch up before you interact with the app again.
