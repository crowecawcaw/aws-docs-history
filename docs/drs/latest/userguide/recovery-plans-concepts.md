# Recovery plan concepts

The following terms are used throughout the recovery plan documentation:

**Recovery plan**

An ordered list of steps that defines how a group of source servers is
recovered. A plan belongs to a single AWS account and Region, and its name
must be unique within that account and Region.

**Step**

One entry in the ordered list. A step is either a
**server step** or a
**wait step**. Steps run one at a time, in
order.

**Server step**

A step that contains one or more source servers. AWS Elastic Disaster Recovery starts
recovery for every server in the step at the same time and considers the
step finished only after every server has finished.

**Wait step**

A step that pauses the plan for a fixed number of minutes before the next
step starts. Use a wait step to give an application time to initialize after
its instances launch. A wait step cannot be the first step in a
plan.

**Impact level**

A per-server setting on a server step that determines whether the failure
of that server stops the plan. A
**Critical** server (the default) fails the
step and the execution. An **Optional** server
does not. For more information, see [Controlling how server failures
affect a plan](recovery-plans-impact-levels.md "recovery-plans-impact-levels.md").

**Execution**

A single run of a recovery plan. An execution is a point-in-time copy of
the plan: it records the steps and servers as they were when the execution
started, so later edits to the plan do not change a run that is already in
progress.

**Execution mode**

Whether the run is a **Drill** or a
**Recovery**. The mode applies to every
server step in the plan and is equivalent to choosing between a drill and a
recovery for an individual source server.
