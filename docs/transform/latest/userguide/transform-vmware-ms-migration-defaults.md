

# Configure Migration Defaults

AWS Transform provides intelligent defaults for your migration configuration, including how Amazon EC2 instances are launched and how replication is set up. You can accept these defaults and start migrating immediately, or customize them through the chat interface or a visual review. Defaults apply across all your target accounts and can be overridden at the wave level during wave setup.

## Amazon EC2 recommendation preferences
<a name="transform-vmware-ms-ec2-recommendations"></a>

AWS Transform analyzes your source server utilization and recommends optimally sized Amazon EC2 instances, which helps you avoid overprovisioning from the start. You can configure your Amazon EC2 recommendation preferences to control how instance types are selected for your migrated servers.

AWS Transform uses the same Amazon EC2 rightsizing mechanism as compute assessments. For more information about how Amazon EC2 recommendations are generated, see [Amazon EC2 right-sizing](transform-app-assessments-compute.md#transform-app-assessments-compute-ec2).

## Storage recommendations
<a name="transform-vmware-ms-storage-recommendations"></a>

AWS Transform analyzes the capacity and performance of your source storage and recommends how to size the target storage for your migrated servers. This helps you avoid overprovisioning, which adds cost, and underprovisioning, which can cause performance issues after migration.

Storage recommendations are based on the data from AWS Transform storage assessments. For more information, see [Storage assessments](transform-app-assessments-storage.md).

The type of recommendation that a server receives depends on the target storage type, Amazon EBS or Amazon FSx for NetApp ONTAP, that you set for the server.

### Amazon EBS recommendations
<a name="transform-vmware-ms-storage-ebs"></a>

For each source server, AWS Transform recommends the following settings for its volumes:
+ Volume type, for example gp3 or io2
+ IOPS
+ Throughput, in MiB/s

MGN sets the size of each volume automatically, based on the size of the corresponding disk on the source server.

AWS Transform adds these recommendations to the server's inventory file, so that MGN launches the Amazon EBS volumes with the recommended configuration. You don't need to enter them manually.

You can review and change the recommended values in either of the following ways:
+ At this stage, ask the agent to show all your source servers with their recommended storage properties, and request any changes in the chat.
+ In the inventory file, during [Step 2: Validate and confirm inventory](transform-vmware-ms-validate-inventory.md).

If a value is missing, validation shows a warning and AWS Transform uses the default value. The warning doesn't block the migration.

**Note**  
AWS Transform recommends one volume configuration for each source server. MGN supports one volume template for each server and applies the same parameters to both the boot volume and the data volumes. All volumes on the same server use the recommended volume type and settings.

### Amazon FSx for NetApp ONTAP recommendations
<a name="transform-vmware-ms-storage-fsx"></a>

For file storage workloads, AWS Transform makes recommendations at the file system level instead of for individual volumes, because a file system's performance is shared by all the volumes on it. AWS Transform recommends the following:
+ The number of file systems to provision. Each source storage array maps to a file system, and several arrays can share one file system.
+ The file system on which to create the target volumes for each source volume. The source data is copied to these target volumes.
+ The SSD storage capacity and throughput capacity for each file system, based on the capacity and peak performance that its workloads require.

Use these recommendations to provision the storage virtual machines (SVMs) directly in Amazon FSx for NetApp ONTAP, outside of AWS Transform. Migration to FSx for ONTAP requires specific file system settings. Configure your FSx for ONTAP file system settings for MGN integration, as described in [Create FSx for ONTAP file system](https://docs.aws.amazon.com/mgn/latest/ug/fsx-ontap.html#fsx-ontap-step2-create-filesystem) in the *MGN User Guide*.

After you provision them, AWS Transform asks whether you want to provide the mapping between your SVM IDs and your source storage arrays. If you provide it, AWS Transform adds the SVM IDs to the inventory file for you. If you skip this step, validation shows a warning, and you provide the SVM IDs during [Step 2: Validate and confirm inventory](transform-vmware-ms-validate-inventory.md). The warning doesn't block the migration.

## Migration initialization
<a name="transform-vmware-ms-mgn-initialization"></a>

AWS Transform automatically sets up the required migration infrastructure in your target accounts before migration begins. This includes initializing MGN for every AWS Region in which you plan to migrate, as well as all target accounts. During the initialization process:
+ The required IAM roles and policies are created.
+ The required default templates are configured.

For information about the initialization process, see [Initializing AWS Transform MGN with the console](https://docs.aws.amazon.com/mgn/latest/ug/mgn-initialize-console.html) in the *MGN User Guide*.

## Amazon EC2 launch template
<a name="transform-vmware-ms-default-launch"></a>

The launch settings include two parts: the general launch settings, and the Amazon EC2 launch template, which determines how a test or cutover instance is launched for each source server in AWS.

Launch settings, including the Amazon EC2 launch template, can be defined at the account level and are then applied to each source server automatically each time you add a source server to AWS Transform MGN. The launch settings defaults defined in this section can be applied to all your target accounts automatically.

AWS Transform presents the list of available launch template settings. You can choose to continue with the defaults or configure your launch template. If you choose to configure, AWS Transform provides a link to a human-in-the-loop (HITL) review that contains all the parameters of the launch template settings. You can also make modifications directly through the chat interface for any parameters you wish.

[Source servers](https://docs.aws.amazon.com/mgn/latest/ug/source-servers.html) are created with the account launch template settings. After source servers are created with these default settings, you can change them at the source server launch settings level. You can change source server settings on any parameter using the chat interface, or for bulk operations using the inventory Excel file during [Step 2: Validate and confirm inventory](transform-vmware-ms-validate-inventory.md).

To review the full list of launch template settings and details, see [Launch general settings](https://docs.aws.amazon.com/mgn/latest/ug/launch-general-settings.html) in the *MGN User Guide*.

## Additional Amazon EC2 launch template changes
<a name="transform-vmware-ms-launch-template-changes"></a>

Make additional Amazon EC2 launch template changes on the template ID for each target account. This option is available inside the wave setup. AWS Transform guides you through it and provides the appropriate link.

## Source actions
<a name="transform-vmware-ms-source-actions"></a>

Source actions run your own scripts on the machines in your on-premises environment during the migration. AWS Transform uses the MGN source actions capability to create and run them. The MGN connector runs the scripts on your machines over SSH for Linux or WinRM for Windows. For more information, see [Source actions](https://docs.aws.amazon.com/mgn/latest/ug/source-actions.html) in the *MGN User Guide*.

Creating and running source actions through AWS Transform is especially useful for multi-account migrations:
+ **Create from a description** – Describe what you need in the chat, and AWS Transform creates both the script and the source action for you.
+ **Apply across all your accounts** – When you work from the MGN delegated admin account, which has access to configure source actions in all the accounts in your organization, AWS Transform can apply your source actions across all the target accounts of your migration. You don't need to create each source action separately in each account.

In a multi-account migration, keep the following in mind:
+ **Account ownership** – Source actions are owned by the member account where the source servers are, but a member account can't run them. The delegated admin account runs them through the MGN connector. A member account can run its own source actions only if it deploys its own MGN connector.
+ **Script parameters in member accounts** – In the MGN console, when you create a source action for a member account from the delegated admin account, the script content option isn't available, and the Systems Manager Parameter Store parameter must already exist in the member account. When you work through AWS Transform from the delegated admin account, AWS Transform configures the source actions in the member accounts for you.

For more information, see the account ownership and multi-account migration content in [Source actions](https://docs.aws.amazon.com/mgn/latest/ug/source-actions.html) in the *MGN User Guide*.

When you create a source action through AWS Transform, you can provide the script in any of the following ways:
+ **Ask AWS Transform to write the script** – You don't need to write the script yourself. Describe in the chat what you want the script to do. AWS Transform writes the script content for you, and then creates the source action in MGN with that script.
+ **Provide your own script** – Paste your script content in the chat. AWS Transform creates the source action in MGN with your script.
+ **Use an existing Systems Manager Parameter Store parameter** – Provide the name or ARN of a parameter that already contains your script. MGN supports only parameters whose names start with `ManagedByAWSApplicationMigrationService`.

### Prerequisites for source actions
<a name="transform-vmware-ms-source-actions-prerequisites"></a>

Before you create and run source actions, make sure that you have the following:
+ An MGN connector that is deployed and registered, with network access to your on-premises machines over SSH (Linux) or WinRM (Windows).
+ Credentials registered for each machine.

For the full list of prerequisites and script requirements, see [Source actions](https://docs.aws.amazon.com/mgn/latest/ug/source-actions.html) in the *MGN User Guide*.

### Creating a source action
<a name="transform-vmware-ms-source-actions-create"></a>

To create a source action, ask the agent in the chat, and then provide the script in one of the ways described earlier. AWS Transform also asks you for the following details:
+ **Action name** – Must be unique within the account.
+ **Action description** – Optional. Helps identify the purpose of the action.
+ **Operating system** – Linux, Windows, or both.
+ **Timeout** – In seconds. The default is 3,600 seconds. The minimum is 60 seconds, and the maximum is 14,400 seconds.

AWS Transform creates the source action in the target accounts where your source servers are. You can ask the agent to apply the source action to all the target accounts of your migration. When AWS Transform writes the script or you provide the script content, MGN creates the AWS Systems Manager Parameter Store parameter for you.

**Important**  
If AWS Transform writes the script for you, review it before AWS Transform creates the source action. The script runs on your on-premises machines with the credentials that you registered for each machine.  
Don't include secrets in your scripts. Source actions don't support `SecureString` parameters.

### Running source actions
<a name="transform-vmware-ms-source-actions-run"></a>

You can run source actions at any point in the migration lifecycle. After the MGN connector is set up and your source servers are associated with it, prompt the agent to run a source action. Choose the source action from the source actions that you created, and the source servers to run it on.

As your job progresses, AWS Transform also suggests running source actions at relevant points, and shows these suggestions in the chat.

**Important**  
A source action can run on a launched test or cutover instance instead of on the source server. The MGN connector runs the source action on whichever machine answers at the address in **FQDN for Action Framework**, and doesn't check that it's the original source server. A launched instance is a copy of the source server, with the same operating system users and passwords. If the connector can reach the launched instance at that address, it can sign in to it.  
This can happen in the following cases:  
**FQDN for Action Framework** is a DNS name, and you point that DNS name to a launched instance.
You launch an instance with Copy private IP enabled, and the connector's network routes that IP address to AWS, for example over a Site-to-Site VPN or AWS Direct Connect.
If you plan to point the source server's DNS name to a launched instance, set **FQDN for Action Framework** to the source server's IP address instead. You can set it in the `mgn:server:fqdn-for-action-framework` field of the inventory file.

### Monitoring source actions
<a name="transform-vmware-ms-source-actions-monitor"></a>

At any point during wave execution, you can ask the agent to show the source actions that ran and their status. You can review them in the following ways:
+ **By source action** – The source servers that each source action ran on, and the status on each server.
+ **By source server** – A summary of the source actions that ran on each source server.
+ **By wave or application** – All the source actions that ran on the source servers in a wave or an application.

## Post-launch actions
<a name="transform-vmware-ms-post-launch-actions"></a>

Post-launch actions automate modernization and validation tasks that run on each source server immediately after it launches as a test or cutover instance in AWS. AWS Transform Rehost takes the post-launch actions available in MGN and provides these capabilities so that the agent can recommend, configure, and run them on your behalf as part of the migration workflow. Actions are run through AWS Systems Manager (Systems Manager), and can be either one of the predefined actions available in MGN or a custom action created from an existing Systems Manager document.

Post-launch actions can be defined at the account level and are then applied to each source server automatically each time you add a source server to MGN. The post-launch action defaults defined in this section can be applied to all your target accounts automatically.

AWS Transform first presents the list of available post-launch actions across your target accounts. It then offers to define a new post-launch action and apply it across your target account migration. AWS Transform also provides AI-powered recommendations based on the operating system and best practices for your inventory. You can choose to continue with the defaults or configure your own actions.

You can also choose a post-launch action that is already defined in MGN. Prompt the agent to show the list of predefined post-launch actions available. For more information about this list, see [Predefined post-launch actions](https://docs.aws.amazon.com/mgn/latest/ug/source-post-launch-settings.html) in the *MGN User Guide*.

### Creating a new post-launch action
<a name="transform-vmware-ms-post-launch-create"></a>

If you choose to create a new post-launch action, the agent prompts you to provide the Systems Manager document name or Systems Manager ARN to build the post-launch action with. The Systems Manager document should be created in advance through the AWS Systems Manager console. For more information about creating a Systems Manager document, see [Creating Systems Manager documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/create-ssm-doc.html) in the *AWS Systems Manager User Guide*.

The agent then generates a human-in-the-loop interface where you provide the required fields:
+ **Post-launch action name** – The agent provides a default name, which you can change.
+ **Post-launch action order** – The default order value is 1001, unless the account already has post-launch actions defined, in which case the new action is placed last in the run order. You can change the order. For more information about post-launch action order, see [Post-launch settings](https://docs.aws.amazon.com/mgn/latest/ug/source-post-launch-settings.html) in the *MGN User Guide*.
+ **Required Systems Manager parameter values** – Provide the values for any parameters required by the Systems Manager document.

You can also make modifications directly through the chat interface for any parameters you wish.

Source servers are created with the account post-launch action settings. After source servers are created with these default settings, you can change them at the source server level. You can change source server settings on any action using the chat interface, or for bulk operations using the inventory Excel file during [Step 2: Validate and confirm inventory](transform-vmware-ms-validate-inventory.md).

### Post-launch actions in the inventory file
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

```json
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