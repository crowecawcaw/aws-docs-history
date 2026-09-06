

# Installing the AWS Replication Agent on Windows
<a name="windows-agent"></a>

To install the AWS Replication Agent on a Windows source server, you should ensure that your source meets all the requirements listed in the [supported Windows operating systems](Supported-Operating-Systems-Windows.md) documentation.

 Prior to installing the AWS Replication Agent, please ensure that you are aware of the following: 
+ You need to run the agent installer file as an Administrator on each Windows server.
+ We recommend using Windows PowerShell, which supports the 'Ctrl\+V' shortcut for pasting. Windows Command Prompt (cmd) does not support this functionality.

## Downloading the installer
<a name="download-replication-agent"></a>

Before installing the AWS Replication Agent, `AwsReplicationWindowsInstaller.exe`, it needs to be downloaded. Copy or distribute the downloaded agent installer to each Windows source server that you want to add to AWS Elastic Disaster Recovery.

The agent installer follows the following format:

 `https://aws-elastic-disaster-recovery-<REGION>.s3.<REGION>.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe`

**Note**  
Replace `<REGION>` with the AWS Region into which you are replicating.

The following is an example command for downloading the installer file from the us-east-1 region:

**Note**  
If you are using Windows Server 2016 or older, you may need to enable TLS 1.2 in PowerShell before downloading: `[System.Net.ServicePointManager]::SecurityProtocol = 'TLS12'` 

```
Invoke-WebRequest "https://aws-elastic-disaster-recovery-us-east-1.s3.us-east-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe" -OutFile .\AwsReplicationWindowsInstaller.exe
```

The command line indicates when the installer has been successfully downloaded.

**Note**  
AWS Regions that are not opt-in also support the shorter installer path: `https://aws-elastic-disaster-recovery-<REGION>.s3.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe` . Replace `<REGION>` with the AWS Region into which you are replicating.
Microsoft Windows Server versions 2008 and 2008 R2 use a version of the AWS Replication Agent that is only valid for those versions - `AwsReplicationWindowsLegacyInstaller.exe`. DO NOT use this installer file to install the agent on any other OS types. You can download it from `https://aws-elastic-disaster-recovery-<REGION>.s3.amazonaws.com/latest/windows_legacy/AwsReplicationWindowsLegacyInstaller.exe` . Replace `<REGION>` with the AWS Region into which you are replicating.
Microsoft Windows Server 2012 uses a version of the AWS Replication Agent that is only valid for that version AwsReplicationWindows2012LegacyInstaller.exe. DO NOT use this installer file to install the agent on any other OS types. You can download it from `https://aws-elastic-disaster-recovery-<REGION>.s3.amazonaws.com/latest/windows_legacy/windows_2012_legacy/AwsReplicationWindows2012LegacyInstaller.exe` . Replace `<REGION>` with the AWS Region into which you are replicating.  
If you need to validate the installer hash, the correct hash is here: `https://aws-elastic-disaster-recovery-hashes-<REGION>.s3.<REGION>.amazonaws.com/latest/windows_legacy/windows_2012_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512` (replace <REGION> with the AWS Region into which you are replicating.)

### AWS Replication Agent download URL for Windows for each supported AWS Region
<a name="installer-download-table"></a>



