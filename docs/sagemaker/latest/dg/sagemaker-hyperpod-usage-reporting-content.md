# Reports details and data

breakdown

SageMaker HyperPod's usage reports provide two distinct lenses for analyzing compute
resource consumption: **summary reports** for cost
allocation and **detailed reports** for granular auditing.
Summary reports aggregate cluster-wide usage by team or namespace, highlighting trends
in allocated versus borrowed compute across GPU, CPU, and Neuron Core resources.
Detailed reports drill into individual tasks, exposing metrics such as execution
windows, task status, and priority-class utilization. In this section, we break down the
structure of these reports, understand their key metrics, and demonstrate how
administrators and finance teams can cross-reference summary trends with task-level data
to validate cost attribution accuracy, resolve discrepancies, and optimize shared
infrastructure.

## Common report

headers

Both summary and detailed reports include the following metadata to contextualize
the usage data:

- **ClusterName:** The EKS-orchestrated
  Hyperpod cluster name where resources were consumed.
- **Type:** The report category (`Summary
Utilization Report` or `Detailed Utilization
Report`).
- **Date Generated:** When the report was
  created (e.g., `2025-04-18`).
- **Date Range (UTC):** The timeframe covered
  (e.g., `2025-04-16 to 2025-04-18`).
- **Missing data periods:** Gaps in data
  collection due to cluster downtime or monitoring issues (e.g.,
  `2025-04-16 00:00:00 to 2025-04-19 00:00:00`).

## Summary

reports

Summary reports provide a per-day high-level overview of compute resource
consumption across teams/namespaces, and instance types distinguishing between
allocated (reserved quota) and borrowed (lended pool) utilization. These reports are
ideal for invoice generation, cost attribution statements, or capacity
forecasting.

_Example: A summary report might show that Team A used 200
GPU hours—170 from their allocated quota and 30 borrowed._

Here's a structured breakdown of the key columns in a summary report:

- **Date:** The date of the reported usage
  (e.g., `2025-04-18`).
- **Namespace:** The Kubernetes namespace
  associated with the team (e.g., `hyperpod-ns-ml-team`).
- **Team:** The Owning team/department (e.g.,
  `ml-team`).
- **Instance Type:** The compute instance used
  (e.g., ml.g5.4xlarge).
- **Total/Allocated/Borrowed Utilization
  (Hours):** The breakdown of GPU, CPU, or Neuron Core usage by
  category.

Where:

    + **Total utilization = Allocated utilization +
     Borrowed utilization**
    + **Allocated utilization** is the
     actual GPU CPU, or Neuron Core hours a team has used, capped at 100%
     of their allocated quota.
    + **Borrowed utilization** is the
     actual GPU, CPU, or Neuron Core hours a team has used *beyond their allocated quota*, drawn
     from the shared cluster pool based on Task Governance priority rules
     and resource availability.

Example: 72 GPU hours total (48 allocated, 24 borrowed).

###### Note

Only total utilization is displayed for namespaces not managed by Task
Governance.

## Detailed

reports

Detailed reports provide forensic-level visibility into compute usage, breaking
down resource consumption by task, exposing granular metrics like task execution
windows, status (e.g., Succeeded, Failed), and priority-class usage. These reports
are ideal for billing discrepancies validation, or ensuring compliance with
governance policies.

Here's a structured breakdown of the key columns in a detailed report:

- **Date:** The date of the reported usage
  (e.g., `2025-04-18`).
- **Period Start/End:** Exact execution window
  (UTC) for the task. (e.g., `19:54:34`)
- **Namespace:** The Kubernetes namespace
  associated with the team (e.g., `hyperpod-ns-ml-team`).
- **Team:** The Owning team/department (e.g.,
  `ml-team`).
- **Task:** The identifier for the job/pod
  (e.g., `pytorchjob-ml-pytorch-job-2p5zt-db686`).
- **Instance:** The compute instance used
  (e.g., `ml.g5.4xlarge`).
- **Status:** Task outcome (Succeeded, Failed,
  Preempted).
- **Total Utilization:** Total consumption
  (hours and instance count) of GPU, CPU, or Neuron Core resources.
- **Priority Class:** The priority tier
  assigned (e.g., training-priority).
