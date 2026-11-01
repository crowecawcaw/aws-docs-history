

This documentation references AWS ParallelCluster. For running HPC and AI workloads, we recommend [AWS Parallel Computing Service (AWS PCS)](https://aws.amazon.com/pcs/), our managed Slurm service that lets you focus on running your workloads rather than managing infrastructure.

# `awsbstat`
<a name="awsbatchcli.awsbstat-v3"></a>

Shows the jobs that are submitted in the cluster’s job queue.

```
awsbstat [-h] [-c {{CLUSTER}}] [-s {{STATUS}}] [-e] [-d] [{{job_ids}} [{{job_ids}} ...]]
```

## Positional Arguments
<a name="awsbatchcli.awsbstat-v3.arguments"></a>

**{{job\_ids}}**  
Specifies the space-separated list of job IDs to show in the output. If the job is a job array, all of the child jobs are displayed. If a single job is requested, it is shown in a detailed version.

## Named Arguments
<a name="awsbatchcli.awsbstat-v3.namedarguments"></a>

**-c {{CLUSTER}}, --cluster {{CLUSTER}}**  
Indicates the cluster to use.

**-s {{STATUS}}, --status {{STATUS}}**  
Specifies a comma-separated list of job statuses to include. The default job status is “active.”. Accepted values are: `SUBMITTED`, `PENDING`, `RUNNABLE`, `STARTING`, `RUNNING`, `SUCCEEDED`, `FAILED`, and `ALL`.  
Default: “`SUBMITTED`,`PENDING`,`RUNNABLE`,`STARTING`,`RUNNING`”

**-e, --expand-children**  
Expands jobs with children (both array and multi-node parallel).  
Default: False

**-d, --details**  
Shows jobs details.  
Default: False