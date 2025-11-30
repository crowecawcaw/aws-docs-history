# Manually

replace or reboot a node using Slurm

This section talks about when you should manually reboot or replace a node, with
instructions on how to do both.

## When to manually reboot or replace a node

The HyperPod auto-resume functionality monitors if the state of your Slurm
nodes turns to `fail` or `down`. You can check the state of Slurm
nodes by running `sinfo`.

If a node remains stuck or unresponsive and the auto-resume process does not recover it,
you can manually initiate recovery. The choice between rebooting and replacing a node depends on
the nature of the issue. Consider rebooting when facing temporary or software-related problems,
such as system hangs, memory leaks, GPU driver issues, kernel updates, or hung processes. However,
if you encounter persistent or hardware-related problems like failing GPUs, memory or networking faults,
repeated health check failures, or nodes that remain unresponsive after multiple reboot attempts,
node replacement is the more appropriate solution.

## Ways to manually reboot or replace nodes

SageMaker SageMaker HyperPod offers two methods for manual node recovery. The preferred
approach is using the SageMaker HyperPod Reboot and Replace APIs, which provides a faster and more transparent
recovery process that works across all orchestrators. Alternatively, you can use traditional Slurm commands
like `scontrol update`, though this legacy method requires direct access to the Slurm's controller node. Both
methods activate the same SageMaker HyperPod recovery processes.

## Manually reboot a node using reboot API

You can use the **BatchRebootClusterNodes** to manually
reboot a faulty node in your SageMaker HyperPod cluster.

Here is an example of running the reboot operation on two Instances of a cluster using the AWS Command Line Interface:

```
 aws sagemaker-dev batch-reboot-cluster-nodes \
                --cluster-name arn:aws:sagemaker:ap-northeast-1:123456789:cluster/test-cluster \
                --node-ids i-abc123 i-def456
```

## Manually replace a node using replace API

You can use the **BatchReplaceClusterNodes** to manually
replace a faulty node in your SageMaker HyperPod cluster.

Here is an example of running the replace operation on two Instances of a cluster using the AWS Command Line Interface:

```
 aws sagemaker-dev batch-replace-cluster-nodes \
                --cluster-name arn:aws:sagemaker:ap-northeast-1:123456789:cluster/test-cluster \
                --node-ids i-abc123 i-def456
```

## Manually reboot a node using Slurm

You can also use the scontrol Slurm commands to trigger node recovery. These commands interact
directly with the Slurm control plane and invoke the same underlying SageMaker HyperPod recovery mechanisms.

In the following command , replace <ip-ipv4> with the Slurm node name (host
name) of the faulty instance you want to reboot.

```
scontrol update node=`<ip-ipv4>` state=`fail` reason="Action:Reboot"
```

This marks the node as FAIL with the specified reason. SageMaker HyperPod detects this and reboots the instance.
Avoid changing the node state or restarting the Slurm controller during the operation.

## Manually replace a node using Slurm

You can use the scontrol update command as follows to replace a node.

In the following command, replace
`<ip-ipv4>` with the Slurm node name
(host name) of the faulty instance you want to replace.

```
scontrol update node=`<ip-ipv4>` state=`fail` reason="Action:Replace"
```

After running this command, the node will go into the `fail` state,
waits for the currently running jobs to finish, is replaced with a healthy instance,
and is recovered with the same host name. This process takes time depending on the
available instances in your Availability Zone and the time it takes to run your
lifecycle scripts. During the update and replacement processes, avoid changing the
state of the node manually again or restarting the Slurm controller; doing so can
lead to a replacement failure. If the node does not get recovered nor turn to the
`idle` state after a long time, contact [AWS Support](https://console.aws.amazon.com/support/ "https://console.aws.amazon.com/support/").

## Manually force change a node

If the faulty node is continuously stuck in the `fail` state, the last
resort you might try is to manually force change the node state to
`down`. This requires administrator privileges (sudo permissions).

###### Warning

Proceed carefully before you run the following command as it forces kill all
jobs, and you might lose all unsaved work.

```
scontrol update node=`<ip-ipv4>` state=`down` reason="Action:Replace"
```
