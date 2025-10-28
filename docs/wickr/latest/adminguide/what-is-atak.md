This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# What is ATAK?

The Android Team Awareness Kit (ATAK)—or Android Tactical Assault Kit (also ATAK) for
military use—is a smart phone geospatial infrastructure and situational awareness
application that enables safe collaboration over geography. While it was initially designed
for use in combat zones, ATAK has been adapted to fit the missions of local, state, and
federal agencies.

###### Topics

- [Enable ATAK in the Wickr Network Dashboard](#atak "#atak")
- [Additional information about ATAK](#additional-information "#additional-information")
- [Install and pair the Wickr plugin for ATAK](install-and-pair.md "install-and-pair.md")
- [Unpair the Wickr Plugin for ATAK](unpair.md "unpair.md")
- [Dial and receive a call in ATAK](dial-and-receive-call.md "dial-and-receive-call.md")
- [Send a file in ATAK](send-a-file.md "send-a-file.md")
- [Send a secure voice message (Push-to-talk)
  in ATAK](send-secure-voice-message.md "send-secure-voice-message.md")
- [Pinwheel (Quick Access) for ATAK](pinwheel.md "pinwheel.md")
- [Navigation for ATAK](navigation.md "navigation.md")

## Enable ATAK in the Wickr Network Dashboard

AWS Wickr supports many agencies that use Android Tactical Assault Kit (ATAK).
However, until now, ATAK operators that use Wickr have had to leave the application in
order to do so. To help reduce disruptions and operational risk, Wickr has developed a
plugin that enhances ATAK with secure communication features. With the Wickr plugin
for ATAK, users can message, collaborate, and transfer files on Wickr within the ATAK
application. This eliminates interruptions, and the complexity of configuration with
ATAK’s chat features.

### Enable ATAK in the Wickr Network Dashboard

Complete the following procedure to enable ATAK in the Wickr Network
Dashboard.

1. Open the AWS Management Console for Wickr at [https://console.aws.amazon.com/wickr/](https://console.aws.amazon.com/wickr/ "https://console.aws.amazon.com/wickr/").
2. On the **Networks** page, select the network name to
   navigate to that network.
3. In the navigation pane, choose
   **Security groups**.
4. On the **Security groups** page, select the desired
   security group for which you want to enable ATAK.
5. On the **Integration** tab, in the **ATAK
   plugin** section, choose **Edit**.
6. On the **Edit ATAK plugin** page, select the checkbox
   **Enable ATAK plugin**.
7. Choose **Add new package**
8. Enter the package name in the **Packages** text
   box. You can enter one of the following values depending on the
   version of the ATAK that your users will install and use:
   - `com.atakmap.app.civ` — Enter this value
     into the **Packages** text box if your
     Wickr end users are going to install and use the civilian
     version of the ATAK application on their Android
     devices.
   - `com.atakmap.app.mil` — Enter this value
     into the **Packages** text box if your
     Wickr end users are going to install and use the military
     version of the ATAK application on their Android
     devices.

9. Choose **Save**.

ATAK is now enabled for the selected Wickr Network, and the selected
Security Group. You should ask the Android users in the security group for
which you enabled the ATAK functionality to install the Wickr plugin for
ATAK. For more information, see [Install and pair the Wickr ATAK
plugin](../userguide/atak.md "../userguide/atak.md").

## Additional information about ATAK

For more information about the Wickr plugin for ATAK, see the following:

- [Wickr ATAK Plugin Overview](https://wickr.com/wp-content/uploads/2022/12/Wickr-ATAK-Plugin-Overview.pdf "https://wickr.com/wp-content/uploads/2022/12/Wickr-ATAK-Plugin-Overview.pdf")

- [Additional Wickr ATAK Plugin
  Information](http://wickr.com/atak-plugin "http://wickr.com/atak-plugin")
