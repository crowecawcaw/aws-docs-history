

# Manage your data on Runtime Instances
<a name="runtime-instances-data-management"></a>

When you host agents on the **Instances** compute type, your data is stored on Amazon EBS volumes in your own AWS account.

This topic describes what AgentCore stores there, and how you read it, change it, get it out, and delete it.

For information about the shared responsibility model that applies to all of Amazon Bedrock AgentCore, see [Data protection in Amazon Bedrock AgentCore](data-protection.md).

## What Instances stores, and where
<a name="runtime-instances-data-management-what"></a>

Instances stores two categories of data. The following table shows where each category lives and which resource controls its lifecycle.


| Category | Where it is stored | Lifecycle is controlled by | 
| --- | --- | --- | 
| Volume content | Amazon Elastic Block Store (Amazon EBS) volumes that AgentCore creates in your AWS account and mounts into your agent | The session that mounts the volume | 
| Resource configuration | The capacity provider and agent runtime records, including the name, description, allowed instance types, networking, and storage definitions | The capacity provider and agent runtime | 

Volume content is whatever your agent reads and writes at its mount path. The Amazon EBS volumes are created in your account, so your existing account controls apply to them. For information about how volumes are encrypted, see [Encryption at rest for Runtime Instances](runtime-instances-encryption.md).

## Read and change your data
<a name="runtime-instances-data-management-read-change"></a>

Your agent reads and writes volume content at its mount path, so it changes that content the same way it created it. The following table shows where to find the operations for everything else.


| To do this | See | 
| --- | --- | 
| Read or change volume content from outside the agent |  [Execute shell commands in AgentCore Runtime sessions](runtime-execute-command.md). `InvokeAgentRuntimeCommand` runs a shell command in the running session, with the same filesystem your agent sees. | 
| Find the instances and volumes that back your sessions |  [Amazon EC2 managed instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-managed-instances.html). AgentCore provisions them as managed instances, which are hidden from list operations and your Amazon EC2 console views by default. Use `describe-instances --include-managed-resources` to list them, or change the [managed resource visibility setting](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-managed-instances.html#managed-resource-visibility-settings). | 
| View mount paths and storage settings |  [File system configurations for AgentCore Runtime](runtime-filesystem-configurations.md)  | 
| View your capacity provider configuration |  `GetCapacityProvider` and `ListCapacityProviders`. To find the agent runtimes that use one, use `ListAgentRuntimeVersionsByCapacityProvider`. | 
| Change your capacity provider configuration | Only the description can change, through `UpdateCapacityProvider`. For any other setting, create a new capacity provider and associate your agent runtimes with it. In the console, use the duplicate flow to start from the existing configuration. | 
| View metrics and logs |  [Observability](runtime-observability.md), or **Observability** and **Logs and tracing** on the runtime’s detail page in the console | 

## Export your data
<a name="runtime-instances-data-management-export"></a>

There is no export operation for volume content, and you can’t take an Amazon EBS snapshot of a capacity provider volume. AgentCore creates and operates these volumes as managed resources, so the snapshot operations that you use on volumes you create yourself aren’t available for them.

To get volume content out, write it to a destination you control, such as an Amazon S3 bucket. You have two ways to do that:
+ Run a command in the session with `InvokeAgentRuntimeCommand`. For more information, see [Execute shell commands in AgentCore Runtime sessions](runtime-execute-command.md).
+ Invoke your agent and have it copy the data, or return it in the response.

Either way, the copy runs with the agent runtime execution role, so grant that role write access to the destination. For more information about the role, see [AWS Identity and Access Management (IAM) roles](runtime-instances-how-it-works.md#runtime-instances-permissions).

**Important**  
Export what you want to keep before you delete a session or a capacity provider. Deleting either one deletes the volumes.

To export your capacity provider configuration, call `GetCapacityProvider` and save the response.

## Delete your data
<a name="runtime-instances-data-management-delete"></a>

Deleting volume content is a property of the session, not of the individual agent. Stopping one agent runtime in a session does not delete data, and does not terminate the instance.

Only persistent volumes hold data across a session stop. The root volume and any ephemeral volumes go away when the instance terminates, so anything your agent writes outside a persistent mount path is temporary. For information about the volume types, see [Encryption at rest for Runtime Instances](runtime-instances-encryption.md).

Persistent volumes survive every event except an explicit delete. The following table shows what each event does to them.


| Event | What it stops | What happens to your persistent volumes | 
| --- | --- | --- | 
|  `StopRuntimeSession`  | One agent runtime within a session. Other agent runtimes in the session are unaffected. | Retained. AgentCore keeps the volume attached to the session. | 
| Idle timeout | The instance, after all of its agents have been idle for `idleInstanceTimeout` seconds. | Retained. AgentCore re-attaches the volume when you invoke the session again. | 
| Maximum lifetime reached | The instance, regardless of activity, at `maxLifetime`. | Retained. AgentCore re-attaches the volume when you invoke the session again. | 
|  `DeleteCapacityProviderSession`  | The entire session, including its Amazon EC2 instance and network interface. | Deleted. AgentCore deletes the session’s persistent volumes. | 
|  `DeleteCapacityProvider`  | The capacity provider and all of its sessions. | Deleted. AgentCore deletes the volumes of every session that belongs to the capacity provider. | 

For information about the idle and lifetime settings, see [Configure Amazon Bedrock AgentCore lifecycle settings](runtime-lifecycle-settings.md).

To delete a session, you need the `runtimeSessionId` that you supplied when you invoked it. Keep a record of the session IDs you use. If you no longer have them, delete the capacity provider to delete all of its sessions and their volumes.

Before you can delete a capacity provider, remove the agent runtimes that reference it by deleting the associated runtimes, versions, or endpoints. Otherwise the request fails with a `ValidationException`.

For information about the operations and examples, see [Get started with Instances using the AWS CLI or SDK](runtime-instances-get-started-cli.md). For information about the console steps, see [Get started with Instances using the console](runtime-instances-get-started-console.md).