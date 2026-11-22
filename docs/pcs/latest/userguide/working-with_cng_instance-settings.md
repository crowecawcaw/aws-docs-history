

# Configuring instance settings for compute node groups in AWS PCS

Instance settings are the AMI, security groups, and SSH key pair that you specify on a compute node group. AWS PCS uses them to launch compute nodes. You can use instance settings with or without a custom launch template. To run setup scripts on compute nodes without launch template user data, use node lifecycle actions. For more information, see [Node lifecycle actions](cng-node-lifecycle-actions.md).

For step-by-step instructions, see [Creating a compute node group in AWS PCS](working-with_cng_create.md) and [Updating a compute node group in AWS PCS](working-with_cng_update.md).

**Contents**
+ [Available instance settings](#working-with_cng_instance-settings_available)
+ [Configuration types](#working-with_cng_instance-settings_types)
+ [How instance settings work with a custom launch template](#working-with_cng_instance-settings_precedence)
+ [Changing and removing instance settings](#working-with_cng_instance-settings_update)
+ [Viewing instance settings](#working-with_cng_instance-settings_view)
+ [Required permissions](#working-with_cng_instance-settings_permissions)
+ [Troubleshooting instance settings](#working-with_cng_instance-settings_troubleshooting)
+ [Migrating a compute node group from a custom launch template to instance settings in AWS PCS](working-with_cng_instance-settings-migrate.md)
  + [Prerequisites](working-with_cng_instance-settings-migrate.md#working-with_cng_instance-settings-migrate_prereq)
  + [Find the settings to move](working-with_cng_instance-settings-migrate.md#working-with_cng_instance-settings-migrate_settings)
  + [Migrate a compute node group](working-with_cng_instance-settings-migrate.md#working-with_cng_instance-settings-migrate_steps)
  + [Migrate a compute node group that you manage with CloudFormation](working-with_cng_instance-settings-migrate.md#working-with_cng_instance-settings-migrate_cfn)

## Available instance settings
<a name="working-with_cng_instance-settings_available"></a>


**Compute node group instance settings**  

| Setting | API parameter (AWS CLI option) | CloudFormation property | Description | 
| --- | --- | --- | --- | 
| AMI ID | `amiId` (`--ami-id`) | `AmiId` | The AMI that AWS PCS uses to launch compute nodes. The AMI must be compatible with AWS PCS. For more information, see [Amazon Machine Images (AMIs) for AWS PCS](working-with_ami.md). | 
| Security groups | `securityGroupIds` (`--security-group-ids`) | `SecurityGroupIds` | The IDs of the security groups for compute nodes. The security groups must be in the same VPC as the cluster and allow traffic between compute nodes and the cluster. For more information, see [Security group requirements and considerations](working-with_networking_sg.md#working-with_networking_sg-requirements). | 
| SSH key pair | `sshKeyName` (`--ssh-key-name`) | `SshKeyName` | The name of the Amazon EC2 key pair for SSH connections to compute nodes. The key pair must exist in the same AWS Region as the cluster. | 

You can configure other Amazon EC2 settings with a custom launch template. These settings include network interfaces for Elastic Fabric Adapter (EFA), capacity reservations, placement groups, block device mappings, and instance metadata options. For more information, see [Using Amazon EC2 launch templates with AWS PCS](working-with_launch-templates.md).

## Configuration types
<a name="working-with_cng_instance-settings_types"></a>

Each compute node group uses one of two configuration types. The console and the API use different names for them.


**Compute node group configuration types**  

| Console | API (`launchTemplateMode`) | Requirements | 
| --- | --- | --- | 
| **Standard configuration** | `MANAGED` | Doesn't use a custom launch template. You must specify `amiId` and `securityGroupIds`. You can't specify `customLaunchTemplate`. Compute nodes require Instance Metadata Service Version 2 (IMDSv2). | 
| **Launch template configuration** | `CUSTOM` | You must specify `customLaunchTemplate`. Instance settings are optional. For each one that you specify, AWS PCS uses it instead of the value in the launch template. | 
+ **Defaults** – The console selects **Standard configuration** by default. In the API and AWS CLI, `launchTemplateMode` defaults to `CUSTOM` when you create a compute node group. To create a compute node group without a custom launch template, you must specify `MANAGED`. When you update a compute node group and omit `launchTemplateMode`, the compute node group keeps its current configuration type.
+ **Switching to standard configuration** – See [Migrating a compute node group from a custom launch template to instance settings in AWS PCS](working-with_cng_instance-settings-migrate.md).
+ **Switching to launch template configuration** – Specify `--launch-template-mode CUSTOM` and `--custom-launch-template` in the same request.
+ **Launch templates that AWS PCS creates** – In both configuration types, AWS PCS creates a launch template of its own, named `pcs-{{identifier}}-do-not-delete`. Don't modify or delete it, and don't choose it as a custom launch template. For more information, see [Launch templates that AWS PCS creates](working-with_cng_create.md#working-with_cng_create_pcs-launch-templates).

When you change the configuration type, AWS PCS replaces the compute nodes in the compute node group after their running jobs finish. For more information, see [Updating a compute node group in AWS PCS](working-with_cng_update.md).

## How instance settings work with a custom launch template
<a name="working-with_cng_instance-settings_precedence"></a>

With launch template configuration, AWS PCS chooses each instance setting separately:
+ If you specify the setting on the compute node group, AWS PCS uses that value instead of any value in the launch template. For security groups, AWS PCS uses only the security groups on the compute node group. It doesn't add the security groups in the launch template.
+ If you don't specify the setting on the compute node group, AWS PCS uses the value in the launch template.
+ If neither the compute node group nor the launch template specifies an AMI or security groups, AWS PCS rejects the request. If neither specifies an SSH key pair, compute nodes don't have a key pair.

AWS PCS doesn't change your launch template. For an example, see [How AWS PCS chooses the AMI, security groups, and SSH key pair](working-with_cng_create.md#working-with_cng_create_instance-settings).

You can't specify `securityGroupIds` if your custom launch template defines network interfaces (`NetworkInterfaces`). Instead, specify security groups for each network interface in the launch template. For more information, see [Multiple network interfaces in AWS PCS](working-with_networking_multi-nic.md).

## Changing and removing instance settings
<a name="working-with_cng_instance-settings_update"></a>

To change an instance setting, specify the new value when you update the compute node group. If you omit an instance setting, AWS PCS doesn't change it. To remove an instance setting from the compute node group, specify an empty value:


**Values that remove instance settings**  

| AWS CLI option | Value to remove the setting | 
| --- | --- | 
| `--ami-id` | `""` | 
| `--security-group-ids` | `'[]'` | 
| `--ssh-key-name` | `""` | 

For example, the following command removes the SSH key pair from a compute node group.

```
aws pcs update-compute-node-group --region {{region}} \
    --cluster-identifier {{my-cluster}} \
    --compute-node-group-identifier {{my-node-group}} \
    --ssh-key-name ""
```

The result of removing a setting depends on the configuration type:
+ **Standard configuration** – AWS PCS rejects a request that removes the AMI or security groups. If you remove the SSH key pair, compute nodes don't have a key pair.
+ **Launch template configuration** – AWS PCS uses the value in the launch template. If the launch template doesn't have an AMI or security groups, AWS PCS rejects the request. If it doesn't have a key pair, compute nodes don't have one.

In the console, there's no separate control to remove a setting. To remove a security group, clear it in the **Security groups** list. In CloudFormation, remove the property from your template.

When you change or remove an instance setting, AWS PCS replaces the compute nodes in the compute node group after their running jobs finish. For more information, see [Updating a compute node group in AWS PCS](working-with_cng_update.md).

## Viewing instance settings
<a name="working-with_cng_instance-settings_view"></a>

The `GetComputeNodeGroup` operation returns only the instance settings that you set on the compute node group. It doesn't return values from your custom launch template. The console details page works the same way. An empty field means that AWS PCS uses the value in the launch template. To see the values in the launch template, view the launch template version in the Amazon EC2 console, or use the Amazon EC2 `DescribeLaunchTemplateVersions` operation.

The response also includes `launchTemplateMode`. With standard configuration, it's `MANAGED`. With launch template configuration, it's `CUSTOM` and the response also includes `customLaunchTemplate`. For an example, see [Getting compute node group details in AWS PCS](working-with_cng_get-details.md).

## Required permissions
<a name="working-with_cng_instance-settings_permissions"></a>

To specify `sshKeyName`, the IAM identity that creates or updates the compute node group needs permission for `ec2:DescribeKeyPairs`. The AMI and security group settings don't need additional permissions. For more information, see [Minimum permissions to use API actions](security-min-permissions.md#security-min-permissions_api).

## Troubleshooting instance settings
<a name="working-with_cng_instance-settings_troubleshooting"></a>

AWS PCS validates instance settings when you create or update a compute node group and returns an error if validation fails.

`You must specify at least 1 security group in securityGroupIds or in your launch template.`  
Neither the request nor the custom launch template specifies security groups. Specify `securityGroupIds`. If you set `launchTemplateMode` to `MANAGED`, specify `securityGroupIds` in the same request.

`The launch template with provided ID and version has no image ID set, and the request doesn't specify an amiId.`  
Neither the request nor the custom launch template specifies an AMI. Specify `amiId`.

`Cannot use securityGroupIds with a launch template that defines NetworkInterfaces. Manage security groups in your launch template NetworkInterfaces, or remove NetworkInterfaces from your launch template.`  
You specified `securityGroupIds` with a custom launch template that defines network interfaces. Remove `securityGroupIds` from the request, or remove the network interfaces from the launch template.

`AWS PCS couldn't find the key pair you specified in sshKeyName: {{key-name}}.`  
The key pair doesn't exist in the same AWS Region as the cluster. Check the key pair name.

`You don't have permission to perform ec2:DescribeKeyPairs.`  
Add `ec2:DescribeKeyPairs` to the IAM policy of the identity that creates or updates the compute node group.

**Important**  
If you delete a security group or key pair that a compute node group uses, AWS PCS can't launch new compute nodes. Before you delete the resource, update the compute node group to stop using it.