# Install the AWS IoT SiteWise Edge

gateway software on your local device

After you've created an AWS IoT SiteWise Edge gateway, install the SiteWise Edge gateway software on
your local device. SiteWise Edge gateway software can be installed on local devices that have
Linux or Microsoft Windows server operating systems installed.

###### Important

Make sure that your local device connects to the internet.

Linux
The following procedure uses SSH to connect to your local device.
Alternatively, you can use a USB flash drive or other tools to transfer the
installer file to your local device. If you don't want to use SSH, skip to
**Step 2: Install the SiteWise Edge gateway software**
below.

**SSH prerequisites**

Before you connect to your device using SSH, complete the following
prerequisites.

- Linux and macOS - Download and install OpenSSH. For more
  information, see [https://www.openssh.com](https://www.openssh.com/ "https://www.openssh.com/").

###### Step 1: Copy the installer to your SiteWise Edge gateway device

The following instructions explain how to connect to your local device
using an SSH client.

1. To connect to your device, run the following command in a terminal
   window on your computer, replacing
   `username` and
   `IP` with a username that has elevated
   privileges and IP address.

```
ssh `username`@`IP`
```

2. To transfer the installer file that AWS IoT SiteWise generated to your
   SiteWise Edge gateway device, run the following command.

###### Note

    * Replace
     `path-to-saved-installer`
     with the path on your computer that you used to save the
     installer file and the name of the installer
     file.
    * Replace `IP-address` with the
     IP address of your local device.
    * Replace
     `directory-to-receive-installer`
     with the path on your local device that you use to
     receive the installer file.

```
scp `path-to-saved-installer`.sh `user-name`@`IP-address`:`directory-to-receive-installer`
```

###### Step 2: Install the SiteWise Edge gateway software

In the following procedures, run the commands in a terminal window on
your SiteWise Edge gateway device.

1. Give the installer file the execute permission.

```
chmod +x `path-to-installer`.sh
```

2. Run the installer.

```
sudo ./`path-to-installer`.sh
```

Windows Server
**Prerequisites**

You must have the following prerequisites to install the SiteWise Edge gateway
software:

- Microsoft Windows Server 2019 or later
  installed
- Administrator privileges
- PowerShell version 5.1 or later installed
- SiteWise Edge gateway installer downloaded to the Windows Server where
  it will be provisioned

###### Step 1: Run PowerShell as administrator

1. On the Windows server where you want to install SiteWise Edge gateway,
   log in as administrator.
2. Enter **PowerShell** in the Windows search
   bar.
3. In the search results, open the context (right-click) menu on the
   Windows PowerShell app. Choose **Run as
   Administrator**.

###### Step 2: Install the SiteWise Edge gateway software

Run the following commands in a terminal window on your SiteWise Edge
Gateway device.

1. Unblock the SiteWise Edge gateway installer.

```
unblock-file path-to-installer.ps1
```

2. Run the Installer.

```
./path-to-installer.ps1
```

###### Note

If the script execution is disabled on the system, change the
script execution policy to `RemoteSigned`.

```
Set-ExecutionPolicy RemoteSigned
```

The next step depends on the _type_ of self-hosted gateway you
need. Continue to [MQTT-enabled, V3 gateways for AWS IoT SiteWise Edge](mqtt-enabled-v3-gateway.md "mqtt-enabled-v3-gateway.md") or [Classic streams, V2 gateways for AWS IoT SiteWise Edge](classic-streams-v2-gateway.md "classic-streams-v2-gateway.md").
