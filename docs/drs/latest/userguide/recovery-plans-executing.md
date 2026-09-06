

# Running a recovery plan
<a name="recovery-plans-executing"></a>

You can run a plan as a drill or as a recovery:

**Drill**  
Launches drill instances to validate your recovery readiness. Drills do not affect your source servers or ongoing replication. Run drills regularly so that your plan is proven before you need it.

**Recovery**  
Launches recovery instances for an actual recovery event.

A plan recovers each server the same way an individual recovery does. Any post-launch actions that are active for a source server run for that server's recovery instance exactly as they would for an individual recovery. For more information, see [Post-launch action settings](post-launch-action-settings-overview.md).

**Important**  
AWS Elastic Disaster Recovery does not terminate the instances that a plan launches, including drill instances, and it does not clean them up when an execution completes, is canceled, or times out. Every instance a plan launches keeps incurring Amazon EC2, Amazon EBS, and associated charges until you terminate it. Because a plan can launch up to 100 instances at once, clean up after every drill. You can terminate recovery instances from the **Recovery instances** page; see [Managing recovery instances](recovery-instances.md#managing-recovery-instances) and [Post recovery drill actions](preparing-failover.md#failback-cleanup-drill). For charge details, see [AWS Elastic Disaster Recovery pricing](https://aws.amazon.com/disaster-recovery/pricing/).

**To run a recovery plan (console)**

1. Open the Elastic Disaster Recovery console at [https://console.aws.amazon.com/drs/home](https://console.aws.amazon.com/drs/home).

1. In the navigation pane, choose **Recovery plans**, and then choose the plan that you want to run.

1. Choose **Execute recovery plan**.

1. Choose **Drill** or **Recovery**.

1. (Optional) Choose a specific recovery point for individual servers. If you do not choose a recovery point for a server, AWS Elastic Disaster Recovery recovers that server from the latest data available. That is the same behavior as recovering the server on its own without choosing a recovery point.

1. Confirm your choices to start the execution.

To start an execution with the AWS CLI, use the `start-recovery-plan-execution` command.

```
aws drs start-recovery-plan-execution \
    --recovery-plan-arn {{PLAN_ARN}} \
    --mode DRILL
```

To recover specific servers from a specific recovery point, add the `--source-servers` parameter. Every server that you list must belong to the plan and must include a `recoverySnapshotID`. You do not have to list every server in the plan. Any server that you omit is recovered from the latest data available.

```
aws drs start-recovery-plan-execution \
    --recovery-plan-arn {{PLAN_ARN}} \
    --mode RECOVERY \
    --source-servers '[
        {"sourceServerID": "s-{{EXAMPLE1}}", "recoverySnapshotID": "pit-{{EXAMPLE1}}"}
    ]'
```

A `recoverySnapshotID` is an AWS Elastic Disaster Recovery recovery point ID. It is always 21 characters long and begins with the `pit-` prefix, for example `pit-1234567890abcdef1`.

**Important**  
A recovery point ID is not an Amazon EBS snapshot ID. An Amazon EBS snapshot ID begins with `snap-`, and although a recovery point lists the Amazon EBS snapshots that back it in its `ebsSnapshots` field, those `snap-` IDs are not valid values for `recoverySnapshotID`. Passing one is rejected as a validation error.

To find the recovery point IDs that are available for a source server, use `describe-recovery-snapshots`. Ordering by `DESC` returns the most recent recovery point first.

```
aws drs describe-recovery-snapshots \
    --source-server-id s-{{EXAMPLE1}} \
    --order DESC \
    --max-results 5
```

Each entry in the response `items` list contains the recovery point ID in the `snapshotID` field, along with its `timestamp`. Take the value of `snapshotID` and pass it as `recoverySnapshotID` when you start the execution; the field is named differently in the two APIs.

```
{
    "items": [
        {
            "snapshotID": "pit-1234567890abcdef1",
            "sourceServerID": "s-1234567890abcdef1",
            "expectedTimestamp": "2026-08-18T09:00:00Z",
            "timestamp": "2026-08-18T09:00:12Z",
            "ebsSnapshots": [
                "snap-0123456789abcdef0",
                "snap-0123456789abcdef1"
            ]
        }
    ]
}
```

In this example, `pit-1234567890abcdef1` is the value to pass as `recoverySnapshotID`. The two `snap-` IDs are the Amazon EBS snapshots that back that recovery point, and are not valid values.

To narrow the results to a time range, add the `--filters` parameter with `fromDateTime` and `toDateTime`.

**Important**  
A recovery point that you pin is validated again at the moment its step begins, not only when the execution starts. In a long plan, a step can run many hours after you started the execution. A recovery point that existed then might be deleted, or age out of your point-in-time retention window, before the step runs. If that happens, the step fails and the plan stops. Pin recovery points only when you need a specific point in time, and prefer recovery points that will still be inside your retention window when the step is expected to run. Omit `--source-servers` to always use the latest data available.

The following conditions prevent an execution from starting. Each one returns the error shown:


| Condition | Error | 
| --- | --- | 
| The plan already has an execution in progress. A plan can have only one execution running at a time. | `ConflictException` — *Another execution is already active for plan {{planId}}* | 
| A source server in this plan also belongs to another plan that has an execution in progress. | `ConflictException` — names the plan and the execution that are holding the server, so that you can wait for that execution or cancel it. | 
| The plan status is not `ACTIVE`. A plan becomes `INVALID` when it has no server steps. | `ConflictException` — *Recovery plan {{planId}} is in status {{status}} and cannot be executed. Only ACTIVE plans can be executed.* | 
| The plan has no steps. | `ValidationException` — *Recovery plan {{planId}} has no steps. Add at least one step to the plan before starting an execution.* | 
| The plan is being deleted. | `ConflictException` — *Cannot start execution: recovery plan {{planId}} is being deleted.* | 
| A server listed in `--source-servers` is not part of the plan, or is missing a `recoverySnapshotID`. | `ValidationException` — *Source server IDs not found in plan* or *Missing recoverySnapshotID for servers*, listing the servers concerned. | 
| The AWS account has not been initialized for AWS Elastic Disaster Recovery. | `UninitializedAccountException` | 