**End of support notice**: On February
20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will
no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more
information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/ "https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/"). **Note:** This does not impact the
availability of the [Amazon Chime SDK
service](https://aws.amazon.com/chime/chime-sdk/ "https://aws.amazon.com/chime/chime-sdk/").

# Understanding Amazon Chime automatic updates

Amazon Chime provides different ways to update its clients. The method varies, depending on whether your users
run Amazon Chime in a browser, on your desktop, or on a mobile device.

The Amazon Chime web application – [https://app.chime.aws](https://app.chime.aws "https://app.chime.aws") – always loads with
the latest features and security fixes.

The Amazon Chime desktop client checks for updates whenever a user chooses **Quit** or **Sign Out**.
This applies to Windows and macOS machines. As users run the client, it checks for updates every three hours. Users can also check for
updates by choosing **Check for Updates** on the Windows Help menu or on the macOS **Amazon Chime**
menu.

When the desktop client detects an update, Amazon Chime prompts users to install it unless they're in an ongoing
meeting. Users are in an _ongoing meeting_ when:

- They're attending a meeting.
- They were invited to a meeting that is still in progress.
  Amazon Chime prompts them to install the latest version, and it gives them a 15-second countdown so they
  can postpone the installation. Choose **Try Later** to postpone the update.

When users postpone an update, and they aren't in an ongoing meeting, the client checks for the update
after three hours and prompts them again to install. The installation begins when the countdown ends.

###### Note

On a macOS machine, users need to choose **Restart Now** to begin the update.

**On a mobile device** – Amazon Chime mobile applications
use the update options provided by the App Store and Google Play to deliver the
latest version of the Amazon Chime client. You can also distribute updates through your mobile device management system. This topic assumes
that you know how.
