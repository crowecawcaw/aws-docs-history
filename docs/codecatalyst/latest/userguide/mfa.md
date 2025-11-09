Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Configure your AWS Builder ID to sign in with multi-factor authentication (MFA)

Whether you created your AWS Builder ID profile for personal use or professional use, we
encourage configuring multi-factor authentication (MFA) as another layer of security. We
especially recommend configuring MFA if you’re a member of a space and collaborate with
others on projects. Because more than one person can have access to a project, more
opportunities exist for security breaches.

When you enable MFA, you must sign in to Amazon CodeCatalyst with your email and password. This
portion of signing in is the first factor, where you use something that you know. You then
sign in with either a code or security key. This is the second factor, which is something
that you have. The second factor could be an authentication code that is generated either by
your mobile device or by tapping or pressing a security key connected to your computer.
Taken together, these multiple factors provide increased security by preventing unauthorized
access.

## How to register a device for use with multi-factor authentication

Use the following procedure on **My profile** > **Multi-factor authentication**
to register your new
device for multi-factor authentication (MFA).

###### Note

We recommend that you first download the appropriate authenticator app onto your
device before starting the steps in this procedure. For a list of apps that you can
use for MFA devices, see [Authenticator applications](#id-auth-apps "#id-auth-apps").

###### To register your device for use with MFA

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. At the top right, choose the arrow next to the icon with your first initial,
   and then choose **User profile**. The CodeCatalyst
   **Profile** page opens.
3. On the profile page, choose **Manage profile and security**.
   The **AWS Builder ID** profile page opens.
4. On the left side of the page, choose **Security**.
5. On the **Multi-factor authentication** page, choose
   **Register device**.
6. On the **Register MFA device** page, choose one of the
   following MFA device types, and follow the instructions:
   - **Security key** or **Built-in
     authenticator**
     1. On the **Register your user's security key**
        page, follow the instructions given to you by your browser or
        platform.

     ###### Note

     This experience varies based on your operating system and
     browser, so follow the instructions displayed by your
     browser or platform. After your device has been successfully
     registered, you will be given the option to associate a
     friendly display name to your newly enrolled device. If you
     want to change this, choose **Rename**,
     enter the new name, and then choose
     **Save**.

   - **Authenticator app**
     1. On the **Set up the authenticator app** page,
        you might notice configuration information for the new MFA
        device, including a QR code graphic. The graphic is a
        representation of the secret key that is available for manual
        entry on devices that do not support QR codes.
     2. Using the physical MFA device, do the following:
        1. Open a compatible MFA authenticator app. For a list of
           tested apps that you can use with MFA devices, see [Tested authenticator apps](#id-mfa-types-apps-tested "#id-mfa-types-apps-tested"). If the
           MFA app supports multiple devices, choose the option to
           create a new MFA device.
        2. Determine whether the MFA app supports QR codes, and
           then do one of the following on the **Set up the
           authenticator app** page:
           1. Choose **Show QR code**, and
              then use the app to scan the QR code. For example,
              you might choose the camera icon or choose an
              option similar to **Scan code**.
              Then use the device's camera to scan the
              code.
           2. Choose **show secret key**,
              and then enter that secret key into your MFA
              app.

           ###### Important

           When you configure an MFA device for
           AWS Builder ID, save a copy of the QR code or secret
           key in a secure place. This can help if you lose
           the phone or have to reinstall the MFA
           authenticator app. If either of those things
           happen, you can quickly reconfigure the app to use
           the same MFA configuration.

     3. On the **Set up the authenticator app** page,
        under **Authenticator code**, enter the
        one-time password that currently appears on the physical MFA
        device.

     ###### Important

     Submit your request immediately after generating the code.
     If you generate the code and then wait too long to submit
     the request, the MFA device is successfully associated with
     your AWS Builder ID profile, but the MFA device is out of sync.
     This happens because time-based one-time passwords (TOTP)
     expire after a short period of time. If this happens, you
     can resync the device. 4. Choose **Assign MFA**. The MFA device can now
     start generating one-time passwords and is now ready for
     use.

## Authenticator applications

Authenticator apps are one-time password (OTP)–based third party-authenticators.
Users can use an authenticator application installed on their mobile device or tablet as
an authorized MFA device. The third-party authenticator application must be compliant
with RFC 6238, which is a standards-based TOTP (time-based one-time password) algorithm
capable of generating six-digit authentication codes.

When prompted for MFA, users must enter a valid code from their authenticator app
within the input box presented. Each MFA device assigned to a user must be unique.
Two authenticator apps can be registered for any given user.

### Tested authenticator apps

Although any TOTP-compliant application will work with IAM Identity Center MFA, the
following table lists well-known third-party authenticator apps to choose
from.

| Operating system | Tested authenticator app                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Android          | [Authy](https://play.google.com/store/apps/details?id=com.authy.authy "https://play.google.com/store/apps/details?id=com.authy.authy"), [Duo Mobile](https://play.google.com/store/apps/details?id=com.duosecurity.duomobile "https://play.google.com/store/apps/details?id=com.duosecurity.duomobile"), [LastPass Authenticator](https://play.google.com/store/apps/details?id=com.lastpass.authenticator "https://play.google.com/store/apps/details?id=com.lastpass.authenticator"), [Microsoft Authenticator](https://play.google.com/store/apps/details?id=com.azure.authenticator "https://play.google.com/store/apps/details?id=com.azure.authenticator"), [Google Authenticator](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2 "https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2") |
| iOS              | [Authy](https://apps.apple.com/us/app/authy/id494168017 "https://apps.apple.com/us/app/authy/id494168017"), [Duo Mobile](https://apps.apple.com/us/app/duo-mobile/id422663827 "https://apps.apple.com/us/app/duo-mobile/id422663827"), [LastPass Authenticator](https://apps.apple.com/us/app/lastpass-authenticator/id1079110004 "https://apps.apple.com/us/app/lastpass-authenticator/id1079110004"), [Microsoft Authenticator](https://apps.apple.com/us/app/microsoft-authenticator/id983156458 "https://apps.apple.com/us/app/microsoft-authenticator/id983156458"), [Google Authenticator](https://apps.apple.com/us/app/google-authenticator/id388497605 "https://apps.apple.com/us/app/google-authenticator/id388497605")                                                                                                                                     |

## Changing your MFA devices

After you register an MFA device, you can change its name or delete it. We recommend
always having at least one MFA device enabled for an extra layer of security. You can
have up to five devices registered. To find out how to add more, see [How to register a device for use with multi-factor authentication](#id-how-to-register "#id-how-to-register").

### Renaming an MFA device

###### To rename your MFA device

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. At the top right, choose the arrow next to the icon with your first
   initial, and then choose **User profile**. The CodeCatalyst
   **Profile** page opens.
3. On the profile page, choose **Manage profile and
   security**. The **AWS Builder ID** profile page
   opens.
4. Choose **Multi-factor authentication** on the left side
   of the page. You'll see that **Rename** is grayed out when
   you arrive at the page.
5. Select the MFA device that you want to change. Choose
   **Rename**. Then a modal pops up.
6. In the prompt that opens, enter the new name in **MFA device
   name**, and then choose **Rename**. The
   renamed device appears under **Multi-factor authentication devices
   (MFA)**.

### Deleting an MFA device

###### To delete an MFA device

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. At the top right, choose the arrow next to the icon with your first
   initial, and then choose **User profile**. The CodeCatalyst
   **Profile** page opens.
3. On the profile page, choose **Manage profile and
   security**. The **AWS Builder ID** profile page
   opens.
4. Choose **Multi-factor authentication** on the left side
   of the page. You'll see that **Delete** is grayed out when
   you arrive at the page.
5. Select the MFA device that you want to change. Choose
   **Delete**. A modal appears that says **Delete
   MFA device?**. Follow the instructions to delete your
   device.
6. Choose **Delete**. The deleted device no longer appears
   under **Multi-factor authentication devices (MFA)**.
