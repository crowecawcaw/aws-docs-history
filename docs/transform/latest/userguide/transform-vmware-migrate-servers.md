

# Migrate servers
<a name="transform-vmware-migrate-servers"></a>

AWS Transform automates the rehosting of your servers to Amazon EC2 at scale. The AI-powered agent guides you through each migration wave, from inventory validation and replication agent deployment through testing and final cutover. AWS Transform handles the orchestration across hundreds of servers while you maintain control over configuration and approval decisions. Internally, AWS Transform uses AWS Transform MGN (MGN) for data replication. For more information about MGN, see [What is AWS Transform MGN?](https://docs.aws.amazon.com/mgn/latest/ug/what-is-mgn.html) in the *MGN User Guide*.

You can migrate servers from virtually any source environment, including on-premises data centers, other cloud providers, or other AWS Regions. AWS Transform supports both physical servers and virtual servers running on VMware, Hyper-V, KVM, or other virtualization platforms. The source infrastructure and hypervisor are not important as long as the source operating system is supported.

Server migration is organized by waves. Each wave represents a group of servers that are migrated together. For each wave, the agent walks you through the following phases:

1. **Prerequisites and Configure Migration Defaults**. Set up your target accounts and configure how instances are launched. AWS Transform provides intelligent defaults so you can get started quickly.

1. **Step 1: Set up migration wave**. The agent configures your target account, validates permissions, and sets up resource tagging automatically.

1. **Step 2: Validate and confirm inventory**. Review your server configurations, instance type recommendations, and network assignments before migration begins.

1. **Step 3: Deploy replication agents**. The agent can deploy agents across all servers in a wave without requiring manual access to each server individually.

1. **Step 4: Data replication**. Continuous block-level replication keeps your target environment synchronized with source servers until you are ready for cutover.

1. **Step 5: Testing**. Launch test instances to validate your migrated servers before committing to the final cutover.

1. **Step 6: Cutover**. Complete the migration with minimal downtime. The agent coordinates the final switchover and verifies success.

For waves with a *containerize* migration strategy, AWS Transform runs the source code containerization workflow instead of the rehost steps. The containerization workflow guides you through cloning source code, generating Docker artifacts, publishing container images, and deploying to Amazon Elastic Container Service or Amazon Elastic Kubernetes Service. For the full containerization workflow, see [Source code containerization](transform-containers.md).

## Prerequisites and Configure Migration Defaults
<a name="transform-vmware-ms-prereqs-and-defaults"></a>

### Prerequisites
<a name="transform-vmware-ms-prerequisites"></a>

If you completed all the steps of an end-to-end migration job in AWS Transform, your target accounts, inventory file, and network infrastructure are already prepared. You can proceed to Configure Migration Defaults.

If you are starting server migration independently, ensure you have the following in place:
+ **Supported operating systems** – Source servers must run a supported operating system. For the full list, see [Supported operating systems](https://docs.aws.amazon.com/mgn/latest/ug/Supported-Operating-Systems.html) in the *MGN User Guide*.
+ **Target accounts for migration** – The AWS account IDs where you need your servers to be migrated. You can use AWS Transform landing zone or any other tools to set up your infrastructure.
+ **Network infrastructure in place** – VPCs, subnets, and security groups deployed and configured. You can use AWS Transform network migration or any other tools to set up your network infrastructure.
+ **Inventory file** – Prepared with server details, wave assignments, target account information, and Amazon EC2 instance type preferences. You can use AWS Transform migration planning to generate this file.

### Configure Migration Defaults
<a name="transform-vmware-ms-migration-defaults"></a>

AWS Transform provides intelligent defaults for your migration configuration, including how Amazon EC2 instances are launched and how replication is set up. You can accept these defaults and start migrating immediately, or customize them through the chat interface or a visual review. Defaults apply across all your target accounts and can be overridden at the wave level during wave setup.

#### Amazon EC2 recommendation preferences
<a name="transform-vmware-ms-ec2-recommendations"></a>

AWS Transform analyzes your source server utilization and recommends optimally sized Amazon EC2 instances, which helps you avoid overprovisioning from the start. You can configure your Amazon EC2 recommendation preferences to control how instance types are selected for your migrated servers.

For more information about generating Amazon EC2 recommendations, see [Generating Amazon EC2 recommendations in AWS Migration Hub](https://docs.aws.amazon.com/migrationhub/latest/ug/generating-ec2-recommendations.html).

**Note**  
You can modify the suggested Amazon EC2 instance types to include recommendations from the [Migration Evaluator](https://aws.amazon.com/migration-evaluator/), [AWS Optimization and Licensing Assessment (OLA)](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/aws-ola.html), or an AWS Transform assessment job.

#### Migration initialization
<a name="transform-vmware-ms-mgn-initialization"></a>

AWS Transform automatically sets up the required migration infrastructure in your target accounts before migration begins. This includes initializing MGN for every AWS Region in which you plan to migrate, as well as all target accounts. During the initialization process:
+ The required IAM roles and policies are created.
+ The required default templates are configured.

For information about the initialization process, see [Initializing AWS Transform MGN with the console](https://docs.aws.amazon.com/mgn/latest/ug/mgn-initialize-console.html) in the *MGN User Guide*.

#### Amazon EC2 launch template
<a name="transform-vmware-ms-default-launch"></a>

The launch settings include two parts: the general launch settings, and the Amazon EC2 launch template, which determines how a test or cutover instance is launched for each source server in AWS.

Launch settings, including the Amazon EC2 launch template, can be defined at the account level and are then applied to each source server automatically each time you add a source server to AWS Transform MGN. The launch settings defaults defined in this section can be applied to all your target accounts automatically.

AWS Transform presents the list of available launch template settings. You can choose to continue with the defaults or configure your launch template. If you choose to configure, AWS Transform provides a link to a human-in-the-loop (HITL) review that contains all the parameters of the launch template settings. You can also make modifications directly through the chat interface for any parameters you wish.

[Source servers](https://docs.aws.amazon.com/mgn/latest/ug/source-servers.html) are created with the account launch template settings. After source servers are created with these default settings, you can change them at the source server launch settings level. You can change source server settings on any parameter using the chat interface, or for bulk operations using the inventory Excel file during [Step 2: Validate and confirm inventory](#transform-vmware-ms-validate-inventory).

To review the full list of launch template settings and details, see [Launch general settings](https://docs.aws.amazon.com/mgn/latest/ug/launch-general-settings.html) in the *MGN User Guide*.

#### Additional Amazon EC2 launch template changes
<a name="transform-vmware-ms-launch-template-changes"></a>

Make additional Amazon EC2 launch template changes on the template ID for each target account. This option is available inside the wave setup. AWS Transform guides you through it and provides the appropriate link.

#### Post-launch actions
<a name="transform-vmware-ms-post-launch-actions"></a>

Post-launch actions automate modernization and validation tasks that run on each source server immediately after it launches as a test or cutover instance in AWS. AWS Transform Rehost takes the post-launch actions available in MGN and provides these capabilities so that the agent can recommend, configure, and run them on your behalf as part of the migration workflow. Actions are run through AWS Systems Manager (Systems Manager), and can be either one of the predefined actions available in MGN or a custom action created from an existing Systems Manager document.

Post-launch actions can be defined at the account level and are then applied to each source server automatically each time you add a source server to MGN. The post-launch action defaults defined in this section can be applied to all your target accounts automatically.

AWS Transform first presents the list of available post-launch actions across your target accounts. It then offers to define a new post-launch action and apply it across your target account migration. AWS Transform also provides AI-powered recommendations based on the operating system and best practices for your inventory. You can choose to continue with the defaults or configure your own actions.

You can also choose a post-launch action that is already defined in MGN. Prompt the agent to show the list of predefined post-launch actions available. For more information about this list, see [Predefined post-launch actions](https://docs.aws.amazon.com/mgn/latest/ug/source-post-launch-settings.html) in the *MGN User Guide*.

##### Creating a new post-launch action
<a name="transform-vmware-ms-post-launch-create"></a>

If you choose to create a new post-launch action, the agent prompts you to provide the Systems Manager document name or Systems Manager ARN to build the post-launch action with. The Systems Manager document should be created in advance through the AWS Systems Manager console. For more information about creating a Systems Manager document, see [Creating Systems Manager documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/create-ssm-doc.html) in the *AWS Systems Manager User Guide*.

The agent then generates a human-in-the-loop interface where you provide the required fields:
+ **Post-launch action name** – The agent provides a default name, which you can change.
+ **Post-launch action order** – The default order value is 1001, unless the account already has post-launch actions defined, in which case the new action is placed last in the run order. You can change the order. For more information about post-launch action order, see [Post-launch settings](https://docs.aws.amazon.com/mgn/latest/ug/source-post-launch-settings.html) in the *MGN User Guide*.
+ **Required Systems Manager parameter values** – Provide the values for any parameters required by the Systems Manager document.

You can also make modifications directly through the chat interface for any parameters you wish.

Source servers are created with the account post-launch action settings. After source servers are created with these default settings, you can change them at the source server level. You can change source server settings on any action using the chat interface, or for bulk operations using the inventory Excel file during [Step 2: Validate and confirm inventory](#transform-vmware-ms-validate-inventory).

##### Post-launch actions in the inventory file
<a name="transform-vmware-ms-post-launch-inventory"></a>

The Rehost agent extends the inventory file with a post-launch action template defined for each source server. This allows customers to update or add post-launch actions per source server during the rehost to MGN import process. To delete specific post-launch actions from a source server, use the `active` column to indicate `FALSE`. Post-launch actions in the inventory file use the following naming convention:

`mgn:launch:post-actions:<ACTION_NAME>:<FIELD_NAME>`

A global toggle controls whether post-launch actions run:

`mgn:launch:post-actions:enabled` (`TRUE`/`FALSE`)

**Fields per action**
+ `ssmDocumentName` (String, required) – The Systems Manager document to execute.
+ `order` (Integer, required) – Execution order; must be between 1000 and 10000. Actions execute in ascending order — lower values run first.
+ `active` (`TRUE`/`FALSE`, optional) – Whether the action is active.
+ `mustSucceedForCutover` (`TRUE`/`FALSE`, optional) – Whether the action must succeed before cutover.
+ `timeoutSeconds` (Integer, optional) – Timeout in seconds.
+ `description` (String, optional) – Human-readable description.
+ `parameters` (JSON, optional) – Systems Manager document parameters.

**Parameters JSON structure**

The `parameters` field is provided as a JSON structure:

```
{
  "parameters": {
    "Operation": [
      {"value": "Scan", "type": "String"}
    ]
  },
  "externalParameters": {
    "InstanceId": "ec2.InstanceId"
  }
}
```
+ `parameters` – Maps document parameter names to a list of value references (each with a `value` and an optional `type`, which defaults to `String`).
+ `externalParameters` – Maps document parameter names to dynamic path strings (no Systems Manager parameter is created).

### Step 1: Set up migration wave
<a name="transform-vmware-ms-setup-wave"></a>

In this phase, AWS Transform prepares the migration wave by configuring the target account, verifying service permissions, setting up resource tags, adding networking data to your inventory, and configuring replication and launch settings.

#### Migration mode and account configuration
<a name="transform-vmware-ms-migration-mode"></a>

AWS Transform supports two migration modes:
+ **Single-account migration** – All servers in the wave migrate to the same target account configured in your connector.
+ **Multi-account migration** – Servers migrate to different target accounts specified in your inventory file. For multi-account migrations, your inventory file must include an `mgn:account-id` column with the target account ID for each server.

AWS Transform confirms the target account configuration and verifies that MGN is initialized in each target account. If MGN is not yet initialized, AWS Transform provides instructions to complete the initialization. During initialization, MGN creates the following IAM service roles for replication and launch operations:
+ `AWSApplicationMigrationReplicationServerRole`
+ `AWSApplicationMigrationConversionServerRole`
+ `AWSApplicationMigrationMGHRole`
+ `AWSApplicationMigrationLaunchInstanceWithDrsRole`
+ `AWSApplicationMigrationLaunchInstanceWithSsmRole`
+ `AWSApplicationMigrationAgentRole`

To learn more about these roles, see [Initializing MGN with the console](https://docs.aws.amazon.com/mgn/latest/ug/mgn-initialize-console.html) or [Initializing MGN with the API](https://docs.aws.amazon.com/mgn/latest/ug/mgn-initialize-api.html) in the *MGN User Guide*.

For multi-account migrations, AWS Transform also creates the following role during the initialization step: `AWSTransformRehostSharingRole_<management-or-delegated-admin-account-id>`. This role is deployed across all migration target accounts.

#### Resource tagging verification
<a name="transform-vmware-ms-resource-tagging"></a>

After service permissions are confirmed, AWS Transform verifies that all required resources are properly tagged for the migration to be operated by the agent successfully. If any resources are missing required tags, AWS Transform provides a link to the tagging page where you can apply the missing tags before continuing. The following tags are required:
+ Existing source servers must have tags `CreatedBy: AWSTransform` and `ATWorkspace: <workspace_id>`. If you have already started replication on source servers and created them in the AWS Transform MGN service, you need to tag these servers so that AWS Transform can correlate them with the source servers discovered from your on-premises environment, and avoid unnecessary creation of duplicate source servers. AWS Transform automatically correlates between them using the user-provided ID, FQDN, or hostname keys.
+ Network resources must be properly tagged for both replication (staging area) and launch instances. AWS Transform displays the full list of network resources in your target account, with an indication of whether each resource is already tagged or not. You can review the list and select any untagged resources you want to add. For each resource you select, AWS Transform applies the relevant tag:
  + `CreatedBy: AWSTransform` or `CreatedFor: AWSTransform`, depending on the resource type.
  + `ATWorkspace: <workspace_id>` is applied to all selected resources.

  VPCs and subnets created by the AWS Transform network migration agent are automatically tagged.
+ In addition to VPCs and subnets, AWS Transform also displays all existing Elastic Network Interfaces (ENIs) found in your target account. If you want AWS Transform to use them as part of your instance launch, they must be tagged with `CreatedFor: AWSTransform` and `ATWorkspace: <workspace_id>`. For more information on how to attach or add ENIs to the Amazon EC2 launch template, see [Detailed considerations](https://docs.aws.amazon.com/mgn/latest/ug/detailed-considerations.html) in the *MGN User Guide*.

#### Add networking data to inventory
<a name="transform-vmware-ms-networking-data"></a>

AWS Transform adds networking information from your network migration to the inventory file. This step maps your servers to the appropriate target subnets and security groups based on the network configuration generated during the migrate network phase.

#### Replication and launch settings
<a name="transform-vmware-ms-replication-settings"></a>

##### Replication settings configuration
<a name="transform-vmware-ms-replication-config"></a>

Replication settings determine how data is replicated from your source servers to AWS. Configure the replication settings in the replication template before adding source servers to AWS Transform MGN. AWS Transform shows you all the replication settings parameters — you can configure them through a dedicated HITL or through the chat interface.

For more details about the replication settings parameters, see [Replication settings template](https://docs.aws.amazon.com/mgn/latest/ug/replication-settings-template.html) in the *MGN User Guide*.

##### Launch template settings
<a name="transform-vmware-ms-launch-template-config"></a>

The launch template allows you to control the way AWS Transform MGN launches instances in AWS. The default configuration defined in the template is automatically applied to every newly added server. You can configure launch template settings through a dedicated HITL or through the chat interface.

For more details about the launch template settings parameters, see [Launch template](https://docs.aws.amazon.com/mgn/latest/ug/launch-template.html) in the *MGN User Guide*.

AWS Transform also provides a link to the Amazon EC2 launch template ID associated with the launch template, allowing you to change additional Amazon EC2 launch template attributes. To edit the Amazon EC2 launch template, follow the instructions in [Launch template](https://docs.aws.amazon.com/mgn/latest/ug/launch-template.html) in the *MGN User Guide*.

#### IP assignment strategy
<a name="transform-vmware-ms-ip-assignment"></a>

You choose how IP addresses are assigned to your migrated servers:
+ **Static IP** – The source server's IP address is maintained. If CIDR transformation is required, AWS Transform automatically converts the IP address to match the new CIDR.
+ **Dynamic IP (DHCP)** – Each server is assigned a new IP address from the subnet's IP pool.

**Note**  
If you selected the MAP security groups mapping strategy during network migration, only static IP assignment is available. For more details, see [Security groups mapping](transform-vmware-migrate-network-new-vpcs.md#transform-vmware-security-group-association).

### Step 2: Validate and confirm inventory
<a name="transform-vmware-ms-validate-inventory"></a>

Before loading your server data into MGN, AWS Transform prepares the inventory file for your review. You can download the file in CSV or XLSX format, review the server configurations, and make changes if needed.

The inventory file includes details such as server names, operating systems, Amazon EC2 instance type recommendations, target subnets, security groups, IP assignments, and licensing options. Required fields include:
+ **Server information** – Server name, VMID, and source specifications.
+ **Wave assignment** – Migration wave grouping.
+ **Application grouping** – Logical application associations.
+ **Target configuration** – Target account, Region, and Amazon EC2 instance type.
+ **Network configuration** – Target subnet and security groups.

You can modify the file to adjust Amazon EC2 configurations, change operating system licensing options (BYOL or License Included), and update tenancy settings.

After you review the inventory, you can either accept it as shown or upload a modified version. AWS Transform then loads the data into MGN, which creates source server records for each server in the wave.

**Note**  
Do not remove columns or change column headers in the inventory file. AWS Transform requires the original file structure to process the data correctly.

**Note**  
AWS Transform allows one import to a given target AWS account and target AWS Region at a time. If you work on more than one wave simultaneously, or if there is more than one migration job running with the same target account, you must wait for an import to finish before you can perform another import in a different wave or job.

You can control the operating system licensing options (BYOL or License Included) and tenancy by specifying the configuration in the inventory file columns `mgn:launch:placement:operating-system-licensing` and `mgn:launch:placement:tenancy`. For more information, see [Import parameters](https://docs.aws.amazon.com/mgn/latest/ug/import-main.html#import-parameters) in the *MGN User Guide*.

### Step 3: Deploy replication agents
<a name="transform-vmware-ms-deploy-agents"></a>

To begin replicating data from your source servers to AWS, you install the AWS Replication Agent on each source server. AWS Transform offers three installation methods:
+ **Organization tools** – Use your organization's existing deployment tools (such as SCCM, Ansible, or Chef) to install agents across your servers. AWS Transform provides the installation commands with additional parameters for silent installation, including `--no-prompt`, `--aws-access-key-id`, `--aws-secret-access-key`, and `--aws-session-token`.
+ **MGN connector** – Use an MGN connector to automate agent installation. The connector connects to source machines over SSH (Linux) or WinRM (Windows) and installs the replication agent automatically. After it is configured, a connector can be reused across multiple waves and different target AWS accounts. For more information about the MGN connector, see [Set up the MGN Connector](https://docs.aws.amazon.com/mgn/latest/ug/mgn-connector-setup-instructions.html) in the *MGN User Guide*.
**Note**  
Before using the MGN connector with AWS Transform, you must tag the connector's managed instance in AWS Systems Manager Fleet Manager with the following tags:  
Key: `CreatedFor` Value: `AWSTransform`
Key: `ATWorkspace` Value: {{workspace-id}}
To tag the managed instance, open the AWS Systems Manager console, navigate to **Fleet Manager** under **Node Tools**, choose the managed instance of your MGN connector, and apply the tags above. Find your workspace ID in the AWS Transform web app URL: `https://.../workspace/{{workspace-id}}/job/{{job-id}}`.
+ **Manual installation** – Install the agent directly on each source server. This method requires direct access to each server but gives you full control over the installation process.

#### AWS Transform MGN connector setup
<a name="transform-vmware-ms-mgn-connector"></a>

The AWS Transform MGN connector automates the deployment of replication agents across your source servers, eliminating the need to log into each server individually. The connector is a lightweight client deployed on a dedicated Linux machine in your on-premises environment. It connects to source servers over SSH (Linux) or WinRM (Windows) to install and configure replication agents, eliminating the need to manually coordinate across multiple AWS services.

##### How the connector works
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

##### Connector machine requirements
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

##### Setup process
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

```
{
  "WinConnectionProtocol": "HTTPS",
  "WinUserName": "windows_username",
  "WinPassword": "windows_password",
  "LinuxUserName": "linux_username",
  "LinuxPrivateKey": "linux_private_key",
  "LinuxHostKeyValidation": false
}
```

##### Agent deployment
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

##### Connector reuse and lifecycle
<a name="transform-vmware-ms-connector-reuse"></a>

When deploying agents for subsequent waves, you can reuse an existing connector or create a new one. AWS Transform lists all connectors configured in your account, showing the connector name, status (Active or Expired), attached server count, and Hybrid Activation expiry date.
+ **Active connector** – The Hybrid Activation is still valid. AWS Transform verifies IAM roles for the new wave and proceeds to credential configuration. No new Hybrid Activation is needed.
+ **Expired connector** – The SSM Hybrid Activation has expired. Expired activations cannot be renewed. You must select a different connector or create a new one.

SSM Hybrid Activations expire after 30 days. The activation is required only for installing the connector on the Linux machine. Once the connector is installed, you can continue to use it to install replication agents on source servers even after the activation expires. If you need to install the connector on a new machine after the activation has expired, you need to create a new connector through the setup process.

#### Manual agent installation
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

After installation, AWS Transform verifies that all agents are successfully connected by checking that servers show a replication state of `INITIATING` or `INITIAL_SYNC`.

**Note**  
AWS Transform does not support MGN agentless replication. For information about agentless replication, see [Agentless replication overview](https://docs.aws.amazon.com/mgn/latest/ug/installing-vcenter-overview-mgn.html) in the *MGN User Guide*.

**Note**  
You must install the replication agent on all servers in a wave. Disconnect and archive servers on which you don't install the replication agent. You can use the `disconnect-from-service` command to disconnect servers, and the `mark-as-archived` command to archive disconnected servers. The archiving command only works for source servers whose lifecycle state is `DISCONNECTED`.

For quotas related to replication, see [MGN service quota limits](https://docs.aws.amazon.com/mgn/latest/ug/MGN-service-limits.html) in the *MGN User Guide*.

### Step 4: Data replication
<a name="transform-vmware-ms-data-replication"></a>

After the replication agents are installed, data replication begins automatically. AWS Transform uses continuous block-level replication to synchronize data from source servers to AWS.

The replication process consists of two phases:
+ **Initial sync** – A complete copy of the source server data to AWS. Data is stored as Amazon Elastic Block Store (Amazon EBS) snapshots or on Amazon FSx for NetApp ONTAP (FSx for ONTAP) volumes in the target account, depending on your configured target storage type. For more information, see [Target storage type](https://docs.aws.amazon.com/mgn/latest/ug/replication-server-settings.html#ebs-volume) in the *MGN User Guide*. Duration depends on data volume and network bandwidth.
+ **Continuous replication** – Ongoing synchronization of changed blocks with minimal impact on source server performance. Maintains an up-to-date copy in AWS.

Replication servers are temporary Amazon EC2 instances deployed in the staging area subnet. They receive replicated data from source servers and are automatically managed by MGN. For more information, see [Replication server settings](https://docs.aws.amazon.com/mgn/latest/ug/replication-server-settings.html) in the *MGN User Guide*.

AWS Transform monitors the replication progress and provides status updates, including replication status, replication lag (the time difference between source and replicated data), and bandwidth usage.

During replication, each server progresses through the following states:
+ **Not ready** – The server is undergoing the initial sync process and is not yet ready for testing.
+ **Ready for testing** – The server has been successfully added and data replication has started. Test or cutover instances can now be launched.

After all servers in the wave have progressed beyond the `NOT_READY` state, the data replication phase is complete and you can proceed to testing.

You can control replication for individual servers or the entire wave at any time:
+ **Pause replication** – Temporarily pause replication for specific servers or the entire wave.
+ **Resume replication** – Resume previously paused replication.
+ **Stop replication** – Permanently stop replication. Stopped replication can be restarted, but it begins from the initial sync.

### Step 5: Testing
<a name="transform-vmware-ms-testing"></a>

After data replication is complete, you can launch test instances to validate your migrated servers before performing the final cutover. For more information, see [Launch test instances](https://docs.aws.amazon.com/mgn/latest/ug/launch-test-instances.html) in the *MGN User Guide*. AWS Transform supports two testing options:
+ **Full wave testing** – Launch test instances for all servers in the wave.
+ **Selective testing** – Launch test instances for specific servers that you select by providing their user-provided IDs from the inventory file.

AWS Transform launches Amazon EC2 instances from the replicated data and provides the instance IDs so you can connect to and validate the test instances. After testing, you can:
+ Proceed to cutover if testing is successful.
+ Launch new test instances to retest.
+ Terminate test instances and address any issues before retesting.

### Step 5b: Mark applications as ready for cutover
<a name="transform-vmware-ms-mark-ready"></a>

After testing is complete and you are satisfied with the results, mark your applications as ready for cutover. AWS Transform reviews the replication status of each application and resolves any replication alerts before allowing you to proceed. Only applications with a clean replication status can be marked for cutover.

### Step 6: Cutover
<a name="transform-vmware-ms-cutover"></a>

Cutover is the final migration step where your production workloads are moved to AWS. For more information, see [Launch cutover instances](https://docs.aws.amazon.com/mgn/latest/ug/launch-cutover-instances.html) in the *MGN User Guide*. Similar to testing, AWS Transform supports full wave cutover or selective cutover for specific servers.

During cutover, AWS Transform launches Amazon EC2 instances from the latest replicated data and provides the instance IDs for each server. After verifying the cutover instances, you finalize the cutover, which stops the ongoing source machine replication.

The cutover process includes the following steps:

1. **Launch cutover instances** – AWS Transform launches Amazon EC2 instances for the selected servers. You can choose full wave cutover or selective cutover.

1. **Verify cutover instances** – Connect to the launched instances and verify they are functioning correctly.

1. **Finalize cutover** – Confirm the cutover to stop source machine replication. You can finalize all servers in the wave or select specific servers. Finalization stops replication agents from sending data, removes replication agents from source servers, and locks the server lifecycle state. This action cannot be easily undone. For more information, see [Finalize cutover](https://docs.aws.amazon.com/mgn/latest/ug/finalizing-cutover-2.html) in the *MGN User Guide*.

1. **Archive source servers (optional)** – After finalization, you can mark source servers as archived to free up source server quota in your account.

**Important**  
Finalizing cutover stops the ongoing source machine replication. Make sure you have verified your cutover instances before finalizing.

**Note**  
Downtime occurs between source shutdown and cutover instance availability. Plan your cutover window accordingly.

### Server lifecycle states
<a name="transform-vmware-ms-server-lifecycle"></a>

During migration, each server progresses through the following lifecycle states. For more information, see [Source server lifecycle](https://docs.aws.amazon.com/mgn/latest/ug/migration-dashboard.html) in the *MGN User Guide*.
+ **Not ready** – The server is undergoing the initial sync process and is not yet ready for testing.
+ **Ready for testing** – Data replication has started and test or cutover instances can be launched.
+ **Test in progress** – A test instance is currently being launched.
+ **Ready for cutover** – The server has been tested and is ready for cutover.
+ **Cutover in progress** – A cutover instance is currently being launched.
+ **Cutover complete** – The server has been cutover. All data has been migrated to the AWS cutover instance.
+ **Disconnected** – The server has been disconnected from MGN.

You can ask AWS Transform about the status of your servers at any time during the migration. AWS Transform provides an interactive wave status table that displays all relevant server information including migration lifecycle, replication status, and recommended next steps. You can also ask in natural language, for example:
+ What is the status of my servers?
+ What's the status of my wave?
+ What's the status of the step that I'm currently in?

During wave migration, you can ask AWS Transform to update or change the status of individual servers. For example, if 9 out of 10 servers in your wave passed the test phase but one failed, you can allow AWS Transform to continue moving the 9 servers into the next phase while re-running the test on the failed server.

### Deployment approvals
<a name="transform-vmware-ms-approvals"></a>

AWS Transform includes built-in approval workflows to ensure production changes go through your organization's review process. When an operation requires approval, AWS Transform routes the request to authorized approvers through the Approvals tab. Only users with the Admin role in AWS Transform can approve deployment requests. Deployments proceed only after receiving confirmation.