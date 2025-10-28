# Update the operating system and software on Amazon EC2 Mac instances

The following topic explains how to update the operating system and software on Apple silicon Mac
instances (Mac2, Mac2-m1ultra, Mac2-m2, Mac2-m2pro, Mac-m4, and Mac-m4pro) and x86 Mac instances
(Mac1).

###### Warning

Installation of beta or preview macOS versions is only available on Apple silicon Mac
instances. Amazon EC2 doesn't qualify beta or preview macOS versions and doesn't ensure instances
will remain functional after an update to a pre-production macOS version.

Attempting to install beta or preview macOS versions on Amazon EC2 x86 Mac instances will lead
to degradation of your Amazon EC2 Mac Dedicated Host when you stop or terminate your instances, and will
prevent you from starting or launching a new instance on that host.

###### Note

If you perform an in-place macOS update before AWS releases an official AMI, the update
applies to the selected host only. If you have other hosts, or if you launch new hosts,
you must perform the same update process on those hosts as well. Each macOS version requires
a minimum firmware version on the underlying Apple Mac hardware. The in-place update only
updates the firmware on the selected host and doesn't transfer to other existing or new
hosts. To check which macOS versions are compatible with your Amazon EC2 Mac Dedicated Host, see
[Find supported macOS versions for your Amazon EC2 Mac Dedicated Host](macos-firmware-visibility.md "macos-firmware-visibility.md").

###### Follow the correct steps below, depending on your Amazon EC2 Mac instance type.

### Prerequisites

Due to an update in the network driver configuration, ENA driver version 1.0.2 isn't
compatible with macOS 13.3 and later. If you want to install any beta, preview, or production
macOS version 13.3 or later and have not installed the latest ENA driver, use the following
procedure to install a new version of the driver.

###### To install a new version of the ENA driver