| Region name | Region identity | Download Link | 
| --- | --- | --- | 
| Africa (Cape Town) | af-south-1 | https://aws-elastic-disaster-recovery-af-south-1.s3.af-south-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| Asia Pacific (Hong Kong) | ap-east-1 | https://aws-elastic-disaster-recovery-ap-east-1.s3.ap-east-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| Asia Pacific (Taipei) | ap-east-2 | https://aws-elastic-disaster-recovery-ap-east-2-f1dcde1a.s3.ap-east-2.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| Asia Pacific (Tokyo) | ap-northeast-1 | https://aws-elastic-disaster-recovery-ap-northeast-1.s3.ap-northeast-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| Asia Pacific (Seoul) | ap-northeast-2 | https://aws-elastic-disaster-recovery-ap-northeast-2.s3.ap-northeast-2.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| Asia Pacific (Osaka) | ap-northeast-3 | https://aws-elastic-disaster-recovery-ap-northeast-3.s3.ap-northeast-3.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| Asia Pacific (Mumbai) | ap-south-1 | https://aws-elastic-disaster-recovery-ap-south-1.s3.ap-south-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| Asia Pacific (Hyderabad) | ap-south-2 | https://aws-elastic-disaster-recovery-ap-south-2.s3.ap-south-2.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| Asia Pacific (Singapore) | ap-southeast-1 | https://aws-elastic-disaster-recovery-ap-southeast-1.s3.ap-southeast-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| Asia Pacific (Sydney) | ap-southeast-2 | https://aws-elastic-disaster-recovery-ap-southeast-2.s3.ap-southeast-2.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| Asia Pacific (Jakarta) | ap-southeast-3 | https://aws-elastic-disaster-recovery-ap-southeast-3.s3.ap-southeast-3.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| Asia Pacific (Melbourne) | ap-southeast-4 | https://aws-elastic-disaster-recovery-ap-southeast-4.s3.ap-southeast-4.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| Asia Pacific (Malaysia) | ap-southeast-5 | https://aws-elastic-disaster-recovery-ap-southeast-5-ebaf53cb.s3.ap-southeast-5.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| Asia Pacific (New Zealand) | ap-southeast-6 | https://aws-elastic-disaster-recovery-ap-southeast-6-8a759f92.s3.ap-southeast-6.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| Asia Pacific (Thailand) | ap-southeast-7 | https://aws-elastic-disaster-recovery-ap-southeast-7-69ef66ac.s3.ap-southeast-7.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| Canada (Central) | ca-central-1 | https://aws-elastic-disaster-recovery-ca-central-1.s3.ca-central-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| Canada West (Calgary) | ca-west-1 | https://aws-elastic-disaster-recovery-ca-west-1-2590fa22.s3.ca-west-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| Europe (Frankfurt) | eu-central-1 | https://aws-elastic-disaster-recovery-eu-central-1.s3.eu-central-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| Europe (Zurich) | eu-central-2 | https://aws-elastic-disaster-recovery-eu-central-2.s3.eu-central-2.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| Europe (Stockholm) | eu-north-1 | https://aws-elastic-disaster-recovery-eu-north-1.s3.eu-north-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| Europe (Milan) | eu-south-1 | https://aws-elastic-disaster-recovery-eu-south-1.s3.eu-south-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| Europe (Spain) | eu-south-2 | https://aws-elastic-disaster-recovery-eu-south-2.s3.eu-south-2.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| Europe (Ireland) | eu-west-1 | https://aws-elastic-disaster-recovery-eu-west-1.s3.eu-west-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| Europe (London) | eu-west-2 | https://aws-elastic-disaster-recovery-eu-west-2.s3.eu-west-2.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| Europe (Paris) | eu-west-3 | https://aws-elastic-disaster-recovery-eu-west-3.s3.eu-west-3.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| Israel (Tel Aviv) | il-central-1 | https://aws-elastic-disaster-recovery-il-central-1.s3.il-central-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| Middle East (UAE) | me-central-1 | https://aws-elastic-disaster-recovery-me-central-1.s3.me-central-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| Middle East (Bahrain) | me-south-1 | https://aws-elastic-disaster-recovery-me-south-1.s3.me-south-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| Mexico (Central) | mx-central-1 | https://aws-elastic-disaster-recovery-mx-central-1-1f310737.s3.mx-central-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| South America (São Paulo) | sa-east-1 | https://aws-elastic-disaster-recovery-sa-east-1.s3.sa-east-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| US East (N. Virginia) | us-east-1 | https://aws-elastic-disaster-recovery-us-east-1.s3.us-east-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| US East (Ohio) | us-east-2 | https://aws-elastic-disaster-recovery-us-east-2.s3.us-east-2.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| US West (N. California) | us-west-1 | https://aws-elastic-disaster-recovery-us-west-1.s3.us-west-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 
| US West (Oregon) | us-west-2 | https://aws-elastic-disaster-recovery-us-west-2.s3.us-west-2.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe | 

### Validating the downloaded AWS Replication Agent installer for Windows.
<a name="installer-hash-table"></a>

**Important**  
If you need to validate the installer hash, the correct hash is here:  
 `https://aws-elastic-disaster-recovery-hashes-<REGION>.s3.<REGION>.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512`   
 Replace `<REGION>` with the AWS Region into which you are replicating, for example: us-east-1:  
`https://aws-elastic-disaster-recovery-hashes-us-east-1.s3.us-east-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 `



