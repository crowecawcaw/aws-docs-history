# Frequently asked questions about updating clusters in AWS PCS

Get answers to common questions about updating cluster configurations in AWS PCS.

**What settings can I modify?**

You can modify accounting configuration (enable/disable managed accounting), scale-down behavior (scaleDownIdleTime parameter), and any of the supported Slurm custom settings that apply at the cluster level. You cannot modify security groups, VPC subnets, cluster size, Slurm version, or cluster name.

**Can I queue multiple updates?**

No. You must wait for the cluster to return to the `ACTIVE` state before submitting another update. All associated resources (Queues, Compute Node Groups) must also be in `ACTIVE` state.

**Can I cancel a cluster update operation?**

No, you cannot cancel an ongoing cluster update operation.

**Can I submit jobs while my cluster is updating?**

We recommend that you avoid submitting jobs during cluster updates. The Slurm controller might be unavailable during the update process.

**Will my jobs continue to run during cluster updates?**

Yes, running jobs continue to execute on compute nodes even when the cluster controller becomes briefly unreachable during the update process. However, job status might not update until the controller becomes available again.

**How is billing affected during updates?**

Standard hourly charges continue during update operations. When disabling accounting, billing stops when the cluster enters `UPDATING` state. When enabling accounting, billing begins when the cluster successfully returns to `ACTIVE` state.
