# Connect to your Linux instance using PuTTY

You can connect to your Linux instance using PuTTY, a free SSH client for Windows.

If you're running Windows Server 2019 or later, we recommend that you use OpenSSH, an
open source connectivity tool for remote login using the SSH protocol.

###### Note

If you receive an error while attempting to connect to your instance, make sure that
your instance meets all of the [SSH connection prerequisites](connect-linux-inst-ssh.md#ssh-prereqs-linux-from-linux-macos "connect-linux-inst-ssh.md#ssh-prereqs-linux-from-linux-macos"). If it meets all of the
prerequisites, and you're still not able to connect to your Linux instance, see [Troubleshoot issues connecting to your Amazon EC2 Linux instance](TroubleshootingInstancesConnecting.md "TroubleshootingInstancesConnecting.md").

###### Contents

- [Prerequisites](#putty-prereqs "#putty-prereqs")
- [Convert your private key using PuTTYgen](#putty-private-key "#putty-private-key")
- [Connect to your Linux instance](#putty-ssh "#putty-ssh")

## Prerequisites

Before you connect to your Linux instance using PuTTY, complete the following tasks.

**Complete the general prerequisites.**

- Check that your instance has passed its status checks.
  It can take a few minutes for an instance to be ready to accept connection requests.
  For more information, see [View status checks](viewing_status.md "viewing_status.md").
- [Get the required instance details](connection-prereqs-general.md#connection-prereqs-get-info-about-instance "connection-prereqs-general.md#connection-prereqs-get-info-about-instance").
- [Locate the private key and set permissions](connection-prereqs-general.md#connection-prereqs-private-key "connection-prereqs-general.md#connection-prereqs-private-key").
- [(Optional) Get the instance fingerprint](connection-prereqs-general.md#connection-prereqs-fingerprint "connection-prereqs-general.md#connection-prereqs-fingerprint").

**Allow inbound SSH traffic from your IP address.**

Ensure that the security group associated with your instance allows incoming SSH
traffic from your IP address. For more information, see [Rules to connect to instances from your computer](security-group-rules-reference.md#sg-rules-local-access "security-group-rules-reference.md#sg-rules-local-access").

**Install PuTTY on your local computer (if needed).**

Download and install PuTTY from the [PuTTY
download page](https://www.chiark.greenend.org.uk/~sgtatham/putty/ "https://www.chiark.greenend.org.uk/~sgtatham/putty/"). If you already have an earlier version of
PuTTY installed, we recommend that you download the latest version. Be
sure to install the entire suite.

**Convert your private key to PPK format using PuTTYgen.**

You must specify the private key for the key pair that you specified
when you launched the instance. If you created the private key in .pem
format, you must convert it to a PPK file for use with PuTTY. Locate
the private key (.pem file), and then follow the steps in
[Convert your private key using PuTTYgen](#putty-private-key "#putty-private-key").

## (Optional) Convert your private key using PuTTYgen

PuTTY does not natively support the PEM format for SSH keys. PuTTY provides a
tool named PuTTYgen, which converts PEM keys to the required PPK format for
PuTTY. If you created the key using PEM format instead of PPK format, you
must convert your private key (.pem file) into this format (.ppk file) for use with
PuTTY.

###### To convert your private key from PEM to PPK format

1. From the **Start** menu, choose **All Programs**,
   **PuTTY**, **PuTTYgen**.
2. Under **Type of key to generate**, choose **RSA**. If
   your version of PuTTYgen does not include this option, choose
   **SSH-2 RSA**.

![RSA key in PuTTYgen.](images/puttygen-key-type.png) 3. Choose **Load**. By default, PuTTYgen displays only files with the
extension `.ppk`. To locate your
`.pem` file, choose the option to display files
of all types.

![Select all file types.](images/puttygen-load-key.png) 4. Select your `.pem` file for the key pair that you specified when you
launched your instance and choose **Open**. PuTTYgen
displays a notice that the `.pem` file was
successfully imported. Choose **OK**. 5. To save the key in the format that PuTTY can use, choose **Save private
key**. PuTTYgen displays a warning about saving the key
without a passphrase. Choose **Yes**.

###### Note

A passphrase on a private key is an extra layer of protection. Even if your private key
is discovered, it can't be used without the passphrase. The downside
to using a passphrase is that it makes automation harder because
human intervention is needed to log on to an instance, or to copy
files to an instance. 6. Specify the same name for the key that you used for the key pair (for example,
`key-pair-name`) and choose
**Save**. PuTTY automatically adds the
`.ppk` file extension.

Your private key is now in the correct format for use with PuTTY. You can now
connect to your instance using PuTTY's SSH client.

## Connect to your Linux instance

Use the following procedure to connect to your Linux instance using PuTTY. You need the
`.ppk` file that you created for your private key. For more information,
see [(Optional) Convert your private key using PuTTYgen](#putty-private-key "#putty-private-key") in the preceding
section. If you receive an error while attempting to connect to your instance, see [Troubleshoot issues connecting to your Amazon EC2 Linux instance](TroubleshootingInstancesConnecting.md "TroubleshootingInstancesConnecting.md").

Last tested version – PuTTY .78

###### To connect to your instance using PuTTY

1.  Start PuTTY (from the **Start** menu, search for
    **PuTTY** and then choose
    **Open**).
2.  In the **Category** pane, choose **Session** and
    complete the following fields:

        1. In the **Host Name** box, do one of the following:


        	* (Public DNS) To connect using your instance's public DNS name, enter
        	 `instance-user-name`@`instance-public-dns-name`.
        	* (IPv6) Alternatively, if your instance has an IPv6 address, to connect using your
        	 instance's IPv6 address, enter
        	 `instance-user-name`@`2001:db8::1234:5678:1.2.3.4`.For information about how to get the username for your instance, and the public DNS
         name or IPv6 address of your instance, see [Get the required instance details](connection-prereqs-general.md#connection-prereqs-get-info-about-instance "connection-prereqs-general.md#connection-prereqs-get-info-about-instance").
        2. Ensure that the **Port** value is 22.
        3. Under **Connection type**, select
         **SSH**.

    ![PuTTY configuration - Session.](images/putty-session-config.png)

3.  (Optional) You can configure PuTTY to automatically send 'keepalive' data at regular
    intervals to keep the session active. This is useful to avoid disconnecting
    from your instance due to session inactivity. In the
    **Category** pane, choose
    **Connection**, and then enter the required interval in
    **Seconds between keepalives**. For example, if your
    session disconnects after 10 minutes of inactivity, enter 180 to configure
    PuTTY to send keepalive data every 3 minutes.
4.  In the **Category** pane, expand **Connection**,
    **SSH**, and **Auth**. Choose
    **Credentials**.
5.  Next to **Private key file for authentication**, choose
    **Browse**. In the **Select private key
    file** dialog box, select the `.ppk` file
    that you generated for your key pair. You can either double-click the file
    or choose **Open** in the **Select private key
    file** dialog box.
6.  (Optional) If you plan to connect to this instance again after this session,
    you can save the session information for future use. In the **Category**
    pane, choose **Session**. Enter a name for the session in
    **Saved Sessions**, and then choose **Save**.
7.  To connect to the instance, choose **Open**.
8.  If this is the first time you have connected to this instance, PuTTY displays a
    security alert dialog box that asks whether you trust the host to which you
    are connecting.
    1. (Optional) Verify that the fingerprint in the security alert dialog box matches the
       fingerprint that you previously obtained in [(Optional) Get the instance fingerprint](connection-prereqs-general.md#connection-prereqs-fingerprint "connection-prereqs-general.md#connection-prereqs-fingerprint"). If these fingerprints
       don't match, someone might be attempting a "man-in-the-middle" attack. If
       they match, continue to the next step.
    2. Choose **Accept**. A window opens and you are connected to your
       instance.

    ###### Note

    If you specified a passphrase when you converted your private key to the PuTTY format,
    you must provide that passphrase when you log in to the
    instance.

If you receive an error while attempting to connect to your instance, see [Troubleshoot issues connecting to your Amazon EC2 Linux instance](TroubleshootingInstancesConnecting.md "TroubleshootingInstancesConnecting.md").
