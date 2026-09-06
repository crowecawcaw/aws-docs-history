

# Monitoring an execution
<a name="recovery-plans-monitoring"></a>

To follow an execution in the console, open the plan and choose the execution from its execution history. The execution details show the status of the execution, the status of each step, and the status of each server within a step, including the recovery job that AWS Elastic Disaster Recovery created for it.

With the AWS CLI, use `get-recovery-plan-execution` for the overall status and `list-recovery-plan-execution-steps` for per-step progress. Use `list-recovery-plan-executions` to see the history for a plan, optionally filtered by status.

```
aws drs get-recovery-plan-execution \
    --recovery-plan-execution-arn {{EXECUTION_ARN}}

aws drs list-recovery-plan-execution-steps \
    --recovery-plan-execution-arn {{EXECUTION_ARN}}
```

An execution reports one of the following statuses:


| Execution status | Description | 
| --- | --- | 
| `CREATED` | The execution was accepted and its source servers are being validated. No servers have been recovered yet. | 
| `IN_PROGRESS` | AWS Elastic Disaster Recovery is running the steps of the plan. | 
| `COMPLETED` | Every step reached a terminal state without a critical failure. An execution that skipped one or more steps also reports `COMPLETED`. | 
| `FAILED` | Either the validation at the start of the execution failed, or a step failed because a critical server did not recover. The remaining steps did not run. If a step failed, you can retry or skip that step to continue. If the validation failed, no step ran, so there is nothing to retry or skip; correct the problem the error reports and start a new execution. | 
| `TIMED_OUT` | The execution reached its 24-hour limit while a step was still running. The remaining steps did not run, and you cannot retry, skip, or resume the execution. Start a new execution of the plan to finish the recovery. | 
| `CANCELLING` | You canceled the execution and AWS Elastic Disaster Recovery is waiting for the step that was already running to finish. | 
| `CANCELLED` | The execution stopped after you canceled it. The steps that had not started were canceled. | 

**Note**  
If an execution completes with skipped steps, the status is still exactly `COMPLETED`. There is no separate status value for it. The detail appears as a message on the execution: *Completed with skipped steps. View execution details for more information.* If you script against these APIs, branch on the `status` field and treat the execution's `errorDetail` as informational text only. In particular, do not branch on `errorDetail.code`, which is not a reliable signal of failure — a successful execution that skipped a step still returns a code value.

Each step within an execution reports one of the following statuses:


| Step status | Description | 
| --- | --- | 
| `NOT_STARTED` | The step is waiting for the steps before it to finish. | 
| `EXECUTING` | A server step is recovering its servers. | 
| `WAITING` | A wait step is counting down its wait duration. | 
| `COMPLETED` | The step finished. A server step can complete even if optional servers failed. | 
| `FAILED` | At least one critical server in the step did not recover. | 
| `TIMED_OUT` | The step was still running when the execution reached its 24-hour limit. | 
| `SKIPPED` | You skipped the step, or the step was not run because the execution was canceled. | 

Recovery plan API calls are recorded by AWS CloudTrail, so you can audit who created, changed, or ran a plan. For more information, see [Logging AWS Elastic Disaster Recovery API calls using AWS CloudTrail](logging-using-cloudtrail.md#logging-using-cloudtrail-).