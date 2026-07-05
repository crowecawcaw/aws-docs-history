# Update the scheduler version of an AWS PCS cluster

Use these steps to update the scheduler version on your cluster. There are two options depending on whether you can tolerate job interruption. For more information about choosing between options, see [Updating the scheduler version of a cluster in AWS PCS](working-with_clusters_version_update.md "working-with_clusters_version_update.md").

## Option 1: Rolling update

The controller is updated while the fleet keeps running. Existing nodes continue using the previous Slurm version until they are drained and replaced. New nodes launched after the update use the target version. Running jobs are not interrupted.

**When to use:**

- The cluster controller is on Slurm version 24.05 or later.
- You can provide AMIs that include both the current and target Slurm versions.

### Step 0 — Check starting state

Your cluster is running controller version "A" (e.g. 24.11) and you want to migrate to version "B" (e.g. 25.11). Confirm all compute nodes in your fleet run the same major version, using this command from a cluster node:

```
scontrol show nodes | grep "Version="

# Example output:
#   NodeAddr=compute-1 NodeHostName=compute-1 Version=24.11.7
#   NodeAddr=compute-2 NodeHostName=compute-2 Version=24.11.7
```

Confirm the AWS PCS agent version on a compute node. Connect to the node with Systems Manager and check the bootstrap log:

```
grep "PCS Agent version" /var/log/amazon/pcs/bootstrap.log | tail -1

# Example output:
#   /opt/aws/pcs/bin/pcs_bootstrap_init.sh: INFO: Bootstrap starting with PCS Agent version: 1.3.2-1
```

Rolling updates require AWS PCS agent version 1.4.0 or later on all compute node AMIs. For more information, see [AWS PCS agent versions](pcs-agent-versions.md "pcs-agent-versions.md").

### Step 1 — Prepare and roll out the dual-version AMIs

Build or identify AMIs that include **both Slurm version A and version B, and the latest AWS PCS agent**.

- You can use the latest **PCS-ready DLAMIs**. Such AMIs ship with the latest three supported Slurm versions. For more information, see [Using PCS-ready DLAMI with AWS PCS](working-with_ami_pcs-ready-dlami.md "working-with_ami_pcs-ready-dlami.md").
- You can build a **custom AMI**, following the installation steps for Slurm packages and AWS PCS agent. For more information, see [Custom Amazon Machine Images (AMIs) for AWS PCS](working-with_ami_custom.md "working-with_ami_custom.md").
- You **cannot** use a **AWS PCS sample AMI**. Such AMIs are not designed for production and currently include only a single Slurm version.

###### Note

If your AMI includes more than two Slurm versions, AWS PCS automatically selects the version that matches the controller. Having additional versions installed does not cause issues.

Once the AMIs are ready:

1. Call `UpdateComputeNodeGroup` on each compute node group to set the new dual-version AMI. Nodes will be set into DRAIN by AWS PCS and will migrate to the new AMI.
2. Wait for drained nodes to complete their jobs, terminate, and be replaced by nodes using the new dual-version AMI. Check all EC2 instances in the cluster are using the new AMI with:

```
aws ec2 describe-instances \
    --filters "Name=tag:aws:pcs:cluster-id,Values=`cluster-id`" \
    --query "Reservations[].Instances[].[InstanceId,ImageId,State.Name]" \
    --output table
```

### Step 2 — Update the cluster controller

Call `UpdateCluster` with `scheduler.version` set to version B.

AWS Management Console