| Region name | Region identity | SHA512 Hash Download Link | 
| --- | --- | --- | 
| Africa (Cape Town) | af-south-1 | https://aws-elastic-disaster-recovery-hashes-af-south-1.s3.af-south-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 
| Asia Pacific (Hong Kong) | ap-east-1 | https://aws-elastic-disaster-recovery-hashes-ap-east-1.s3.ap-east-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 
| Asia Pacific (Taipei) | ap-east-2 | https://aws-elastic-disaster-recovery-hashes-ap-east-2-f1dcde1a.s3.ap-east-2.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 
| Asia Pacific (Tokyo) | ap-northeast-1 | https://aws-elastic-disaster-recovery-hashes-ap-northeast-1.s3.ap-northeast-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 
| Asia Pacific (Seoul) | ap-northeast-2 | https://aws-elastic-disaster-recovery-hashes-ap-northeast-2.s3.ap-northeast-2.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 
| Asia Pacific (Osaka) | ap-northeast-3 | https://aws-elastic-disaster-recovery-hashes-ap-northeast-3.s3.ap-northeast-3.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 
| Asia Pacific (Mumbai) | ap-south-1 | https://aws-elastic-disaster-recovery-hashes-ap-south-1.s3.ap-south-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 
| Asia Pacific (Hyderabad) | ap-south-2 | https://aws-elastic-disaster-recovery-hashes-ap-south-2.s3.ap-south-2.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 
| Asia Pacific (Singapore) | ap-southeast-1 | https://aws-elastic-disaster-recovery-hashes-ap-southeast-1.s3.ap-southeast-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 
| Asia Pacific (Sydney) | ap-southeast-2 | https://aws-elastic-disaster-recovery-hashes-ap-southeast-2.s3.ap-southeast-2.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 
| Asia Pacific (Jakarta) | ap-southeast-3 | https://aws-elastic-disaster-recovery-hashes-ap-southeast-3.s3.ap-southeast-3.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 
| Asia Pacific (Melbourne) | ap-southeast-4 | https://aws-elastic-disaster-recovery-hashes-ap-southeast-4.s3.ap-southeast-4.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 
| Asia Pacific (Malaysia) | ap-southeast-5 | https://aws-elastic-disaster-recovery-hashes-ap-southeast-5-ebaf53cb.s3.ap-southeast-5.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 
| Asia Pacific (New Zealand) | ap-southeast-6 | https://aws-elastic-disaster-recovery-hashes-ap-southeast-6-8a759f92.s3.ap-southeast-6.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 
| Asia Pacific (Thailand) | ap-southeast-7 | https://aws-elastic-disaster-recovery-hashes-ap-southeast-7-69ef66ac.s3.ap-southeast-7.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 
| Canada (Central) | ca-central-1 | https://aws-elastic-disaster-recovery-hashes-ca-central-1.s3.ca-central-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 
| Canada West (Calgary) | ca-west-1 | https://aws-elastic-disaster-recovery-hashes-ca-west-1-2590fa22.s3.ca-west-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 
| Europe (Frankfurt) | eu-central-1 | https://aws-elastic-disaster-recovery-hashes-eu-central-1.s3.eu-central-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 
| Europe (Zurich) | eu-central-2 | https://aws-elastic-disaster-recovery-hashes-eu-central-2.s3.eu-central-2.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 
| Europe (Stockholm) | eu-north-1 | https://aws-elastic-disaster-recovery-hashes-eu-north-1.s3.eu-north-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 
| Europe (Milan) | eu-south-1 | https://aws-elastic-disaster-recovery-hashes-eu-south-1.s3.eu-south-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 
| Europe (Spain) | eu-south-2 | https://aws-elastic-disaster-recovery-hashes-eu-south-2.s3.eu-south-2.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 
| Europe (Ireland) | eu-west-1 | https://aws-elastic-disaster-recovery-hashes-eu-west-1.s3.eu-west-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 
| Europe (London) | eu-west-2 | https://aws-elastic-disaster-recovery-hashes-eu-west-2.s3.eu-west-2.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 
| Europe (Paris) | eu-west-3 | https://aws-elastic-disaster-recovery-hashes-eu-west-3.s3.eu-west-3.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 
| Middle East (UAE) | me-central-1 | https://aws-elastic-disaster-recovery-hashes-me-central-1.s3.me-central-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 
| Middle East (Bahrain) | me-south-1 | https://aws-elastic-disaster-recovery-hashes-me-south-1.s3.me-south-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 
| Mexico (Central) | mx-central-1 | https://aws-elastic-disaster-recovery-hashes-mx-central-1-1f310737.s3.mx-central-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 
| South America (São Paulo) | sa-east-1 | https://aws-elastic-disaster-recovery-hashes-sa-east-1.s3.sa-east-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 
| US East (N. Virginia) | us-east-1 | https://aws-elastic-disaster-recovery-hashes-us-east-1.s3.us-east-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 
| US East (Ohio) | us-east-2 | https://aws-elastic-disaster-recovery-hashes-us-east-2.s3.us-east-2.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 
| US West (N. California) | us-west-1 | https://aws-elastic-disaster-recovery-hashes-us-west-1.s3.us-west-1.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 
| US West (Oregon) | us-west-2 | https://aws-elastic-disaster-recovery-hashes-us-west-2.s3.us-west-2.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe.sha512 | 

### AWS Replication Agent download URL for Windows versions 2008 and 2008 R2 for each supported AWS Region
<a name="installer-download-table-eol"></a>


