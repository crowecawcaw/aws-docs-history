# Configure error handling with Workflow Studio in Step Functions

###### Managing state and transforming data

Learn about [Passing data between states with variables](workflow-variables.md "workflow-variables.md") and [Transforming data with JSONata](transforming-data.md "transforming-data.md").

You can configure error handling within the Workflow Studio visual editor. By default, when a state
reports an error, Step Functions causes the workflow execution to fail entirely. For actions and
some flow states, you can configure how Step Functions handles errors.

Even if you have configured error handling, some errors may still cause a workflow
execution to fail. For more information, see [Handling errors in Step Functions workflows](concepts-error-handling.md "concepts-error-handling.md"). In Workflow Studio, configure error handling in the
**Error handling** tab of the [Inspector
panel](workflow-studio.md#workflow-studio-components-formdefinition "workflow-studio.md#workflow-studio-components-formdefinition").

## Retry on errors

You can add one or more rules to action states and the [Parallel workflow state](state-parallel.md "state-parallel.md") flow state
to retry the task when an error occurs. These rules are called
_retriers_. To add a retrier, choose the edit icon in **Retrier #1** box, then configure its options:

- (Optional) In the **Comment** field, add your
  comment. It will not affect the workflow, but can be used to annotate your workflow.
- Place the cursor in the **Errors** field and choose an error that will trigger the retrier, or enter a custom error name. You can choose or add multiple errors.
- (Optional) Set an **Interval**. This is the time in seconds before
  Step Functions make its first retry. Additional retries will follow at intervals that you can
  configure with **Max attempts** and **Backoff
  rate**.
- (Optional) Set **Max attempts**. This is the maximum number of retries
  before Step Functions will cause the execution to fail.
- (Optional) Set the **Backoff rate**. This is a multiplier that
  determines by how much the retry interval will increase with each attempt.

###### Note

Not all error handling options are available for all states. Lambda Invoke has one
retrier configured by default.

## Catch errors

You can add one or more rules to action states and to the [Parallel workflow state](state-parallel.md "state-parallel.md") and
[Map workflow state](state-map.md "state-map.md") flow states to catch an error. These rules are called
_catchers_. To add a catcher, choose **Add new
catcher**, then configure its options:

- (Optional) In the **Comment** field, add your
  comment. It will not affect the workflow, but can be used to annotate your workflow.
- Place the cursor in **Errors** field and choose an error that will trigger the catcher, or enter a custom error name. You can choose or add multiple errors.
- In the **Fallback state** field, choose a [fallback state](concepts-error-handling.md#error-handling-fallback-states "concepts-error-handling.md#error-handling-fallback-states"). This is the state that the workflow
  will move to next, after an error is caught.
- (Optional) In the **ResultPath** field, add a `ResultPath` filter to add the error to the original
  state input. The [ResultPath](input-output-resultpath.md "input-output-resultpath.md")
  must be a valid [JsonPath](https://datatracker.ietf.org/wg/jsonpath/about/ "https://datatracker.ietf.org/wg/jsonpath/about/"). This will be sent to the fallback state.

## Timeouts

You can configure a timeout for action states to set the maximum number of seconds your
state can run before it fails. Use timeouts to prevent stuck executions. To configure a
timeout, enter the number of seconds your state should wait before the execution fails. For
more information about timeouts, see `TimeoutSeconds` in [Task workflow state](state-task.md "state-task.md") state.

## HeartbeatSeconds

You can configure a _Heartbeat_ or periodic notification sent by your
task. If you set a heartbeat interval, and your state doesn't send heartbeat notifications
in the configured intervals, the task is marked as failed. To configure a heartbeat, set a
positive, non-zero integer number of seconds. For more information, see
`HeartBeatSeconds` in [Task workflow state](state-task.md "state-task.md") state.
