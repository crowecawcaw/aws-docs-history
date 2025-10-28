# Smart card authentication for WorkSpaces client

Smart cards are supported using the DCV for Windows and Amazon Linux 2 WorkSpaces, on Windows and macOS clients.
WorkSpaces using the PCoIP protocol do not support smart cards. Ubuntu, Rocky Linux, and Red Hat Enterprise Linux WorkSpaces
do not currently support smart cards on any protocol.

You can use smart cards for both _pre-session authentication_ and
_in-session authentication_. Authentication is the process of
verifying your identity and confirming that you have access to certain resources.
Pre-session authentication refers to smart card authentication that's performed while you're
logging in to your WorkSpace. In-session authentication refers to authentication that's
performed during your WorkSpace session, after you log in.

For example, you can use smart cards for in-session authentication while working with web
browsers and applications. You can also use smart cards for performing actions that require
administrative permissions. For example, if you have administrative permissions on your
Linux WorkSpace, you can use smart cards to authenticate yourself when running
`sudo` and `sudo -i` commands.

###### Note

- Both [Common Access Card (CAC)](https://www.cac.mil/Common-Access-Card/ "https://www.cac.mil/Common-Access-Card/")
  and [Personal Identity Verification Card 101](https://www.idmanagement.gov/university/piv/ "https://www.idmanagement.gov/university/piv/") smart
  cards are supported. Other types of hardware or software-based smart cards might also work, but
  they haven't been fully tested for use with the DCV protocol.
- For in-session authentication and pre-session authentication on Linux or Windows WorkSpaces, only
  one smart card is currently allowed at a time.
- In-session authentication is available in all Regions where DCV is supported.
  Pre-session authentication is available in the following
  Regions:
  - Asia Pacific (Sydney) Region
  - Asia Pacific (Tokyo) Region
  - Europe (Ireland) Region
  - AWS GovCloud (US-East) Region
  - AWS GovCloud (US-West) Region
  - US East (N. Virginia) Region
  - US West (Oregon) Region

- Only the WorkSpaces Windows client application version 3.1.1 or later and the macOS client
  application version 3.1.5 or later are currently supported for smart card authentication.
- The WorkSpaces Windows client application 3.1.1 or later supports smart cards only when the client is
  running on a 64-bit version of Windows.

###### Contents

- [Use a smart card to log in to your WorkSpace](#smart-card-login "#smart-card-login")
- [Use a smart card with Chrome or Firefox on Windows WorkSpaces (in-session)](#smart-card-windows-browsers "#smart-card-windows-browsers")
- [Use a smart card with Chrome or Firefox on Linux WorkSpaces (in-session)](#smart-card-linux-browsers "#smart-card-linux-browsers")

## Use a smart card to log in to your WorkSpace

###### To use your smart card to log in to your WorkSpace

1. Enter the registration code provided by your WorkSpaces administrator, and then choose
   **Register**. You might need to choose **Change Registration Code**
   at the bottom of the login page so that you can enter a new registration code.

After you've entered your registration code, **Insert your smart card** appears
on the login page. If you don't see this text, verify that you've entered the correct registration code.
If you've entered the correct registration code and you don't see this text, contact your WorkSpaces
administrator for help. 2. If you haven't done so already, plug your smart card reader into your local machine, and then insert
your smart card into your smart card reader. 3. On the login page, choose **Insert your smart card**. 4. The **Certificates** dialog box appears. Select your certificate, and then choose
**OK**. 5. The **Smart Card** dialog box appears. Enter your PIN, and then choose
**OK**. 6. On the Windows desktop login page, choose **Sign-in options**, then choose the smart card icon.
If you have multiple smart cards, choose the one you want to use. Enter
your PIN again, then choose **Submit**. On the Linux login page, enter your PIN and choose **Sign In**.

You should be logged in to your WorkSpace. If you're unable to sign in, close and reopen the WorkSpaces client
application, and then try again. After trying again, if you still aren't able to sign in, contact your WorkSpaces
administrator for help.

After you have logged in to your WorkSpace, you can continue to use the smart card on your local device as well
as in the WorkSpace.

## Use a smart card with Chrome or Firefox on Windows WorkSpaces (in-session)

You can use a smart card within a Windows WorkSpace, on Chrome or Firefox, to authenticate other applications.

Chrome doesn't require any special configuration to work with your smart card.

You WorkSpaces administrator may have already enabled Firefox to work with smart cards. If you want to use a smart card on Firefox
but it doesn't work, contact your WorkSpaces administrator.

## Use a smart card with Chrome or Firefox on Linux WorkSpaces (in-session)

You can use a smart card within a Linux WorkSpace, on Chrome or Firefox, to authenticate other applications.

###### To use your smart card with the Chrome browser

1. Log in to your Linux WorkSpace using the WorkSpaces for Windows client application.
2. Open Terminal (**Applications** > **System Tools** > **MATE Terminal**).
3. Run the following command:

```
cd; modutil -dbdir sql:.pki/nssdb/ -add "OpenSC" -libfile /lib64/opensc-pkcs11.so
```

4. If Chrome is already running, close it, and then press **Enter**. When the command finishes
   running, you should see this message:

`Module "OpenSC" added to database.`

###### To use your smart card with the Firefox browser

Your WorkSpaces administrator might have already enabled Firefox to work with smart cards. If your smart
card doesn't work in Firefox, use the following procedure to enable it.

1. Open Firefox. Choose the menu button

![Firefox menu button on your browser](images/firefox-menu-button.png)

in the upper-right corner, and then choose **Preferences**. 2. On the **about:preferences** page, in the left navigation
pane, choose **Privacy & Security**. 3. Under **Certificates**, choose **Security Devices**. 4. In the **Device Manager** dialog box, choose **Load**. 5. In the **Load PKCS#11 Device Driver** dialog box, enter the following:

**Module Name**: `OpenSC`

**Module filename**: `/lib64/opensc-pkcs11.so` 6. Choose **OK**.
