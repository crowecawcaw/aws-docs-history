# USB Devices

The following sections provide information about WorkSpaces Applications support for USB
devices.

###### Contents

- [USB Redirection](#feature-support-USB-devices-USB-redirection "#feature-support-USB-devices-USB-redirection")
- [Smart Cards](#feature-support-USB-devices-qualified-smart-cards "#feature-support-USB-devices-qualified-smart-cards")

## USB Redirection

USB redirection is required for most local USB devices to be used
during WorkSpaces Applications streaming sessions. When USB redirection is required, you
must [qualify the device](qualify-usb-devices.md "qualify-usb-devices.md")
before your users can use it during their WorkSpaces Applications streaming sessions.
After you qualify the device, users must [share the device with WorkSpaces Applications](client-application-windows-how-to-share-usb-devices-user.md "client-application-windows-how-to-share-usb-devices-user.md"). With USB redirection, during
WorkSpaces Applications streaming sessions, users' devices are not accessible for use
with local applications.

In other cases, USB devices are already enabled for use with WorkSpaces Applications
and no further configuration is required. For example, smart card
redirection is already enabled by default when the WorkSpaces Applications client is
installed. Because USB redirection isn't used when this feature is
enabled, you don't need to qualify smart card readers, and users don't
need to share these devices with WorkSpaces Applications to use them during streaming
sessions.

###### Note

USB redirection is currently not supported for Linux-based fleet
instances, or when using the WorkSpaces Applications macOS client application.

## Smart Cards

WorkSpaces Applications supports using a smart card for Windows sign in to Active
Directory-joined streaming instances and in-session authentication for
streaming applications. Because smart card redirection is
enabled by default, users can use smart card readers that are connected
to their local computer and their smart cards without USB redirection.

###### Contents

- [Windows Sign In and In-Session Authentication](#feature-support-USB-devices-qualified-smart-cards-windows-signin-in-session-auth "#feature-support-USB-devices-qualified-smart-cards-windows-signin-in-session-auth")
- [Smart Card Redirection](#feature-support-USB-devices-qualified-smart-cards-support "#feature-support-USB-devices-qualified-smart-cards-support")

### Windows Sign In and In-Session Authentication

WorkSpaces Applications supports the use of Active Directory domain passwords or smart cards such as [Common Access Card (CAC)](https://www.cac.mil/Common-Access-Card "https://www.cac.mil/Common-Access-Card")
and [Personal Identity Verification (PIV)](https://piv.idmanagement.gov/ "https://piv.idmanagement.gov/")
smart cards for Windows sign in to WorkSpaces Applications streaming instances (fleets and image builders). Your users can use smart card readers connected to their local computer and their smart cards to sign in to an WorkSpaces Applications streaming instance that is joined to a
Microsoft Active Directory domain. They can also use their local smart card readers and smart cards to sign in to
applications within their streaming session.

To ensure that your users can use their smart cards for Windows sign in to Active Directory-joined streaming instances and for
in-session authentication for streaming applications, you must:

- Use an image that meets the following requirements:
  - The image must be created from a base image published by AWS on or after December 28, 2020. For more information, see [WorkSpaces Applications Base Image and Managed Image Update Release Notes](base-image-version-history.md "base-image-version-history.md").
  - The image must use a version of the WorkSpaces Applications agent released on or after January 4, 2021. For
    more information, see [WorkSpaces Applications Agent Release Notes](agent-software-versions.md "agent-software-versions.md").

- Enable **Smart card sign in for Active Directory** on the WorkSpaces Applications stack that your users access for streaming sessions, as described in this section.

###### Note

This setting controls only the authentication method that can be used for Windows sign in to
an WorkSpaces Applications streaming instance (fleet or image builder).
It doesn't control the authentication method that can be
used for in-session authentication, after a user signs
in to a streaming instance.

- Ensure that your users have WorkSpaces Applications client version 1.1.257 or later
  installed. For more information, see [WorkSpaces Applications Windows Client Release Notes](client-release-versions.md "client-release-versions.md").

By default, password sign in for Active Directory is enabled on WorkSpaces Applications stacks. You can enable smart card sign in for Active Directory by performing the following steps in the WorkSpaces Applications console.

###### To enable smart card sign in for Active Directory by using the WorkSpaces Applications console

1. Open the WorkSpaces Applications console at
   [https://console.aws.amazon.com/appstream2/home](https://console.aws.amazon.com/appstream2/home "https://console.aws.amazon.com/appstream2/home").
2. In the left navigation pane, choose
   **Stacks**.
3. Choose the stack for which you want to enable smart card authentication for Active Directory.
4. Choose the **User Settings** tab, and then expand the **Clipboard,
   file transfer, print to local device, and authentication permissions**
   section.
5. For **Smart card sign in for Active Directory**, choose **Enabled**.

You can also enable **Password sign in for Active
Directory**, if it's not already enabled. At least one authentication method must be enabled. 6. Choose **Update**.

Alternatively, you can enable smart card sign in for Active Directory by using the WorkSpaces Applications API, an AWS SDK, or the AWS Command Line Interface (AWS CLI).

### Smart Card Redirection

When the WorkSpaces Applications client is installed, smart card redirection is
enabled by default. When this feature is enabled, users can use
smart card readers that are connected to their local computer and
their smart cards during WorkSpaces Applications streaming sessions without USB
redirection. During WorkSpaces Applications streaming sessions, users' smart card
readers and smart cards remain accessible for use with local
applications. The WorkSpaces Applications client redirects the smart card API calls
from users’ streaming applications to their local smart card.

###### Note

Smart card redirection is currently not supported for
Linux-based fleet instances or multi-session fleet instances, or
when using the WorkSpaces Applications macOS client application.

###### Note

If your smart card requires middleware software to operate,
the middleware software must be installed on both the user’s
device, and the WorkSpaces Applications streaming instance.

You can disable smart card redirection during client installation
on managed devices. For more information, see [Choose Whether to Disable Smart Card Redirection](install-client-configure-settings.md#disable-local-smart-card-support-client "install-client-configure-settings.md#disable-local-smart-card-support-client"). If
you disable smart card redirection, your users can't use their smart
card reader and smart card during an WorkSpaces Applications streaming session
without USB redirection. In this case, you must [qualify the device](qualify-usb-devices.md "qualify-usb-devices.md"). After
you qualify the device, users must [share the device with WorkSpaces Applications](client-application-windows-how-to-share-usb-devices-user.md "client-application-windows-how-to-share-usb-devices-user.md"). When smart card
redirection is disabled, during users' WorkSpaces Applications streaming sessions,
their smart card reader and smart card are not accessible for use
with local applications.
