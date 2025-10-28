# Connect to your Mac instance using SSH or a GUI

You can connect to your Mac instance using SSH or a graphical user interface (GUI).

Multiple users can access the OS simultaneously. Typically there is a 1:1 user:GUI session,
due to the built-in Screen Sharing service on port 5900. Using SSH within macOS supports
multiple sessions up until the "Max Sessions" limit in the `sshd_config` file.

## Connect to your instance using SSH

Amazon EC2 Mac instances do not allow remote root SSH by default. The ec2-user
account is configured to log in remotely using SSH. The ec2-user account
also has **sudo** privileges. After you connect to your instance, you can
add other users.

To support connecting to your instance using SSH, launch the instance using a key pair
and a security group that allows SSH access, and ensure that the instance has internet
connectivity. You provide the `.pem` file for the key pair when
you connect to the instance.

Use the following procedure to connect to your Mac instance using an SSH client.
If you receive an error while attempting to connect to your instance, see [Troubleshoot issues connecting to your Amazon EC2 Linux instance](TroubleshootingInstancesConnecting.md "TroubleshootingInstancesConnecting.md").

###### To connect to your instance using SSH

1. Verify that your local computer has an SSH client installed by entering
   **ssh** at the command line. If your computer doesn't
   recognize the command, search for an SSH client for your operating system
   and install it.
2. Get the public DNS name of your instance. Using the Amazon EC2 console, you can
   find the public DNS name on both the **Details** and the
   **Networking** tabs. Using the AWS CLI, you can find the
   public DNS name using the [describe-instances](../../../cli/latest/reference/ec2/describe-instances.md "../../../cli/latest/reference/ec2/describe-instances.md") command.
3. Locate the `.pem` file for the key pair that you specified
   when you launched the instance.
4. Connect to your instance using the following **ssh** command,
   specifying the public DNS name of the instance and the `.pem`
   file.

```
ssh -i `/path/key-pair-name`.pem ec2-user@`instance-public-dns-name`
```

Password authentication is disabled to prevent brute-force password attacks.
Before you make changes to the SSH configuration, open `/usr/local/aws/ec2-macos-init/init.toml`
and set `secureSSHDConfig` to `false`.

## Connect to your instance's graphical user interface (GUI)

Use the following procedure to connect to your instance's GUI using VNC, Apple Remote
Desktop (ARD), or the Apple Screen Sharing application (included with macOS).

###### Note

macOS 10.14 and later only allows control if Screen Sharing is enabled through
[System Preferences](https://support.apple.com/guide/remote-desktop/enable-remote-management-apd8b1c65bd/mac "https://support.apple.com/guide/remote-desktop/enable-remote-management-apd8b1c65bd/mac").

###### To connect to your instance using ARD client or VNC client

1. Verify that your local computer has an ARD client or a VNC client that
   supports ARD installed. On macOS, you can leverage the built-in Screen Sharing
   application. Otherwise, search for ARD for your operating system and install
   it.
2. From your local computer, [connect to your
   instance using SSH](#mac-instance-ssh "#mac-instance-ssh").
3. Set up a password for the ec2-user account using the **passwd**
   command as follows.

```
`[ec2-user ~]$` sudo passwd ec2-user
```

4. Install and start macOS Screen Sharing using the following command.

```
`[ec2-user ~]$` sudo launchctl enable system/com.apple.screensharing
sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.screensharing.plist
```

5. Disconnect from your instance by typing **exit** and pressing Enter.
6. From your computer, connect to your instance using the following
   **ssh** command. In addition to the options shown in the
   previous section, use the **-L** option to enable port forwarding
   and forward all traffic on local port 5900 to the ARD server on the
   instance.

```
ssh -L 5900:localhost:5900 -i `/path/key-pair-name`.pem ec2-user@`instance-public-dns-name`
```

7. From your local computer, use the ARD client or VNC client that supports ARD
   to connect to `localhost:5900`. For example, use the Screen Sharing
   application on macOS as follows:
   1. Open **Finder** and select **Go**.
   2. Select **Connect to Server**.
   3. In the **Server Address** field, enter `vnc://localhost:5900`.
   4. Log in as prompted, using `ec2-user` as the username
      and the password that you created for the ec2-user account.

## Modify macOS screen resolution on Mac instances

After you connect to your EC2 Mac instance using ARD or a VNC client that supports
ARD, you can modify the screen resolution of your macOS environment using any of the
publicly available macOS tools or utilities, such as [displayplacer](https://github.com/jakehilborn/displayplacer "https://github.com/jakehilborn/displayplacer").

###### To modify the screen resolution using displayplacer

1. Install displayplacer.

```
`[ec2-user ~]$` brew tap jakehilborn/jakehilborn && brew install displayplacer
```

2. Show the current screen information and possible screen resolutions.

```
`[ec2-user ~]$` displayplacer list
```

3. Apply the desired screen resolution.

```
`[ec2-user ~]$` displayplacer "id:<screenID> res:<width>x<height> origin:(0,0) degree:0"
```

For example:

```
RES="2560x1600"
displayplacer "id:69784AF1-CD7D-B79B-E5D4-60D937407F68 res:${RES} scaling:off origin:(0,0) degree:0"

```
