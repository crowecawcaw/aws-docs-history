# Updating an AWS PCS compute node group

This topic provides an overview of available options and describes what to consider when you
update an AWS PCS compute node group. For information about Slurm custom settings, see [Custom Slurm settings for AWS PCS compute node groups](slurm-custom-settings-cng.md "slurm-custom-settings-cng.md").

## Options for updating an AWS PCS compute node

group

Updating an AWS PCS compute node group enables you to change the properties of instances
launched by AWS PCS, as well as the rules for how those instances are launched. For example, you
can replace the AMI for node group instances with another one with different software installed
on it. Or, you can update security groups to change inbound or outbound network connectivity. You
can also change the scaling configuration and the preferred purchase option.

The following node group settings cannot be altered after creation:

- Name
- Instances

## Considerations when updating an

AWS PCS compute node group

Compute node groups define EC2 instances that are used to process jobs, provide interactive
shell access, and other tasks. They are often associated with one or more AWS PCS queues. As
you update your compute node group to change its behavior (or that of its nodes), consider the
following:

- Changes to compute node group properties become effective when the compute node group
  status changes from **Updating** to **Active**. New instances launch with the updated properties.
- Updates that don't impact the configuration of specific nodes don't affect running nodes.
  For example, adding a subnet and changing the allocation strategy.
- If you update the launch template for a compute node group, you must update the compute
  node group to use the new version.
- To add or remove a security group from nodes in a compute node group, edit its launch
  template and update the compute node group. New instances launch with the updated set of
  security groups.
- If you directly edit a security group used by a compute node group, it takes immediate
  effect on running and future instances.
- If you add or remove permissions from the IAM instance profile used by a compute node
  group, it takes immediate effect on running and future instances.
- To change the AMI used by a compute node group's instances, update the compute node group
  (or its launch template) to use the new AMI and wait for AWS PCS to replace the instances.
- AWS PCS replaces existing instances in the node group after a node group update
  operation. If there are jobs running on a node, those jobs are allowed to complete before
  AWS PCS replaces the node. Interactive user processes (such as on login node instances) are
  terminated. Node group status returns to `Active` when AWS PCS marks the instances
  for replacement, but the actual replacement occurs when the instances are idle.
- If you decrease the maximum number of instances allowed in a compute node group,
  AWS PCS removes nodes from Slurm to meet the new maximum. AWS PCS terminates running
  instances associated with the removed Slurm nodes. The running jobs on the removed nodes fail
  and return to their queues.
- AWS PCS creates a managed launch template for each compute node group. They are named
  `pcs-`identifier`-do-not-delete`. Don't select them when
  you create or update a compute node group, or the node group will not function correctly.
- If you update a compute node group to use **Spot** for its
  purchase option, you must have the **AWSServiceRoleForEC2Spot**
  service-linked role in your account. For more information, see [Amazon EC2 Spot role for AWS PCS](spot-role.md "spot-role.md").

## To update an AWS PCS compute node group

You can update a node group using the AWS Management Console or the AWS CLI.

AWS Management Console

###### To update a compute node group

1.  Open the AWS PCS console at
    `https://console.aws.amazon.com/pcs/home#/clusters`
2.  Select the cluster where you wish to update a compute node group.
3.  Navigate to **Compute node groups**, go to the node group you wish to
    update, then select **Edit**.
4.  In the **Computing configuration**, **Additional
    settings**, and **Slurm customization** settings
    sections, update any values except:

        * **Instances** – You can't change the instances in a
         compute node group.

    For more information about Slurm custom settings, see [Custom Slurm settings for AWS PCS compute node groups](slurm-custom-settings-cng.md "slurm-custom-settings-cng.md").

5.  Choose **Update**. The **Status** field will show
    _Updating_ while changes are being applied.

###### Important

Compute node group updates can take several minutes.

AWS CLI

###### To update a compute node group

1. Update your compute node group with the command that follows. Before running the
   command, make the following replacements:
   1. Replace `region-code` with the AWS Region that you want to
      create your cluster in.
   2. Replace `my-node-group` with the name or
      `computeNodeGroupId` for your compute node group.
   3. Replace `my-cluster` with the name or `clusterId`
      of your cluster.

```
aws pcs update-compute-node-group --region `region-code` \
    --cluster-identifier `my-cluster` \
    --compute-node-group-identifier `my-node-group`
```

###### Example – Updating a compute node group with custom Slurm settings

```
aws pcs update-compute-node-group --region `region-code` \
    --cluster-identifier `my-cluster` \
    --compute-node-group-identifier `my-node-group` \
    --slurm-configuration \
    'slurmCustomSettings=[{parameterName=Features,parameterValue="`gpu,nvme`"}]'
```

For more information, see [Custom Slurm settings for AWS PCS compute node groups](slurm-custom-settings-cng.md "slurm-custom-settings-cng.md"). 2. Update any node group parameters except for `--instance-configs`. For example, to
set a new AMI ID, pass `--amiId my-custom-ami-id` where
`my-custom-ami-id` is replaced by your AMI of choice.

###### Important

It can take several minutes to update the compute node group.

You can query the status of your node group with the following command.

```
aws pcs get-compute-node-group --region `region-code` \
    --cluster-identifier `my-cluster` \
    --compute-node-group-identifier `my-node-group`
```
