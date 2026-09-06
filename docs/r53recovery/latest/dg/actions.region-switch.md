

# Region switch API operations
<a name="actions.region-switch"></a>

The following table lists ARC operations that you can use for Region switch, with links to relevant documentation.


| Action | Using the ARC console | Using the ARC API | Data plane API | 
| --- | --- | --- | --- | 
| Approve or deny a plan execution step | See [Manual approval execution block](manual-approval-block.md) | See [ApprovePlanExecutionStep](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ApprovePlanExecutionStep.html) | Yes | 
| Cancel a plan execution | See [Create a Region switch plan](working-with-rs-create-plan.md) | See [CancelPlanExecution](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_CancelPlanExecution.html) | Yes | 
| Create a plan | See [Create a Region switch plan](working-with-rs-create-plan.md) | See [CreatePlan](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_CreatePlan.html) | No | 
| Delete a plan | See [Working with Region switch](working-with-rs.md) | See [DeletePlan](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_DeletePlan.html) | No | 
| Get a plan | See [Working with Region switch](working-with-rs.md) | See [GetPlan](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_GetPlan.html) | No | 
| Get plan evaluation status | See [Plan evaluation](region-switch-plans.md#region-switch-plans.plan-evaluation) | See [GetPlanEvaluationStatus](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_GetPlanEvaluationStatus.html) | Yes | 
| Get a plan execution | See [Region switch dashboards](region-switch.dashboarding-and-reports.md) | See [GetPlanExecution](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_GetPlanExecution.html) | Yes | 
| Get a plan in Region | See [Working with Region switch](working-with-rs.md) | See [GetPlanInRegion](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_GetPlanInRegion.html) | Yes | 
| List plan execution events | See [Execute a Region switch plan to recover an application](plan-execution-rs.md) | See [ListPlanExecutionEvents](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListPlanExecutionEvents.html) | Yes | 
| List plan executions | See [Execute a Region switch plan to recover an application](plan-execution-rs.md) | See [ListPlanExecutions](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListPlanExecutions.html) | Yes | 
| List plans | See [Working with Region switch](working-with-rs.md) | See [ListPlans](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListPlans.html) | No | 
| List plans in Region | See [Working with Region switch](working-with-rs.md) | See [ListPlansInRegion](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListPlansInRegion.html) | Yes | 
| List Route 53 health checks for a plan | See [Amazon Route 53 health check execution block](route53-health-check-block.md) | See [ListRoute53HealthChecksForPlan](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListRoute53HealthChecks.html) | No | 
| List Route 53 health checks for a plan in Region | See [Amazon Route 53 health check execution block](route53-health-check-block.md) | See [ListRoute53HealthChecksForPlanInRegion](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListRoute53HealthChecksInRegion.html) | Yes | 
| List tags for a resource | See [Tagging for ARC Region switch;](tagging.region-switch.md) | See [ListTagsForResource](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListTagsForResource.html) | No | 
| Start a plan execution | See [Execute a Region switch plan to recover an application](plan-execution-rs.md) | See [StartPlanExecution](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_StartPlanExecution.html) | Yes | 
| Tag a resource | See [Create a Region switch plan](working-with-rs-create-plan.md) | See [TagResource](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_TagResource.html) | No | 
| Remove tags from a resource | See [Tagging for ARC Region switch;](tagging.region-switch.md) | See [UntagResource](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_UntagResource.html) | No | 
| Update a plan | See [Create a Region switch plan](working-with-rs-create-plan.md) | See [UpdatePlan](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_UpdatePlan.html) | No | 
| Update a plan execution | See [Create a Region switch plan](working-with-rs-create-plan.md) | See [UpdatePlanExecution](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_UpdatePlanExecution.html) | Yes | 
| Update a plan execution step | See [Create a Region switch plan](working-with-rs-create-plan.md) | See [UpdatePlanExecutionStep](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_UpdatePlanExecutionStep.html) | Yes | 