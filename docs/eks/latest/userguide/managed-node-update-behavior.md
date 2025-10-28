**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Understand each phase of node updates

The Amazon EKS managed worker node upgrade strategy has four different phases described in the following sections.

## Setup phase

The setup phase has these steps:

1. It creates a new Amazon EC2 launch template version for the Auto Scaling Group that’s associated with your node group. The new launch template version uses the target AMI or a custom launch template version for the update.
2. It updates the Auto Scaling Group to use the latest launch template version.
3. It determines the maximum quantity of nodes to upgrade in parallel using the `updateConfig` property for the node group. The maximum unavailable has a quota of 100 nodes. The default value is one node. For more information, see the [updateConfig](../APIReference/API_UpdateNodegroupConfig.md#API_UpdateNodegroupConfig_RequestSyntax "../APIReference/API_UpdateNodegroupConfig.md#API_UpdateNodegroupConfig_RequestSyntax") property in the _Amazon EKS API Reference_.

## Scale up phase

When upgrading the nodes in a managed node group, the upgraded nodes are launched in the same Availability Zone as those that are being upgraded. To guarantee this placement, we use Amazon EC2’s Availability Zone Rebalancing. For more information, see [Availability Zone Rebalancing](../../../autoscaling/ec2/userguide/auto-scaling-benefits.md#AutoScalingBehavior.InstanceUsage "../../../autoscaling/ec2/userguide/auto-scaling-benefits.md#AutoScalingBehavior.InstanceUsage") in the _Amazon EC2 Auto Scaling User Guide_. To meet this requirement, it’s possible that we’d launch up to two instances per Availability Zone in your managed node group.

The scale up phase has these steps:

1.  It increments the Auto Scaling Group’s maximum size and desired size by the larger of either:
    - Up to twice the number of Availability Zones that the Auto Scaling Group is deployed in.
    - The maximum unavailable of upgrade.

    For example, if your node group has five Availability Zones and `maxUnavailable` as one, the upgrade process can launch a maximum of 10 nodes. However when `maxUnavailable` is 20 (or anything higher than 10), the process would launch 20 new nodes.

2.  After scaling the Auto Scaling Group, it checks if the nodes using the latest configuration are present in the node group. This step succeeds only when it meets these criteria:
    - At least one new node is launched in every Availability Zone where the node exists.
    - Every new node should be in `Ready` state.
    - New nodes should have Amazon EKS applied labels.

    These are the Amazon EKS applied labels on the worker nodes in a regular node group:

        + `eks.amazonaws.com/nodegroup-image=$amiName`
        + `eks.amazonaws.com/nodegroup=$nodeGroupName`

    These are the Amazon EKS applied labels on the worker nodes in a custom launch template or AMI node group:

        + `eks.amazonaws.com/nodegroup-image=$amiName`
        + `eks.amazonaws.com/nodegroup=$nodeGroupName`
        + `eks.amazonaws.com/sourceLaunchTemplateId=$launchTemplateId`
        + `eks.amazonaws.com/sourceLaunchTemplateVersion=$launchTemplateVersion`

3.  It marks nodes as unschedulable to avoid scheduling new Pods. It also labels nodes with `node.kubernetes.io/exclude-from-external-load-balancers=true` to remove the old nodes from load balancers before terminating the nodes.

The following are known reasons which lead to a `NodeCreationFailure` error in this phase:

**Insufficient capacity in the Availability Zone**

There is a possibility that the Availability Zone might not have capacity of requested instance types. It’s recommended to configure multiple instance types while creating a managed node group.

**EC2 instance limits in your account**

You may need to increase the number of Amazon EC2 instances your account can run simultaneously using Service Quotas. For more information, see [EC2 Service Quotas](../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md "../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md") in the _Amazon Elastic Compute Cloud User Guide for Linux Instances_.

**Custom user data**

Custom user data can sometimes break the bootstrap process. This scenario can lead to the `kubelet` not starting on the node or nodes not getting expected Amazon EKS labels on them. For more information, see [Specifying an AMI](launch-templates.md#launch-template-custom-ami "launch-templates.md#launch-template-custom-ami").

**Any changes which make a node unhealthy or not ready**

Node disk pressure, memory pressure, and similar conditions can lead to a node not going to `Ready` state.

**Each node most bootstrap within 15 minutes**

If any node takes more than 15 minutes to bootstrap and join the cluster, it will cause the upgrade to time out. This is the total runtime for bootstrapping a new node measured from when a new node is required to when it joins the cluster. When upgrading a managed node group, the time counter starts as soon as the Auto Scaling Group size increases.

## Upgrade phase

The upgrade phase behaves in two different ways, depending on the _update strategy_. There are two update strategies: **default** and **minimal**.

We recommend the default strategy in most scenarios. It creates new nodes before terminating the old ones, so that the available capacity is maintained during the upgrade phase.
The minimal strategy is useful in scenarios where you are constrained to resources or costs, for example with hardware accelerators such as GPUs. It terminating the old nodes before creating the new ones, so that total capacity never increases beyond your configured quantity.

The _default_ update strategy has these steps:

1. It increases the quantity of nodes (desired count) in the Auto Scaling Group, causing the node group to create additional nodes.
2. It randomly selects a node that needs to be upgraded, up to the maximum unavailable configured for the node group.
3. It drains the Pods from the node. If the Pods don’t leave the node within 15 minutes and there’s no force flag, the upgrade phase fails with a `PodEvictionFailure` error. For this scenario, you can apply the force flag with the `update-nodegroup-version` request to delete the Pods.
4. It cordons the node after every Pod is evicted and waits for 60 seconds. This is done so that the service controller doesn’t send any new requests to this node and removes this node from its list of active nodes.
5. It sends a termination request to the Auto Scaling Group for the cordoned node.
6. It repeats the previous upgrade steps until there are no nodes in the node group that are deployed with the earlier version of the launch template.

The _minimal_ update strategy has these steps:

1. It cordons all nodes of the node group in the beginning, so that the service controller doesn’t send any new requests to these nodes.
2. It randomly selects a node that needs to be upgraded, up to the maximum unavailable configured for the node group.
3. It drains the Pods from the selected nodes. If the Pods don’t leave the node within 15 minutes and there’s no force flag, the upgrade phase fails with a `PodEvictionFailure` error. For this scenario, you can apply the force flag with the `update-nodegroup-version` request to delete the Pods.
4. After every Pod is evicted and waits for 60 seconds, it sends a termination request to the Auto Scaling Group for the selected nodes. The Auto Scaling Group creates new nodes (same as the number of selected nodes) to replace the missing capacity.
5. It repeats the previous upgrade steps until there are no nodes in the node group that are deployed with the earlier version of the launch template.

### `PodEvictionFailure` errors during the upgrade phase

The following are known reasons which lead to a `PodEvictionFailure` error in this phase:

**Aggressive PDB**

Aggressive PDB is defined on the Pod or there are multiple PDBs pointing to the same Pod.

**Deployment tolerating all the taints**

Once every Pod is evicted, it’s expected for the node to be empty because the node is [tainted](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/ "https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/") in the earlier steps. However, if the deployment tolerates every taint, then the node is more likely to be non-empty, leading to Pod eviction failure.

## Scale down phase

The scale down phase decrements the Auto Scaling group maximum size and desired size by one to return to values before the update started.

If the Upgrade workflow determines that the Cluster Autoscaler is scaling up the node group during the scale down phase of the workflow, it exits immediately without bringing the node group back to its original size.
