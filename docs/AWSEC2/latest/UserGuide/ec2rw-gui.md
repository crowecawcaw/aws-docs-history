# Troubleshoot impaired Windows instance with the EC2Rescue GUI

EC2Rescue for Windows Server can perform the following analysis on **offline instances**:

| Option              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Diagnose and Rescue | EC2Rescue for Windows Server can detect and address issues with the following<br>service settings:<br>• System Time<br>+ **RealTimeisUniversal\*<br>• ‐ Detects whether the<br>`RealTimeisUniversal` registry key is enabled. If disabled,<br>Windows system time drifts when the timezone is set to a value other than<br>UTC.<br>• Windows Firewall<br>+ **Domain networks*<br>• ‐ Detects whether this Windows<br>Firewall profile is enabled or disabled.<br>+ \*\*Private networks*<br>• ‐ Detects whether this<br>Windows Firewall profile is enabled or disabled.<br>+ **Guest or public networks\*<br>• ‐ Detects whether<br>this Windows Firewall profile is enabled or disabled.<br>• Remote Desktop<br>+ **Service Start*<br>• ‐ Detects whether the Remote<br>Desktop service is enabled.<br>+ \*\*Remote Desktop Connections*<br>• ‐ Detects whether<br>this is enabled.<br>+ **TCP Port\*<br>• ‐ Detects which port the Remote<br>Desktop service is listening on.<br>• EC2Config (Windows Server 2012 R2 and earlier)<br>+ **Installation*<br>• ‐ Detects which EC2Config version<br>is installed.<br>+ \*\*Service Start*<br>• ‐ Detects whether the EC2Config<br>service is enabled.<br>+ **Ec2SetPassword\*<br>• ‐ Generates a new administrator<br>password.<br>+ **Ec2HandleUserData*<br>• ‐ Allows you to run a<br>user data script on the next boot of the instance.<br>• EC2Launch (Windows Server 2016 and later)<br>+ \*\*Installation*<br>• ‐ Detects which EC2Launch version<br>is installed.<br>+ **Ec2SetPassword\*<br>• ‐ Generates a new administrator<br>password.<br>• Network Interface<br>+ **DHCP Service Startup*<br>• ‐ Detects whether the<br>DHCP service is enabled.<br>+ \*\*Ethernet detail*<br>• ‐ Displays information about<br>the network driver version, if detected.<br>+ **DHCP on Ethernet\*<br>• ‐ Detects whether DHCP is<br>enabled.<br>• Disk signature status<br>+ **Signature on disk*<br>• and \*\*Signature on Boot<br>Configuration Database (BCD)*<br>• ‐ Detects whether the disk<br>signature and the BCD signature are the same. If the values are different,<br>EC2Rescue attempts to overwrite the disk signature with the signature on<br>BCD. |
| Restore             | Perform one of the following actions:<br>• **Last Known Good Configuration** ‐ Attempts to boot<br>the instance into the last known bootable state.<br>• **Restore registry from backup** ‐ Restores the<br>registry from `\Windows\System32\config\RegBack`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Capture Logs        | Allows you to capture logs on the instance for analysis.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

EC2Rescue for Windows Server can collect the following data from **active and offline instances**:

| Item                                           | Description                                                                                                                                                 |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Event Log                                      | Collects application, system, and EC2Config event logs.                                                                                                     |
| Registry                                       | Collects `SYSTEM` and `SOFTWARE`<br>hives.                                                                                                                  |
| Windows Update Log                             | Collects log files generated by Windows Update.<br>NoteIn Windows Server 2016 and later, the log is collected in Event<br>Tracing for Windows (ETW) format. |
| Sysprep Log                                    | Collects log files generated by the Windows System Preparation tool.                                                                                        |
| Driver Setup Log                               | Collects Windows SetupAPI logs (`setupapi.dev.log` and<br>`setupapi.setup.log`).                                                                            |
| Boot Configuration                             | Collects `HKEY_LOCAL_MACHINE\BCD00000000` hive.                                                                                                             |
| Memory Dump                                    | Collects any memory dump files that exist on the instance.                                                                                                  |
| EC2Config File                                 | Collects log files generated by the EC2Config service.                                                                                                      |
| EC2Launch File                                 | Collects log files generated by the EC2Launch scripts.                                                                                                      |
| SSM Agent File                                 | Collects log files generated by SSM Agent and Patch Manager logs.                                                                                           |
| EC2 ElasticGPUs File                           | Collects event logs related to elastic GPUs.                                                                                                                |
| ECS                                            | Collects logs related to Amazon ECS.                                                                                                                        |
| CloudEndure                                    | Collects log files related to CloudEndure Agent.                                                                                                            |
| AWS Replication Agent for MGN or DRS Log Files | Collects log files related to AWS Application Migration Service or AWS Elastic Disaster Recovery.                                                           |

