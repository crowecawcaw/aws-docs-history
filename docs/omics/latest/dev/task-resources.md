

# Task resources in a HealthOmics workflow definition
<a name="task-resources"></a>

In the workflow definition, define the following for each task:
+ The container image for task. For more information, see [Container images for private workflows](workflows-ecr.md).
+ The number of CPUs and memory required for the task. For more information, see [Compute and memory requirements for HealthOmics tasks](memory-and-compute-tasks.md).
+ The optional per-task ephemeral storage that the task can use at `/tmp` when enabled for the run. For more information, see [Ephemeral storage for HealthOmics workflow tasks](workflows-ephemeral-storage.md).

HealthOmics provides run storage that all tasks in the run can access. For more information, see [Run storage types in HealthOmics workflows](workflows-run-types.md).

------
#### [ WDL ]

```
task my_task {
   runtime {
      container: "<aws-account-id>.dkr.ecr.<aws-region>.amazonaws.com/<image-name>"
      cpu: 2
      memory: "4 GB"
      disks: "100 GiB"                 # optional
   }
   ...
}
```

For a WDL workflow, HealthOmics attempts up to two retries for a task that fails because of service errors (API request returns a 5XX HTTP status code). For more information about task retries, see [Task Retries](monitoring-runs.md#run-status-task-retries).

You can opt out of the retry behavior by specifying the following configuration for the task in the WDL definition file:

```
runtime {
   preemptible: 0
}
```

------
#### [ NextFlow ]

```
process my_task {
   container "<aws-account-id>.dkr.ecr.<aws-region>.amazonaws.com/<image-name>"
   cpus 2
   memory "4 GiB"
   disk '100 GB'                       // optional
   ...
}
```

------
#### [ CWL ]

```
cwlVersion: v1.2
class: CommandLineTool
requirements:
    DockerRequirement:
        dockerPull: "<aws-account-id>.dkr.ecr.<aws-region>.amazonaws.com/<image-name>"
    ResourceRequirement:
        coresMax: 2
        ramMax: 4000 # specified in mebibytes
        tmpdirMin: 102400 # 100 gibibytes expressed in mebibytes
```

------