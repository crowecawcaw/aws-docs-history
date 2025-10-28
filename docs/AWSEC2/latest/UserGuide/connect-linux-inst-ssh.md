# Connect to your Linux instance using an SSH client

You can use Secure Shell (SSH) to connect to your Linux instance from your local computer.
For more information about other options, see [Connect to your EC2 instance](connect.md "connect.md").

###### Note

If you receive an error while attempting to connect to your instance, make sure that
your instance meets all of the [SSH connection prerequisites](#ssh-prereqs-linux-from-linux-macos "#ssh-prereqs-linux-from-linux-macos"). If it meets all of the
prerequisites, and you're still not able to connect to your Linux instance, see [Troubleshoot issues connecting to your Amazon EC2 Linux instance](TroubleshootingInstancesConnecting.md "TroubleshootingInstancesConnecting.md").

###### Contents

- [SSH connection prerequisites](#ssh-prereqs-linux-from-linux-macos "#ssh-prereqs-linux-from-linux-macos")
- [Connect to your Linux instance using an SSH client](#connect-linux-inst-sshClient "#connect-linux-inst-sshClient")

## SSH connection prerequisites

Before you can connect to your Linux instance using SSH, complete the following tasks.

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

**Install an SSH client on your local computer (if needed).**

Your local computer might have an SSH client installed by default. You can
verify this by entering the following command in a terminal window. If your
computer doesn't recognize the command, you must install an SSH client.

```
ssh
```

The following are some of the possible options for Windows. If your computer
runs a different operating system, see the documentation for that operating system
for SSH client options.

After you install OpenSSH on Windows, you can connect to your Linux instance
from your Windows computer using SSH. Before you begin, ensure that you meet
the following requirements.

**Windows version**

The version of Windows on your computer must be Windows Server 2019 or later.

For earlier versions of Windows, download and install [Win32-OpenSSH](https://github.com/PowerShell/Win32-OpenSSH/wiki "https://github.com/PowerShell/Win32-OpenSSH/wiki") instead.

**PowerShell requirements**

To install OpenSSH on your Windows OS using PowerShell, you must be running PowerShell
version 5.1 or later, and your account must be a member of the built-in
Administrators group. Run `$PSVersionTable.PSVersion` from PowerShell to check your
PowerShell version.

To check whether you are a member of the built-in Administrators
group, run the following PowerShell command:

```
(New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
```

If you are a member of the built-in Administrators group, the output
is `True`.

To install OpenSSH for Windows using PowerShell, run the following PowerShell command.

```
Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0
```

The following is example output.

```
Path          :
Online        : True
RestartNeeded : False
```

To uninstall OpenSSH from Windows using PowerShell, run the following PowerShell command.

```
Remove-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0
```

The following is example output.

```
Path          :
Online        : True
RestartNeeded : True
```

After you install WSL on Windows, you can connect to your Linux instance from
your Windows computer using Linux command line tools, such as an SSH client.

Follow the instructions in [Install Windows Subsystem for Linux on your EC2 Windows instance](install-wsl-on-ec2-windows-instance.md "install-wsl-on-ec2-windows-instance.md"). If you follow the instructions
in Microsoft's installation guide, they install the Ubuntu distribution of Linux.
You can install a different Linux distribution if you prefer.

In a WSL terminal window, copy the `.pem` file (for the key
pair that you specified for your instance at launch) from Windows to WSL. Note
the fully-qualified path to the `.pem` file on WSL to
use when connecting to your instance. For information about how to
specify the path to your Windows hard drive, see [How do I access my C drive?](https://learn.microsoft.com/en-us/windows/wsl/faq#how-do-i-access-my-c--drive- "https://learn.microsoft.com/en-us/windows/wsl/faq#how-do-i-access-my-c--drive-").

```
cp /mnt/`<Windows drive letter>/path/my-key-pair`.pem ~/`WSL-path/my-key-pair`.pem
```

For information about uninstalling Windows Subsystem for Linux, see [How do I uninstall a WSL Distribution?](https://learn.microsoft.com/en-us/windows/wsl/faq#how-do-i-uninstall-a-wsl-distribution- "https://learn.microsoft.com/en-us/windows/wsl/faq#how-do-i-uninstall-a-wsl-distribution-").

## Connect to your Linux instance using an SSH client

Use the following procedure to connect to your Linux instance using an SSH client.

###### To connect to your instance using an SSH client

1. Open a terminal window on your computer.
2. Use the **ssh** command to connect to the instance.
   You need the details about your instance that you gathered as part of the
   prerequisites. For example, you need the location of the private key
   (`.pem` file), the username, and the public DNS name
   or IPv6 address. The following are example commands.
   - (Public DNS) To use the public DNS name, enter the following command.

   ```
   ssh -i `/path/key-pair-name`.pem `instance-user-name`@`instance-public-dns-name`
   ```

   - (IPv6) Alternatively, if your instance has an IPv6 address, enter
     the following command to use the IPv6 address.

   ````
   ssh -i `/path/key-pair-name`.pem `instance-user-name`@`2001:db8::1234:5678:1.2.3.4`
   ```The following is an example response.
   ````

```
The authenticity of host 'ec2-198-51-100-1.compute-1.amazonaws.com (198-51-100-1)' can't be established.
ECDSA key fingerprint is l4UB/neBad9tvkgJf1QZWxheQmR59WgrgzEimCG6kZY.
Are you sure you want to continue connecting (yes/no)?
```

3. (Optional) Verify that the fingerprint in the security alert matches the
   fingerprint. If these fingerprints don't match, someone might be attempting
   a man-in-the-middle attack. If they match, continue to the next step. For more
   information, see [Get the instance
   fingerprint](connection-prereqs-general.md#connection-prereqs-fingerprint "connection-prereqs-general.md#connection-prereqs-fingerprint").
4. Enter `yes`.

You see a response like the following:

```
Warning: Permanently added 'ec2-198-51-100-1.compute-1.amazonaws.com' (ECDSA) to the list of known hosts.
```
