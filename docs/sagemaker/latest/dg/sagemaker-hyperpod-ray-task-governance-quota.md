# Quota and scheduling behavior for Ray workloads

Task Governance accounts quota at `RayCluster` granularity. A cluster reserves
quota for its full declared size when it is admitted, and holds that quota for its whole
lifetime regardless of load. A long-lived cluster that sits idle still counts against your
team quota until you delete it.

## Gang scheduling

Task Governance admits the head and all workers together. A `RayCluster` is
not admitted until quota exists for the entire declared size, so a partially scheduled
cluster never starts.

## Preemption

When higher-priority work needs capacity, Task Governance preempts a lower-priority
Ray workload. Preemption deletes the whole cluster, including the head.
