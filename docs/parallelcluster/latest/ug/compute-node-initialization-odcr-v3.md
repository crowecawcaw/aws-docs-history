# I configured on demand capacity reservations (ODCRs) or zonal Reserved Instances

## ODCRs that include instances that have multiple network interfaces, such as P4d,

P4de, and AWS Trainium (Trn)

In the cluster configuration file, check that the `HeadNode` is in a public subnet and that the compute nodes are in a private
subnet.

## ODCRs are targeted ODCRS

### Seeing `Unable to read file '/opt/slurm/etc/pcluster/run_instances_overrides.json'.`

even though I already have `/opt/slurm/etc/pcluster/run_instances_overrides.json` in place by following the instructions given in
[Launch instances with On-Demand Capacity Reservations (ODCR)](launch-instances-odcr-v3.md "launch-instances-odcr-v3.md")

If you are using AWS ParallelCluster versions 3.1.1 to 3.2.1 with targeted ODCRs, and you are also using the [run instances override JSON file](launch-instances-odcr-v3.md "launch-instances-odcr-v3.md"), it's possible that you don’t have the JSON file formatted
correctly. You could see an error in `clustermgtd.log`, such as the following:

```
Unable to read file '/opt/slurm/etc/pcluster/run_instances_overrides.json'.
Using default: {} in  /var/log/parallelcluster/clustermgtd.
```

Validate that the JSON file format is correct by running the following:

```
`$` `echo /opt/slurm/etc/pcluster/run_instances_overrides.json | jq`
```

### Seeing `Found RunInstances parameters override.`

in `clustermgtd.log` when cluster creation failed, or in `slurm_resume.log` when run job failed

If you are using [run instances override JSON file](launch-instances-odcr-v3.md "launch-instances-odcr-v3.md"), check that you correctly set the queue
name and the compute resources name in the `/opt/slurm/etc/pcluster/run_instances_overrides.json` file.

### Seeing `An error occurred (InsufficientInstanceCapacity)` in `slurm_resume.log`

when I fail to a run job, or in `clustermgtd.log` when I fail to create a cluster

#### Using PG-ODCR (Placement Group ODCR)

When creating an ODCR with an associated placement group, the same placement group name must be used in the configuration file. Set the
corresponding [placement group name](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup "Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup") in the cluster
configuration.

#### Using zonal Reserved Instances

If you are using zonal Reserved Instances with `PlacementGroup` / `Enabled` to `true` in the cluster
configuration, you might see an error, such as the following:

```
We currently do not have sufficient trn1.32xlarge capacity in the Availability Zone you requested (us-east-1d). Our system will be working on provisioning additional capacity.
You can currently get trn1.32xlarge capacity by not specifying an Availability Zone in your request or choosing us-east-1a, us-east-1b, us-east-1c, us-east-1e, us-east-1f.
```

You might see this because the zonal Reserved Instances aren't placed in the same UC (or spine), which can cause insufficient capacity
errors (ICEs) when using placement groups. You can check this case by disabling the `PlacementGroup`Group setting in the cluster
configuration to determine if the cluster can allocate the instances.
