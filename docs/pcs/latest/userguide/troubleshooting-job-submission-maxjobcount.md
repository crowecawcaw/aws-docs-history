# Troubleshooting job submission failures due to MaxJobCount limit

**Problem:** Job submissions fail with the following error message:

```
sbatch: error: Slurm temporarily unable to accept job, sleeping and retrying
```

This error occurs even when the number of running and pending jobs appears to be well below the cluster's job limit.

**Cause:** The `MaxJobCount` limit includes all jobs tracked by Slurm, not just running or pending jobs. Completed jobs remain in Slurm's memory for a period of time (by default, 5 minutes) before being purged. During high job throughput periods, the total count of active plus recently completed jobs can exceed the limit.

You can verify the total job count by running the following command on a cluster node:

```
scontrol show jobs | grep -c JobId
```

This shows the total number of jobs Slurm is tracking, including completed jobs awaiting purge.

**Solution:** Consider one of the following approaches:

- **Create a larger cluster** – If your workload consistently requires more concurrent jobs, create a new cluster with a larger size. For more information about cluster sizes and their limits, see [Cluster size in AWS PCS](working-with_clusters_size.md "working-with_clusters_size.md").
- **Reduce job submission rate** – Adjust your job submission scripts to submit jobs at a slower rate, allowing completed jobs time to be purged from Slurm's tracking.
