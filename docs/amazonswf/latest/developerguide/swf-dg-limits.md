# Amazon SWF Quotas

Amazon SWF places quotas on the sizes of certain workflow parameters, such as on the number of
domains per account and on the size of the workflow execution history. These quotas are designed
to prevent erroneous workflows from consuming all of the resources of the system, but are not
hard limits. If you find that your application is frequently exceeding these quotas, you can
[request a service quota increase](#swf-dg-limits-how-to-increase "#swf-dg-limits-how-to-increase").

###### Contents

- [General Account Quotas for Amazon SWF](swf-dg-limits.md#swf-dg-limits-general "swf-dg-limits.md#swf-dg-limits-general")
- [Quotas on Workflow Executions](swf-dg-limits.md#swf-dg-limits-workflow-executions "swf-dg-limits.md#swf-dg-limits-workflow-executions")
- [Quotas on Task Executions](swf-dg-limits.md#swf-dg-limits-tasks "swf-dg-limits.md#swf-dg-limits-tasks")
- [Amazon SWF throttling quotas](swf-dg-limits.md#swf-throttling-limits "swf-dg-limits.md#swf-throttling-limits")
  - [Throttling quotas for all Regions](swf-dg-limits.md#throttle-limits-all-regions "swf-dg-limits.md#throttle-limits-all-regions")
  - [Decision quotas for all Regions](swf-dg-limits.md#decision-quota-limits-all-regions "swf-dg-limits.md#decision-quota-limits-all-regions")
  - [Workflow-level quotas](swf-dg-limits.md#wf-wflow-level-quotas "swf-dg-limits.md#wf-wflow-level-quotas")

- [Requesting a quota increase](swf-dg-limits.md#swf-dg-limits-how-to-increase "swf-dg-limits.md#swf-dg-limits-how-to-increase")

## General Account Quotas for Amazon SWF

- **Maximum registered domains** – 100

This quota includes both registered and deprecated domains.

- **Maximum workflow and activity types** – 10,000
  each per domain

This quota includes both registered and deprecated types.

- **API call quota** – Beyond infrequent spikes,
  applications may be throttled if they make a large number of API calls in a very short
  period of time.
- **Maximum request size** – 1 MB per request

This is the _total_ data size per Amazon SWF API request, including the
request header and all other associated request data.

- **Truncated responses for _Count_
  APIs** – Indicates that an internal quota was reached and that the
  response is not the full count.

Some queries will internally reach the 1 MB quota mentioned above before returning a
full response. The following can return a truncated response instead of the full
count.

    + [CountClosedWorkflowExecutions](../apireference/API_CountClosedWorkflowExecutions.md "../apireference/API_CountClosedWorkflowExecutions.md")
    + [CountOpenWorkflowExecutions](../apireference/API_CountOpenWorkflowExecutions.md "../apireference/API_CountOpenWorkflowExecutions.md")
    + [CountPendingActivityTasks](../apireference/API_CountPendingActivityTasks.md "../apireference/API_CountPendingActivityTasks.md")
    + [CountPendingDecisionTasks](../apireference/API_CountPendingDecisionTasks.md "../apireference/API_CountPendingDecisionTasks.md")

For each of these, if the `truncated` response is set to true, the count is
less than the full amount. This internal quota can not be increased.

- **Maximum number of tags** – 50 tags per
  resource.

Attempting to add tags beyond 50 will result in a 400 error,
`TooManyTagsFault`.

## Quotas on Workflow Executions

- **Maximum open workflow executions** – 100,000 per
  domain

This count includes child workflow executions.

- **Maximum workflow execution time** – 1 year. This is a hard quota that can't be changed.
- **Maximum workflow execution history size** –
  25,000 events. This is a hard quota that can't be changed.

Best practice is to structure each workflow such that its history does not grow beyond
10,000 events. Because the decider has to fetch the workflow history, a smaller history
allows the decider to complete more quickly. If using the [Flow Framework](resources.md#aws-flow-framework-documentation "resources.md#aws-flow-framework-documentation"), you can use
ContinueAsNew to continue a workflow with a fresh history.

- **Maximum open child workflow executions** – 1,000
  per workflow execution

If your use case requires you to go beyond these quotas, you can use features Amazon SWF
provides to continue executions and structure your applications using [child workflow](swf-dev-adv-child-workflows.md "swf-dev-adv-child-workflows.md") executions. If you find that you
still need a quota increase, see [Requesting a quota increase](#swf-dg-limits-how-to-increase "#swf-dg-limits-how-to-increase").

## Quotas on Task Executions

- **Maximum pollers per task list** – 1,000 per task
  list

You can have a maximum of 1,000 pollers which simultaneously poll a particular task
list. If you go over 1,000, you receive a `LimitExceededException`.

###### Note

While the maximum is 1,000, you might encounter `LimitExceededException` errors well before this quota. This error does not mean your tasks are being delayed. Instead, it means that you have the maximum amount of idle pollers on a task list. Amazon SWF sets this limit to save resources on both the client and server side. Setting the limit prevents an excessive number of pollers from waiting unnecessarily. You can reduce the `LimitExceededException` errors by using multiple task lists to distribute polling.

- **Maximum tasks scheduled per second** – 2,000 per
  task list

You can schedule a maximum of 2,000 tasks per second on a particular task list. If
you exceed 2,000, your `ScheduleActivityTask` decisions will fail with
`ACTIVITY_CREATION_RATE_EXCEEDED` error.

###### Note

While the maximum is 2,000, you might encounter
`ACTIVITY_CREATION_RATE_EXCEEDED` errors well before this quota. To reduce
these errors, use multiple task lists to distribute the load.

- **Maximum task execution time** – 1 year
  (constrained by workflow execution time maximum)

You can configure [activity timeouts](swf-timeout-types.md "swf-timeout-types.md") to cause
a timeout event to occur if a particular stage of your [activity task](swf-dev-tasks.md "swf-dev-tasks.md") execution takes too long.

- **Maximum time SWF will keep a task in the queue**
  – 1 year (constrained by workflow execution time quota)

You can configure default [activity timeouts](swf-timeout-types.md "swf-timeout-types.md")
during activity registration that will cause a timeout event to occur if a particular
stage of your [activity task](swf-dev-tasks.md "swf-dev-tasks.md") execution takes too long.
You can also override the default activity timeouts when you schedule an activity task in
your decider code.

- **Maximum open activity tasks** – 1,000 per
  workflow execution.

This quota includes both activity tasks that have been scheduled and those being
processed by workers.

- **Maximum open timers** – 1,000 per workflow
  execution
- **Maximum input/result data size** – 32,768
  characters

This quota affects activity or workflow execution result data, input data when
scheduling activity tasks or workflow executions, and input sent with a [workflow execution signal](swf-dev-adv-signals.md "swf-dev-adv-signals.md").

- **Maximum decisions in a decision task response** –
  varies

Due to the 1 MB quota on the [maximum API request
size](#swf-dg-limits-general "#swf-dg-limits-general"), the number of decisions returned in a single call to `RespondDecisionTaskCompleted` will be limited according to the size of
the data used by each decision, including the size of any input data provided to scheduled
activity tasks or to workflow executions.

## Amazon SWF throttling quotas

In addition to the service quotas described previously, certain Amazon SWF API calls and
decision events are throttled to maintain service bandwidth, using a [token bucket](https://en.wikipedia.org/wiki/Token_bucket "https://en.wikipedia.org/wiki/Token_bucket") scheme. If your rate
of requests consistently exceeds the rates that are listed here, you can [request a throttle quota increase](#swf-dg-limits-how-to-increase "#swf-dg-limits-how-to-increase").

The throttling and decision quotas are same across all regions.

### Throttling quotas for all Regions

The following quotas are applicable at individual account-levels. You can also request an increase to the following quotas. For information about doing this, see
[Requesting a quota increase](#swf-dg-limits-how-to-increase "#swf-dg-limits-how-to-increase").

| API name                         | Bucket size | Refill rate per second |
| -------------------------------- | ----------- | ---------------------- |
| `CountClosedWorkflowExecutions`  | 2000        | 6                      |
| `CountOpenWorkflowExecutions`    | 2000        | 6                      |
| `CountPendingActivityTasks`      | 200         | 6                      |
| `CountPendingDecisionTasks`      | 200         | 6                      |
| `DeleteActivityType`             | 200         | 6                      |
| `DeleteWorkflowType`             | 200         | 6                      |
| `DeprecateActivityType`          | 200         | 6                      |
| `DeprecateDomain`                | 100         | 6                      |
| `DeprecateWorkflowType`          | 200         | 6                      |
| `DescribeActivityType`           | 2000        | 6                      |
| `DescribeDomain`                 | 200         | 6                      |
| `DescribeWorkflowExecution`      | 2000        | 6                      |
| `DescribeWorkflowType`           | 2000        | 6                      |
| `GetWorkflowExecutionHistory`    | 2000        | 60                     |
| `ListActivityTypes`              | 200         | 6                      |
| `ListClosedWorkflowExecutions`   | 200         | 6                      |
| `ListDomains`                    | 100         | 6                      |
| `ListOpenWorkflowExecutions`     | 200         | 48                     |
| `ListTagsForResource`            | 50          | 30                     |
| `ListWorkflowTypes`              | 200         | 6                      |
| `PollForActivityTask`            | 2000        | 200                    |
| `PollForDecisionTask`            | 2000        | 200                    |
| `RecordActivityTaskHeartbeat`    | 2000        | 160                    |
| `RegisterActivityType`           | 200         | 60                     |
| `RegisterDomain`                 | 100         | 6                      |
| `RegisterWorkflowType`           | 200         | 60                     |
| `RequestCancelWorkflowExecution` | 2000        | 30                     |
| `RespondActivityTaskCanceled`    | 2000        | 200                    |
| `RespondActivityTaskCompleted`   | 2000        | 200                    |
| `RespondActivityTaskFailed`      | 2000        | 200                    |
| `RespondDecisionTaskCompleted`   | 2000        | 200                    |
| `SignalWorkflowExecution`        | 2000        | 30                     |
| `StartWorkflowExecution`         | 2000        | 200                    |
| `TagResource`                    | 50          | 30                     |
| `TerminateWorkflowExecution`     | 2000        | 60                     |
| `UndeprecateActivityType`        | 200         | 6                      |
| `UndeprecateDomain`              | 100         | 6                      |
| `UndeprecateWorkflowType`        | 200         | 6                      |
| `UntagResource`                  | 50          | 30                     |

### Decision quotas for all Regions

The following quotas are applicable at individual account-levels. You can also request an increase to the following quotas. For information about doing this, see
[Requesting a quota increase](#swf-dg-limits-how-to-increase "#swf-dg-limits-how-to-increase").

| API name                                 | Bucket size | Refill rate per second |
| ---------------------------------------- | ----------- | ---------------------- |
| `RequestCancelExternalWorkflowExecution` | 1200        | 120                    |
| `ScheduleActivityTask`                   | 1000        | 200                    |
| `SignalExternalWorkflowExecution`        | 1200        | 120                    |
| `StartChildWorkflowExecution`            | 500         | 12                     |
| `StartTimer`                             | 2000        | 200                    |

### Workflow-level quotas

The following quotas are applicable at workflow-levels and can't be increased.

| API name                         | Bucket size | Refill rate per second |
| -------------------------------- | ----------- | ---------------------- |
| `GetWorkflowExecutionHistory`    | 400         | 200                    |
| `SignalWorkflowExecution`        | 1000        | 1000                   |
| `RecordActivityTaskHeartbeat`    | 1000        | 1000                   |
| `RequestCancelWorkflowExecution` | 200         | 200                    |

## Requesting a quota increase

For more information, see
[AWS service quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md") in the
_AWS General Reference_.