| Region name | Region identity | Download Link | 
| --- | --- | --- | 
| Africa (Cape Town) | af-south-1 | https://aws-elastic-disaster-recovery-af-south-1.s3.af-south-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 
| Asia Pacific (Hong Kong) | ap-east-1 | https://aws-elastic-disaster-recovery-ap-east-1.s3.ap-east-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 
| Asia Pacific (Taipei) | ap-east-2 | https://aws-elastic-disaster-recovery-ap-east-2-f1dcde1a.s3.ap-east-2.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 
| Asia Pacific (Tokyo) | ap-northeast-1 | https://aws-elastic-disaster-recovery-ap-northeast-1.s3.ap-northeast-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 
| Asia Pacific (Seoul) | ap-northeast-2 | https://aws-elastic-disaster-recovery-ap-northeast-2.s3.ap-northeast-2.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 
| Asia Pacific (Osaka) | ap-northeast-3 | https://aws-elastic-disaster-recovery-ap-northeast-3.s3.ap-northeast-3.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 
| Asia Pacific (Mumbai) | ap-south-1 | https://aws-elastic-disaster-recovery-ap-south-1.s3.ap-south-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 
| Asia Pacific (Hyderabad) | ap-south-2 | https://aws-elastic-disaster-recovery-ap-south-2.s3.ap-south-2.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 
| Asia Pacific (Singapore) | ap-southeast-1 | https://aws-elastic-disaster-recovery-ap-southeast-1.s3.ap-southeast-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 
| Asia Pacific (Sydney) | ap-southeast-2 | https://aws-elastic-disaster-recovery-ap-southeast-2.s3.ap-southeast-2.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 
| Asia Pacific (Jakarta) | ap-southeast-3 | https://aws-elastic-disaster-recovery-ap-southeast-3.s3.ap-southeast-3.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 
| Asia Pacific (Melbourne) | ap-southeast-4 | https://aws-elastic-disaster-recovery-ap-southeast-4.s3.ap-southeast-4.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 
| Asia Pacific (Malaysia) | ap-southeast-5 | https://aws-elastic-disaster-recovery-ap-southeast-5-ebaf53cb.s3.ap-southeast-5.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 
| Asia Pacific (New Zealand) | ap-southeast-6 | https://aws-elastic-disaster-recovery-ap-southeast-6-8a759f92.s3.ap-southeast-6.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 
| Asia Pacific (Thailand) | ap-southeast-7 | https://aws-elastic-disaster-recovery-ap-southeast-7-69ef66ac.s3.ap-southeast-7.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 
| Canada (Central) | ca-central-1 | https://aws-elastic-disaster-recovery-ca-central-1.s3.ca-central-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 
| Canada West (Calgary) | ca-west-1 | https://aws-elastic-disaster-recovery-ca-west-1-2590fa22.s3.ca-west-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 
| Europe (Frankfurt) | eu-central-1 | https://aws-elastic-disaster-recovery-eu-central-1.s3.eu-central-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 
| Europe (Zurich) | eu-central-2 | https://aws-elastic-disaster-recovery-eu-central-2.s3.eu-central-2.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 
| Europe (Stockholm) | eu-north-1 | https://aws-elastic-disaster-recovery-eu-north-1.s3.eu-north-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 
| Europe (Milan) | eu-south-1 | https://aws-elastic-disaster-recovery-eu-south-1.s3.eu-south-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 
| Europe (Spain) | eu-south-2 | https://aws-elastic-disaster-recovery-eu-south-2.s3.eu-south-2.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 
| Europe (Ireland) | eu-west-1 | https://aws-elastic-disaster-recovery-eu-west-1.s3.eu-west-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 
| Europe (London) | eu-west-2 | https://aws-elastic-disaster-recovery-eu-west-2.s3.eu-west-2.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 
| Europe (Paris) | eu-west-3 | https://aws-elastic-disaster-recovery-eu-west-3.s3.eu-west-3.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 
| Middle East (UAE) | me-central-1 | https://aws-elastic-disaster-recovery-me-central-1.s3.me-central-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 
| Middle East (Bahrain) | me-south-1 | https://aws-elastic-disaster-recovery-me-south-1.s3.me-south-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 
| Mexico (Central) | mx-central-1 | https://aws-elastic-disaster-recovery-mx-central-1-1f310737.s3.mx-central-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 
| South America (São Paulo) | sa-east-1 | https://aws-elastic-disaster-recovery-sa-east-1.s3.sa-east-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 
| US East (N. Virginia) | us-east-1 | https://aws-elastic-disaster-recovery-us-east-1.s3.us-east-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 
| US East (Ohio) | us-east-2 | https://aws-elastic-disaster-recovery-us-east-2.s3.us-east-2.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 
| US West (N. California) | us-west-1 | https://aws-elastic-disaster-recovery-us-west-1.s3.us-west-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 
| US West (Oregon) | us-west-2 | https://aws-elastic-disaster-recovery-us-west-2.s3.us-west-2.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe | 

### Validating the downloaded AWS Replication Agent installer for Windows versions 2008 and 2008 R2.
<a name="installer-hash-table-eol"></a>

**Important**  
If you need to validate the installer hash, the correct hash is here:  
 `https://aws-elastic-disaster-recovery-hashes-<REGION>.s3.<REGION>.amazonaws.com/latest/windows_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512`   
 Replace `<REGION>` with the AWS Region into which you are replicating, for example: us-east-1:  
`https://aws-elastic-disaster-recovery-hashes-us-east-1.s3.us-east-1.amazonaws.com/latest/windows_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 `


