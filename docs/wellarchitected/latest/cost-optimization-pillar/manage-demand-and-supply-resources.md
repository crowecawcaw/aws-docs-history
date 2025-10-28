# Manage demand and supply resources

When you move to the cloud, you pay only for what you need. You can
supply resources to match the workload demand at the time they’re
needed — eliminating the need for costly and wasteful
overprovisioning. You can also modify the demand using a throttle,
buffer, or queue to smooth the demand and serve it with less
resources.

The economic benefits of just-in-time supply should be balanced
against the need to provision to account for resource failures, high
availability, and provision time. Depending on whether your demand
is fixed or variable, plan to create metrics and automation that
will ensure that management of your environment is minimal – even as
you scale. When modifying the demand, you must know the acceptable
and maximum delay that the workload can allow.

In AWS, you can use a number of different approaches for managing
demand and supplying resources. The following best practices describe how
to use these approaches.

###### Best practices

- [COST09-BP01 Perform an analysis on the workload demand](cost_manage_demand_resources_cost_analysis.md "cost_manage_demand_resources_cost_analysis.md")
- [COST09-BP02 Implement a buffer or throttle to manage
  demand](cost_manage_demand_resources_buffer_throttle.md "cost_manage_demand_resources_buffer_throttle.md")
- [COST09-BP03 Supply resources dynamically](cost_manage_demand_resources_dynamic.md "cost_manage_demand_resources_dynamic.md")
