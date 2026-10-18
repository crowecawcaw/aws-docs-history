

# Update the scheduler version of an AWS PCS cluster
<a name="working-with_clusters_version_update_procedure"></a>

Use these steps to update the scheduler version on your cluster. There are two options depending on whether you can tolerate job interruption. For more information about choosing between options, see [Updating the scheduler version of a cluster in AWS PCS](working-with_clusters_version_update.md).

**Note**  
We recommend that you test the new AMI and the update procedure on a non-production cluster before you apply changes to your production environment.

## Option 1: Rolling update
<a name="version_update-procedure-option1"></a>

The controller is updated while the fleet keeps running. Existing nodes continue using the previous Slurm version until they are drained and replaced. New nodes launched after the update use the target version. Running jobs are not interrupted.

**When to use:**
+ The cluster controller is on Slurm version 24.05 or later.
+ You can provide AMIs that include both the current and target Slurm versions.

### Step 0 — Check starting state
<a name="version_update-procedure-option1-step0"></a>

Your cluster is running controller version "A" (e.g. 24.11) and you want to migrate to version "B" (e.g. 25.11). Confirm all compute nodes in your fleet run the same major version, using this command from a cluster node:

```
sinfo -N -o "%N %T %v"

# Example output:
#   NODELIST    STATE VERSION
#   compute-1   idle  24.11.7
#   compute-2   idle  24.11.7
```

Confirm the AWS PCS agent version on a compute node. Connect to the node with Systems Manager and check the bootstrap log:

```
grep "PCS Agent version" /var/log/amazon/pcs/bootstrap.log | tail -1

# Example output:
#   /opt/aws/pcs/bin/pcs_bootstrap_init.sh: INFO: Bootstrap starting with PCS Agent version: 1.3.2-1
```

Rolling updates require AWS PCS agent version 1.5.1-1 or later on all compute node AMIs. For more information, see [AWS PCS agent versions](pcs-agent-versions.md).

### Step 1 — Prepare and roll out the dual-version AMIs
<a name="version_update-procedure-option1-step1"></a>

Build or identify AMIs that include **both Slurm version A and version B, and the latest AWS PCS agent**.
+ You can use the latest **PCS-ready DLAMIs**. Such AMIs ship with the latest three supported Slurm versions. For more information, see [Using PCS-ready DLAMI with AWS PCS](working-with_ami_pcs-ready-dlami.md).
+ You can build a **custom AMI**, following the installation steps for Slurm packages and AWS PCS agent. For more information, see [Custom Amazon Machine Images (AMIs) for AWS PCS](working-with_ami_custom.md).
+ We do not recommend the **AWS PCS sample AMI** for production use. These AMIs are for testing only.

**Note**  
If your AMI includes more than one Slurm version, AWS PCS automatically selects the version that matches the controller. Having additional versions installed does not cause issues.

Once the AMIs are ready:

1. Call `UpdateComputeNodeGroup` on each compute node group to set the new dual-version AMI. Nodes will be set into DRAIN by AWS PCS and will migrate to the new AMI.