1. Open the AWS PCS console at [https://console.aws.amazon.com/pcs/](https://console.aws.amazon.com/pcs/ "https://console.aws.amazon.com/pcs/").
2. In the navigation pane, choose **Clusters**.
3. Select the cluster to update and choose **Edit**.
4. Under **Cluster details**, select the target scheduler version from the **Scheduler** dropdown.
5. Choose **Update** to submit the version update.
6. Monitor the cluster status. The cluster shows as `UPDATING` during the update and returns to `ACTIVE` when complete. The update typically completes in 5–15 minutes.

AWS CLI

```
aws pcs update-cluster \
  --cluster-identifier `cluster-id` \
  --scheduler version=`25.11`
```

Wait for the cluster to return to `ACTIVE`. The update typically completes in 5–15 minutes.

During this operation the controller is briefly unavailable:

- Running jobs on compute nodes **continue executing**.
- New job submissions and scheduler commands are unavailable until the update completes.
- Automatic scaling is paused until the cluster returns to `ACTIVE`.

After the update, the compute fleet is in a **mixed state**: nodes running before the update continue using Slurm version A's `slurmd`; new nodes use Slurm version B. This is expected.

###### Note

Do not add Slurm settings specific to version B while the fleet still contains nodes on version A. Configuration is distributed to all nodes; the old `slurmd` may not recognize new parameters.

If the cluster does not return to `ACTIVE` or `UPDATE_FAILED` within 30 minutes, contact AWS Support for assistance.

### Step 3 — Drain nodes still running Slurm version A

Identify and drain nodes still on the previous version. From a node of the cluster, run:

```
scontrol show nodes | grep "Version="
scontrol update NodeName=`node` State=DRAIN Reason="Slurm version update"
```

Once drained nodes finish their current jobs they terminate and are replaced by nodes on Slurm version B.

### Step 4 — Verify consistent fleet on Slurm version B

Confirm all nodes report version B. From a node of the cluster, run:

```
scontrol show nodes | grep "Version="
```

All nodes should now report Slurm version B. The update is complete.

## Option 2: Full-fleet recycle

The entire fleet is terminated before the controller is updated, then scaled back up from a new AMI with the target Slurm version. This procedure is simpler, but requires all nodes and running jobs to be terminated.

**When to use:**

- You cannot provide AMIs with both Slurm versions installed.
- The cluster controller is on version 23.11 (Option 1 is unavailable for 23.11 clusters).

###### Note

Terminating the entire fleet at once increases the likelihood of insufficient capacity errors when scaling back up. Consider using reserved capacity or scheduling during off-peak hours.

### Step 0 — Check starting state

Your cluster is running controller version "A" (e.g. 24.11) and you want to migrate to version "B" (e.g. 25.11). Confirm all compute nodes in your fleet run the same major version, using this command from a cluster node:

```
scontrol show nodes | grep "Version="

# Example output:
#   NodeAddr=compute-1 NodeHostName=compute-1 Version=24.11.7
#   NodeAddr=compute-2 NodeHostName=compute-2 Version=24.11.7
```

Confirm the AWS PCS agent version on a compute node. Connect to the node with Systems Manager and check the bootstrap log:

```
grep "PCS Agent version" /var/log/amazon/pcs/bootstrap.log | tail -1

# Example output:
#   /opt/aws/pcs/bin/pcs_bootstrap_init.sh: INFO: Bootstrap starting with PCS Agent version: 1.3.2-1
```

Use the latest AWS PCS agent on your target AMIs. For more information, see [AWS PCS agent versions](pcs-agent-versions.md "pcs-agent-versions.md").

### Step 1 — Prepare the target AMIs

Build or identify AMIs that include **Slurm version B and the latest AWS PCS agent**.

- You can use the latest **PCS-ready DLAMIs**. Such AMIs ship with the latest three supported Slurm versions. For more information, see [Using PCS-ready DLAMI with AWS PCS](working-with_ami_pcs-ready-dlami.md "working-with_ami_pcs-ready-dlami.md").
- You can build a **custom AMI**, following the installation steps for Slurm packages and AWS PCS agent. For more information, see [Custom Amazon Machine Images (AMIs) for AWS PCS](working-with_ami_custom.md "working-with_ami_custom.md").
- Using the **AWS PCS sample AMI is not recommended**. Such AMIs are not designed for production.

### Step 2 — Scale down the entire fleet

Record the current `minNodeCount` and `maxNodeCount` for each compute node group — you will restore these in Step 4.

```
for cng in $(aws pcs list-compute-node-groups --cluster-identifier `cluster-id` --query "computeNodeGroups[].id" --output text); do
    aws pcs get-compute-node-group \
      --cluster-identifier `cluster-id` \
      --compute-node-group-identifier "$cng" \
      --query "computeNodeGroup.{Id:id,AmiId:amiId,Min:scalingConfiguration.minInstanceCount,Max:scalingConfiguration.maxInstanceCount}" \
      --output table
  done
```

###### Warning

The following operation terminates all running nodes and the jobs on them.

Set `minNodeCount` and `maxNodeCount` to `0` on every compute node group:

```
aws pcs update-compute-node-group \
  --cluster-identifier `cluster-id` \
  --compute-node-group-identifier `cng-id` \
  --scaling-configuration '{"minNodeCount": 0, "maxNodeCount": 0}'
```

Verify no instances tagged `aws:pcs:cluster-id` matching your cluster are running before continuing:

```
aws ec2 describe-instances \
    --filters "Name=tag:aws:pcs:cluster-id,Values=`cluster-id`" \
    --query "Reservations[].Instances[].[InstanceId,ImageId,State.Name]" \
    --output table
```

### Step 3 — Update the cluster controller

AWS Management Console

1. Open the AWS PCS console at [https://console.aws.amazon.com/pcs/](https://console.aws.amazon.com/pcs/ "https://console.aws.amazon.com/pcs/").
2. In the navigation pane, choose **Clusters**.
3. Select the cluster to update and choose **Edit**.
4. Under **Cluster details**, select the target scheduler version from the **Scheduler** dropdown.
5. Choose **Update** to submit the version update.
6. Monitor the cluster status. The cluster shows as `UPDATING` during the update and returns to `ACTIVE` when complete. The update typically completes in 5–15 minutes.

AWS CLI

```
aws pcs update-cluster \
  --cluster-identifier `cluster-id` \
  --scheduler version=`25.11`
```

Wait for the cluster to return to `ACTIVE`. The update typically completes in 5–15 minutes.

If the cluster does not return to `ACTIVE` or `UPDATE_FAILED` within 30 minutes, contact AWS Support for assistance.

### Step 4 — Update compute node groups and restore capacity

For each compute node group, set the new AMI and restore the original minimum and maximum capacity limits:

```
aws pcs update-compute-node-group \
  --cluster-identifier `cluster-id` \
  --compute-node-group-identifier `cng-id` \
  --ami-id `new-ami-id` \
  --scaling-configuration '{"minNodeCount": `previous-min`, "maxNodeCount": `previous-max`}'
```

The cluster scales back up. All new nodes run Slurm version B with the latest AWS PCS agent.

## Example: Updating across multiple versions

If the target version is outside the compatibility window of your current version, you must move the controller through one or more intermediate versions, updating it one hop at a time. Each hop must target a supported version within the compatibility window of the current controller version.

Because [Option 2: Full-fleet recycle](#version_update-procedure-option2 "#version_update-procedure-option2") scales the fleet to zero before updating the controller, no compute nodes are running while the controller moves between versions. As a result, your AMIs can use the **final** target version directly — only the controller update (Step 3) is repeated for each hop.

The following example updates a cluster from **23.11 to 25.11** using the Option 2 procedure. 23.11 is outside the compatibility window of 25.11, so the controller is updated in two hops (23.11 to 25.05, then 25.05 to 25.11). Follow the Option 2 steps, with Step 3 split into one update per hop:

1. **Step 1 — Prepare the target AMIs.** Build or identify AMIs with the **final** version (25.11) and the latest AWS PCS agent. See [Step 1 — Prepare the target AMIs](#version_update-procedure-option2-step1 "#version_update-procedure-option2-step1").
2. **Step 2 — Scale down the entire fleet.** Record current capacity (see [Step 2 — Scale down the entire fleet](#version_update-procedure-option2-step2 "#version_update-procedure-option2-step2")), then set every compute node group to zero.

```
aws pcs update-compute-node-group \
--cluster-identifier `my-cluster` \
--compute-node-group-identifier `my-cng` \
--scaling-configuration '{"minNodeCount": 0, "maxNodeCount": 0}'
```

3. **Step 3a — Update the controller from 23.11 to 25.05.** Wait for the cluster to return to `ACTIVE`.

```
aws pcs update-cluster --cluster-identifier `my-cluster` \
--scheduler version=25.05
```

4. **Step 3b — Update the controller from 25.05 to 25.11.** Wait for the cluster to return to `ACTIVE`.

```
aws pcs update-cluster --cluster-identifier `my-cluster` \
--scheduler version=25.11
```

5. **Step 4 — Update compute node groups and restore capacity.** Set the 25.11 AMI on each compute node group and restore the original capacity limits (see [Step 4 — Update compute node groups and restore capacity](#version_update-procedure-option2-step4 "#version_update-procedure-option2-step4")).

```
aws pcs update-compute-node-group \
--cluster-identifier `my-cluster` \
--compute-node-group-identifier `my-cng` \
--ami-id `ami-0123456789abcdef0` \
--scaling-configuration '{"minNodeCount": `previous-min`, "maxNodeCount": `previous-max`}'
```

###### Note

Each controller hop must land on a version within the compatibility window of the previous one. To find valid intermediate versions, see [Version compatibility](working-with_clusters_version_update.md#version_update-cluster-compatibility "working-with_clusters_version_update.md#version_update-cluster-compatibility"). The fleet remains at zero through Steps 3a and 3b, so no intermediate AMI updates are required.
