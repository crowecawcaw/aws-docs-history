

# Troubleshooting agent issues
<a name="Troubleshooting-Agent-Issues"></a>

Use the information in this section to troubleshoot issues with installing the replication agent.

**Topics**
+ [Error: Installation failed](#Error-Installation-Failed)
+ [Where can I find the MGN Agent logs?](#MGN-Agent-Log)

## Error: Installation failed
<a name="Error-Installation-Failed"></a>

This type of error means that the agent was not installed on the source server, and therefore the server will not appear on the AWS Transform MGN console. After you fix the issue that caused the installation to fail, you need to rerun the Agent Installer file to install the agent. 

### Error: too many volumes selected for replication
<a name="Installation-Failed-Disk-Limit"></a>

Installation fails with an error similar to the following when you select more disks than the AWS Replication Agent supports:

```
The devices you entered span over more than 63 volumes. Up to 63 volumes are supported per machine.
Installation failed.
```

The AWS Replication Agent can replicate up to 63 disks from a single source server. To resolve this error, select 63 or fewer disks for replication and rerun the Agent Installer file.

### This app can't run on your PC error - Windows
<a name="this-app-error"></a>

If you encounter the following error "This app can't run on your PC", when trying to install the AWS Replication Agent on your Windows 10 source Server, try the following. 

This error is indicative that your particular version of Windows 10 is likely the 32-bit version. To verify this, you can

 1. Use the Windows key \+ I keyboard shortcut to open the Settings app.

 2. Choose System.

 3. Choose About.

 4. Under System type, you will see two pieces of information: if it says 32-bit operating system, x64-based processor, then it means that your PC is running a 32-bit version of Windows 10 on a 64-bit processor. 

If it says 32-bit operating system, x86-based processor, then your computer doesn't support Windows 10 (64-bit). 

If your OS is indeed 64-bit, then there may be other elements blocking the installation of your agent. The block is actually coming from the Windows Operating System itself. You would need to identify what the cause is. One of the ways is running [sfc scan](https://support.microsoft.com/en-au/topic/use-the-system-file-checker-tool-to-repair-missing-or-corrupted-system-files-79aa86cb-ca52-166a-92a3-966e85d4094e). 

### Is having a mounted '/tmp' directory a requirement for the agent?
<a name="Agent-TMP"></a>

The simple requirement is just to have enough free space. There is no need for this to be a separate mount. The need for the '/tmp' requirement is actually only if '/tmp' is a separate mount. If '/tmp' is not a separate mount, then it would fall under '/', for which we have the 2 GB free requirement. This allows for the '/tmp' to fall into this requirement.

### Installation failed - old agent
<a name="Installation-Failed-Old"></a>

Installation may fail due to an old AWS Replication Agent. Ensure that you are attempting to install the latest version of the AWS Replication Agent. You can learn how to download the Agent [here](adding-servers.md). 

### Installation cannot be completed - CloudEndure Agent
<a name="Installation-Failed-installed-agent"></a>

Agent installation will fail if the source server already has the CloudEndure User Agent installed on it. You will need to[ uninstall the CloudEndure Agent](https://docs.cloudendure.com/#Installing_the_CloudEndure_Agents/Uninstalling_the_Agents/Uninstalling_the_Agents.htm#Uninstalling_the_Agents%3FTocPath%3DNavigation%7CInstalling%2520the%2520CloudEndure%2520Agents%7CUninstalling%2520the%2520Agents%7C_____0) and then install the AWS Replication Agent in order to proceed. 

At times, uninstalling the CloudEndure Agent alone is not enough, as the Agent driver may remain. If that is the case, you will need to delete the agent driver manually. 

**Linux**

Run the following command to identify the CloudEndure driver:

`lsmod | grep CE_AgentDriver`

Then, run the following command to delete the driver if it exists:

`rmmod CE_AgentDriver`

**Windows**

Run the following command in cmd to identify the CloudEndure driver:

`sc query ce_driver`

`sc query ce_filter_driver`

Then, run the following command to delete the driver if it exists:

`sc delete ce_driver`

`sc delete ce_filter_driver`

### Installation failed on Linux Server
<a name="Installation-Failed-Linux"></a>

If the installation failed on a Linux Source server, check the following:

1. **Free Disk Space**

   Free disk space on the root directory – verify that you have at least 2 GB of free disk on the root directory (/) of your Source Server. To check the available disk space on the root directory, run the following command: df -h /

   Free disk space on the /tmp directory – for the duration of the installation process only, verify that you have at least 1 GB of free disk on the /tmp directory. To check the available disk space on the /tmp directory run the following command: df -h /tmp 

   After you have entered the above commands for checking the available disk space, the results will be displayed as follows:   
![Terminal output showing disk space usage with root filesystem at 19% and tmp at 19% usage.](https://docs.aws.amazon.com/mgn/latest/ug/images/troubleshooting-25-re.png)

1. **The format of the list of disks to replicate** 

   During the installation, when you are asked to enter the disks you want to replicate, do NOT use apostrophes, brackets, or disk paths that do not exist. Type only existing disk paths, and separate them with a comma, as follows:

    `/dev/xvda,/dev/xvdb`. 

1. **Version of the Kernel headers package**

   Make sure that the kernel headers installed on the source server exactly match the running kernel version. For instructions on how to verify and install the correct kernel headers, see [Linux installation requirements](installation-requirements.md#linux-requirements).

1. **The make, openssl, wget, curl, gcc and build-essential packages.**

   **Note**: Usually, the existence of these packages is not required for Agent installation. However, in some cases where the installation fails, installing these packages will solve the problem.

   If the installation failed, the make, openssl, wget, curl, gcc, and build-essential packages should be installed and stored in your current path.

   To verify the existence and location of the required packages, run the following command:

   which <package>

   For Example, to locate the make package:

   which make  
![Terminal command output showing the result of the 'which make' command.](https://docs.aws.amazon.com/mgn/latest/ug/images/troubleshooting-30-re.png)

1. **Error: urlopen error [Errno 10060] Connection times out.**

   This error occurs when outbound traffic is not allowed over TCP Port 443. Port 443 needs to be open outbound to the MGN Service endpoint.

1. **Powerpath support**

   Contact AWS Support for instructions on how to install the AWS Transform MGN Agent on such machines.

1. **Error: You need to have root privileges to run this script.**

   Make sure you run the installer either as root or by adding sudo at the beginning:

   `sudo ./aws-replication-installer-init`

1. Error: *version `GLIBC\_2.7' not found (required by ./aws-replication-installer-64bit)*

   You receive this error when you try to install the agent on an unsupported Linux operating system. See [Supported Linux operating systems ](https://docs.aws.amazon.com/mgn/latest/ug/Supported-Operating-Systems.html#Supported-Operating-Systems-Linux).

### Installation failed on Windows machine
<a name="Installation-Failed-Windows"></a>

If the installation failed on a Windows Source server, check the following:

1. **.NET Framework**

   Verify that .NET Framework version 3.5 or above is installed on your Windows Source servers. 

1. **Free disk space**

   Verify that there is at least 1 GB of free disk space on the root directory (C:\\) of your Source servers for the installation. 

1. **net.exe and sc.exe location **

   Verify that the net.exe and/or sc.exe files, located by default in the C:\\Windows\\System32 folder, are included in the **PATH Environment Variable**.

   1. Navigate to **Control Panel >System and Security >System >Advanced system settings.**

   1. On the **System Properties** dialog box **Advanced** tab, choose the **Environment Variables** button.

   1. On the **System Variables** section of the **Environment Variables** pane, select the **Path** variable. Then, choose the **Edit** button to view its contents.

   1. On the **Edit System Variable** pane, review the defined paths in the **Variable value** field. If the path of the net.exe and/or sc.exe files does not appear there, manually add it to the **Variable value** field, and choose **OK**.

### Windows - Installation Failed - Request Signature
<a name="windows-Agent-error-copy"></a>

If the AWS Replication Agent installation fails on Windows with the following error:

```
botocore.exceptions.ClientError: An error occurred (InvalidSignatureException) when calling the GetAgentInstallationAssetsForMgn operation: {"message":"The request signature we calculated does not match the signature you provided. Check your AWS Secret Access Key and signing method. Consult the service documentation  for details.
```

Attempt to rerun the installer with PowerShell instead of CMD. At times, when the installer is run in CMD, the AWS Secret Key does not get pasted properly into the installer and causes installation to fail.

### Error – certificate verify failed
<a name="error-certificate-verify-failed"></a>

This error (CERTIFICATE\_VERIFY\_FAILED) may indicate that the OS does not trust the certification authority used by our endpoints. To resolve this issue, try the following steps: 

1. Open Microsoft Edge or Internet Explorer to update the operating system trusted root certificates. This will work if the operating system does not have restrictions to download the certificates.

1. If the first step does not resolve the issue, [download and install the Amazon Root Certificates manually](https://www.amazontrust.com/repository/).

## Where can I find the MGN Agent logs?
<a name="MGN-Agent-Log"></a>

The MGN Agent logs are stored in agent.log.0:
+ **Linux:** /var/lib/aws-replication-agent/agent.log.0
+ **Windows 64 bit:** C:\\Program Files (x86)\\AWS Replication Agent\\agent.log.0
+ **Windows 32 bit:** C:\\Program Files\\AWS Replication Agent\\agent.log.0

In addition, you can review the installation log located in: <install\_path>\\aws\_replication\_agent\_installer.log