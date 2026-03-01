# Troubleshooting WorkSpaces Applications User Issues

## Enable advanced logging

To help troubleshoot issues that your users might experience, you can enable
advanced logging on any WorkSpaces Applications client. Advanced logging generates log files that
contain diagnostic information and debugging-level details, including verbose
performance data.

###### Note

To get an AWS review of advanced logging files, and receive technical support for issues
with your WorkSpaces Applications clients, contact Support. For more information, see the [AWS Support Center Console](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

### Enable advanced logging for web access

If users are using SAML, User Pool, or have access to the Application
Catalogue page, follow these steps:

1. Load the catalog page.
2. Open **Developer tools** and choose the
   **Console** tab.
3. In the browser console, enter `window.siteConfig.logLevel =
"INFO"` and choose **Enter**.
4. Launch the application, and you should see
   **Logging** on the **Console**
   tab.
5. Reproduce the issue.
6. Right-click on the **Console** tab and choose
   **Save all Messages to File**.

### Enable advanced logging for Windows clients

To enable advanced logging for Windows clients, follow these steps:

1. On the client machine, go to
   `%localappdata%\AppStreamClient\app-<versionID>`.
2. Open `Log4Net.config` in Notepad.
3. Change the root level of logging from **INFO** to
   **DEBUG**.
4. Save the file.
5. Restart the WorkSpaces Applications Client and try connecting again.
6. Gather the logs from
   `C:\Users\%USERNAME%\AppData\Local\Amazon\AppStreamClient\'`
   by zipping the complete folder.

The following are specific issues that might occur for your users when they use
WorkSpaces Applications.

###### Issues

- [My users' WorkSpaces Applications client installations fail, and they're getting a message stating that .NET Framework 4.6 is required.](#troubleshooting-client-no-internet-net-framework-462-fails "#troubleshooting-client-no-internet-net-framework-462-fails")
- [My users' USB driver installations fail when they install the WorkSpaces Applications client, and now they can't use their USB devices with WorkSpaces Applications.](#troubleshooting-client-no-internet-usb-driver-install-fails "#troubleshooting-client-no-internet-usb-driver-install-fails")
- [My WorkSpaces Applications client users are getting disconnected from their WorkSpaces Applications session after every 60 minutes.](#troubleshooting-client-users-disconnected-every-60-minutes "#troubleshooting-client-users-disconnected-every-60-minutes")
- [My users can’t copy and paste between their local device and their streaming session.](#copy-paste-doesnt-work "#copy-paste-doesnt-work")
- [Some keyboard shortcuts aren’t working for users during their streaming sessions.](#keyboard-shortcuts-dont-work "#keyboard-shortcuts-dont-work")
- [My users' drawing tablets are not working with the streaming applications I deployed.](#troubleshooting-client-users-drawing-tablets-not-working "#troubleshooting-client-users-drawing-tablets-not-working")
- [The Japanese language input method doesn't work for my users during their streaming sessions](#japanese-language-input-method-doesnt-work-for-users "#japanese-language-input-method-doesnt-work-for-users")
- [My user sees an error about reaching the max number of streaming sessions when they try to launch an application from the application catalog.](#troubleshooting-max-sessions "#troubleshooting-max-sessions")
- [My user sees a black screen or the desktop, and their application doesn’t launch on an Elastic fleet. No error appears.](#troubleshooting-black-screen "#troubleshooting-black-screen")

## My users' WorkSpaces Applications client installations fail, and they're getting a message stating that .NET Framework 4.6 is required.

When users install the WorkSpaces Applications client, WorkSpaces Applications also installs .NET Framework version
4.6.2, if that version or a later version is not already installed. If the PC on
which the client is being installed is not connected to the internet, .NET Framework
can't be installed. In this case, a message prompts users to install .NET Framework
version 4.6 manually. However, when users choose **Install**, an
error message is displayed stating that the installation failed. Users are then
prompted to try installing the latest version of the .NET Framework manually. When
they choose **Close**, they exit the installation.

To resolve this issue, users must establish an internet connection from the PC on which they plan to install the client, and then download and install .NET Framework version 4.6.2 or later on the same PC. For a list of the .NET Framework versions available for download, see [Download .NET Framework](https://dotnet.microsoft.com/download/dotnet-framework "https://dotnet.microsoft.com/download/dotnet-framework").

###### Note

Users who have version 1.1.156 of the WorkSpaces Applications client installed must have .NET Framework version 4.7.2 or later installed on the same PC.

## My users' USB driver installations fail when they install the WorkSpaces Applications client, and now they can't use their USB devices with WorkSpaces Applications.

When users install the WorkSpaces Applications client, they choose whether to install the WorkSpaces Applications
USB driver. The driver is required to use USB devices with applications streamed
through WorkSpaces Applications. However, the USB driver installation fails if both of the following
occur:

- The root certificate used to sign the `AppStreamUsbDriver.exe` file is not
  present in the Windows certificate store.
- The PC on which the client is being installed is not connected to the internet.

In this case, the certificate for the Amazon AppStream USB driver can't be validated, and
an error message notifies users that the USB driver installation failed. When users
choose **OK**, the WorkSpaces Applications client installation is completed without
the USB driver. Although users can still use the WorkSpaces Applications client for application
streaming, their USB devices won't work with applications streamed through WorkSpaces Applications.

To resolve this issue, users must establish an internet connection from the PC on which they plan to install the WorkSpaces Applications client, and reinstall the client.

## My WorkSpaces Applications client users are getting disconnected from their WorkSpaces Applications session after every 60 minutes.

If you have configured identity federation using SAML 2.0 for access to WorkSpaces Applications,
depending on your identity provider (IdP), you may need to configure the information
that the IdP passes as SAML attributes to AWS as part of the authentication
response. This includes configuring the **Attribute** element with
the `SessionDuration` attribute set to
`https://aws.amazon.com/SAML/Attributes/SessionDuration`.

`SessionDuration` specifies the maximum amount of time that a federated streaming session for a user can remain active before reauthentication is required. Although `SessionDuration` is an optional attribute, we recommend that you include it in the SAML authentication response. If you do not specify this attribute, the session duration is set to a default value of 60
minutes.

To resolve this issue, configure your SAML-compatible IdP to include the `SessionDuration` value in the SAML authentication response, and set the value as required. For more information, see [Step 5: Create Assertions for the SAML Authentication Response](external-identity-providers-setting-up-saml.md#external-identity-providers-create-assertions "external-identity-providers-setting-up-saml.md#external-identity-providers-create-assertions").

###### Note

If your users access their streaming applications in WorkSpaces Applications by using the WorkSpaces Applications native client
or by using the web browser on the new experience, their sessions are
disconnected after their session duration expires. If your users access their
streaming applications in WorkSpaces Applications by using a web browser on the old/classic
experience, after the users' session duration expires and they refresh their
browser page, their sessions are disconnected.

If your users sign in to the new portal experience with a SAML-compatible IdP, and
they continue to have random disconnections, it might be due to the session cookies
used by the WorkSpaces Applications session being invalidated by other web applications using
`aws.amazon.com` as a subdomain. The following are common user
scenarios:

- If a user initiates a new WorkSpaces Applications session in the same browser, the existing
  WorkSpaces Applications session will be disconnected.
- If a user initiates any other web applications in the same browser,
  resulting in a new user authentication under the `aws.amazon.com`
  domain, the existing WorkSpaces Applications session will be disconnected.
- If a user signs into an AWS Management Console with new IAM credentials in the same
  browser, the existing WorkSpaces Applications session will be disconnected.

You can resolve this issue by using the new relay state endpoints to configure your
SAML 2.0 federation, and by using the WorkSpaces Applications client version 1.1.1300 and later. For
more information, see Table 1 on [Step 6: Configure the Relay State of Your Federation](external-identity-providers-setting-up-saml.md#external-identity-providers-relay-state "external-identity-providers-setting-up-saml.md#external-identity-providers-relay-state").

## My users can’t copy and paste between their local device and their streaming session.

WorkSpaces Applications takes advantage of the [W3C
specification](https://www.w3.org/TR/2017/WD-clipboard-apis-20170929/ "https://www.w3.org/TR/2017/WD-clipboard-apis-20170929/") for enabling asynchronous clipboard operations in web
applications. This enables users to copy and paste content between their local
device and their streaming session in the same ways that they copy and paste between
applications on their local device, including using keyboard shortcuts.

The only browser that currently supports the W3C asynchronous clipboard
specification is Google Chrome version 66 or later, which supports copying and
pasting only for text. For all other browsers, users can use the clipboard feature
in the WorkSpaces Applications web portal, which provides a dialog box for copying or pasting
text.

If your users run into issues using the clipboard during their streaming sessions,
you can provide them with the following information:

- **I’m using Chrome version 66 or later, and keyboard shortcuts aren’t working.**

Chrome displays a prompt for you to choose whether to allow WorkSpaces Applications to access content copied to
the clipboard. Choose **Allow** to enable pasting to your
remote session. If you’re copying text from your remote session to your
local device, both the Chrome application and the tab containing your
streaming session must stay in focus on your local device long enough for
the text to be copied from your streaming session. Small amounts of text
should be copied almost immediately, but for large amounts of text, you
might need to wait 1 to 2 seconds before switching away from Chrome or from
the tab containing your streaming session. The time required to copy the
text varies based on network conditions.

- **Copying and pasting doesn’t work when I try to copy and paste a large amount of text.**

WorkSpaces Applications has a default limit of 20 MB for the amount of text that you can copy and paste between
your local device and your streaming session. If you try to copy more than
20 MB, no text is copied. However, the text will be truncated if your admin
set a limit and you go beyond that limit. This limit doesn’t apply if you
try to copy and paste text between applications on your local device or
between applications in your streaming session. Administrators can also
limit the number of characters that you copy/paste in/out of your streaming
sessions. If you need to copy or paste text more than 20 MB or the specified
limit between your local device and your streaming session, you can divide
it into smaller chunks or upload it as a file instead.

- **I’m using the WorkSpaces Applications web portal clipboard feature to paste text to my streaming session and it’s not working.**

In some cases, after you paste text into the clipboard dialog box and the dialog box closes,
nothing happens when you try to use keyboard shortcuts to paste the text in
your streaming session. This issue occurs because when the clipboard dialog
box appears, it takes the focus away from your streaming application. After
the dialog box closes, the focus might not automatically return to your
streaming application. Clicking your streaming application should return the
focus to it and enable you to use keyboard shortcuts to paste your text into
your streaming session.

## Some keyboard shortcuts aren’t working for users during their streaming sessions.

The following keyboard shortcuts work on users' local computers, but are not
passed to WorkSpaces Applications streaming sessions:

Windows:

- Win+L
- Ctrl+Alt+Del

Mac:

- Ctrl+F3
- All shortcuts that use Alt or Option key combinations

This issue is due to the following limitations on users’ local computers:

- The keyboard shortcuts are filtered by the operating system that is running on users’ local
  computers and not propagated to the browsers on which users are accessing
  WorkSpaces Applications. This behavior applies to the Windows Win+L and Ctrl+Alt+Del keyboard
  shortcuts and Mac Ctrl+F3 keyboard shortcut.
- When used with web applications, some keyboard shortcuts are filtered by the browser and don’t generate an event for the web applications. As a result, the web applications can’t respond to the keyboard shortcuts typed by users.
- The keyboard shortcuts are translated by the browser before a keyboard event is generated and
  so are not translated correctly. For example, Alt key combinations and
  Option key combinations on Mac computers are translated as if they are Alt
  Graph key combinations on Windows. When this occurs, the results are not as
  the users intend when they use these key combinations.

## My users' drawing tablets are not working with the streaming applications I deployed.

If your users' drawing tablets are not working with streaming applications, make
sure that you meet the requirements and understand additional considerations for
enabling this feature. Following are the requirements and considerations for
enabling your users to use drawing tablets during WorkSpaces Applications streaming sessions.

###### Note

Drawing tablets are supported for users who access WorkSpaces Applications by using the WorkSpaces Applications client, or through a supported web browser.

- To enable your users to use this feature, you must configure your WorkSpaces Applications fleet to use an image that runs Windows Server 2019.
- To use this feature, users must access WorkSpaces Applications by using the WorkSpaces Applications client, or through the Google Chrome or Mozilla Firefox browsers only.
- Streaming applications must support Windows Ink technology. For more information, see [Pen interactions and Windows Ink in Windows apps](https://docs.microsoft.com/en-us/windows/uwp/design/input/pen-and-stylus-interactions "https://docs.microsoft.com/en-us/windows/uwp/design/input/pen-and-stylus-interactions").
- Some applications, such GIMP, must detect drawing tablets on the streaming instance to support
  pressure sensitivity. If this is the case, your users must use the
  WorkSpaces Applications client to access WorkSpaces Applications and stream these applications. In
  addition, you must qualify your users' drawing tablets, and users
  must share their drawing tablets with WorkSpaces Applications every time they start a
  new streaming session.
- This feature is not supported on Chromebooks.

## The Japanese language input method doesn't work for my users during their streaming sessions

To enable your users to use the Japanese language input method during their WorkSpaces Applications streaming sessions, do the following:

- Configure your fleet to use the Japanese input method. To do so, enable the Japanese input method on your image builder when you create an image, and then configure your fleet to use the image. For more information, see [Specify a Default Input Method](configure-default-input-method.md "configure-default-input-method.md"). Doing so enables WorkSpaces Applications to automatically configure your image to use a Japanese keyboard. For more information, see [Japanese Keyboards](special-considerations-japanese-language-settings.md#special-considerations-japanese-language-keyboards "special-considerations-japanese-language-settings.md#special-considerations-japanese-language-keyboards").
- Ensure that the Japanese input method is also enabled on the user's local computer.

If the fleet instance and the user’s local computer don't use the same language input method, the mismatch might result in unexpected keyboard inputs on the fleet instance during the user’s streaming sessions. For example, if the fleet instance uses the Japanese input method and the user’s local computer uses the English input method, during a streaming session, the local computer will send keys to the fleet instance that have different key mappings than the fleet instance.

To verify whether the Japanese input method is enabled for a fleet instance, enable the **Desktop** stream view for the fleet. For more information, see Step 6 in [Create a Fleet in Amazon WorkSpaces Applications](set-up-stacks-fleets-create.md "set-up-stacks-fleets-create.md").

### Windows Keyboard Shortcuts

Following are Windows keyboard shortcuts for switching Japanese input modes and for Japanese conversions. For these keyboard shortcuts to work, the WorkSpaces Applications streaming session must be active.

**Windows keyboard shortcuts for switching Japanese input modes**

| Keyboard shortcut                                              | Description                                                                               |
| -------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| 半角/全角/漢字<br>(Hankaku/Zenkaku/Kanji)<br>Or Alt+`          | Switches the input mode between alphanumeric and Japanese mode                            |
| 無変換<br>(Muhenkan)                                           | Converts characters to Hiragana, full-width Katakana, and half-width Katakana in sequence |
| カタカナ/ひらがな/ローマ字<br>(Katakana/Hiragana/Romaji)       | Changes the input mode to Hiragana                                                        |
| Shift+カタカナ/ひらがな/ローマ字<br>(Katakana/Hiragana/Romaji) | Changes the input mode to Katakana                                                        |
| Alt+カタカナ/ひらがな/ローマ字<br>(Katakana/Hiragana/Romaji)   | Switches the input mode between Japanese Romaji and Japanese Kana                         |

**Windows keyboard shortcuts for Japanese conversions**

| Keyboard shortcut     | Description                     |
| --------------------- | ------------------------------- |
| 変換 (Henkan) + Space | Lists conversion options        |
| F6                    | Converts to Hiragana            |
| F7                    | Converts to full-width Katakana |
| F8                    | Converts to half-width Katakana |
| F9                    | Converts to full-width Romaji   |
| F10                   | Converts to half-width Romaji   |

### Mac Keyboard Shortcuts

For information about Mac keyboard shortcuts for switching Japanese input methods and for Japanese conversions, see the following articles in the Mac Support documentation.

###### Note

Because WorkSpaces Applications streaming sessions run on Windows instances, Mac users might experience different key mappings.

- Keyboard shortcuts for switching Japanese input methods — [Set up and switch to a Japanese input source on Mac](https://support.apple.com/guide/japanese-input-method/set-up-and-switch-to-japanese-jpim10267/mac "https://support.apple.com/guide/japanese-input-method/set-up-and-switch-to-japanese-jpim10267/mac")
- Keyboard short link cuts for Japanese conversions — [Keyboard shortcuts for Japanese conversions on Mac](https://support.apple.com/guide/japanese-input-method/keyboard-shortcuts-jpim10263/6.2.1/mac "https://support.apple.com/guide/japanese-input-method/keyboard-shortcuts-jpim10263/6.2.1/mac")

## My user sees an error about reaching the max number of streaming sessions when they try to launch an application from the application catalog.

With WorkSpaces Applications Elastic fleets, you specify a maximum number of users that can stream
concurrently using the max concurrency parameter. Any user that tries to stream
beyond that value receives this error. To resolve this issue, you can increase the
maximum number of concurrent streams, or advise your user to wait for another user
to complete their streaming session.

###### Note

You might need to request a limit increase to increase the instance type and
size limit.

## My user sees a black screen or the desktop, and their application doesn’t launch on an Elastic fleet. No error appears.

This can happen if the application launch path is incorrect, and AppStream 2.0 can't
launch the application. You can validate the application launch path by using
Desktop View on the fleet to navigate the root volume. Validate that the application
executable exists at the path specified.

If you're not able to find the app block's VHD or setup script on the streaming
instance, AppStream 2.0 might not have been able to download them from the S3
bucket. Validate that the VPC you specified has access to S3. For more information,
see [Using Amazon S3 VPC Endpoints for WorkSpaces Applications Features](managing-network-vpce-iam-policy.md "managing-network-vpce-iam-policy.md").
