

# Manual agent installation
<a name="transform-vmware-ms-manual-install"></a>

For manual installation, you first generate AWS credentials (temporary or permanent) and then install the agent on each source server.

**Credential options:**
+ **Temporary credentials (recommended)** – Create an IAM role with the `AWSApplicationMigrationAgentInstallationPolicy` managed policy, then use `aws sts assume-role` to generate temporary credentials. For more information, see [Agent installation permissions](https://docs.aws.amazon.com/mgn/latest/ug/agent-installation-permissions.html) in the *MGN User Guide*.
+ **Permanent credentials** – Create an IAM user with the `AWSApplicationMigrationAgentInstallationPolicy` managed policy and generate an access key.

**Installation steps:**

For Linux servers, download and run the installer:

```
wget -O ./aws-replication-installer-init \
  https://aws-application-migration-service-{{region}}.s3.{{region}}.amazonaws.com/latest/linux/aws-replication-installer-init
sudo chmod +x aws-replication-installer-init
sudo ./aws-replication-installer-init --region {{region}} --user-provided-id {{server-identifier}}
```

For Windows servers, download and run the appropriate installer using PowerShell as Administrator:

```
Invoke-WebRequest -Uri "https://aws-application-migration-service-{{region}}.s3.{{region}}.amazonaws.com/latest/windows/AwsReplicationWindowsInstaller.exe" `
  -OutFile "C:\AwsReplicationWindowsInstaller.exe"
C:\AwsReplicationWindowsInstaller.exe --region {{region}} --user-provided-id {{server-identifier}}
```

**Important**  
The `--user-provided-id` parameter is required. Replace {{server-identifier}} with the exact value from the `mgn:server:user-provided-id` column in your inventory file. This identifier links the physical server to its MGN source server record.

For more information about agent installation, see [Linux agent](https://docs.aws.amazon.com/mgn/latest/ug/linux-agent.html) and [Windows agent](https://docs.aws.amazon.com/mgn/latest/ug/windows-agent.html) in the *MGN User Guide*.