| Region name | Region identity | SHA512 Hash Download Link | 
| --- | --- | --- | 
| Africa (Cape Town) | af-south-1 | https://aws-elastic-disaster-recovery-hashes-af-south-1.s3.af-south-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 
| Asia Pacific (Hong Kong) | ap-east-1 | https://aws-elastic-disaster-recovery-hashes-ap-east-1.s3.ap-east-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 
| Asia Pacific (Taipei) | ap-east-2 | https://aws-elastic-disaster-recovery-hashes-ap-east-2-f1dcde1a.s3.ap-east-2.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 
| Asia Pacific (Tokyo) | ap-northeast-1 | https://aws-elastic-disaster-recovery-hashes-ap-northeast-1.s3.ap-northeast-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 
| Asia Pacific (Seoul) | ap-northeast-2 | https://aws-elastic-disaster-recovery-hashes-ap-northeast-2.s3.ap-northeast-2.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 
| Asia Pacific (Osaka) | ap-northeast-3 | https://aws-elastic-disaster-recovery-hashes-ap-northeast-3.s3.ap-northeast-3.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 
| Asia Pacific (Mumbai) | ap-south-1 | https://aws-elastic-disaster-recovery-hashes-ap-south-1.s3.ap-south-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 
| Asia Pacific (Hyderabad) | ap-south-2 | https://aws-elastic-disaster-recovery-hashes-ap-south-2.s3.ap-south-2.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 
| Asia Pacific (Singapore) | ap-southeast-1 | https://aws-elastic-disaster-recovery-hashes-ap-southeast-1.s3.ap-southeast-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 
| Asia Pacific (Sydney) | ap-southeast-2 | https://aws-elastic-disaster-recovery-hashes-ap-southeast-2.s3.ap-southeast-2.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 
| Asia Pacific (Jakarta) | ap-southeast-3 | https://aws-elastic-disaster-recovery-hashes-ap-southeast-3.s3.ap-southeast-3.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 
| Asia Pacific (Melbourne) | ap-southeast-4 | https://aws-elastic-disaster-recovery-hashes-ap-southeast-4.s3.ap-southeast-4.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 
| Asia Pacific (Malaysia) | ap-southeast-5 | https://aws-elastic-disaster-recovery-hashes-ap-southeast-5-ebaf53cb.s3.ap-southeast-5.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 
| Asia Pacific (New Zealand) | ap-southeast-6 | https://aws-elastic-disaster-recovery-hashes-ap-southeast-6-8a759f92.s3.ap-southeast-6.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 
| Asia Pacific (Thailand) | ap-southeast-7 | https://aws-elastic-disaster-recovery-hashes-ap-southeast-7-69ef66ac.s3.ap-southeast-7.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 
| Canada (Central) | ca-central-1 | https://aws-elastic-disaster-recovery-hashes-ca-central-1.s3.ca-central-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 
| Canada West (Calgary) | ca-west-1 | https://aws-elastic-disaster-recovery-hashes-ca-west-1-2590fa22.s3.ca-west-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 
| Europe (Frankfurt) | eu-central-1 | https://aws-elastic-disaster-recovery-hashes-eu-central-1.s3.eu-central-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 
| Europe (Zurich) | eu-central-2 | https://aws-elastic-disaster-recovery-hashes-eu-central-2.s3.eu-central-2.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 
| Europe (Stockholm) | eu-north-1 | https://aws-elastic-disaster-recovery-hashes-eu-north-1.s3.eu-north-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 
| Europe (Milan) | eu-south-1 | https://aws-elastic-disaster-recovery-hashes-eu-south-1.s3.eu-south-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 
| Europe (Spain) | eu-south-2 | https://aws-elastic-disaster-recovery-hashes-eu-south-2.s3.eu-south-2.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 
| Europe (Ireland) | eu-west-1 | https://aws-elastic-disaster-recovery-hashes-eu-west-1.s3.eu-west-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 
| Europe (London) | eu-west-2 | https://aws-elastic-disaster-recovery-hashes-eu-west-2.s3.eu-west-2.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 
| Europe (Paris) | eu-west-3 | https://aws-elastic-disaster-recovery-hashes-eu-west-3.s3.eu-west-3.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 
| Middle East (UAE) | me-central-1 | https://aws-elastic-disaster-recovery-hashes-me-central-1.s3.me-central-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 
| Middle East (Bahrain) | me-south-1 | https://aws-elastic-disaster-recovery-hashes-me-south-1.s3.me-south-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 
| Mexico (Central) | mx-central-1 | https://aws-elastic-disaster-recovery-hashes-mx-central-1-1f310737.s3.mx-central-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 
| South America (São Paulo) | sa-east-1 | https://aws-elastic-disaster-recovery-hashes-sa-east-1.s3.sa-east-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 
| US East (N. Virginia) | us-east-1 | https://aws-elastic-disaster-recovery-hashes-us-east-1.s3.us-east-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 
| US East (Ohio) | us-east-2 | https://aws-elastic-disaster-recovery-hashes-us-east-2.s3.us-east-2.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 
| US West (N. California) | us-west-1 | https://aws-elastic-disaster-recovery-hashes-us-west-1.s3.us-west-1.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 
| US West (Oregon) | us-west-2 | https://aws-elastic-disaster-recovery-hashes-us-west-2.s3.us-west-2.amazonaws.com/latest/windows\_legacy/AwsReplicationWindowsLegacyInstaller.exe.sha512 | 

### AWS Replication Agent download URL for Windows 2012 for each supported AWS Region
<a name="installer-download-table-2012"></a>