EC2Rescue for Windows Server can collect the following additional data from **active instances**:

| Item                | Description                     |
| ------------------- | ------------------------------- |
| System Information  | Collects MSInfo32.              |
| Group Policy Result | Collects a Group Policy report. |

## Analyze an offline instance

The **Offline Instance** option is useful for debugging boot issues
with Windows instances.

###### To perform an action on an offline instance

1. From a working Windows Server instance, download the [EC2Rescue for Windows Server](https://s3.amazonaws.com/ec2rescue/windows/EC2Rescue_latest.zip?x-download-source=docs "https://s3.amazonaws.com/ec2rescue/windows/EC2Rescue_latest.zip?x-download-source=docs") tool and extract the files.

You can run the following PowerShell command to download EC2Rescue without changing your Internet Explorer
Enhanced Security Configuration (ESC):

```

Invoke-WebRequest https://s3.amazonaws.com/ec2rescue/windows/EC2Rescue_latest.zip -OutFile $env:USERPROFILE\Desktop\EC2Rescue_latest.zip
```

This command will download the EC2Rescue .zip file to the desktop of the currently logged in user.

###### Note

If you receive an error when downloading the file, and you
are using Windows Server 2016 or earlier, TLS 1.2 might need
to be enabled for your PowerShell terminal. You can enable
TLS 1.2 for the current PowerShell session with the
following command and then try again:

```
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
```

2. Stop the faulty instance, if it is not stopped already.
3. Detach the EBS root volume from the faulty instance and attach the volume to a
   working Windows instance that has EC2Rescue for Windows Server installed.
4. Run the EC2Rescue for Windows Server tool on the working instance and choose
   **Offline Instance**.
5. Select the disk of the newly mounted volume and choose
   **Next**.
6. Confirm the disk selection and choose **Yes**.
7. Choose the offline instance option to perform and choose
   **Next**.

The EC2Rescue for Windows Server tool scans the volume and collects troubleshooting
information based on the selected log files.

## Collect data from an active instance

You can collect logs and other data from an active instance.

###### To collect data from an active instance

1. Connect to your Windows instance.
2. Download the [EC2Rescue for Windows Server](https://s3.amazonaws.com/ec2rescue/windows/EC2Rescue_latest.zip?x-download-source=docs "https://s3.amazonaws.com/ec2rescue/windows/EC2Rescue_latest.zip?x-download-source=docs") tool to your Windows instance and extract the files.

You can run the following PowerShell command to download EC2Rescue without changing your Internet Explorer
Enhanced Security Configuration (ESC):

```

Invoke-WebRequest https://s3.amazonaws.com/ec2rescue/windows/EC2Rescue_latest.zip -OutFile $env:USERPROFILE\Desktop\EC2Rescue_latest.zip

```

This command will download the EC2Rescue .zip file to the desktop of the currently logged in user.

###### Note

If you receive an error when downloading the file, and you
are using Windows Server 2016 or earlier, TLS 1.2 might need
to be enabled for your PowerShell terminal. You can enable
TLS 1.2 for the current PowerShell session with the
following command and then try again:

```
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
```

3. Open the EC2Rescue for Windows Server application and accept the license
   agreement.
4. Choose **Next**, **Current instance**,
   **Capture logs**.
5. Select the data items to collect and choose **Collect...**. Read
   the warning and choose **Yes** to continue.
6. Choose a file name and location for the ZIP file and choose
   **Save**.
7. After EC2Rescue for Windows Server completes, choose **Open Containing
   Folder** to view the ZIP file.
8. Choose **Finish**.
