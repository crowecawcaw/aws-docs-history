# Frequently asked questions about updating clusters in AWS PCS

Get answers to common questions about updating cluster configurations in AWS PCS.

**What settings can I modify?**

You can modify accounting configuration (enable/disable accounting), scale-down behavior (scaleDownIdleTime parameter), the scheduler version, and any of the supported Slurm custom settings that apply at the cluster level. You cannot modify security groups, VPC subnets, cluster size, or cluster name.

**Can I queue multiple updates?**

No. You must wait for the cluster to return to the `ACTIVE` state before submitting another update. All associated resources (Queues, Compute Node Groups) must also be in `ACTIVE` state.

**Can I cancel a cluster update operation?**

No, you cannot cancel an ongoing cluster update operation.

**Can I submit jobs while my cluster is updating?**

We recommend that you avoid submitting jobs during cluster updates. The Slurm controller might be unavailable during the update process.

**Will my jobs continue to run during cluster updates?**

Yes, running jobs continue to execute on compute nodes even when the cluster controller becomes briefly unreachable during the update process. However, job status might not update until the controller becomes available again.

**How do I update standalone login nodes during a scheduler version update?**

Standalone login nodes are EC2 instances that are not managed by AWS PCS compute node groups. AWS PCS does not automatically update these instances during a scheduler version update. To update them, replace them with new instances that use an AMI containing the target Slurm version and the latest AWS PCS agent. The timing depends on which update option you use:

- **Option 1 (rolling update)** — Update login nodes after the controller update is complete and the fleet is fully on the new version.
- **Option 2 (full-fleet maintenance stop)** — Update login nodes at any point during the process.

For more information, see [Update the scheduler version of an AWS PCS cluster](working-with_clusters_version_update_procedure.md "working-with_clusters_version_update_procedure.md").

**How is billing affected during updates?**

Standard hourly charges continue during update operations. When disabling accounting, billing stops when the cluster enters `UPDATING` state. When enabling accounting, billing begins when the cluster successfully returns to `ACTIVE` state.
