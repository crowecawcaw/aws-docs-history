

# Manage costs and usage for Deadline Cloud farms
<a name="manage-costs"></a>

Use the cost management topics to control estimated spending and capacity, review farm usage, and understand what drives your actual costs.

**Note**  
The budget manager and usage explorer show estimates based on available pricing and usage information. Use your AWS bill as the source of record for actual charges.

## Control spending and capacity
<a name="cost-concurrency-controls"></a>

Budgets are the primary Deadline Cloud control for cumulative estimated spending. Combine a budget with capacity or concurrency controls when you also need to limit peak compute usage, prevent one job from consuming the fleet, or protect a shared resource.<a name="cost-concurrency-comparison"></a>
+ <a name="cost-concurrency-budgets"></a>[Control costs with a budget](using-budget-manager.md) – Set a cumulative estimated spending limit for a queue and choose what happens when spending reaches a threshold. Use a separate queue and budget for each project, department, or vendor that needs its own spending cap.
+ <a name="cost-concurrency-fleet-max"></a><a name="cost-concurrency-spend-rate"></a>[Minimum and maximum worker counts](auto-scaling-configuration.md#auto-scaling-worker-counts) – Set the minimum and maximum workers in a fleet. The maximum worker count limits concurrent compute usage. Your actual spend rate also depends on factors such as instance types and licenses.<a name="cost-concurrency-market-options"></a>

  To combine Spot, On-Demand, or Wait and Save capacity, see [Service-managed fleets](fleet-types.md#fleet-types-smf).
+ <a name="cost-concurrency-job-max"></a><a name="cost-concurrency-priority"></a>[Control job worker limits and priority](deadline-cloud-jobs.md#jobs-scheduling-controls) – Limit the workers assigned to one job and set job priority. Use these controls to prevent one large job from consuming the fleet or to prioritize urgent work.
+ <a name="cost-concurrency-limits"></a>[Create resource limits for jobs](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/build-job-limits.html) – Limit the tasks that can use a constrained resource, such as floating software licenses or a file server with limited throughput.

### Combine controls
<a name="cost-concurrency-choosing"></a>

Use multiple controls when your workload has more than one constraint:
+ **Set a project budget and limit peak capacity.** Set a maximum worker count on each fleet and create a budget for the project's queue. The worker count limits concurrent compute usage. When cumulative estimated spending reaches a threshold, the budget either stops scheduling new tasks or also cancels running tasks, depending on the limit action that you choose.
+ **Keep a large job from delaying urgent work.** Set a maximum worker count on the large job and assign a higher priority to urgent jobs. The job limit reserves fleet capacity, and priority determines which waiting work runs first.
+ **Limit compute and software-license use.** Set the fleet's maximum worker count to cap total compute and create a resource limit that matches the number of available licenses.
+ <a name="cost-concurrency-crunch"></a>**Temporarily increase capacity for a busy period.** Before a delivery deadline, you can raise fleet worker limits, adjust the budget amount or actions, and add standby workers. Restore the previous settings after the busy period. For capacity options, see [Adjust capacity for busy periods](auto-scaling-configuration.md#auto-scaling-temporary-capacity).

## Other cost management goals
<a name="cost-management-other-goals"></a>
+ [Track usage and costs with the Deadline Cloud usage explorer](using-usage-explorer.md) – Filter farm usage and understand the estimates and cost scale factor used by the usage explorer and budgets.
+ [Understand the cost model for service-managed fleets](cost-model-smf.md) – Understand worker metering and compare the elastic service-managed fleet cost model with a traditional render farm.
+ [Understand estimated and actual costs for Deadline Cloud](cost-management.md) – See why usage explorer and budget estimates differ from actual costs, including charges from connected AWS services.