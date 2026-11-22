

# AWS Transform MGN connector setup

The AWS Transform MGN connector automates the deployment of replication agents across your source servers, eliminating the need to log into each server individually. The connector is a lightweight client deployed on a dedicated Linux machine in your on-premises environment. It connects to source servers over SSH (Linux) or WinRM (Windows) to install and configure replication agents, eliminating the need to manually coordinate across multiple AWS services.

## How the connector works
<a name="transform-vmware-ms-connector-how-it-works"></a>

The connector operates through the following components:
+ **Connector client** – Deployed on a dedicated Linux machine in your environment.
+ **SSM Agent** – Installed on the same machine to enable secure communication with AWS.
+ **SSM Hybrid Activation** – Links the connector machine to AWS Systems Manager for secure command execution.
+ **Credentials management** – Retrieves source server credentials from AWS Secrets Manager.

When you deploy agents, AWS Transform sends an SSM document to the connector machine. The connector then does the following:

1. Retrieves source server credentials from AWS Secrets Manager.

1. Establishes a connection to each source server.

1. Validates that the source server meets prerequisites.

1. Installs and configures the replication agent.

1. Verifies successful installation.

## Connector machine requirements
<a name="transform-vmware-ms-connector-requirements"></a>


| Requirement | Details | 
| --- | --- | 
| Operating system | Supported Linux operating system. For the full list, see [MGN connector prerequisites](https://docs.aws.amazon.com/mgn/latest/ug/mgn-connector-prerequisites.html) in the MGN User Guide. | 
| Network access | Must reach all source servers (Linux over SSH, Windows over WinRM) | 
| Internet connectivity | Outbound HTTPS (443) to AWS endpoints (Systems Manager, Secrets Manager, MGN) | 
| Disk space | Minimum 200 MB free | 
| Permissions | Root or sudo access | 

**Note**  
The connector must be installed on a Linux machine, but it can deploy agents to both Linux and Windows source servers.

## Setup process
<a name="transform-vmware-ms-connector-setup-process"></a>

AWS Transform guides you through the following steps to set up the connector:

**Step 1: Connector configuration**

Provide a name for your connector, or use the auto-generated default name. The connector can be installed on the management account or on a delegated administrator account in MGN. For multi-account migrations, the connector can deploy agents to servers across member accounts.

**Step 2: AWS resource setup**

AWS Transform opens a setup page that runs in your browser using your AWS credentials. You must be logged in to the AWS Management Console with either your management account or your delegated administrator account. This must be the same account your AWS Transform target connector is connected to.

The setup page automatically creates the following resources:
+ **IAM roles** (created idempotently — skipped if they already exist):
  + `AWSApplicationMigrationConnectorManagementRole` – Used during agent installation to access credentials.
  + `AWSApplicationMigrationConnectorSharingRole_<ACCOUNT-ID>` – Contains permissions for agent installation.
+ **SSM Hybrid Activation** – 30-day expiration period. Links the connector machine to AWS Systems Manager and generates secure activation credentials.

Alternatively, you can download a CloudFormation template from the setup page to deploy the IAM roles yourself.

The setup page generates a one-line installation command with all necessary credentials and configuration.

**Important**  
Keep the setup page open until installation is complete. Closing it will require restarting the process. All credentials exist only in your browser and are not stored by AWS Transform.

**Step 3: Connector installation**

Install the connector on a Linux machine in your environment:

1. Copy the installation link from the setup page.

1. SSH into your chosen Linux machine.

1. Paste and execute the installation command.

1. Wait for installation to complete (typically 2–3 minutes).

**Step 4: Attach source servers**

After installation, AWS Transform identifies all source servers that belong to the current wave and automatically attaches them to the MGN connector.

**Step 5: Configure credentials**

Provide AWS Secrets Manager ARNs for your source server credentials. AWS Transform offers three credential configuration options:
+ **Single secret for Linux servers** – One shared secret containing SSH keys or username/password for all Linux source servers.
+ **Single secret for Windows servers** – One shared secret containing username and password for all Windows source servers.
+ **Multiple per-server secrets** – Different secrets per server or group of servers. Use this when servers have different credentials. AWS Transform generates a CSV file pre-populated with your server list. You fill in the `secret_arn` column for each server and upload the completed file.

**Note**  
You can combine the Linux and Windows single-secret options if you have both server types with one shared secret each. The per-server secrets option is mutually exclusive with the single-secret options.

Credential secret format. For more information, see [MGN connector credentials](https://docs.aws.amazon.com/mgn/latest/ug/mgn-connector-credentials.html) in the *MGN User Guide*:

```json
{
  "WinConnectionProtocol": "HTTPS",
  "WinUserName": "windows_username",
  "WinPassword": "windows_password",
  "LinuxUserName": "linux_username",
  "LinuxPrivateKey": "linux_private_key",
  "LinuxHostKeyValidation": false
}
```

## Agent deployment
<a name="transform-vmware-ms-connector-deployment"></a>

After credentials are configured and verified, AWS Transform deploys replication agents to your source servers. You can deploy to all servers in the current wave or select specific servers.

The deployment process for each server:

1. AWS Transform sends deployment commands to the connector by using SSM.

1. The connector retrieves credentials from AWS Secrets Manager.

1. The connector connects to the source server using the configured credentials.

1. The connector validates that the source server meets all prerequisites required to run the replication agent.

1. The connector installs and configures the replication agent.

1. The connector verifies successful installation and connectivity.

You can monitor deployment progress in real time with per-server status tracking, including the current installation step, elapsed time, and estimated time remaining. If any servers fail, AWS Transform displays the failure reason and offers retry options per server. Successfully deployed servers can proceed independently while failed servers are retried.

## Connector reuse and lifecycle
<a name="transform-vmware-ms-connector-reuse"></a>

When deploying agents for subsequent waves, you can reuse an existing connector or create a new one. AWS Transform lists all connectors configured in your account, showing the connector name, status (Active or Expired), attached server count, and Hybrid Activation expiry date.
+ **Active connector** – The Hybrid Activation is still valid. AWS Transform verifies IAM roles for the new wave and proceeds to credential configuration. No new Hybrid Activation is needed.
+ **Expired connector** – The SSM Hybrid Activation has expired. Expired activations cannot be renewed. You must select a different connector or create a new one.

SSM Hybrid Activations expire after 30 days. The activation is required only for installing the connector on the Linux machine. Once the connector is installed, you can continue to use it to install replication agents on source servers even after the activation expires. If you need to install the connector on a new machine after the activation has expired, you need to create a new connector through the setup process.