# Task lists in Amazon SWF

Task lists provide a way of organizing the various tasks associated with a workflow. You can think of task lists
as similar to dynamic queues. When a task is scheduled in Amazon SWF, you can specify a queue (task list) to put it in.
Similarly, when you poll Amazon SWF for a task you say which queue (task list) to get the task from.

Task lists provide a flexible mechanism to route tasks to workers as your use case necessitates. Task lists are
dynamic in that you don't need to register a task list or explicitly create it through an action: simply scheduling
a task creates the task list if it doesn't already exist.

There are separate lists for _activity_ tasks and _decision_ tasks. A task
is always scheduled on only one task list; tasks are not shared across lists. Furthermore, like activities and
workflows, task lists are scoped to a particular AWS region and Amazon SWF domain.

###### Topics

- [Decision Task Lists](#decision-task-lists "#decision-task-lists")
- [Activity Task Lists](#activity-task-lists "#activity-task-lists")
- [Task Routing](#task-routing "#task-routing")

## Decision Task Lists

Each workflow execution is associated with a specific decision task list. When a workflow type is registered
([RegisterWorkflowType](../apireference/API_RegisterWorkflowType.md "../apireference/API_RegisterWorkflowType.md") action), you can specify a
default task list for executions of that workflow type. When the workflow starter initiates the workflow execution
(`StartWorkflowExecution` action), it has the option of specifying a different task list for that
workflow execution.

When a decider polls for a new decision task (`PollForDecisionTask` action), the decider specifies
a decision task list to draw from. A single decider could serve multiple workflow executions by calling
`PollForDecisionTask` multiple times, using a different task list in each call, where each task list is
specific to a particular workflow execution. Alternatively, the decider could poll a single decision task list
that provides decision tasks for multiple workflow executions. You could also have multiple deciders serving a
single workflow execution by having all of them poll the task list for that workflow execution.

## Activity Task Lists

A single activity task list can contain tasks of different activity types. Tasks are scheduled on the task
list in order. Amazon SWF returns the tasks from the list in order on a best effort basis. Under some circumstances,
the tasks may not come off the list in order.

When an activity type is registered ([RegisterActivityType](../apireference/API_RegisterActivityType.md "../apireference/API_RegisterActivityType.md") action), you can specify a default
task list for that activity type. By default, activity tasks of this type will be scheduled on the specified task
list; however, when the decider schedules an activity task ([ScheduleActivityTask](../apireference/API_ScheduleActivityTaskDecisionAttributes.md "../apireference/API_ScheduleActivityTaskDecisionAttributes.md") decision), the
decider can optionally specify a different task list on which to schedule the task. If the decider doesn't
specify a task list, the default task list is used. As a result, you can place activity tasks on specific task
lists according to attributes of the task. For example, you could place all instances of an activity task for a
given credit card type on a particular task list.

## Task Routing

When an activity worker polls for a new task ([PollForActivityTask](../apireference/API_PollForActivityTask.md "../apireference/API_PollForActivityTask.md") action), it can specify an activity
task list to draw from. If it does, the activity worker will accept tasks only from that list. In this way, you
can ensure that certain tasks get assigned only to particular activity workers. For example, you might create a
task list that holds tasks that require the use of a high-performance computer. Only activity workers running on
the appropriate hardware would poll that task list. Another example would be to create a task list for a
particular geographic region. You could then ensure that only workers deployed in that region would pick up those
tasks. Or you could create a task list for high-priority orders and always check that list first.

Assigning particular tasks to particular activity workers in this way is called _task
routing_. Task routing is optional; if you don't specify a task list when scheduling an activity
task, the task is automatically placed on the default task list.
