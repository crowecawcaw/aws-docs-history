AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# Task resources in a HealthOmics workflow definition

In the workflow definition, define the following for each task:

- The container image for task. For more information, see
  [Container images for private workflows](workflows-ecr.md "workflows-ecr.md").
- The number of CPUs and memory required for the task. For more information, see
  [Compute and memory requirements for HealthOmics tasks](memory-and-compute-tasks.md "memory-and-compute-tasks.md").
  HealthOmics ignores any per-task storage specifications. HealthOmics provides run
  storage that all tasks in the run can access. For more information, see
  [Run storage types in HealthOmics workflows](workflows-run-types.md "workflows-run-types.md").

WDL

```
task my_task {
   runtime {
      container: "<aws-account-id>.dkr.ecr.<aws-region>.amazonaws.com/<image-name>"
      cpu: 2
      memory: "4 GB"
   }
   ...
}
```

For a WDL workflow, HealthOmics attempts up to two retries for a task that fails because of service errors
(API request returns a 5XX HTTP status code). For more information about task retries, see
[Task Retries](monitoring-runs.md#run-status-task-retries "monitoring-runs.md#run-status-task-retries").

You can opt out of the retry behavior by specifying the following configuration for the task in the WDL definition file:

```
runtime {
   preemptible: 0
}
```

NextFlow

```
process my_task {
   container "<aws-account-id>.dkr.ecr.<aws-region>.amazonaws.com/<image-name>"
   cpus 2
   memory "4 GiB"
   ...
}
```

CWL

```
cwlVersion: v1.2
class: CommandLineTool
requirements:
    DockerRequirement:
        dockerPull: "<aws-account-id>.dkr.ecr.<aws-region>.amazonaws.com/<image-name>"
    ResourceRequirement:
        coresMax: 2
        ramMax: 4000 # specified in mebibytes

```
