# Endpoint Security and Antivirus

The brief ephemeral nature of Amazon AppStream 2.0 instances and the lack of persistency
of data means a different approach is required to ensure user experience and performance is
not compromised by activities that would be required on a persistent desktop. Endpoint
Security agents are installed in AppStream 2.0 images when there is an organizational policy
or when used with external data ingress e.g. e-mail, files ingress, external web
browsing.

## Removing unique identifiers

Endpoint Security agents may have a globally unique identifier (GUID) which must be
reset during the fleet instance creation process. Vendors have instructions on installing
their products in images which will ensure a new GUID is generated for each instance
generated from an image.

To ensure the GUID is not generated, install the Endpoint Security agent as the last
action before running the AppStream 2.0 Assistant to generate the image.

## Performance optimization

Endpoint Security Vendors provide switches and setting that optimize the performance of
AppStream 2.0. The settings vary between vendors and can be found in their documentation,
typically in a section on VDI. Some common settings include but are not limited to
are:

- Turn off boot up scans to ensure instance creation, startup and login times
  are minimized
- Turn off scheduled scans to prevent unnecessary scans
- Turn off signature caches to prevent file enumeration
- Enable VDI optimized IO settings
- Exclusions required by applications to ensure performance

Endpoint security vendors provide instructions for use with virtual desktop environments
which optimize performance.

- Trend Micro Office Scan [Support for Virtual Desktop Infrastructure - Apex One/OfficeScan
  (trendmicro.com)](https://success.trendmicro.com/solution/1055260-best-practice-for-setting-up-virtual-desktop-infrastructure-vdi-in-officescan "https://success.trendmicro.com/solution/1055260-best-practice-for-setting-up-virtual-desktop-infrastructure-vdi-in-officescan")
- CrowdStrike and [How to
  Install the CrowdStrike Falcon in the Data Center](https://www.crowdstrike.com/blog/tech-center/install-falcon-datacenter/ "https://www.crowdstrike.com/blog/tech-center/install-falcon-datacenter/")
- Sophos and [Sophos
  Central Endpoint: How to install on a gold image to avoid duplicate identities](https://support.sophos.com/support/s/article/KB-000035040?language=en_US "https://support.sophos.com/support/s/article/KB-000035040?language=en_US")
  and [Sophos
  Central: Best practices when installing Windows Endpoints in Virtual Desktop
  Environments](https://support.sophos.com/support/s/article/KB-000039009?language=en_US "https://support.sophos.com/support/s/article/KB-000039009?language=en_US")
- McAfee and [McAfee Agent
  provisioning and deployment on Virtual Desktop Infrastructure systems](https://kc.mcafee.com/corporate/index?page=content&id=KB87654 "https://kc.mcafee.com/corporate/index?page=content&id=KB87654")
- Microsoft Endpoint Security and [Configuring Microsoft Defender Antivirus for non-persistent VDI machines - Microsoft
  Tech Community](https://techcommunity.microsoft.com/t5/microsoft-defender-for-endpoint/configuring-microsoft-defender-antivirus-for-non-persistent-vdi/ba-p/1489633 "https://techcommunity.microsoft.com/t5/microsoft-defender-for-endpoint/configuring-microsoft-defender-antivirus-for-non-persistent-vdi/ba-p/1489633")

## Scanning exclusions

If security software is installed in AppStream 2.0 instances,
the security software must not interfere with the following
processes.

_Table 6 — AppStream 2.0 processes security software must not interfere with the
following processes._

| **Service**               | **Processes**                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **AmazonCloudWatchAgent** | "C:\Program Files\Amazon\AmazonCloudWatchAgent\start-amazon- cloudwatch-agent.exe"                                                                                                                                                                                                                                                                               |
| **AmazonSSMAgent**        | "C:\Program Files\Amazon\SSM\amazon-ssm-agent.exe"                                                                                                                                                                                                                                                                                                               |
| **NICE DCV**              | "C:\Program Files\NICE\DCV\Server\bin\dcvserver.exe" "C:\Program Files\NICE\DCV\Server\bin\dcvagent.exe"                                                                                                                                                                                                                                                         |
| **AppStream 2.0**         | "C:\Program Files\Amazon\AppStream2\StorageConnector\StorageConnector.exe" In the folder "C:\Program Files\Amazon\Photon\" ".\Agent\PhotonAgent.exe" ".\Agent\s5cmd.exe" ".\WebServer\PhotonAgentWebServer.exe" ".\CustomShell\PhotonWindowsAppSwitcher.exe" ".\CustomShell\PhotonWindowsCustomShell.exe" ".\CustomShell\PhotonWindowsCustomShellBackground.exe" | ## Folders If security software is installed in AppStream 2.0 instances, the software must not interfere with the following folders: `C:\Program Files\Amazon\* C:\ProgramData\Amazon\* C:\Program Files (x86)\AWS Tools\* C:\Program Files (x86)\AWS SDK for .NET\* C:\Program Files\NICE\* C:\ProgramData\NICE\* C:\AppStream\*` ## Endpoint security console hygiene Amazon AppStream 2.0 will create new unique instances each time a user connects beyond the idle and disconnect timeouts. The instances will have a unique name and will build up in endpoint security management condoles. Setting unused aged machines over 4 or more days old (or lower depending on AppStream 2.0 session timeouts) to be deleted will minimize the number of expired instances in the console. |
