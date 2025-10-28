# Connect to your Windows instance using an RDP client

You can connect to your Windows instance using an RDP client as follows.

###### Tip

Alternatively, you can connect to your Windows instance using
[Systems Manager Fleet Manager](connect-rdp-fleet-manager.md "connect-rdp-fleet-manager.md") or
[EC2 Instance Connect Endpoint](connect-with-ec2-instance-connect-endpoint.md "connect-with-ec2-instance-connect-endpoint.md").

## Prerequisites

You must meet the following prerequisites to connect to your Windows instance using an RDP
client.

- Complete the general prerequisites.
  - Check that your instance has passed its status checks.
    It can take a few minutes for an instance to be ready to accept connection requests.
    For more information, see [View status checks](viewing_status.md "viewing_status.md").
  - [Get the required instance details](connection-prereqs-general.md#connection-prereqs-get-info-about-instance "connection-prereqs-general.md#connection-prereqs-get-info-about-instance").
  - [Locate the private key and set permissions](connection-prereqs-general.md#connection-prereqs-private-key "connection-prereqs-general.md#connection-prereqs-private-key").
  - [(Optional) Get the instance fingerprint](connection-prereqs-general.md#connection-prereqs-fingerprint "connection-prereqs-general.md#connection-prereqs-fingerprint").

- Install an RDP client.
  - (Windows) Windows includes an RDP client by default. To verify, type
    **mstsc** at a Command Prompt window. If your
    computer doesn't recognize this command, download the [Microsoft Remote Desktop app](https://apps.microsoft.com/detail/9wzdncrfj3ps "https://apps.microsoft.com/detail/9wzdncrfj3ps")
    from the Microsoft Store.
  - (macOS X) Download the [Windows App for Mac (previously named Microsoft Remote Desktop](https://apps.apple.com/us/app/windows-app/id1295203466?mt=12 "https://apps.apple.com/us/app/windows-app/id1295203466?mt=12")
    from the Mac App Store.
  - (Linux) Use [Remmina](https://remmina.org/ "https://remmina.org/").

- Allow inbound RDP traffic from your IP address.

Ensure that the security group associated with your instance allows incoming RDP traffic from your IP address.
For more information, see [Rules to connect to instances from your computer](security-group-rules-reference.md#sg-rules-local-access "security-group-rules-reference.md#sg-rules-local-access").

## Retrieve the administrator password

If you joined your instance to a domain, you can connect to your instance using the domain
credentials from AWS Directory Service. On the Remote Desktop login screen, instead of using the local computer
name and the generated password, use the fully-qualified username for the administrator
(for example, `corp.example.com\Admin`), and the password for this account.

To connect to a Windows instance using RDP, you must retrieve the initial administrator password and
then enter this password when you connect to your instance. It takes a few minutes after instance launch before this password is available.
Your account must have permission to call the [GetPasswordData](../APIReference/API_GetPasswordData.md "../APIReference/API_GetPasswordData.md") action.
For more information, see [Example policies to control access the Amazon EC2 API](ExamplePolicies_EC2.md "ExamplePolicies_EC2.md").

The default username for the Administrator account depends on the language of the operating system (OS) contained in the AMI.
To determine the correct username, identify the language of the OS, and then choose the corresponding username. For example,
for an English OS, the username is `Administrator`, for a French OS it's `Administrateur`, and for a Portuguese OS it's `Administrador`.
If a language version of the OS does not have a username in the same language, choose the username `Administrator (Other)`.
For more information, see [Localized Names for Administrator Account in Windows](https://learn.microsoft.com/en-us/archive/technet-wiki/13813.localized-names-for-administrator-account-in-windows "https://learn.microsoft.com/en-us/archive/technet-wiki/13813.localized-names-for-administrator-account-in-windows") in the Microsoft website.

###### To retrieve the initial administrator password

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the instance and then choose **Connect**.
4. On the **Connect to instance** page, choose the **RDP client** tab.
5. For **Username**, choose the default username for the Administrator
   account. The username you choose must match the language of the operating system
   (OS) contained in the AMI that you used to launch your instance. If there is no
   username in the same language as your OS, choose **Administrator
   (Other)**.
6. Choose **Get password**.
7. On the **Get Windows password** page, do the following:
   1. Choose **Upload private key file** and navigate to
      the private key (`.pem`) file that you specified when you launched
      the instance. Select the file and choose **Open** to
      copy the entire contents of the file to this window.
   2. Choose **Decrypt password**. The **Get
      Windows password** page closes, and the default
      administrator password for the instance appears under
      **Password**, replacing the **Get
      password** link shown previously.
   3. Copy the password and save it in a safe place. This password is required to connect to the instance.

## Connect to your Windows instance

The following procedure uses the Remote Desktop Connection client for Windows (MSTSC). If you're using a different RDP client,
download the RDP file and then see the documentation for the RDP client for the steps to establish the RDP connection.

###### To connect to a Windows instance using an RDP client

1. On the **Connect to instance** page, choose **Download remote desktop file**.
   When the file download is finished, choose **Cancel** to return to the **Instances**
   page. The RDP file is downloaded to your `Downloads` folder.
2. Run `mstsc.exe` to open the RDP client.
3. Expand **Show options**, choose **Open**, and select the .rdp file from your
   `Downloads` folder.
4. By default, **Computer** is the public IPv4 DNS name of the instance and **User name**
   is the administrator account. To connect to the instance using IPv6 instead, replace the public IPv4 DNS name of the instance
   with its IPv6 address. Review the default settings and change them as needed.
5. Choose **Connect**. If you receive a warning that the publisher of the remote connection is unknown,
   choose **Connect** to continue.
6. Enter the password that you saved previously, and then choose **OK**.
7. Due to the nature of self-signed certificates, you might get a warning that the security certificate could not be authenticated.
   Do one of the following:
   - If you trust the certificate, choose **Yes** to connect to your instance.
   - [Windows] Before you proceed, compare the thumbprint of the certificate with the value in the system log to confirm the identity of the remote computer.
     Choose **View certificate** and then choose **Thumbprint** from the **Details** tab.
     Compare this value to the value of `RDPCERTIFICATE-THUMBPRINT` in **Actions**, **Monitor and troubleshoot**,
     **Get system log**.
   - [Mac OS X] Before you proceed, compare the fingerprint of the certificate with the value in the system log to confirm the identity of the remote computer.
     Choose **Show Certificate**, expand **Details**, and choose **SHA1 Fingerprints**.
     Compare this value to the value of `RDPCERTIFICATE-THUMBPRINT` in **Actions**, **Monitor and troubleshoot**,
     **Get system log**.

8. If the RDP connection is successful, the RDP client displays the Windows login screen and then the Windows desktop. If you receive an error message instead,
   see [Remote Desktop can't connect to the remote computer](troubleshoot-connect-windows-instance.md#rdp-issues "troubleshoot-connect-windows-instance.md#rdp-issues"). When you are finished with the RDP connection, you can close the RDP client.

## Configure user accounts

After you connect to your instance over RDP, we recommend that you perform the following tasks:

- Change the administrator password from the default value. You [can change the password while you are logged on to the instance
  itself](https://support.microsoft.com/en-us/windows/change-or-reset-your-windows-password-8271d17c-9f9e-443f-835a-8318c8f68b9c "https://support.microsoft.com/en-us/windows/change-or-reset-your-windows-password-8271d17c-9f9e-443f-835a-8318c8f68b9c"), just as you would on any computer running Windows
  Server.
- Create another user with administrator privileges on the instance. This is a safeguard in
  case you forget the administrator password or have a problem with the
  administrator account. The new user must have permission to access the instance
  remotely. Open **System Properties** by right-clicking on the
  **This PC** icon on your Windows desktop or File Explorer
  and selecting **Properties**. Choose **Remote
  settings**, and choose **Select Users** to add the
  user to the **Remote Desktop Users** group.

![System Properties window.](images/windows-connect-properties-rdp.png)