------
#### [ AWS Management Console ]

   1. Open the AWS PCS console at [https://console.aws.amazon.com/pcs/](https://console.aws.amazon.com/pcs/).

   1. In the navigation pane, choose **Clusters**, and then select the cluster.

   1. Choose **Compute node groups**, select the compute node group to update, and choose **Edit**.

   1. Under **Computing configuration**, enter the ID of the dual-version AMI in **AMI ID**.

   1. Choose **Update**. The compute node group shows as `UPDATING` while the change is applied.

   1. Repeat these steps for each compute node group in the cluster.

------
#### [ AWS CLI ]

   Run the following command for each compute node group in the cluster:

   ```
   aws pcs update-compute-node-group \
     --cluster-identifier {{cluster-id}} \
     --compute-node-group-identifier {{cng-id}} \
     --ami-id {{new-ami-id}}
   ```

------

1. Wait for drained nodes to complete their jobs, terminate, and be replaced by nodes using the new dual-version AMI. Check all EC2 instances in the cluster are using the new AMI with:

   ```
   aws ec2 describe-instances \
       --filters "Name=tag:aws:pcs:cluster-id,Values={{cluster-id}}" \
       --query "Reservations[].Instances[].[InstanceId,ImageId,State.Name]" \
       --output table
   ```

### Step 2 — Update the cluster controller
<a name="version_update-procedure-option1-step2"></a>

Call `UpdateCluster` with `scheduler.version` set to version B.

------
#### [ AWS Management Console ]

1. Open the AWS PCS console at [https://console.aws.amazon.com/pcs/](https://console.aws.amazon.com/pcs/).

1. In the navigation pane, choose **Clusters**.

1. Select the cluster to update and choose **Edit**.

1. Under **Cluster details**, select the target scheduler version from the **Scheduler** dropdown.

1. Choose **Update** to submit the version update.

1. Monitor the cluster status. The cluster shows as `UPDATING` during the update and returns to `ACTIVE` when complete. The update typically completes in 5–15 minutes.

------
#### [ AWS CLI ]

```
aws pcs update-cluster \
  --cluster-identifier {{cluster-id}} \
  --scheduler version={{25.11}}
```

Wait for the cluster to return to `ACTIVE`. The update typically completes in 5–15 minutes.

------

During this operation the controller is briefly unavailable:
+ Running jobs on compute nodes **continue executing**.
+ New job submissions and scheduler commands are unavailable until the update completes.
+ Automatic scaling is paused until the cluster returns to `ACTIVE`.

After the update, the compute fleet is in a **mixed state**: nodes running before the update continue using Slurm version A's `slurmd`; new nodes use Slurm version B. This is expected.

**Note**  
Do not add Slurm settings specific to version B while the fleet still contains nodes on version A. Configuration is distributed to all nodes; the old `slurmd` may not recognize new parameters.

If the cluster does not return to `ACTIVE` or `UPDATE_FAILED` within 30 minutes, contact AWS Support for assistance.

### Step 3 — Drain nodes still running Slurm version A
<a name="version_update-procedure-option1-step3"></a>

Identify and drain nodes still on the previous version. From a node of the cluster, list each node with its state and Slurm version:

```
sinfo -N -o "%N %T %v"
```

For each node that still reports version A, run the following command. Use the node name from the `NODELIST` column. The EC2 host name isn't a valid Slurm node name.

```
scontrol update NodeName={{node}} State=POWER_DOWN_ASAP Reason="Slurm version update"
```

Once drained nodes finish their current jobs they terminate and are replaced by nodes on Slurm version B.

### Step 4 — Verify consistent fleet on Slurm version B
<a name="version_update-procedure-option1-step4"></a>

Monitor the fleet until all nodes report Slurm version B. From a node of the cluster, run:

```
sinfo -N -o "%N %T %v"
```

While nodes are recycled they pass through the `DRAINING`, `POWERING_DOWN`, and `POWERED_DOWN` states. A node in the `POWERED_DOWN` state (shown with a `~` suffix, such as `idle~`) isn't running. Until AWS PCS launches it again, it shows the version that it last ran, or `N/A` if it has never launched. The update is complete when no nodes remain in a `DRAIN`, `DRAINING`, or `POWERING_DOWN` state and every node that isn't powered down reports version B.

## Option 2: Full-fleet maintenance stop
<a name="version_update-procedure-option2"></a>

You terminate the entire fleet before updating the controller, then scale it back up from a new AMI with the target Slurm version. This procedure is simpler, but it terminates all nodes and running jobs.

**When to use:**
+ The cluster controller is on version 23.11 (Option 1 is unavailable for 23.11 clusters).

**Note**  
Terminating the entire fleet at once increases the likelihood of insufficient capacity errors when scaling back up. Consider using reserved capacity or scheduling during off-peak hours.

### Step 0 — Check starting state
<a name="version_update-procedure-option2-step0"></a>

Your cluster is running controller version "A" (e.g. 24.11) and you want to migrate to version "B" (e.g. 25.11). Confirm all compute nodes in your fleet run the same major version, using this command from a cluster node:

```
sinfo -N -o "%N %T %v"

# Example output:
#   NODELIST    STATE VERSION
#   compute-1   idle  24.11.7
#   compute-2   idle  24.11.7
```

Confirm the AWS PCS agent version on a compute node. Connect to the node with Systems Manager and check the bootstrap log:

```
grep "PCS Agent version" /var/log/amazon/pcs/bootstrap.log | tail -1

# Example output:
#   /opt/aws/pcs/bin/pcs_bootstrap_init.sh: INFO: Bootstrap starting with PCS Agent version: 1.3.2-1
```

Use the latest AWS PCS agent on your target AMIs. For more information, see [AWS PCS agent versions](pcs-agent-versions.md).

### Step 1 — Prepare the target AMIs
<a name="version_update-procedure-option2-step1"></a>

Build or identify AMIs that include **Slurm version B and the latest AWS PCS agent**.
+ You can use the latest **PCS-ready DLAMIs**. Such AMIs ship with the latest three supported Slurm versions. For more information, see [Using PCS-ready DLAMI with AWS PCS](working-with_ami_pcs-ready-dlami.md).
+ You can build a **custom AMI**, following the installation steps for Slurm packages and AWS PCS agent. For more information, see [Custom Amazon Machine Images (AMIs) for AWS PCS](working-with_ami_custom.md).
+ We do not recommend the **AWS PCS sample AMI** for production use. These AMIs are for testing only.

### Step 2 — Scale down the entire fleet
<a name="version_update-procedure-option2-step2"></a>

Record the current `minNodeCount` and `maxNodeCount` for each compute node group — you will restore these in Step 4.

```
for cng in $(aws pcs list-compute-node-groups --cluster-identifier {{cluster-id}} --query "computeNodeGroups[].id" --output text); do
    aws pcs get-compute-node-group \
      --cluster-identifier {{cluster-id}} \
      --compute-node-group-identifier "$cng" \
      --query "computeNodeGroup.{Id:id,AmiId:amiId,Min:scalingConfiguration.minInstanceCount,Max:scalingConfiguration.maxInstanceCount}" \
      --output table
  done
```

**Warning**  
The following operation terminates all running nodes and the jobs on them.

Set `minNodeCount` and `maxNodeCount` to `0` on every compute node group:

```
aws pcs update-compute-node-group \
  --cluster-identifier {{cluster-id}} \
  --compute-node-group-identifier {{cng-id}} \
  --scaling-configuration '{"minNodeCount": 0, "maxNodeCount": 0}'
```

Verify no instances tagged `aws:pcs:cluster-id` matching your cluster are running before continuing:

```
aws ec2 describe-instances \
    --filters "Name=tag:aws:pcs:cluster-id,Values={{cluster-id}}" \
    --query "Reservations[].Instances[].[InstanceId,ImageId,State.Name]" \
    --output table
```

### Step 3 — Update the cluster controller
<a name="version_update-procedure-option2-step3"></a>

------
#### [ AWS Management Console ]

1. Open the AWS PCS console at [https://console.aws.amazon.com/pcs/](https://console.aws.amazon.com/pcs/).

1. In the navigation pane, choose **Clusters**.

1. Select the cluster to update and choose **Edit**.

1. Under **Cluster details**, select the target scheduler version from the **Scheduler** dropdown.

1. Choose **Update** to submit the version update.

1. Monitor the cluster status. The cluster shows as `UPDATING` during the update and returns to `ACTIVE` when complete. The update typically completes in 5–15 minutes.

------
#### [ AWS CLI ]

```
aws pcs update-cluster \
  --cluster-identifier {{cluster-id}} \
  --scheduler version={{25.11}}
```

Wait for the cluster to return to `ACTIVE`. The update typically completes in 5–15 minutes.

If the cluster does not return to `ACTIVE` or `UPDATE_FAILED` within 30 minutes, contact AWS Support for assistance.

------

### Step 4 — Update compute node groups and restore capacity
<a name="version_update-procedure-option2-step4"></a>

For each compute node group, set the new AMI and restore the original minimum and maximum capacity limits:

```
aws pcs update-compute-node-group \
  --cluster-identifier {{cluster-id}} \
  --compute-node-group-identifier {{cng-id}} \
  --ami-id {{new-ami-id}} \
  --scaling-configuration '{"minNodeCount": {{previous-min}}, "maxNodeCount": {{previous-max}}}'
```

The cluster scales back up. All new nodes run Slurm version B with the latest AWS PCS agent.

## Example: Updating across multiple versions
<a name="version_update-procedure-multi-hop"></a>

If the target version is outside the compatibility window of your current version, you must move the controller through one or more intermediate versions, updating it one hop at a time. Each hop must target a supported version within the compatibility window of the current controller version.

Because [Option 2: Full-fleet maintenance stop](#version_update-procedure-option2) scales the fleet to zero before updating the controller, no compute nodes are running while the controller moves between versions. As a result, your AMIs can use the **final** target version directly — only the controller update (Step 3) is repeated for each hop.

The following example updates a cluster from **23.11 to 25.11** using the Option 2 procedure. 23.11 is outside the compatibility window of 25.11, so the controller is updated in two hops (23.11 to 25.05, then 25.05 to 25.11). Follow the Option 2 steps, with Step 3 split into one update per hop:

1. **Step 1 — Prepare the target AMIs.** Build or identify AMIs with the **final** version (25.11) and the latest AWS PCS agent. See [Step 1 — Prepare the target AMIs](#version_update-procedure-option2-step1).

1. **Step 2 — Scale down the entire fleet.** Record current capacity (see [Step 2 — Scale down the entire fleet](#version_update-procedure-option2-step2)), then set every compute node group to zero.

   ```
   aws pcs update-compute-node-group \
   --cluster-identifier {{my-cluster}} \
   --compute-node-group-identifier {{my-cng}} \
   --scaling-configuration '{"minNodeCount": 0, "maxNodeCount": 0}'
   ```

1. **Step 3a — Update the controller from 23.11 to 25.05.** Wait for the cluster to return to `ACTIVE`.

   ```
   aws pcs update-cluster --cluster-identifier {{my-cluster}} \
   --scheduler version=25.05
   ```

1. **Step 3b — Update the controller from 25.05 to 25.11.** Wait for the cluster to return to `ACTIVE`.

   ```
   aws pcs update-cluster --cluster-identifier {{my-cluster}} \
   --scheduler version=25.11
   ```

1. **Step 4 — Update compute node groups and restore capacity.** Set the 25.11 AMI on each compute node group and restore the original capacity limits (see [Step 4 — Update compute node groups and restore capacity](#version_update-procedure-option2-step4)).

   ```
   aws pcs update-compute-node-group \
   --cluster-identifier {{my-cluster}} \
   --compute-node-group-identifier {{my-cng}} \
   --ami-id {{ami-0123456789abcdef0}} \
   --scaling-configuration '{"minNodeCount": {{previous-min}}, "maxNodeCount": {{previous-max}}}'
   ```

**Note**  
Each controller hop must land on a version within the compatibility window of the previous one. To find valid intermediate versions, see [Version compatibility](working-with_clusters_version_update.md#version_update-cluster-compatibility). The fleet remains at zero through Steps 3a and 3b, so no intermediate AMI updates are required.