

# How a recovery plan runs
<a name="recovery-plans-how-it-works"></a>

When you start an execution, AWS Elastic Disaster Recovery does the following:

1. Takes a point-in-time copy of the plan, including its steps, its servers, and each server's impact level.

1. Validates every source server across all of the server steps in the plan. If any server fails validation, the execution fails immediately and AWS Elastic Disaster Recovery recovers no servers. Validation applies to every server regardless of its impact level. For what is checked, see [Validation that runs before a server is recovered](recovery-plans-validation.md).

1. Runs each step in order. For a server step, AWS Elastic Disaster Recovery starts a recovery job for every server in the step at the same time. For a wait step, AWS Elastic Disaster Recovery pauses for the configured number of minutes.

1. Revalidates the servers in a server step at the moment that step begins. A server that passed validation when the execution started can still fail here if something changed in the meantime, such as replication stalling or a chosen recovery point being deleted.

1. Waits for every server in the current step to finish before evaluating the step's outcome and moving to the next step.

1. Marks the execution `COMPLETED` after the last step finishes, or `FAILED` as soon as a step fails.

Because each server step launches its servers in parallel, a step takes as long as its slowest server. Recovery plans use the same recovery process, launch settings, and launch templates as an individual recovery. A recovery that a plan launches behaves exactly like one that you start yourself. The resulting recovery instances appear on the **Recovery instances** page and each server's recovery job appears in [Recovery job history](recovery-job.md#recovery-job-history).

**Important**  
An execution must finish within 24 hours of the time it started. If it does not, AWS Elastic Disaster Recovery stops advancing the plan and marks the step that was running as `TIMED_OUT`. AWS Elastic Disaster Recovery does not cancel the recovery jobs that are already in progress, and those jobs run to completion. The steps after the timed-out step do not run, and you cannot resume the execution. To finish the recovery, start a new execution of the plan, or recover the remaining servers individually.  
Size your plans so that they finish well inside this limit. A step takes as long as its slowest server, so the practical ceiling is the sum of your server steps plus the sum of your wait steps.