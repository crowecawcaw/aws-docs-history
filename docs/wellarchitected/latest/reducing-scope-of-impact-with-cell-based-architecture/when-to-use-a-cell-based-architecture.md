# When to use a cell-based architecture?

There are applications that serve such a large number of customers that interruption of
all customers is unacceptable, either for reputation, or financial reasons, where every
unavailable second has a big impact. Workloads that have the following characteristics can
benefit from a cell-based architecture:

- Applications where any downtime can have a huge negative impact on customers.
- FSI customers with workloads critical to economic stability.
- Ultra-scale systems that are too big/critical to fail.
- Less than 5 seconds of [Recovery Point Objective (RPO)](../reliability-pillar/rel_planning_for_recovery_objective_defined_recovery.md "../reliability-pillar/rel_planning_for_recovery_objective_defined_recovery.md").
- Less than 30 seconds of [Recovery Time Objective (RTO)](../reliability-pillar/rel_planning_for_recovery_objective_defined_recovery.md "../reliability-pillar/rel_planning_for_recovery_objective_defined_recovery.md").
- Multi-tenant services where some tenants require fully dedicated tenancy (meaning,
  their own dedicated cell).

A question to ponder regarding your workload is this:
_"Is it better for 100% of customers to experience a
5% failure rate, or 5% of customers to experience a 100% failure
rate?"_

Cell-based architecture will not be a good choice for all your
workloads, but it can bring great benefits for some your most
critical workloads.

Implementing a cell-based architecture is not a simple task, among
the disadvantages are:

- Increase in the complexity of the architecture due to the redundancy of infrastructure
  and components.
- High cost of infrastructure and services, although utilization
  based fee structures like Amazon EC2 Reserved Instances (RIs) and saving
  plans help close this delta.
- Requires specialized operational tools and practices to operate
  these multiple replicas (cells) of the workload.
- Necessity to invest in a cell routing layer.
