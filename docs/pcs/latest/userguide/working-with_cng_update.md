

# Updating a compute node group in AWS PCS

This topic describes how to update a compute node group in AWS Parallel Computing Service (AWS PCS). It also describes which changes cause AWS PCS to replace compute nodes. For information about custom Slurm settings, see [Custom Slurm settings for AWS PCS compute node groups](slurm-custom-settings-cng.md).

## Options for updating an AWS PCS compute node group
<a name="working-with_cng_update_options"></a>

You can change the settings that AWS PCS uses to launch compute nodes and the rules for how it launches them. For example, you can change the AMI to install different software, change the security groups to control network access, or change the SSH key pair. You can also change the configuration type, subnets, IAM instance profile, scaling configuration, purchase option, Slurm settings, node lifecycle actions, and instance health checks.

You can't change these settings after you create a compute node group:
+ Name
+ Instance types

## Considerations when updating an AWS PCS compute node group
<a name="working-with_cng_update_considerations"></a>

Before you update a compute node group, consider the following:
+ Changes take effect when the compute node group status changes from `UPDATING` to `ACTIVE`. New compute nodes launch with the updated settings.
+ If you change a setting that AWS PCS uses to launch compute nodes, AWS PCS replaces the existing compute nodes. These settings include the AMI, security groups, SSH key pair, custom launch template or its version, configuration type, node lifecycle actions, and instance health checks. AWS PCS lets running jobs finish before it replaces a node. AWS PCS terminates interactive user processes, such as processes on login nodes.
+ When AWS PCS marks compute nodes for replacement, the compute node group status returns to `ACTIVE`. The replacement happens later, when the nodes are idle.
+ AWS PCS doesn't replace running compute nodes for changes that don't affect how it launches them. For example, adding a subnet or changing the Spot allocation strategy affects only compute nodes that AWS PCS launches later.
+ If you change the SSH key pair, running compute nodes keep the previous key pair until AWS PCS replaces them. If you specify an SSH key pair, the IAM identity that updates the compute node group also needs `ec2:DescribeKeyPairs`. For more information, see [Minimum permissions to use API actions](security-min-permissions.md#security-min-permissions_api).
+ For On-Demand compute node groups with more than one subnet, the order in which you list the subnets sets the launch priority. AWS PCS tries to launch instances in the first subnet, and tries the next subnet if the first can't provide the requested capacity. To change the priority, update the compute node group with the subnets in your preferred order. The change affects only future launches. AWS PCS doesn't move or replace running compute nodes.
+ If you create a new version of a custom launch template, you must update the compute node group to use the new version.
+ To change the AMI, security groups, or SSH key pair, specify the new value on the compute node group. If the compute node group uses a custom launch template, you can also change the value in the launch template. Then update the compute node group to use the new launch template version. If you specify a value in both places, AWS PCS uses the value on the compute node group instead of the value in the launch template. To remove a value from the compute node group, see [Changing and removing instance settings](working-with_cng_instance-settings.md#working-with_cng_instance-settings_update).
+ You can switch a compute node group between standard configuration (`MANAGED`) and launch template configuration (`CUSTOM`). To switch to standard configuration, see [Migrating a compute node group from a custom launch template to instance settings in AWS PCS](working-with_cng_instance-settings-migrate.md). To switch to launch template configuration, specify `--launch-template-mode CUSTOM` and `--custom-launch-template` in the same request.
+ If you directly edit a security group that a compute node group uses, the change takes effect immediately on running and future compute nodes.
+ Permission changes in the IAM instance profile of a compute node group take effect immediately on running and future compute nodes.
+ If you decrease the maximum number of instances in a compute node group, AWS PCS removes nodes from Slurm to meet the new maximum. AWS PCS terminates the instances for the removed nodes. Jobs running on those nodes fail and return to their queues.
+ Don't use a launch template named `pcs-{{identifier}}-do-not-delete`. AWS PCS creates launch templates with this name for its own use. For more information, see [Launch templates that AWS PCS creates](working-with_cng_create.md#working-with_cng_create_pcs-launch-templates).
+ To change the purchase option to Spot, you must have the `AWSServiceRoleForEC2Spot` service-linked role in your AWS account. For more information, see [Amazon EC2 Spot role for AWS PCS](spot-role.md).
+ To use an On-Demand Capacity Reservation (ODCR), an interruptible ODCR (I-ODCR), or a Capacity Block, the compute node group must use a custom launch template that targets the reservation.

## Update a compute node group in AWS PCS
<a name="working-with_cng_update_update"></a>

You can update a compute node group by using the AWS Management Console or the AWS CLI.

------
#### [ AWS Management Console ]

**To update a compute node group (console)**

1. Open the [AWS PCS console](https://console.aws.amazon.com/pcs/home#/clusters).

1. Choose the cluster that has the compute node group.

1. Choose **Compute node groups**, choose the compute node group, and then choose **Edit**.

1. (Optional) Change the configuration type. You can switch between **Standard configuration** and **Launch template configuration**. For the requirements of each, see [How AWS PCS chooses the AMI, security groups, and SSH key pair](working-with_cng_create.md#working-with_cng_create_instance-settings).

1. In the **Computing configuration**, **Network**, **Additional settings**, **Scheduler configuration**, **Slurm custom settings**, **Node lifecycle actions**, and **Instance health checks** sections, change any values except **Instances**. You can't change the instance types in a compute node group.
   + **Security groups** – To remove a security group, clear it in the list.
   + **Scale-down idle time** – Enter a value from 1 to 10000000 seconds. AWS PCS uses this value instead of the cluster-level value. To use the cluster-level value, clear the field. This setting requires Slurm version 25.11 or later.

   With **Launch template configuration**, the **AMI ID**, **Security groups**, and **SSH key pair** fields show only values that you set on the compute node group. They don't show values from the launch template. An empty field means that AWS PCS uses the value in the launch template.

1. Choose **Update**. The **Status** field shows `Updating` while AWS PCS applies the changes. Updates can take several minutes.

------
#### [ AWS CLI ]

To update a compute node group, run `update-compute-node-group` with the settings that you want to change. AWS PCS doesn't change settings that you omit. You can change any setting except the name and `--instance-configs`. In the examples that follow, make these replacements:
+ Replace {{region}} with the ID of the AWS Region where your cluster is, such as `us-east-1`.
+ Replace {{my-cluster}} with the name or `clusterId` of your cluster.
+ Replace {{my-node-group}} with the name or `computeNodeGroupId` of your compute node group.

**Example – Updating the AMI, security groups, and SSH key pair**  

```
aws pcs update-compute-node-group --region {{region}} \
    --cluster-identifier {{my-cluster}} \
    --compute-node-group-identifier {{my-node-group}} \
    --ami-id {{ami-ExampleID1}} \
    --security-group-ids {{sg-ExampleID1}} {{sg-ExampleID2}} \
    --ssh-key-name {{my-key-pair}}
```
Specify only the options that you want to change. The security groups that you specify become the complete list of security groups on the compute node group. To remove a value from the compute node group, see [Changing and removing instance settings](working-with_cng_instance-settings.md#working-with_cng_instance-settings_update).

**Example – Updating the launch template version**  

```
aws pcs update-compute-node-group --region {{region}} \
    --cluster-identifier {{my-cluster}} \
    --compute-node-group-identifier {{my-node-group}} \
    --custom-launch-template id={{lt-ExampleID1}},version='{{launch-template-version}}'
```
Use this command after you create a new version of the custom launch template. To switch a compute node group from standard configuration to launch template configuration, also specify `--launch-template-mode CUSTOM`.

**Example – Updating custom Slurm settings**  

```
aws pcs update-compute-node-group --region {{region}} \
    --cluster-identifier {{my-cluster}} \
    --compute-node-group-identifier {{my-node-group}} \
    --slurm-configuration \
    'slurmCustomSettings=[{parameterName=Features,parameterValue="{{gpu,nvme}}"}]'
```
For more information, see [Custom Slurm settings for AWS PCS compute node groups](slurm-custom-settings-cng.md).

**Example – Updating node lifecycle actions**  
To change the scripts that run at defined points in a compute node's lifecycle, specify `--node-lifecycle-actions`. For the format and example commands, see [Node lifecycle action examples for AWS PCS](cng-node-lifecycle-actions-examples.md).

**Example – Updating instance health checks**  
To turn on, change, or turn off instance health checks, specify `--instance-health-checks`. The value replaces all of the compute node group's instance health check settings. For example commands, see [Changing or turning off instance health checks](cng-instance-health-checks-configure.md#cng-instance-health-checks-configure-update).

**Example – Updating the scale-down idle time**  

```
aws pcs update-compute-node-group --region {{region}} \
    --cluster-identifier {{my-cluster}} \
    --compute-node-group-identifier {{my-node-group}} \
    --slurm-configuration scaleDownIdleTimeInSeconds={{600}}
```
AWS PCS uses this value instead of the cluster-level scale-down idle time. Valid values are 1–10000000. To use the cluster-level value again, set `scaleDownIdleTimeInSeconds` to `-1`. This setting requires Slurm version 25.11 or later.

Updates can take several minutes. To check the status of the compute node group, run the following command.

```
aws pcs get-compute-node-group --region {{region}} \
    --cluster-identifier {{my-cluster}} \
    --compute-node-group-identifier {{my-node-group}}
```

------