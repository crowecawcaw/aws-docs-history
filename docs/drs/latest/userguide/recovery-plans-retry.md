

# Retrying a failed step
<a name="recovery-plans-retry"></a>

Retrying a step recovers only the servers in that step that failed or timed out. Servers in the step that already recovered stay as they are, and AWS Elastic Disaster Recovery does not recover them a second time. After the retried step completes, the execution continues automatically with the steps that follow it.

```
aws drs retry-recovery-plan-execution-step \
    --recovery-plan-execution-step-arn {{EXECUTION_STEP_ARN}}
```

The following conditions apply to a retry:
+ The execution must be `FAILED`. You cannot retry a step while the execution is still in progress.
+ The step must be `FAILED`.
+ You cannot retry a wait step. Skip it instead.
+ No other execution of the same plan may be running.

**Important**  
An execution that stopped because it reached the 24-hour limit reports `TIMED_OUT`, not `FAILED`. You cannot retry or resume it. To finish the recovery in that case, start a new execution of the plan, or recover the remaining servers individually.

Each retry increments the step's attempt count, which is returned with the step.