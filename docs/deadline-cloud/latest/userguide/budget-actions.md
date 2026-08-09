# How budget actions affect running and new work

When spending against a budget reaches a limit you set, Deadline Cloud applies the action that
you chose for that limit. Both actions stop the queue from scheduling new tasks. They
differ in what happens to tasks that are already running on workers:

**Stop after finishing current work**
(`STOP_SCHEDULING_AND_COMPLETE_TASKS`)

The queue stops assigning new tasks to workers. Tasks that are already
running finish normally and continue to incur cost until they complete.
Choose this action to stop new spending without losing partially completed
frames.

**Immediately stop work**
(`STOP_SCHEDULING_AND_CANCEL_TASKS`)

The queue stops assigning new tasks to workers and cancels tasks that are
running, including partially completed frames. Choose this action when a
hard spending cap matters more than finishing frames that are in
flight.

You can add several limit actions to one budget at different remaining amounts. For
example, stop scheduling new work when $500 remains so that current frames finish, and
 cancel all work when $0 remains as a hard stop.

Each budget tracks the estimated cost of a single queue. To give each project,
department, or vendor its own spending cap, route each one's jobs through its own queue
and create a budget for that queue. For an overview of how budgets combine with worker
counts, resource limits, and job priority, see [Control costs and concurrency](cost-concurrency-controls.md "cost-concurrency-controls.md").

To receive notifications before a budget reaches its limit, use the EventBridge events that
Deadline Cloud sends as spending crosses each threshold percentage. For more information, see
[Monitor a budget with EventBridge events](budget-threshold-events.md "budget-threshold-events.md").

You can also create and adjust budgets programmatically with the [CreateBudget](../APIReference/API_CreateBudget.md "../APIReference/API_CreateBudget.md")
and [UpdateBudget](../APIReference/API_UpdateBudget.md "../APIReference/API_UpdateBudget.md")
API operations. When a budget action triggers, the queue reports a blocked reason of
`BUDGET_THRESHOLD_REACHED` in the [GetQueue](../APIReference/API_GetQueue.md "../APIReference/API_GetQueue.md")
response.
