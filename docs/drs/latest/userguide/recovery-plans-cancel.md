

# Canceling an execution
<a name="recovery-plans-cancel"></a>

Canceling an execution stops AWS Elastic Disaster Recovery from starting any more steps.

```
aws drs cancel-recovery-plan-execution \
    --recovery-plan-execution-arn {{EXECUTION_ARN}}
```

**Important**  
Canceling does not stop recovery jobs that have already started. The step that is running when you cancel continues until all of its servers finish, and any instances that it launches are created. The execution moves to `CANCELLING` until that step finishes, and then to `CANCELLED`. Steps that had not started are canceled and never run. To clean up instances that were launched before you canceled, terminate them from the **Recovery instances** page.

You can cancel an execution that is `CREATED` or `IN_PROGRESS`. You cannot cancel one that has already completed, failed, or been canceled.