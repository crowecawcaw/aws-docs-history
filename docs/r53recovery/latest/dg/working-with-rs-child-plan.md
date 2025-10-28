# Create child plans

To support more complex recovery scenarios, you can create child plans by adding them with
Region switch plan execution blocks. The hierarchy is limited to two levels, but one parent plan can
include multiple child plans.

###### Important

Before you create a child plan, make sure that you have the correct IAM policy in place.
For more information, see [Region switch plan execution block sample policy](security_iam_region_switch_plan_execution.md "security_iam_region_switch_plan_execution.md").

For compatibility, child plans must support all Regions that the parent plan supports. In addition,
the recovery approach, active/active or active/passive, must be the same for the parent and child plans.

Keep in mind the following ways in which a child plan respond to changes that you make to
a parent plan and to parent plan scenarios.

- A parent execution block is marked as completed when all child plans and other execution blocks within
  it are completed.
- If any step fails in any child plan, the Region switch plan execution block fails in the parent plan.
- Control actions that are initiated in the parent plan during the Region switch step, such as pause, a graceful or
  ungraceful switches, or a cancellation, are automatically attempted on the child plan, regardless of the child plan's
  current step.
- Skips operations have a special behavior: the parent plan is skipped, but the child plan will still execute.
- If a child plan is already executing in a Region switch block, to determine if it continues to run,
  Region switch assesses the child plan's compatibility with the parent plan. If the child plan's configuration matches
  the parent plan's requirements, Region switch treats the child plan as if it were initiated by the parent plan.
- The parent plan step will fail if the child plan is running with incompatible configuration parameters,
  such as the following:
  - The child plan is operating in a different Region
  - The child plan is executing a deactivating operation when Region switch expects it to execute an
    activating operation

- If the child plan completes successfully during a time that a parent plan is paused, the parent plan
  will succeed when the parent plan resumes.