1. In a Terminal window, connect to your Apple silicon Mac instance using
   [SSH](connect-to-mac-instance.md#mac-instance-ssh "connect-to-mac-instance.md#mac-instance-ssh").
2. Update Homebrew and download the ENA application into the `Applications` file using the following command.

```
`[ec2-user ~]$` brew update
```

```
`[ec2-user ~]$` brew install amazon-ena-ethernet-dext
```

3. Disconnect from your instance by typing **exit** and pressing return.
4. Use the VNC client to activate the ENA application.
   1. Setup the VNC client using [Connect to your instance's graphical user interface (GUI)](connect-to-mac-instance.md#mac-instance-vnc "connect-to-mac-instance.md#mac-instance-vnc").
   2. Once you have connected to your instance using the Screen Sharing
      application, go to the **Applications**
      folder and open the ENA application.
   3. Choose **Activate**
   4. To confirm the driver was activated correctly, run the following
      command in the Terminal window. The output of the command shows that
      the old driver is in the terminating state and the new driver is in
      the activated state.

   ```
   systemextensionsctl list;
   ```

   5. After you restart the instance, only the new driver will be present.

### Perform the software update

On Apple silicon Mac instances, you must complete several steps to perform an in-place
operating system update. This includes delegating ownership of the Amazon EBS root volume to the
EBS root volume administrative user. You can choose to do this either automatically using
an Amazon EC2 API, or you can do it manually by running the commands on your instance.

Automated volume ownership delegation (Recommended)

###### Considerations

- It can take between 30 and 90 minutes for the volume ownership delegation
  task to complete. During this time, the instance is unreachable.
- The following macOS versions are supported:
  - **Mac2 | Mac2-m1ultra** — macOS
    Ventura (version 13.0 or later)
  - **Mac2-m2 | Mac2-m2pro** — macOS
    Ventura (version 13.2 or later)
  - **Mac-m4 | Mac-m4pro** — macOS
    Sequoia (version 15.6 or later)

- Instances must have only one bootable volume, and each attached volume can
  have only one additional admin user.

###### Step 1: Set a password and enable the secure token for the EBS root volume administrative user

You must set a password and enable the secure token for the Amazon EBS root volume administrative
user (`ec2-user`).

###### Note

The password and secure token are set the first time you connect to an Apple
silicon Mac instance using the GUI. If you previously [connected to the instance using the GUI](connect-to-mac-instance.md#mac-instance-vnc "connect-to-mac-instance.md#mac-instance-vnc"), you **do
not** need to perform these steps.

1. [Connect to the instance using SSH](connect-to-mac-instance.md#mac-instance-ssh "connect-to-mac-instance.md#mac-instance-ssh").
2. Set the password for the `ec2-user` user.

```
`$` sudo /usr/bin/dscl . -passwd /Users/ec2-user
```

3. Enable the secure token for the `ec2-user` user. For `-oldPassword`,
   specify the same password from the previous step. For `-newPassword`, specify
   a different password. The following command assumes that you have your old and new passwords
   saved in `.txt` files.

```
`$` sysadminctl -oldPassword `cat old_password.txt` -newPassword `cat new_password.txt`
```

4. Verify that the secure token is enabled.

```
`$` sysadminctl -secureTokenStatus ec2-user
```

###### Step 2: Delegate ownership of the Amazon EBS root volume to the EBS root volume administrative user

To delegate ownership, you must create a volume ownership delegation task.

1. Use the [create-delegate-mac-volume-ownership-task](../../../cli/latest/reference/ec2/create-delegate-mac-volume-ownership-task.md "../../../cli/latest/reference/ec2/create-delegate-mac-volume-ownership-task.md") command to create the task. For
   `--instance-id`, specify the ID of the instance. For `--mac-credentials`,
   specify the following credentials:
   - **Internal disk administrative user**
     - **Username** — Only the default administrative
       user (`aws-managed-user`) is supported and it is used by default. You can't
       specify a different administrative user.
     - **Password** — If you did not change the default
       password for `aws-managed-user`, specify the default password, which
       is _blank_. Otherwise, specify your password.

   - **Amazon EBS root volume administrative user**
     - **Username** — If you did not change the default
       administrative user, specify `ec2-user`. Otherwise, specify the username
       for your administrative user.
     - **Password** — Specify the password that you set
       for root volume admin user in Step 1 above.

```
aws ec2 create-delegate-mac-volume-ownership-task \
--instance-id `i-1234567890abcdef0` \
--mac-credentials file://mac-credentials.json
```

The following is the contents of the `mac-credentials.json` file referenced
in the preceding examples.

```
{
  "internalDiskPassword":"*internal-disk-admin\_password*",
  "rootVolumeUsername":"*root-volume-admin\_username*",
  "rootVolumepassword":"*root-volume-admin\_password*"
}
```

2. Wait for the volume ownership delegation task to complete and for the instance to return
   to a healthy state. Use the [describe-mac-modification-tasks](../../../cli/latest/reference/ec2/describe-mac-modification-tasks.md "../../../cli/latest/reference/ec2/describe-mac-modification-tasks.md") command. For `--mac-modification-task-id`,
   specify the ID of the volume ownership delegation task from the previous step.

```
aws ec2 describe-mac-modification-tasks \
--mac-modification-task-id `task-id`
```

3. After the volume ownership delegation task completes, continue to Step 3.

###### Step 3: Update the software

After you have delegated ownership of the Amazon EBS root volume, follow the steps
described in [Update software on x86 Mac instances](#x86-mac1 "#x86-mac1") (below) to
update the software.

Manual volume ownership delegation
As you work through this procedure, you create two passwords. One password is for the Amazon EBS root volume
administrative user (`ec2-user`), and the other password is for the internal disk administrative
user (`aws-managed-user`). Remember these passwords since you will use them as you work through
the procedure.

###### Note

With this procedure on macOS Big Sur, you can only perform minor updates such as updating from
macOS Big Sur 11.7.3 to macOS Big Sur 11.7.4. For macOS Monterey or above, you can perform major
software updates.

###### To access the internal disk

1. From your local computer, in the Terminal, connect to your Apple silicon
   Mac instance using SSH with the following command. For more
   information, see [Connect to your instance using SSH](connect-to-mac-instance.md#mac-instance-ssh "connect-to-mac-instance.md#mac-instance-ssh").

```
ssh -i `/path/key-pair-name`.pem ec2-user@`instance-public-dns-name`
```

2. Install and start macOS Screen Sharing using the following command.

```
`[ec2-user ~]$` sudo launchctl enable system/com.apple.screensharing
sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.screensharing.plist
```

3. Set a password for `ec2-user` with the following command. Remember the password as you will use it later.

```
`[ec2-user ~]$` sudo /usr/bin/dscl . -passwd /Users/ec2-user
```

4. Disconnect from the instance by typing **exit** and pressing return.
5. From your local computer, in the Terminal, reconnect to your instance with
   an SSH tunnel to the VNC port using the following command.

```
ssh -i `/path/key-pair-name`.pem -L 5900:localhost:5900 ec2-user@`instance-public-dns-name`
```

###### Note

Do not exit this SSH session until the following VNC connection and GUI steps are completed. When the instance is restarted, the connection will close automatically. 6. From your local computer, connect to `localhost:5900` using the following steps:

    1. Open **Finder** and select **Go**.
    2. Select **Connect to Server**.
    3. In the **Server Address** field, enter `vnc://localhost:5900`.

7. In the macOS window, connect to the remote session of the Apple silicon Mac
   instance as `ec2-user` with the password you created in
   [Step 3](#passwd-step "#passwd-step").
8. Access the internal disk, named **InternalDisk**, using one of the following options.
   1. For macOS Ventura or above: Open **System
      Settings**, select **General** in the left pane, then **Startup Disk** at the lower right of
      the pane.
   2. For macOS Monterey or below: Open **System
      Preferences**, select **Startup
      Disk**, then unlock the pane by choosing the lock
      icon in the lower left of the window.###### Troubleshooting tip

If you need to mount the internal disk, run the following command in the Terminal.

```
APFSVolumeName="InternalDisk" ; SSDContainer=$(diskutil list | grep "Physical Store disk0" -B 3 | grep "/dev/disk" | awk {'print $1'} ) ; diskutil apfs addVolume $SSDContainer APFS $APFSVolumeName
```

9. Choose the internal disk, named **InternalDisk**, and select **Restart**. Select **Restart** again when prompted.

###### Important

If the internal disk is named **Macintosh HD** instead of **InternalDisk**, your
instance needs to be stopped and restarted so the dedicated host can be updated. For more information, see [Stop or terminate your Amazon EC2 Mac instance](mac-instance-stop.md "mac-instance-stop.md").

Use the following procedure to delegate ownership to the administrative user. When you reconnect to your instance with SSH, you boot from the internal disk using the special administrative user
(`aws-managed-user`). The initial password for `aws-managed-user` is blank, so you need to overwrite it on your first connection. Then, you need to repeat the steps to install and start
macOS Screen Sharing since the boot volume has changed.

###### To delegate ownership to the administrator on an Amazon EBS volume

1. From your local computer, in the Terminal, connect to your Apple silicon
   Mac instance using the following command.

```
ssh -i `/path/key-pair-name`.pem aws-managed-user@`instance-public-dns-name`
```

2. When you receive the warning `WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!`, use one of the following commands to resolve this issue.
   1. Clear out the known hosts using the following command. Then, repeat the previous step.

   ```
   rm ~/.ssh/known_hosts
   ```

   2. Add the following to the SSH command in the previous step.

   ```
   -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no
   ```

3. Set the password for `aws-managed-user`
   with the following command. The `aws-managed-user` initial
   password is blank, so you need to overwrite it on your first
   connection.
   1. ```
      `[aws-managed-user ~]$` sudo /usr/bin/dscl . -passwd /Users/aws-managed-user `password`
      ```

   ```
   2. When you receive the prompt, `Permission denied. Please enter user's old password:`, press enter.


   ###### Troubleshooting tip

   If you get the error `passwd: DS error: eDSAuthFailed`, use the following command.


   ```

   `[aws-managed-user ~]$` sudo passwd aws-managed-user

   ```

   ```

4. Install and start macOS Screen Sharing using the following command.

```
`[aws-managed-user ~]$` sudo launchctl enable system/com.apple.screensharing
sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.screensharing.plist
```

5. Disconnect from the instance by typing **exit** and pressing return.
6. From your local computer, in the Terminal, reconnect to your instance with
   an SSH tunnel to the VNC port using the following command.

```
ssh -i `/path/key-pair-name`.pem -L 5900:localhost:5900 aws-managed-user@`instance-public-dns-name`
```

7. From your local computer, connect to `localhost:5900` using the following steps:
   1. Open **Finder** and select **Go**.
   2. Select **Connect to Server**.
   3. In the **Server Address** field, enter `vnc://localhost:5900`.

8. In the macOS window, connect to the remote session of the Apple silicon
   Mac instance as `aws-managed-user` with the password you
   created in [Step 3](#amu-passwd "#amu-passwd").

###### Note

When prompted to sign in with your Apple ID, select **Set Up Later**. 9. Access the Amazon EBS volume using one of the following options.

    1. For macOS Ventura or later: Open **System
     Settings**, select **General**
     in the left pane, then **Startup Disk** at
     the lower right of the pane.
    2. For macOS Monterey or earlier: Open **System
     Preferences**, select **Startup
     Disk**, then unlock the pane using the lock
     icon in the lower left of the window.###### Note

Until the reboot takes place, when prompted for an administrator
password, use the password you set above for
`aws-managed-user`. This password might be
different from the one you set for `ec2-user` or the
default administrator account on your instance. The following
instructions specify when to use your instance's administrator
password. 10. Select the Amazon EBS volume (the volume not named **InternalDisk** in the **Startup
Disk** window) and choose **Restart**.

###### Note

If you have multiple bootable Amazon EBS volumes attached to your Apple
silicon Mac instance, be sure to use a unique name for each
volume. 11. Confirm the restart, then choose **Authorize Users** when prompted. 12. On the **Authorize user on this volume** pane,
verify that the administrative user (`ec2-user` by default) is
selected, then select **Authorize**. 13. Enter the `ec2-user` password you created in [Step 3](#passwd-step "#passwd-step") of the previous procedure, then
select **Continue**. 14. Enter the password for the special administrative user (`aws-managed-user`) when prompted. 15. From your local computer, in the Terminal, reconnect to your instance using
SSH with username `ec2-user`.

###### Troubleshooting tip

If you get the warning `WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!`, run the following command and reconnect to your instance using SSH.

```
rm ~/.ssh/known_hosts
```

16. To perform the software update, use the commands under [Update software on x86 Mac instances](#x86-mac1 "#x86-mac1").

On x86 Mac instances, you can install operating system updates from Apple using the
`softwareupdate` command.

###### To install operating system updates from Apple on x86 Mac instances

1. List the packages with available updates using the following command.

```
`[ec2-user ~]$` softwareupdate --list
```

2. Install all updates or only specific updates. To install specific updates, use
   the following command.

```
`[ec2-user ~]$` sudo softwareupdate --install `label`
```

To install all updates instead, use the following command.

```
`[ec2-user ~]$` sudo softwareupdate --install --all --restart
```

System administrators can use AWS Systems Manager to roll out pre-approved operating system
updates on x86 Mac instances. For more information, see the [AWS Systems Manager User Guide](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md").

You can use Homebrew to install updates to packages in the EC2 macOS AMIs, so
that you have the latest version of these packages on your instances. You can also
use Homebrew to install and run common macOS applications on Amazon EC2 macOS. For more
information, see the [Homebrew
Documentation](https://docs.brew.sh/ "https://docs.brew.sh/").

###### To install updates using Homebrew

1. Update Homebrew using the following command.

```
`[ec2-user ~]$` brew update
```

2. List the packages with available updates using the following command.

```
`[ec2-user ~]$` brew outdated
```

3. Install all updates or only specific updates. To install specific updates, use
   the following command.

```
`[ec2-user ~]$` brew upgrade `package name`
```

To install all updates instead, use the following command.

```
`[ec2-user ~]$` brew upgrade
```
