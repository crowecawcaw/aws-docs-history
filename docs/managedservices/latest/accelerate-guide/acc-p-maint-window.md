

# Create a patch maintenance window in AMS
<a name="acc-p-maint-window"></a>

A patch maintenance window runs AMS patch automations on a set schedule for targeted Amazon EC2 instances. Targets are defined by a tag or tags for a group of instances. You can set schedules based on days and times around Patch Tuesday, or you can define a schedule using a *cron expression*. For more information, see [Reference: Cron and rate expressions for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/reference-cron-and-rate-expressions.html) in the *AWS Systems Manager User Guide*. Before patching, AMS creates a snapshot of each instance's root volume. If AMS detects that patching impacts the instance's health, or if you notify AMS of application impact from patching, then AMS uses this snapshot to restore the root volume to a pre-patch state.

## AMS Accelerate patch maintenance window limits
<a name="acc-p-maint-limit"></a>

AMS patching uses AWS Systems Manager (Systems Manager). In addition to Systems Manager service limits, AMS patching has a limit of 300 target instances per patch maintenance window. Given a general patch completion time of 30 mins per instance, the following table provides examples for numbers of maintenance windows and durations.


| Instances to patch | Maintenance windows duration (hrs) | Concurrent maintenance windows needed | 
| --- | --- | --- | 
| 100 | 1 | 1 | 
| 200 | 1 | 1 | 
| 300 | 2 | 1 | 
| 600 | 3 | 2 | 
| 800 | 4 | 3 | 
| 1200 | 6 | 4 | 
| 1500 | 8 | 5 | 

**Important**  
These examples assume no other Systems Manager maintenance windows are active and no other automations are running.

For more information on limits, see [AWS Systems Manager endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html).

**Topics**
+ [AMS Accelerate patch maintenance window limits](#acc-p-maint-limit)
+ [Create a recurring "Patch Tuesday" maintenance window from the AMS console (recommended)](acc-p-maint-window-ams-console.md)
+ [Create a patch maintenance window using CloudFormation for AMS Accelerate](acc-p-maint-window-cfn.md)
+ [Create a maintenance window from the Systems Manager console for AMS Accelerate](acc-p-maint-window-console.md)
+ [Create a maintenance window with the Systems Manager command line interface (CLI) for AMS Accelerate](acc-p-maint-window-cli.md)