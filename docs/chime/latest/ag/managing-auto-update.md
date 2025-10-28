**End of support notice**: On February
20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will
no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more
information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/ "https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/"). **Note:** This does not impact the
availability of the [Amazon Chime SDK
service](https://aws.amazon.com/chime/chime-sdk/ "https://aws.amazon.com/chime/chime-sdk/").

# How Amazon Chime manages automatic updates

Amazon Chime provides different ways to update its clients. The method varies, depending on whether you
run Amazon Chime in a browser, on your desktop, or on a mobile device.

The Amazon Chime web application – [https://app.chime.aws](https://app.chime.aws "https://app.chime.aws") – always loads with
the latest features and security fixes.

The Amazon Chime desktop client checks for updates whenever you choose **Quit** or **Sign Out**.
This applies to Windows and macOS machines. As you run the client, it checks for updates every three hours. You can also check for
updates by choosing **Check for Updates** on the Windows Help menu or on the macOS **Amazon Chime**
menu.

When the desktop client detects an update, Amazon Chime prompts user to install it unless they're in an ongoing
meeting. They're in an _ongoing meeting_ when:

- They attend a meeting.
- They were invited to a meeting that is still in progress.
  Amazon Chime prompts them to install the latest version, and it provides a 15-second
  countdown so they can postpone the installation. Users choose **Try
  Later** to postpone the update.

If users postpone an update, and they aren't in an ongoing meeting, the client checks for the update
after three hours and prompts them again to install. The installation begins when the countdown ends.

###### Note

On a macOS machine, users need to choose **Restart Now** to begin the update.

**On mobile devices** – Amazon Chime mobile applications
use the update options provided by the App Store and Google Play to deliver the
latest version of the Amazon Chime client. You can also use mobile device management system to deploy updates.
