# Custom bootstrap actions

If you define the [HeadNode](HeadNode-v3.md "HeadNode-v3.md") /
[CustomActions](HeadNode-v3.md#HeadNode-v3-CustomActions "HeadNode-v3.md#HeadNode-v3-CustomActions") /
[OnNodeStart](HeadNode-v3.md#yaml-HeadNode-CustomActions-OnNodeStart "HeadNode-v3.md#yaml-HeadNode-CustomActions-OnNodeStart") configuration
settings, AWS ParallelCluster runs arbitrary code immediately after the node starts. If you define the
[HeadNode](HeadNode-v3.md "HeadNode-v3.md") /
[CustomActions](HeadNode-v3.md#HeadNode-v3-CustomActions "HeadNode-v3.md#HeadNode-v3-CustomActions") /
[OnNodeConfigured](HeadNode-v3.md#yaml-HeadNode-CustomActions-OnNodeConfigured "HeadNode-v3.md#yaml-HeadNode-CustomActions-OnNodeConfigured")
configuration settings, AWS ParallelCluster runs the code after the node configuration is correctly
completed.

Starting with AWS ParallelCluster version 3.4.0, the code can be run after the head node update,
if you define the [HeadNode](HeadNode-v3.md "HeadNode-v3.md") /
[CustomActions](HeadNode-v3.md#HeadNode-v3-CustomActions "HeadNode-v3.md#HeadNode-v3-CustomActions") /
[OnNodeUpdated](HeadNode-v3.md#yaml-HeadNode-CustomActions-OnNodeUpdated "HeadNode-v3.md#yaml-HeadNode-CustomActions-OnNodeUpdated")
configuration settings.

In most cases, this code is stored in Amazon Simple Storage Service (Amazon S3) and accessed through an HTTPS connection.
The code is run as `root` and can be in any script language that's supported by the cluster
OS. Often the code is in _Bash_ or _Python_.

###### Note

Starting with AWS ParallelCluster version 3.7.0, the cluster
[Imds](Imds-cluster-v3.md#Imds-cluster-v3.title "Imds-cluster-v3.md#Imds-cluster-v3.title") /
[ImdsSupport](Imds-cluster-v3.md#yaml-cluster-Imds-ImdsSupport "Imds-cluster-v3.md#yaml-cluster-Imds-ImdsSupport") default setting
is `v2.0`.

When you create a new cluster to upgrade to version 3.7.0 and later versions, either update
your custom bootstrap action scripts to be compatible with IMDSv2 or set
[Imds](Imds-cluster-v3.md#Imds-cluster-v3.title "Imds-cluster-v3.md#Imds-cluster-v3.title") /
[ImdsSupport](Imds-cluster-v3.md#yaml-cluster-Imds-ImdsSupport "Imds-cluster-v3.md#yaml-cluster-Imds-ImdsSupport") to `v1.0`
in your cluster configuration file.

###### Warning

It is your responsibility to configure the custom scripts and arguments as described in the
[Shared responsibility
model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/"). Verify that your custom bootstrap scripts and arguments are from sources that you
trust to have full access to your cluster nodes.

###### Warning

AWS ParallelCluster doesn't support the use of internal variables that are provided through the
`/etc/parallelcluster/cfnconfig` file. This file might be removed as part of
a future release.

`OnNodeStart` actions are called before any node deployment bootstrap action is
started, such as configuring NAT, Amazon Elastic Block Store (Amazon EBS) or the scheduler. `OnNodeStart`
bootstrap actions may include modifying storage, adding extra users, and adding packages.

###### Note

If you configure [DirectoryService](DirectoryService-v3.md "DirectoryService-v3.md")
and a [HeadNode](HeadNode-v3.md "HeadNode-v3.md") /
[CustomActions](HeadNode-v3.md#HeadNode-v3-CustomActions "HeadNode-v3.md#HeadNode-v3-CustomActions") /
[OnNodeStart](HeadNode-v3.md#yaml-HeadNode-CustomActions-OnNodeStart "HeadNode-v3.md#yaml-HeadNode-CustomActions-OnNodeStart") script
for your cluster, AWS ParallelCluster configures `DirectoryService` and restarts the
`sssd`, before it runs the `OnNodeStart` script.

`OnNodeConfigured` actions are called after the node bootstrap processes are complete.
`OnNodeConfigured` actions serve the last actions to occur before an instance is considered
fully configured and complete. Some `OnNodeConfigured` actions include changing scheduler
settings, modifying storage, and modifying packages. You can pass arguments to scripts by specifying
them during configuration.

`OnNodeUpdated` actions are called after the head node update is completed and the
scheduler and shared storage are aligned with the latest cluster configuration changes.

When `OnNodeStart` or `OnNodeConfigured` custom actions succeed, success is
indicated with exit code zero (0). Any other exit code indicates the instance bootstrap failed.

When `OnNodeUpdated` custom actions succeed, success is signaled with exit code zero (0).
Any other exit code indicates the update failed.

###### Note

If you configure [OnNodeUpdated](HeadNode-v3.md#yaml-HeadNode-CustomActions-OnNodeUpdated "HeadNode-v3.md#yaml-HeadNode-CustomActions-OnNodeUpdated"),
you must manually restore the `OnNodeUpdated` actions to the previous state on
update failures.

If an `OnNodeUpdated` custom action fails, the update rolls back to the previous state.
However, the `OnNodeUpdated` action is only run at update time and not at stack
rollback time.

You can specify different scripts for the head node and for each queue, in the
[HeadNode](HeadNode-v3.md "HeadNode-v3.md") /
[CustomActions](HeadNode-v3.md#HeadNode-v3-CustomActions "HeadNode-v3.md#HeadNode-v3-CustomActions") and i
[Scheduling](Scheduling-v3.md "Scheduling-v3.md") /
[SlurmQueues](Scheduling-v3.md#Scheduling-v3-SlurmQueues "Scheduling-v3.md#Scheduling-v3-SlurmQueues") /
[CustomActions](Scheduling-v3.md#Scheduling-v3-SlurmQueues-CustomActions "Scheduling-v3.md#Scheduling-v3-SlurmQueues-CustomActions")
configuration sections. [OnNodeUpdated](HeadNode-v3.md#yaml-HeadNode-CustomActions-OnNodeUpdated "HeadNode-v3.md#yaml-HeadNode-CustomActions-OnNodeUpdated")
can only be configured in the `HeadNode` section.

###### Note

Before AWS ParallelCluster version 3.0, it was not possible to specify different scripts for
head and compute nodes. Please refer to [Moving from AWS ParallelCluster 2.x to 3.x](moving-from-v2-to-v3.md "moving-from-v2-to-v3.md").

###### Topics

- [Configuration settings to define actions
  and arguments](custom-bootstrap-actions-config-v3.md "custom-bootstrap-actions-config-v3.md")
- [Arguments](custom-bootstrap-actions-args-v3.md "custom-bootstrap-actions-args-v3.md")
- [Example cluster with custom
  bootstrap actions](custom-bootstrap-actions-example-cluster-v3.md "custom-bootstrap-actions-example-cluster-v3.md")
- [Example of how to update a custom
  bootstrap script for IMDSv2](custom-bootstrap-actions-example-imdsv2-v3.md "custom-bootstrap-actions-example-imdsv2-v3.md")
- [Example of how to update a configuration
  for IMDSv1](custom-bootstrap-actions-example-imdsv1-v3.md "custom-bootstrap-actions-example-imdsv1-v3.md")