| Region name | Region identity | Download Link | 
| --- | --- | --- | 
| Africa (Cape Town) | af-south-1 | https://aws-elastic-disaster-recovery-af-south-1.s3.af-south-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 
| Asia Pacific (Hong Kong) | ap-east-1 | https://aws-elastic-disaster-recovery-ap-east-1.s3.ap-east-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 
| Asia Pacific (Taipei) | ap-east-2 | https://aws-elastic-disaster-recovery-ap-east-2-f1dcde1a.s3.ap-east-2.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 
| Asia Pacific (Tokyo) | ap-northeast-1 | https://aws-elastic-disaster-recovery-ap-northeast-1.s3.ap-northeast-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 
| Asia Pacific (Seoul) | ap-northeast-2 | https://aws-elastic-disaster-recovery-ap-northeast-2.s3.ap-northeast-2.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 
| Asia Pacific (Osaka) | ap-northeast-3 | https://aws-elastic-disaster-recovery-ap-northeast-3.s3.ap-northeast-3.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 
| Asia Pacific (Mumbai) | ap-south-1 | https://aws-elastic-disaster-recovery-ap-south-1.s3.ap-south-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 
| Asia Pacific (Hyderabad) | ap-south-2 | https://aws-elastic-disaster-recovery-ap-south-2.s3.ap-south-2.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 
| Asia Pacific (Singapore) | ap-southeast-1 | https://aws-elastic-disaster-recovery-ap-southeast-1.s3.ap-southeast-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 
| Asia Pacific (Sydney) | ap-southeast-2 | https://aws-elastic-disaster-recovery-ap-southeast-2.s3.ap-southeast-2.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 
| Asia Pacific (Jakarta) | ap-southeast-3 | https://aws-elastic-disaster-recovery-ap-southeast-3.s3.ap-southeast-3.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 
| Asia Pacific (Melbourne) | ap-southeast-4 | https://aws-elastic-disaster-recovery-ap-southeast-4.s3.ap-southeast-4.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 
| Asia Pacific (Malaysia) | ap-southeast-5 | https://aws-elastic-disaster-recovery-ap-southeast-5-ebaf53cb.s3.ap-southeast-5.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 
| Asia Pacific (New Zealand) | ap-southeast-6 | https://aws-elastic-disaster-recovery-ap-southeast-6-8a759f92.s3.ap-southeast-6.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 
| Asia Pacific (Thailand) | ap-southeast-7 | https://aws-elastic-disaster-recovery-ap-southeast-7-69ef66ac.s3.ap-southeast-7.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 
| Canada (Central) | ca-central-1 | https://aws-elastic-disaster-recovery-ca-central-1.s3.ca-central-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 
| Canada West (Calgary) | ca-west-1 | https://aws-elastic-disaster-recovery-ca-west-1-2590fa22.s3.ca-west-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 
| Europe (Frankfurt) | eu-central-1 | https://aws-elastic-disaster-recovery-eu-central-1.s3.eu-central-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 
| Europe (Zurich) | eu-central-2 | https://aws-elastic-disaster-recovery-eu-central-2.s3.eu-central-2.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 
| Europe (Stockholm) | eu-north-1 | https://aws-elastic-disaster-recovery-eu-north-1.s3.eu-north-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 
| Europe (Milan) | eu-south-1 | https://aws-elastic-disaster-recovery-eu-south-1.s3.eu-south-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 
| Europe (Spain) | eu-south-2 | https://aws-elastic-disaster-recovery-eu-south-2.s3.eu-south-2.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 
| Europe (Ireland) | eu-west-1 | https://aws-elastic-disaster-recovery-eu-west-1.s3.eu-west-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 
| Europe (London) | eu-west-2 | https://aws-elastic-disaster-recovery-eu-west-2.s3.eu-west-2.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 
| Europe (Paris) | eu-west-3 | https://aws-elastic-disaster-recovery-eu-west-3.s3.eu-west-3.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 
| Middle East (UAE) | me-central-1 | https://aws-elastic-disaster-recovery-me-central-1.s3.me-central-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 
| Middle East (Bahrain) | me-south-1 | https://aws-elastic-disaster-recovery-me-south-1.s3.me-south-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 
| Mexico (Central) | mx-central-1 | https://aws-elastic-disaster-recovery-mx-central-1-1f310737.s3.mx-central-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 
| South America (São Paulo) | sa-east-1 | https://aws-elastic-disaster-recovery-sa-east-1.s3.sa-east-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 
| US East (N. Virginia) | us-east-1 | https://aws-elastic-disaster-recovery-us-east-1.s3.us-east-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 
| US East (Ohio) | us-east-2 | https://aws-elastic-disaster-recovery-us-east-2.s3.us-east-2.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 
| US West (N. California) | us-west-1 | https://aws-elastic-disaster-recovery-us-west-1.s3.us-west-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 
| US West (Oregon) | us-west-2 | https://aws-elastic-disaster-recovery-us-west-2.s3.us-west-2.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe | 

### Validating the downloaded AWS Replication Agent installer for Windows 2012.
<a name="installer-hash-table-2012"></a>

**Important**  
If you need to validate the installer hash, the correct hash is here:  
 `https://aws-elastic-disaster-recovery-hashes-<REGION>.s3.<REGION>.amazonaws.com/latest/windows_legacy/windows_2012_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512`   
 Replace `<REGION>` with the AWS Region into which you are replicating, for example: us-east-1:  
`https://aws-elastic-disaster-recovery-hashes-us-east-1.s3.us-east-1.amazonaws.com/latest/windows_legacy/windows_2012_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 `


