# Graceful decommission of Spot Instances

with Flink on Amazon EMR on EKS

Flink with Amazon EMR on EKS can improve the job restart time during task recovery or
scaling operations.

## Overview

Amazon EMR on EKS releases 6.15.0 and higher support graceful decommission of Task
Managers on Spot Instances in Amazon EMR on EKS with Apache Flink. As part of this feature,
Amazon EMR on EKS with Flink provides the following capabilities:

- Just-in-time checkpointing – Flink
  streaming jobs can respond to Spot Instance interruption, perform
  just-in-time (JIT) checkpoint of the running jobs, and prevent scheduling of
  additional tasks on these Spot Instances. JIT checkpoint is supported with
  default and adaptive scheduler.
- Combined restart mechanism – A
  combined restart mechanism makes a best-effort attempt to restart the job
  after it reaches target resource parallelism or the end of the current
  configured window. This also prevents consecutive job restarts that might be
  caused by multiple Spot Instance terminations. Combined restart mechanism is
  available with adaptive scheduler only.

These capabilities provide the following benefits:

- You can leverage Spot Instances to run Task Managers and reduce cluster
  expenditure.
- Improved liveness for Spot Instance Task Manager results in higher
  resilience and more efficient job scheduling.
- Your Flink jobs will have more uptime because there will be less restarts
  from Spot Instance termination.

## How graceful decommissioning works

Consider the following example: you provision an Amazon EMR on EKS cluster running Apache
Flink, and you specify On-Demand nodes for Job Manager, and Spot Instance nodes for
Task Manager. Two minutes before termination, Task Manager receives an interruption
notice.

In this scenario, the Job Manager would handle the Spot Instance interruption
signal, block scheduling of additional tasks on the Spot Instance, and initiate JIT
checkpointing for the streaming job.

Then, the Job Manager would restart the job graph only after there is sufficient
availability of new resources to satisfy current job parallelism in the current
restart interval window. The restart window interval is decided on the basis of Spot
Instance replacement duration, creation of new Task Manager pods, and registration
with Job Manager.

## Prerequisites

To use graceful decommisioning, create and run a streaming job on an Amazon EMR on EKS
cluster running Apache Flink. Enable Adaptive Scheduler and Task Managers scheduled
on at least one Spot Instance, as shown in the following example. You should use
On-Demand nodes for Job Manager, and you can use On-Demand nodes for Task Managers
as long as there's at least one Spot Instance, too.

```
apiVersion: flink.apache.org/v1beta1
kind: FlinkDeployment
metadata:
  name: `deployment_name`
spec:
  flinkVersion: v1_17
  flinkConfiguration:
    taskmanager.numberOfTaskSlots: "2"
    cluster.taskmanager.graceful-decommission.enabled: "true"
    execution.checkpointing.interval: "240s"
    jobmanager.adaptive-scheduler.combined-restart.enabled: "true"
    jobmanager.adaptive-scheduler.combined-restart.window-interval : "1m"
  serviceAccount: flink
  jobManager:
    resource:
      memory: "2048m"
      cpu: 1
    nodeSelector:
      'eks.amazonaws.com/capacityType': 'ON_DEMAND'
  taskManager:
    resource:
      memory: "2048m"
      cpu: 1
    nodeSelector:
      'eks.amazonaws.com/capacityType': 'SPOT'
  job:
    jarURI: `flink_job_jar_path`
```

## Configuration

This section covers most of the configurations that you can specify for your
decommissioning needs.

| Key                                                              | Description                                                                                                                           | Default value | Acceptable values                 |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------- | --------------------------------- |
| `cluster.taskmanager.graceful-decommission.enabled`              | Enable graceful decommission of Task Manager.                                                                                         | `true`        | `true`, `false`                   |
| `jobmanager.adaptive-scheduler.combined-restart.enabled`         | Enable combined restart mechanism in Adaptive Scheduler.                                                                              | `false`       | `true`, `false`                   |
| `jobmanager.adaptive-scheduler.combined-restart.window-interval` | The combined restart window interval to perfom merged restarts for the job. An integer without a unit is interpreted as milliseconds. | `1m`          | Examples: `30`, `60s`, `3m`, `1h` |
