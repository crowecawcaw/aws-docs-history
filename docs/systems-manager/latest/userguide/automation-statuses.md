# Learn about statuses returned by Systems Manager

Automation

AWS Systems Manager Automation reports detailed status information about the various statuses an
automation action or step goes through when you run an automation and for the overall
automation. Automation is a tool in AWS Systems Manager. You can monitor automation statuses using
the following methods:

- Monitor the **Execution status** in the Systems Manager Automation
  console.
- Use your preferred command line tools. For the AWS Command Line Interface (AWS CLI), you can use
  [describe-automation-step-executions](../../../cli/latest/reference/ssm/describe-automation-step-executions.md "../../../cli/latest/reference/ssm/describe-automation-step-executions.md") or [get-automation-execution](../../../cli/latest/reference/ssm/get-automation-execution.md "../../../cli/latest/reference/ssm/get-automation-execution.md"). For the AWS Tools for Windows PowerShell, you can use [Get-SSMAutomationStepExecution](../../../powershell/latest/reference/items/Get-SSMAutomationStepExecution.md "../../../powershell/latest/reference/items/Get-SSMAutomationStepExecution.md") or [Get-SSMAutomationExecution](../../../powershell/latest/reference/items/Get-SSMAutomationExecution.md "../../../powershell/latest/reference/items/Get-SSMAutomationExecution.md").
- Configure Amazon EventBridge to respond to action or automation status changes.
  For more information about handling timeouts in an automation, see [Handling timeouts in runbooks](automation-handling-timeouts.md "automation-handling-timeouts.md").

## About automation statuses

Automation reports status details for individual automation actions in addition to
the overall automation.

The overall automation status can be different than the status reported by an
individual action or step as noted in the following tables.

| Detailed status for actions | Status                                                                                                                                                                                                                                                                      | Details                           |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- | ------ | ------- |
| Pending                     | The step hasn't started running. If your automation uses conditional actions, steps remain in this state after an automation has completed if the condition wasn't met to run the step. Steps also remain in this state if the automation is canceled before the step runs. |
| InProgress                  | The step is running.                                                                                                                                                                                                                                                        |
| Waiting                     | The step is waiting for input.                                                                                                                                                                                                                                              |
| Success                     | The step completed successfully. This is a terminal state.                                                                                                                                                                                                                  |
| TimedOut                    | A step or approval wasn't completed before the specified timeout period. This is a terminal state.                                                                                                                                                                          |
| Cancelling                  | The step is in the process of stopping after being canceled by a requester.                                                                                                                                                                                                 |
| Cancelled                   | The step was stopped by a requester before it completed. This is a terminal state.                                                                                                                                                                                          |
| Failed                      | The step didn't complete successfully. This is a terminal state.                                                                                                                                                                                                            |
| Exited                      | Only returned by the `aws:loop` action. The loop didn't fully complete. A step inside the loop moved to an outside step using the `nextStep`, `onCancel`, or `onFailure` properties.                                                                                        | Detailed status for an automation | Status | Details |
| ---                         | ---                                                                                                                                                                                                                                                                         |
| Pending                     | The automation hasn't started running.                                                                                                                                                                                                                                      |
| InProgress                  | The automation is running.                                                                                                                                                                                                                                                  |
| Waiting                     | The automation is waiting for input.                                                                                                                                                                                                                                        |
| Success                     | The automation completed successfully. This is a terminal state.                                                                                                                                                                                                            |
| TimedOut                    | A step or approval wasn't completed before the specified timeout period. This is a terminal state.                                                                                                                                                                          |
| Cancelling                  | The automation is in the process of stopping after being canceled by a requester.                                                                                                                                                                                           |
| Cancelled                   | The automation was stopped by a requester before it completed. This is a terminal state.                                                                                                                                                                                    |
| Failed                      | The automation didn't complete successfully. This is a terminal state.                                                                                                                                                                                                      |
