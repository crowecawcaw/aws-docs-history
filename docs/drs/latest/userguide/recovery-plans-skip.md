

# Skipping a step
<a name="recovery-plans-skip"></a>

Skip a step to move past it without recovering its servers.

```
aws drs update-recovery-plan-execution-step \
    --recovery-plan-execution-step-arn {{EXECUTION_STEP_ARN}} \
    --status SKIPPED
```

The following conditions apply to a skip:
+ The step must be `NOT_STARTED`, `FAILED`, or `TIMED_OUT`. You cannot skip a step that is currently `EXECUTING` or `WAITING`, and you cannot skip one that already reached `COMPLETED`.
+ You can skip a `NOT_STARTED` step while the execution is `IN_PROGRESS` and an earlier step is still running. The skip is recorded immediately and the plan steps over that step when it reaches it. Skipping ahead does not start any step early; only one server step runs at a time.
+ Skipping a `FAILED` step in a `FAILED` execution resumes the execution at the following step.

An execution that finishes with skipped steps reports `COMPLETED`.