| Region name | Region identity | SHA512 Hash Download Link | 
| --- | --- | --- | 
| Africa (Cape Town) | af-south-1 | https://aws-elastic-disaster-recovery-hashes-af-south-1.s3.af-south-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 
| Asia Pacific (Hong Kong) | ap-east-1 | https://aws-elastic-disaster-recovery-hashes-ap-east-1.s3.ap-east-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 
| Asia Pacific (Taipei) | ap-east-2 | https://aws-elastic-disaster-recovery-hashes-ap-east-2-f1dcde1a.s3.ap-east-2.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 
| Asia Pacific (Tokyo) | ap-northeast-1 | https://aws-elastic-disaster-recovery-hashes-ap-northeast-1.s3.ap-northeast-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 
| Asia Pacific (Seoul) | ap-northeast-2 | https://aws-elastic-disaster-recovery-hashes-ap-northeast-2.s3.ap-northeast-2.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 
| Asia Pacific (Osaka) | ap-northeast-3 | https://aws-elastic-disaster-recovery-hashes-ap-northeast-3.s3.ap-northeast-3.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 
| Asia Pacific (Mumbai) | ap-south-1 | https://aws-elastic-disaster-recovery-hashes-ap-south-1.s3.ap-south-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 
| Asia Pacific (Hyderabad) | ap-south-2 | https://aws-elastic-disaster-recovery-hashes-ap-south-2.s3.ap-south-2.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 
| Asia Pacific (Singapore) | ap-southeast-1 | https://aws-elastic-disaster-recovery-hashes-ap-southeast-1.s3.ap-southeast-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 
| Asia Pacific (Sydney) | ap-southeast-2 | https://aws-elastic-disaster-recovery-hashes-ap-southeast-2.s3.ap-southeast-2.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 
| Asia Pacific (Jakarta) | ap-southeast-3 | https://aws-elastic-disaster-recovery-hashes-ap-southeast-3.s3.ap-southeast-3.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 
| Asia Pacific (Melbourne) | ap-southeast-4 | https://aws-elastic-disaster-recovery-hashes-ap-southeast-4.s3.ap-southeast-4.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 
| Asia Pacific (Malaysia) | ap-southeast-5 | https://aws-elastic-disaster-recovery-hashes-ap-southeast-5-ebaf53cb.s3.ap-southeast-5.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 
| Asia Pacific (New Zealand) | ap-southeast-6 | https://aws-elastic-disaster-recovery-hashes-ap-southeast-6-8a759f92.s3.ap-southeast-6.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 
| Asia Pacific (Thailand) | ap-southeast-7 | https://aws-elastic-disaster-recovery-hashes-ap-southeast-7-69ef66ac.s3.ap-southeast-7.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 
| Canada (Central) | ca-central-1 | https://aws-elastic-disaster-recovery-hashes-ca-central-1.s3.ca-central-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 
| Canada West (Calgary) | ca-west-1 | https://aws-elastic-disaster-recovery-hashes-ca-west-1-2590fa22.s3.ca-west-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 
| Europe (Frankfurt) | eu-central-1 | https://aws-elastic-disaster-recovery-hashes-eu-central-1.s3.eu-central-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 
| Europe (Zurich) | eu-central-2 | https://aws-elastic-disaster-recovery-hashes-eu-central-2.s3.eu-central-2.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 
| Europe (Stockholm) | eu-north-1 | https://aws-elastic-disaster-recovery-hashes-eu-north-1.s3.eu-north-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 
| Europe (Milan) | eu-south-1 | https://aws-elastic-disaster-recovery-hashes-eu-south-1.s3.eu-south-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 
| Europe (Spain) | eu-south-2 | https://aws-elastic-disaster-recovery-hashes-eu-south-2.s3.eu-south-2.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 
| Europe (Ireland) | eu-west-1 | https://aws-elastic-disaster-recovery-hashes-eu-west-1.s3.eu-west-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 
| Europe (London) | eu-west-2 | https://aws-elastic-disaster-recovery-hashes-eu-west-2.s3.eu-west-2.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 
| Europe (Paris) | eu-west-3 | https://aws-elastic-disaster-recovery-hashes-eu-west-3.s3.eu-west-3.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 
| Middle East (UAE) | me-central-1 | https://aws-elastic-disaster-recovery-hashes-me-central-1.s3.me-central-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 
| Middle East (Bahrain) | me-south-1 | https://aws-elastic-disaster-recovery-hashes-me-south-1.s3.me-south-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 
| Mexico (Central) | mx-central-1 | https://aws-elastic-disaster-recovery-hashes-mx-central-1-1f310737.s3.mx-central-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 
| South America (São Paulo) | sa-east-1 | https://aws-elastic-disaster-recovery-hashes-sa-east-1.s3.sa-east-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 
| US East (N. Virginia) | us-east-1 | https://aws-elastic-disaster-recovery-hashes-us-east-1.s3.us-east-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 
| US East (Ohio) | us-east-2 | https://aws-elastic-disaster-recovery-hashes-us-east-2.s3.us-east-2.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 
| US West (N. California) | us-west-1 | https://aws-elastic-disaster-recovery-hashes-us-west-1.s3.us-west-1.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 
| US West (Oregon) | us-west-2 | https://aws-elastic-disaster-recovery-hashes-us-west-2.s3.us-west-2.amazonaws.com/latest/windows\_legacy/windows\_2012\_legacy/AwsReplicationWindows2012LegacyInstaller.exe.sha512 | 

## Installing the agent
<a name="install-replication-agent"></a>

1.  Run the agent installer file `AwsReplicationWindowsInstaller.exe` as an Administrator. 

   ```
   .\AwsReplicationWindowsInstaller.exe
   ```

   The installer confirms that the installation of the AWS Replication Agent has started. 

   ```
   The installation of the AWS Replication Agent has started.
   ```
**Note**  
To install the agent on a secured network, [learn about the additional required configurations](installing-agent-blocked.md).

