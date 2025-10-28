# Scenario 2: Spot Instance running single node jobs is

interrupted

The job fails with a state code of `NODE_FAIL`, and the job is requeued (unless
`--no-requeue` is specified when the job is submitted). If the node is a static node, it's replaced.
If the node is a dynamic node, the node is terminated and reset. For more information about `sbatch`,
including the `--no-requeue` parameter, see [sbatch](https://slurm.schedmd.com/sbatch.html "https://slurm.schedmd.com/sbatch.html") in the _Slurm documentation_.
