

This documentation references AWS ParallelCluster. For running HPC and AI workloads, we recommend [AWS Parallel Computing Service (AWS PCS)](https://aws.amazon.com/pcs/), our managed Slurm service that lets you focus on running your workloads rather than managing infrastructure.

# `pcluster version`

Displays the version of AWS ParallelCluster.

```sh
pcluster version [-h] [--debug]
```

## Named arguments
<a name="pcluster-v3.version.namedargs"></a>

**-h, --help**  
Shows the help text for `pcluster version`.

**--debug**  
Enables debug logging.

**Example using AWS ParallelCluster version 3.1.4:**

```
$ pcluster version
{
  "version": "3.1.4"
}
```