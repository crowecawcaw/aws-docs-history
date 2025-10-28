# What particular configurations HyperPod manages in Slurm configuration

files

When you create a Slurm cluster on HyperPod, the HyperPod agent sets
up the [`slurm.conf`](https://slurm.schedmd.com/slurm.conf.html "https://slurm.schedmd.com/slurm.conf.html") and [`gres.conf`](https://slurm.schedmd.com/gres.conf.html "https://slurm.schedmd.com/gres.conf.html") files
at `/opt/slurm/etc/` to manage the Slurm cluster based on your
HyperPod cluster creation request and lifecycle scripts. The following list
shows which specific parameters the HyperPod agent handles and overwrites.

###### Important

We strongly recommend that you **do not** change
these parameters managed by HyperPod.

- In [`slurm.conf`](https://slurm.schedmd.com/slurm.conf.html "https://slurm.schedmd.com/slurm.conf.html"), HyperPod sets up the
  following basic parameters: `ClusterName`,
  `SlurmctldHost`, `PartitionName`, and
  `NodeName`.

Also, to enable the [Automatic node
recovery and auto-resume](sagemaker-hyperpod-resiliency-slurm-auto-resume.md "sagemaker-hyperpod-resiliency-slurm-auto-resume.md") functionality, HyperPod requires the `TaskPlugin` and
`SchedulerParameters` parameters set as follows. The
HyperPod agent sets up these two parameters with the required values by
default.

```
TaskPlugin=task/none
SchedulerParameters=permit_job_expansion
```

- In [`gres.conf`](https://slurm.schedmd.com/gres.conf.html "https://slurm.schedmd.com/gres.conf.html"), HyperPod manages
  `NodeName` for GPU nodes.
