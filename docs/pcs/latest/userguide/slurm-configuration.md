

# Slurm configuration in AWS PCS
<a name="slurm-configuration"></a>

AWS PCS manages the Slurm configuration of your cluster. The cluster controller holds the authoritative configuration files, which include `slurm.conf`, `cgroup.conf`, and `slurmdbd.conf`. AWS PCS generates these files from your cluster, queue, and compute node group settings, and updates them as your cluster changes.

## Configless mode
<a name="slurm-configuration-configless"></a>

AWS PCS runs Slurm in configless mode. In configless mode, nodes fetch the configuration directly from the cluster controller (`slurmctld`). For more information, see [Configless Slurm](https://slurm.schedmd.com/configless_slurm.html) on the SchedMD website.
+ On compute nodes, `slurmd` fetches the configuration from the controller when it starts.
+ On login nodes, the Slurm authentication and credential kiosk daemon (`sackd`) fetches the configuration so that client commands such as `sbatch`, `srun`, and `scontrol` can use it.

Slurm caches the files that it fetches on the node, and creates a symbolic link to them at `/run/slurm/conf`. The configuration that a node runs with is `/run/slurm/conf/slurm.conf`.

To review the configuration that a node runs with, use the following command on the node.

```
scontrol show config
```

With AWS PCS, you can configure a limited group of Slurm settings. For the settings that each configuration file supports, see the following topics.

**Topics**
+ [Configless mode](#slurm-configuration-configless)
+ [Configuring custom Slurm settings in AWS PCS](slurm-custom-settings.md)
+ [Configuring custom cgroup settings in AWS PCS](cgroup-custom-settings.md)
+ [Configuring custom SlurmDBD settings in AWS PCS](slurmdbd-custom-settings.md)
+ [Configuring custom GRES settings in AWS PCS](gres-custom-settings.md)