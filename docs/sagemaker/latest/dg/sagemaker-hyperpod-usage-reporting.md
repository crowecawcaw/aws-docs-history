# Usage reporting for cost attribution in

SageMaker HyperPod

Usage reporting in SageMaker HyperPod EKS-orchestrated clusters provides granular visibility
into compute resource consumption. The capability allows organizations to implement
transparent cost attribution, allocating cluster costs to teams, projects, or departments
based on their actual usage. By tracking metrics such as GPU/CPU hours, and Neuron Core
utilization - captured in _both team-level aggregates and
task-specific breakdowns_ - usage reporting complements HyperPod's
[Task
Governance](sagemaker-hyperpod-eks-operate-console-ui-governance.md "sagemaker-hyperpod-eks-operate-console-ui-governance.md") functionality, ensuring fair cost distribution in shared multi-tenant
clusters by:

- Eliminating guesswork in cost allocation
- Directly linking expenses to measurable resource consumption
- Enforcing usage-based accountability in shared infrastructure environments

## Prerequisites

To use this capability:

- You need:
  - An active **SageMaker HyperPod environment**
    with a running EKS-orchestrated cluster.
  - (Strongly recommended) **Task Governance
    configured** with compute quotas and priority rules. For
    setup instructions, see [Task Governance setup](sagemaker-hyperpod-eks-operate-console-ui-governance-setup.md "sagemaker-hyperpod-eks-operate-console-ui-governance-setup.md").

- Familiarize yourself with these core concepts:
  - **Allocated compute quota:** Resources
    reserved for a team based on predefined quotas in their Task Governance
    policies. This is _guaranteed capacity_
    for their workloads.
  - **Borrowed compute:** Idle resources from
    the shared cluster pool that teams can temporarily use _beyond their allocated quota_. Borrowed
    compute is assigned dynamically based on priority rules in the Task
    Governance policies and availability of unused resources.
  - **Compute usage:** The measurement of
    resources (GPU, CPU, Neuron Core hours) consumed by a team, tracked
    as:
    - **Allocated utilization**: Usage
      within the team's quota.
    - **Borrowed utilization**: Usage
      beyond the quota, drawn from the shared pool.

  - **Cost attribution:** The process of
    allocating cluster costs to teams based on their _actual compute usage_, including both resources consumed
    within their predefined quota and resources temporarily used from the
    shared cluster pool beyond their quota.

## Reports types

HyperPod's usage reports provide varying operational granularity:

- **Summary reports** provide organization-wide
  visibility into compute usage, aggregating total GPU/CPU/Neuron Core hours per
  team (namespace) while distinguishing between _regular
  usage_ (resources from a team's allocated quota) and _borrowed compute_ (overflow capacity from shared
  pools).
- **Detailed reports** offer task-level breakdowns
  by team, tracking exact compute hours spent running specific tasks – including
  preempted tasks, hourly utilization patterns, and namespace-specific
  allocations.

###### Important

HyperPod usage reporting tracks compute utilization across _all
Kubernetes namespaces_ in a cluster—including those managed by Task
Governance, default namespaces, and namespaces created **outside
of Task Governance** (e.g., via direct Kubernetes API calls or external
tools). This infrastructure-level monitoring ensures comprehensive usage-based
accountability, preventing gaps in cost attribution for shared clusters regardless
of how namespaces are managed.

## Reports formats and time

range

Using the Python script provided in [Generate reports](sagemaker-hyperpod-usage-reporting-generate.md "sagemaker-hyperpod-usage-reporting-generate.md"), administrators can generate
usage reports on demand in CSV or PDF formats, selecting time ranges from daily
snapshots to 180-day (6-month) historical windows.

###### Note

You can configure the historical window to extend beyond the default 180-day
maximum when setting up the reporting infrastructure. For more information on
configuring the data retention period, see [Install Usage Report Infrastructure using CloudFormation](https://github.com/awslabs/sagemaker-hyperpod-usage-report/blob/main/README.md#install-usage-report-infrastructure-using-cloudformation "https://github.com/awslabs/sagemaker-hyperpod-usage-report/blob/main/README.md#install-usage-report-infrastructure-using-cloudformation").

## Illustrative use

cases

This capability addresses critical scenarios in multi-tenant AI/ML environments such
as:

1. **Cost allocation for shared clusters**: An
   administrator manages a HyperPod cluster shared by 20 teams training
   generative AI models. Using a _summary usage
   report_, they analyze daily GPU utilization over 180 days and
   discover Team A consumed 200 GPU hours of a specific instance type—170 from
   their allocated quota and 30 from borrowed compute. The administrator invoices
   Team A based on this reported usage.
2. **Auditing and dispute resolution**: A finance
   team questions cost attribution accuracy, citing inconsistencies. The
   administrator can export a _detailed task-level
   report_ to audit discrepancies. By cross-referencing timestamps,
   instance types, and preempted jobs within the team's namespace, the report
   transparently reconcile disputed usage data.
