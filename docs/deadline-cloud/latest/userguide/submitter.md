# Set up your workstation

Set up a workstation so that you can submit jobs to AWS Deadline Cloud from your
digital content creation (DCC) application. A Deadline Cloud _submitter_ is a DCC plugin. You use it to submit jobs from a
third-party DCC interface that you're familiar with. You can follow these steps
yourself, or an administrator can install the software in advance. You sign in
with your own user account.

Before you begin, you need the following:

- The monitor URL for your farm, which looks like
  `https://`MY-MONITOR`.`REGION`.deadlinecloud.amazonaws.com/`.
  Your administrator shares it with you. If you're the administrator, see
  [Share the Deadline Cloud monitor URL](share-monitor-url.md "share-monitor-url.md").
- A user that can sign in to the monitor. If your organization uses single
  sign-on, sign in with your existing company account. If your administrator
  creates a user for you in AWS IAM Identity Center, accept the emailed invitation first.
  If you're the administrator, see [Managing users in Deadline Cloud](managing-users.md "managing-users.md").
- The DCC installed on the workstation. For example, if you want to download
  the Deadline Cloud submitter for Blender, you need to have
  Blender already installed on your workstation.
  Complete this process on every workstation that you use to submit
  renders.

###### Topics

- [Step 1: Install the Deadline Cloud submitter](#submitter-installation "#submitter-installation")
- [Step 2: Install and set up Deadline Cloud monitor](#install-deadline-cloud-monitor "#install-deadline-cloud-monitor")
- [Step 3: Launch the Deadline Cloud submitter](#load-dca-plugin "#load-dca-plugin")

## Step 1: Install the Deadline Cloud submitter

Download the submitter installer for your operating system:

|                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Download for Windows](https://downloads.deadlinecloud.amazonaws.com/submitters/latest/windows/DeadlineCloudSubmitter-windows-x64-installer.exe "https://downloads.deadlinecloud.amazonaws.com/submitters/latest/windows/DeadlineCloudSubmitter-windows-x64-installer.exe") | [Download for Linux](https://downloads.deadlinecloud.amazonaws.com/submitters/latest/linux/DeadlineCloudSubmitter-linux-x64-installer.run "https://downloads.deadlinecloud.amazonaws.com/submitters/latest/linux/DeadlineCloudSubmitter-linux-x64-installer.run") | [Download for MacOS (arm64)](https://downloads.deadlinecloud.amazonaws.com/submitters/latest/macos/DeadlineCloudSubmitter-osx-installer.app.zip "https://downloads.deadlinecloud.amazonaws.com/submitters/latest/macos/DeadlineCloudSubmitter-osx-installer.app.zip") |

With the installer, you can install the following submitters:

| Software                                                                 | Supported versions | Windows installer | Linux installer | MacOS (arm64) installer |
| ------------------------------------------------------------------------ | ------------------ | ----------------- | --------------- | ----------------------- |
| [Adobe After Effects](adobe-after-effects.md "adobe-after-effects.md")   | 2024<br>• 2026     | Included          | Not included    | Included                |
| [Autodesk 3ds Max](autodesk-3ds-max.md "autodesk-3ds-max.md")            | 2024<br>• 2027     | Included          | Not included    | Not included            |
| [Autodesk Arnold for Cinema 4D](maxon-cinema-4d.md "maxon-cinema-4d.md") | 4.8.4.1            | Included          | Not included    | Included                |
| [Autodesk Arnold for Maya](autodesk-maya.md "autodesk-maya.md")          | 7.1<br>• 7.4       | Included          | Included        | Included                |
| [Autodesk Maya](autodesk-maya.md "autodesk-maya.md")                     | 2023<br>• 2026     | Included          | Included        | Included                |
| [Autodesk VRED](autodesk-vred.md "autodesk-vred.md")                     | 2025<br>• 2026     | Included          | Not included    | Not included            |
| [Blender](blender.md "blender.md")                                       | 3.6<br>• 5.1       | Included          | Included        | Included                |
| [Chaos V-Ray for Maya](autodesk-maya.md "autodesk-maya.md")              | 6<br>• 7           | Included          | Included        | Included                |
| [Foundry Nuke](foundry-nuke.md "foundry-nuke.md")                        | 15<br>• 17         | Included          | Included        | Included                |
| [KeyShot Studio](keyshot.md "keyshot.md")                                | 2023<br>• 2025     | Included          | Not included    | Included                |
| [Maxon Cinema 4D](maxon-cinema-4d.md "maxon-cinema-4d.md")               | 2024<br>• 2026     | Included          | Not included    | Included                |
| [Maxon Redshift for Maya](autodesk-maya.md "autodesk-maya.md")           | 2025-2026          | Included          | Included        | Included                |
| [SideFX Houdini](sidefx-houdini.md "sidefx-houdini.md")                  | 19.5<br>• 22.0     | Included          | Included        | Included                |

The standard installer doesn't include the Unreal Engine
submitter, which has a separate setup process. For installation
instructions, see the [Unreal Engine Submitter Setup Guide](https://github.com/aws-deadline/deadline-cloud-for-unreal-engine "https://github.com/aws-deadline/deadline-cloud-for-unreal-engine") on the GitHub
website.

Windows

1. In a file browser, navigate to the folder where the installer
   downloaded, and then select
   `DeadlineCloudSubmitter-windows-x64-installer.exe`.

   1. If a **Windows protected your PC**
      pop-up displays, choose **More
      info**.
   2. Choose **Run anyway**.

2. After the AWS Deadline Cloud Submitter Setup Wizard opens, choose
   **Next**.
3. Choose the installation scope by completing one of the
   following steps:

   - To install for only the current user, choose
     **User**.
   - To install for all users, choose
     **System**.

   If you choose **System**, you must
   exit the installer and re-run it as an administrator by
   completing the following steps:

        1. Right-click on
         `DeadlineCloudSubmitter-windows-x64-installer.exe`,
         and then choose **Run as
         administrator**.
        2. Enter your administrator credentials, and then
         choose **Yes**.
        3. Choose **System** for the
         installation scope.

4. After selecting the installation scope, choose
   **Next**.
5. Choose **Next** again to accept the
   installation directory.
6. Select **Integrated submitter for
   Nuke**, or whichever submitter you
   want to install.
7. Choose **Next**.
8. Review the installation, and choose
   **Next**.
9. Choose **Next** again, and then choose
   **Finish**.

Linux

###### Note

The Deadline Cloud integrated Nuke installer for
Linux and Deadline Cloud monitor can only be installed on
Linux distributions with at least GLIBC 2.31.

1. Open a terminal window.
2. To do a system install of the installer, enter the command
   `sudo -i` and press
   **Enter** to become root.
3. Navigate to the location where you downloaded the
   installer.

For example, `cd
 /home/`USER`/Downloads`. 4. To make the installer executable, enter `chmod +x
 DeadlineCloudSubmitter-linux-x64-installer.run`. 5. To run the Deadline Cloud submitter installer, enter
`./DeadlineCloudSubmitter-linux-x64-installer.run`. 6. When the installer opens, follow the prompts on your screen to
complete the Setup Wizard.

macOS (arm64)

1. In a file browser, navigate to the folder where the installer
   downloaded, and then select the file.
2. After the AWS Deadline Cloud Submitter Setup Wizard opens, choose
   **Next**.
3. Choose **Next** again to accept the
   installation directory.
4. Select **Integrated submitter for
   Maya**, or whichever submitter you
   want to install.
5. Choose **Next**.
6. Review the installation, and choose
   **Next**.
7. Choose **Next** again, and then choose
   **Finish**.

## Step 2: Install and set up Deadline Cloud monitor

You can install the Deadline Cloud monitor desktop application with Windows, Linux, or
macOS.

Windows

1. Download the Deadline Cloud monitor installer for Windows:

[Download Deadline Cloud monitor for Windows](https://downloads.deadlinecloud.amazonaws.com/dcm/latest/DeadlineCloudMonitor_x64-setup.exe "https://downloads.deadlinecloud.amazonaws.com/dcm/latest/DeadlineCloudMonitor_x64-setup.exe") 2. Run the downloaded installer and follow the prompts to complete the installation.

To perform a silent install, use the following command:

```
DeadlineCloudMonitor_x64-setup.exe /S
```

By default the monitor is installed in
`C:\Users{username}\AppData\Local\DeadlineCloudMonitor`. To
change the installation directory, use this command instead:

```
DeadlineCloudMonitor_x64-setup.exe /S /D={InstallDirectory}
```

Linux (AppImage)

###### To install Deadline Cloud monitor AppImage on RPM or Debian distros

###### Note

Deadline Cloud monitor requires GLIBC 2.34 or later. On Ubuntu
22 machines, install the Debian package instead of
the AppImage. For instructions, see the **Linux
(Debian)** tab.

1. Download the Deadline Cloud monitor AppImage:

[Download Deadline Cloud monitor (AppImage)](https://downloads.deadlinecloud.amazonaws.com/dcm/latest/deadline-cloud-monitor_amd64.AppImage "https://downloads.deadlinecloud.amazonaws.com/dcm/latest/deadline-cloud-monitor_amd64.AppImage") 2. On RHEL-family systems such as Red Hat
Linux, Rocky Linux, and Alma
Linux, create a symbolic link to the CA bundle.
RHEL-family systems keep the CA bundle at
`/etc/ssl/certs/ca-bundle.crt`, but Deadline Cloud monitor
expects `/etc/ssl/certs/ca-certificates.crt` and
blocks profile creation with the error `Couldn't load TLS
 file database` until that file exists. To create the
link, enter:

```
sudo ln -sf /etc/ssl/certs/ca-bundle.crt /etc/ssl/certs/ca-certificates.crt
```

3. To make the AppImage executable, enter:

```
chmod a+x deadline-cloud-monitor_amd64.AppImage
```

Linux (Debian)

###### To install Deadline Cloud monitor Debian package on Debian distros

###### Note

Deadline Cloud monitor requires GLIBC 2.34 or later.

1. Download the Deadline Cloud monitor Debian package:

[Download Deadline Cloud monitor (.deb)](https://downloads.deadlinecloud.amazonaws.com/dcm/latest/deadline-cloud-monitor_amd64.deb "https://downloads.deadlinecloud.amazonaws.com/dcm/latest/deadline-cloud-monitor_amd64.deb") 2. To install the Deadline Cloud monitor Debian package, enter:

```
sudo apt update
sudo apt install ./deadline-cloud-monitor_amd64.deb
```

3. If the install fails on packages that have unmet dependencies, fix
   the broken packages and then run the following commands.

```
sudo apt --fix-missing update
sudo apt update
sudo apt install -f
```

Linux (RPM)

###### To install Deadline Cloud monitor RPM on Red Hat Linux 10, Rocky Linux 10, or later

###### Note

Deadline Cloud monitor requires GLIBC 2.34 or later and
`webkit2gtk-4.1`, which isn't available on
Red Hat Linux 9 or Rocky Linux 9. On those systems, install the AppImage instead.
For instructions, see the **Linux
(AppImage)** tab.

1. Download the Deadline Cloud monitor RPM:

[Download Deadline Cloud monitor (.rpm)](https://downloads.deadlinecloud.amazonaws.com/dcm/latest/deadline-cloud-monitor.x86_64.rpm "https://downloads.deadlinecloud.amazonaws.com/dcm/latest/deadline-cloud-monitor.x86_64.rpm") 2. Install the Deadline Cloud monitor:

```
sudo dnf install deadline-cloud-monitor.x86_64.rpm
```

macOS (arm64)

1. Download the Deadline Cloud monitor installer for macOS:

[Download Deadline Cloud monitor for macOS (arm64)](https://downloads.deadlinecloud.amazonaws.com/dcm/latest/Deadline Cloud Monitor aarch64.dmg "https://downloads.deadlinecloud.amazonaws.com/dcm/latest/Deadline Cloud Monitor aarch64.dmg") 2. Open the downloaded file. When the window displays, select and
drag the Deadline Cloud monitor icon into the **Applications**
folder.

After you complete the download, you can verify the authenticity of the downloaded
software. You might want to do this to ensure no one has tampered with the files during
or after the download process. See [Verify the authenticity of downloaded software](verify-installer.md "verify-installer.md").

After downloading Deadline Cloud monitor, use the following procedure
to set up the Deadline Cloud monitor.

###### To set up Deadline Cloud monitor

1. Open **Deadline Cloud monitor**.
2. When prompted to create a new profile, complete the following steps.

   1. Enter your monitor URL into the URL input, which looks like
      `https://``MY-MONITOR``.``REGION``.deadlinecloud.amazonaws.com/`
   2. Enter a **Profile** name.
   3. Choose **Create Profile**.

   Your profile is created and your credentials are now shared with any
   software that uses the profile name that you created.

3. After you create the Deadline Cloud monitor profile, you can't change the profile name or the
   studio URL. If you need to make changes, do the following instead:

   1. Delete the profile. In the left navigation pane, choose
      **Deadline Cloud monitor** > **Settings**

   > **Delete**.
   2. Create a new profile with the changes that you want.

4. From the left navigation pane, use the **>Deadline Cloud monitor** option to
   do the following:

   - Change the Deadline Cloud monitor profile to log in to a different monitor.
   - Enable **Autologin** so you don't have to enter your
     monitor URL on subsequent opens of Deadline Cloud monitor.

5. Close the Deadline Cloud monitor window. It continues to run in the background and
   enable other Deadline Cloud tools to access your render farm.
6. For each digital content creation (DCC) application that you plan to use for
   your rendering projects, complete the following steps:

   1. From your Deadline Cloud submitter, open the Deadline Cloud workstation
      configuration.
   2. In the workstation configuration, select the profile that you created
      in the Deadline Cloud monitor. Your Deadline Cloud credentials are now shared with this DCC and
      your tools should work as expected.

## Step 3: Launch the Deadline Cloud submitter

The steps to load and launch the submitter are unique to each DCC. For the
instructions for your DCC, see [Supported Software](supported-software.md "supported-software.md").

If you want a free DCC to test your setup with, Blender is a
good choice. See the Blender [Installation](blender.md#blender-installation "blender.md#blender-installation") instructions.

After you submit a job from your DCC, your Deadline Cloud farm receives it and a compatible fleet processes it. To verify your setup, open the monitor and confirm that your job appears and completes. For information on how to view job progress in the monitor, see [Using the Monitor](working-with-deadline-monitor.md "working-with-deadline-monitor.md").
