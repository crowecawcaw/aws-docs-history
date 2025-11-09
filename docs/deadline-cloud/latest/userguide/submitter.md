# Set up Deadline Cloud submitters

This process is for administrators and artists who want to install, set up, and launch the
AWS Deadline Cloud submitter. A Deadline Cloud _submitter_ is a digital
content creation (DCC) plugin. Artists use it to submit jobs from a third-party DCC
interface that they're familiar with.

###### Note

This process must be completed on all workstations that artists will use for
submitting renders.

Each workstation must have the DCC installed before installing the corresponding
submitter. For example, if you want to download the Deadline Cloud submitter for Blender,
you need to have Blender already installed on your workstation.

We provide reasonable defaults for keeping workstations secure. For more information about
securing your workstation, see
[Security best practices

- workstations](security-best-practices.md#workstations "security-best-practices.md#workstations").

###### Topics

- [Step 1: Install the Deadline Cloud submitter](#submitter-installation "#submitter-installation")
- [Step 2: Install and set up
  Deadline Cloud monitor](#install-deadline-cloud-monitor "#install-deadline-cloud-monitor")
- [Step 3: Launch the Deadline Cloud submitter](#load-dca-plugin "#load-dca-plugin")
- [Supported submitters](supported-submitters.md "supported-submitters.md")

## Step 1: Install the Deadline Cloud submitter

The following sections guide you through the steps to install the Deadline Cloud
submitter.

### Download the submitter installer

Before you can install the Deadline Cloud submitter, you must download the submitter
installer.

1. Sign in to the AWS Management Console and open the Deadline Cloud [console](https://console.aws.amazon.com/deadlinecloud/home "https://console.aws.amazon.com/deadlinecloud/home").
2. From the side navigation pane, choose
   **Downloads**.
3. From the Deadline Cloud submitter installer section, select the
   **installer** for your computer's operating
   system, and then choose **Download**.
4. (Optional) [Verify the authenticity of downloaded software](security-best-practices.md#verify-installer "security-best-practices.md#verify-installer").

### Install the Deadline Cloud

submitter

With the installer, you can install the following submitters:

| Software                 | Supported versions | Windows installer                                                                                                   | Linux installer                                                                                                 | MacOS (arm64) installer                                                                                             |
| ------------------------ | ------------------ | ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Adobe After Effects      | 2024<br>• 2025     | Included                                                                                                            | Not included                                                                                                    | Included                                                                                                            |
| Autodesk 3ds Max         | 2024<br>• 2026     | Included                                                                                                            | Not included                                                                                                    | Not included                                                                                                        |
| Autodesk Arnold for Maya | 7.1<br>• 7.4       | Included                                                                                                            | Included                                                                                                        | Included                                                                                                            |
| Autodesk Maya            | 2023<br>• 2026     | [Included](supported-submitters.md#submitter-launch-maya "supported-submitters.md#submitter-launch-maya")           | [Included](supported-submitters.md#submitter-launch-maya "supported-submitters.md#submitter-launch-maya")       | [Included](supported-submitters.md#submitter-launch-maya "supported-submitters.md#submitter-launch-maya")           |
| Autodesk VRED            | 2025<br>• 2026     | Included                                                                                                            | Not included                                                                                                    | Not included                                                                                                        |
| Blender                  | 3.6<br>• 4.5       | [Included](supported-submitters.md#submitter-launch-blender "supported-submitters.md#submitter-launch-blender")     | [Included](supported-submitters.md#submitter-launch-blender "supported-submitters.md#submitter-launch-blender") | [Included](supported-submitters.md#submitter-launch-blender "supported-submitters.md#submitter-launch-blender")     |
| Chaos V-Ray for Maya     | 6<br>• 7           | Included                                                                                                            | Included                                                                                                        | Included                                                                                                            |
| Foundry Nuke             | 15<br>• 16         | [Included](supported-submitters.md#submitter-launch-nuke "supported-submitters.md#submitter-launch-nuke")           | [Included](supported-submitters.md#submitter-launch-nuke "supported-submitters.md#submitter-launch-nuke")       | [Included](supported-submitters.md#submitter-launch-nuke "supported-submitters.md#submitter-launch-nuke")           |
| KeyShot Studio           | 2023<br>• 2025     | [Included](supported-submitters.md#submitter-launch-keyshot "supported-submitters.md#submitter-launch-keyshot")     | Not included                                                                                                    | [Included](supported-submitters.md#submitter-launch-keyshot "supported-submitters.md#submitter-launch-keyshot")     |
| Maxon Cinema 4D          | 2024<br>• 2025     | [Included](supported-submitters.md#submitter-launch-cinema-4d "supported-submitters.md#submitter-launch-cinema-4d") | Not included                                                                                                    | [Included](supported-submitters.md#submitter-launch-cinema-4d "supported-submitters.md#submitter-launch-cinema-4d") |
| Maxon Redshift for Maya  | 2025               | Included                                                                                                            | Included                                                                                                        | Included                                                                                                            |
| SideFX Houdini           | 19.5<br>• 21.0     | [Included](supported-submitters.md#submitter-launch-houdini "supported-submitters.md#submitter-launch-houdini")     | [Included](supported-submitters.md#submitter-launch-houdini "supported-submitters.md#submitter-launch-houdini") | [Included](supported-submitters.md#submitter-launch-houdini "supported-submitters.md#submitter-launch-houdini")     |

You can install other submitters not listed here. We use Deadline Cloud libraries to build
submitters. Some of the other submitters include Unreal Engine and 3ds Max. You can
find the source code for these libraries and submitters in the [aws-deadline GitHub](https://github.com/aws-deadline "https://github.com/aws-deadline")
organization.

Windows

1.  In a file browser, navigate to the folder where the installer
    downloaded, and then select
    `DeadlineCloudSubmitter-windows-x64-installer.exe`.
    1. If a **Windows protected your PC**
       pop-up displays, choose **More
       info**.
    2. Choose **Run anyway**.

2.  After the AWS Deadline Cloud Submitter Setup Wizard opens, choose
    **Next**.
3.  Choose the installation scope by completing one of the
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

4.  After selecting the installation scope, choose
    **Next**.
5.  Choose **Next** again to accept the
    installation directory.
6.  Select **Integrated submitter for
    Nuke**, or whichever submitter you
    want to install.
7.  Choose **Next**.
8.  Review the installation, and choose
    **Next**.
9.  Choose **Next** again, and then choose
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

## Step 2: Install and set up

Deadline Cloud monitor

You can install the Deadline Cloud monitor desktop application with Windows, Linux, or
macOS.

Windows

1. If you haven't already, sign in to the AWS Management Console and open the
   Deadline Cloud [console](https://console.aws.amazon.com/deadlinecloud/home "https://console.aws.amazon.com/deadlinecloud/home").
2. From the left navigation pane, choose
   **Downloads**.
3. In the **Deadline Cloud monitor** section, select the latest
   Windows file, and choose **Download**.

To perform a silent install, use the following command:

```
DeadlineCloudMonitor_VERSION_x64-setup.exe /S
```

By default the monitor is installed in
`C:\Users{username}\AppData\Local\DeadlineCloudMonitor`. To
change the installation directory, use this command instead:

```
DeadlineCloudMonitor_VERSION_x64-setup.exe /S /D={InstallDirectory}
```

Linux (AppImage)

###### To install Deadline Cloud monitor AppImage on Debian distros

1. Download the latest Deadline Cloud monitor AppImage.
2. ###### Note

This step is for Ubuntu 22 and up. For other versions of
Ubuntu, skip this step.

To install libfuse2, enter:

```
sudo apt update
sudo apt install libfuse2
```

3. To make the AppImage executable, enter:

```
chmod a+x deadline-cloud-monitor_`<APP_VERSION>`_amd64.AppImage
```

Linux (Debian)

###### To install Deadline Cloud monitor Debian package on Debian distros

1. Download the latest Deadline Cloud monitor Debian package.
2. ###### Note

This step is for Ubuntu 22 and up. For other versions of
Ubuntu, skip this step.

To install libssl1.1, enter:

```
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2_amd64.deb
sudo apt install ./libssl1.1_1.1.1f-1ubuntu2_amd64.deb
```

3. To install the Deadline Cloud monitor Debian package, enter:

```
sudo apt update
sudo apt install ./deadline-cloud-monitor_`<APP_VERSION>`_amd64.deb
```

4. If the install fails on packages that have unmet dependencies, fix
   the broken packages and then run the following commands.

```
sudo apt --fix-missing update
sudo apt update
sudo apt install -f
```

Linux (RPM)

###### To install Deadline Cloud monitor RPM on Rocky Linux 9 or Alma

Linux 9

1. Download the latest Deadline Cloud monitor RPM.
2. Add the extra packages for the Enterprise Linux 9
   repository:

```
sudo dnf install epel-release
```

3. Install compat-openssl11 for the libssl.so.1.1 dependency:

```
sudo dnf install compat-openssl11 deadline-cloud-monitor-`<VERSION>`-1.x86_64.rpm
```

###### To install Deadline Cloud monitor RPM on Red Hat Linux 9

1. Download the latest Deadline Cloud monitor RPM.
2. Enable the CodeReady Linux Builder
   repository:

```
subscription-manager repos --enable codeready-builder-for-rhel-9-x86_64-rpms
```

3. Install the extra packages for Enterprise
   RPM:

```
sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
```

4. Install compat-openssl11 for the libssl.so.1.1 dependency:

```
sudo dnf install compat-openssl11 deadline-cloud-monitor-`<VERSION>`-1.x86_64.rpm
```

###### To install Deadline Cloud monitor RPM on Rocky Linux 8, Alma

Linux 8, or Red Hat Linux 8

1. Download the latest Deadline Cloud monitor RPM.
2. Install the Deadline Cloud monitor:

```
sudo dnf install deadline-cloud-monitor-`<VERSION>`-1.x86_64.rpm
```

macOS (arm64)

1. If you haven't already, sign in to the AWS Management Console and open the
   Deadline Cloud [console](https://console.aws.amazon.com/deadlinecloud/home "https://console.aws.amazon.com/deadlinecloud/home").
2. From the left navigation pane, choose
   **Downloads**.
3. In the **Deadline Cloud monitor** section, select the latest
   macOS file, and choose **Download**.
4. Open the downloaded file. When the window displays, select and
   drag the Deadline Cloud monitor icon into the **Applications**
   folder.

After you complete the download, you can verify the authenticity of the downloaded
software. You might want to do this to ensure no one has tampered with the files during
or after the download process. See Verify authenticity of downloaded software in Step

1.

After downloading Deadline Cloud monitor and verifying the authenticity, use the following procedure
to set up the Deadline Cloud monitor.

###### To set up Deadline Cloud monitor

1. Open **Deadline Cloud monitor**.
2. When prompted to create a new profile, complete the following steps.
   1. Enter your monitor URL into the URL input, which looks like
      `https://``MY-MONITOR``.deadlinecloud.amazonaws.com/`
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
   - Enable **Autologin** so you don’t have to enter your
     monitor URL on subsequent opens of Deadline Cloud monitor.

5. Close the Deadline Cloud monitor window. It continues to run in the background and sync your
   credentials every 15 minutes.
6. For each digital content creation (DCC) application that you plan to use for
   your rendering projects, complete the following steps:
   1. From your Deadline Cloud submitter, open the Deadline Cloud workstation
      configuration.
   2. In the workstation configuration, select the profile that you created
      in the Deadline Cloud monitor. Your Deadline Cloud credentials are now shared with this DCC and
      your tools should work as expected.

## Step 3: Launch the Deadline Cloud submitter

The following example shows how to install the Blender submitter. You
can install other submitters using the instructions in [Supported submitters](supported-submitters.md "supported-submitters.md").

###### To launch the Deadline Cloud submitter in Blender

###### Note

Support for Blender is provided using the Conda
environment for service-managed fleets. For more information, see [Default Conda queue
environment](create-queue-environment.md#conda-queue-environment "create-queue-environment.md#conda-queue-environment").

1. Open **Blender**.
2. Choose **Edit**, then **Preferences**. Under
   **File Paths** choose **Script
   Directories**, then choose **Add**. Add a script
   directory for the python folder where the Blender submitter was
   installed:

```
Windows:
   %USERPROFILE%\DeadlineCloudSubmitter\Submitters\Blender\python\
Linux:
   ~/DeadlineCloudSubmitter/Submitters/Blender/python/
MacOS:
   ~/DeadlineCloudSubmitter/Submitters/Blender/python/
```

3. Restart Blender.
4. Choose **Edit**, then **Preferences**. Next,
   choose **Add-ons**, then search for **Deadline Cloud for
   Blender**. Select the checkbox to enable the
   add-on.
5. Open a Blender scene with dependencies that exist within the
   asset root directory.
6. In the **Render** menu, select the Deadline Cloud dialog.
   1. If you are not already authenticated in the Deadline Cloud submitter, the
      **Credentials Status** shows as
      **NEEDS_LOGIN**.
   2. Choose **Login**.
   3. A login browser window displays. Log in with your user
      credentials.
   4. Choose **Allow**. You are now logged in and the
      **Credentials Status** shows as
      **AUTHENTICATED**.

7. Choose **Submit**.