1. The installer prompts you to enter your **AWS Region Name**, the **AWS Access Key ID** and the **AWS Secret Access Key** that you previously generated. Enter the complete AWS Region name (for example: eu-central-1), and the full AWS Access Key ID and AWS Secret Access Key. If you are using temporary credentials, you also need to specify the session token.

   ```
   The installation of the AWS Replication Agent has started.
   AWS Region name: us-east-1
   AWS Access Key ID: AKIAI0SF0DNN71EXAMPLE
   AWS Secret Access Key: wJalrXUtnFEMI/K71MDENG/bPxRfiCYEXAMPLEKEY
   ```
**Note**  
You can also enter these values as part of the installation script command parameters. If you do not enter these parameters as part of the installation script, you are prompted to enter them one by one as described above. (for example: `.\AwsReplicationWindowsInstaller.exe --region regionname --aws-access-key-id AKIAIOSFODNN7EXAMPLE --aws-secret-access-key wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`)
**Note**  
You can also pass credentials through environment variables. We recommend using temporary credentials from AWS STS. Set `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN` in your PowerShell session. Then run the installer with `--no-prompt`:  

   ```
   $env:AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
   $env:AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
   $env:AWS_SESSION_TOKEN = "AQoDYXdzEJr//////////wEa8AMDSomethingEXAMPLE"
   .\AwsReplicationWindowsInstaller.exe --region us-east-1 --no-prompt
   ```

    If you require additional customization, you can add a variety of parameters to the installation script in order to manipulate the way the Agent is installed on your server. See the [Installer Parameters](installer-parameters.md) for more information. 

1. Once you have entered your credentials, the installer verifies that the source server has enough free disk space for Agent installation and identify volumes for replication. The installer displays the identified disks and prompts you to choose the disks you want to replicate. 

   ```
   ...
   AWS Secret Access Key: wJalrXUtnFEMI/K71MDENG/bPxRfiCYEXAMPLEKEY
   Verifying that the source server has enough free disk space to install the AWS Replication Agent.
   (a minimum of 2GB of free disk space is required)
   Identifying volumes for replication.
   Choose the disks you want to replicate. Your disks are: c:
   To replicate some of the disks, type the path of the disks, separated with a comma (for example, C:,D:).
   To replicate all disks, press Enter:
   ```

   To replicate some of the disks, type the path of the disks, separated by a comma, as illustrated in the installer (for example: C:, D:, etc). To replicate all of the disks, press **Enter**. The installer identifies the selected disks and prints their size.

   ```
   ...
   Identifying volumes for replication.
   Choose the disks you want to replicate. Your disks are: c:
   To replicate some of the disks, type the path of the disks, separated with a comma (for example, C:,D:).
   To replicate all disks, press Enter:
   Disk to replicate identified: c:0 of size 30GiB
   ```

   The installer confirms that all of the disks were successfully identified. 

   ```
   ...
   Identifying volumes for replication.
   Choose the disks you want to replicate. Your disks are: c:
   To replicate some of the disks, type the path of the disks, separated with a comma (for example, C:,D:).
   To replicate all disks, press Enter:
   Disk to replicate identified: c:0 of size 30GiB
   All volumes for replication were successfully identified
   ```
**Note**  
When identifying specific disks for replication, do not use apostrophes, brackets, or disk paths that do not exist. Type only existing disk paths. Each disk that you selected for replication is displayed with the caption **Disk to replicate identified**. However, the displayed list of identified disks for replication may differ from the data you entered. This difference can be due to several reasons:  
The root disk of the source server is always replicated, whether you select it or not. Therefore, it always appears on the list of identified disks for replication.
AWS Elastic Disaster Recovery replicates whole disks. Therefore, if you choose to replicate a partition, its entire disk appears on the list and is later replicated. If several partitions on the same disk are selected, then the disk encompassing all of them appears only once on the list.
Incorrect disks may be chosen by accident. Ensure that the correct disks have been chosen.
**Important**  
If disks are disconnected from a server, AWS Elastic Disaster Recovery can no longer replicate them, so they are removed from the list of replicated disks. When they are reconnected, the AWS Replication Agent cannot know that these were the same disks that were disconnected and therefore does not add them automatically. To add the disks after they are reconnected, rerun the AWS Replication Agent installer on the server.   
Note that the returned disks need to be replicated from the beginning. Any disk size changes are automatically identified, but also cause a resync. Perform a test after installing the Agent to ensure that the correct disks have been added.

1. After all of the disks to be replicated have been successfully identified, the installer downloads and installs the AWS Replication Agent on the source server.

   ```
   ...
   All volumes for replication were successfully identified
   Downloading the AWS Replication Agent onto the source server... Finished
   Installing the AWS Replication Agent onto the source server... Finished
   ```

1. Once the AWS Replication Agent is installed, the server is added to the AWS Elastic Disaster Recovery console and undergoes the initial sync process. The installer provides the source server's ID. 

   ```
   ...
   All volumes for replication were successfully identified
   Downloading the AWS Replication Agent onto the source server... Finished
   Installing the AWS Replication Agent onto the source server... Finished
   Syncing the source server with the Elastic Disaster Recovery Console... Finished
   The following is the source server ID: s-3146f90b19example
   The AWS Replication Agent was successfully installed.
   Press Enter to close...
   ```

   You can review this process in real time on the **Source servers** page.