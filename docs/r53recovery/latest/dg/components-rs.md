# Region switch components

The following are components of, and concepts about, the Region switch feature in Amazon Application Recovery Controller (ARC).

**Plan**
A plan is the fundamental recovery process for your application. You create a
plan by building one or more workflows with execution blocks to be run in sequence or in parallel. Then, when there is a
Regional impairment, you execute the plan to complete a recovery for your application by
shifting the application to run in a healthy Region.

**Child plan**
A child plan is a self-contained plan that can be run from within a parent
plan, to coordinate more complex application recovery scenarios. You can nest Region switch plans one level.

**Workflow**
A Region switch plan includes one or more workflows. A workflow is made up
of steps that contain execution blocks, which you specify to be run in parallel or in sequence, to
complete the activation or deactivation of a Region as part of a recovery plan. For a plan that
you configure to have an active/passive approach, you create either one workflow that can be used
to activate either of your Regions, or separate activation workflows, one for each Region. For
a plan that you configure for an active/active approach, you create one workflow to activate
your Regions and one workflow to deactivate your Regions.

**Execution block**
You add steps to your Region switch plan workflows containing an execution block.
Execution blocks allow you to specify the recovery for multiple applications or resources
into an activating Region. When you add a step to a workflow, you can add it in
sequence with other steps, or in parallel with one or more other steps.

**Graceful and ungraceful configurations**
You can choose to run specific execution blocks with graceful (planned) or ungraceful
(unplanned) execution. When your environment is healthy, you can use the graceful workflow to
run all steps for an orderly plan execution. The ungraceful workflow mode uses only the necessary
steps and actions. When you run a plan in ungraceful mode, it either changes the behavior of
execution blocks in a workflow or skips specific execution blocks, depending on the type of
execution block.

Specific types of execution blocks have different behavior when they run ungracefully.
Details about these differences are described in the section that includes details about
each type of execution block. For more information, see [Add execution blocks](working-with-rs-execution-blocks.md "working-with-rs-execution-blocks.md").

**Active/active and active/passive configurations**
There are two main approaches to creating a resilient configuration for an application
across multiple Regions: active/passive and active/active. Region switch supports application recovery
for both of these approaches.

With an active/passive configuration, you deploy two replicas of your application in two
different Regions, with customer traffic only going to one Region.

With an active/active configuration, you deploy two replicas to two different Regions, but
both replicas are processing work or receiving traffic.

**Plan execution**
When a Region switch plan executes, it implements recovery for an application when a
Region becomes impaired by activating a healthy Region for your application and traffic it's
receiving. With an active/active configuration, you also run a plan execution to deactivate the
impaired Region.

**Application health alarms**
Application health alarms are CloudWatch alarms that you specify for a plan to indicate the
health of your application in each Region. Region switch uses application health alarms to help determine the
actual recovery time after you switch Regions to implement recovery.

**Triggers**
You can use triggers in Region switch to automate application recovery. When you create a trigger, you specify
one or more Amazon CloudWatch alarms and define which alarm conditions (such as "red" or "green") should initiate
plan execution. When the specified conditions are met, Region switch automatically executes the plan. Triggers are
distinct from application health alarms: triggers start plan execution, while application health alarms help
Region switch calculate actual recovery time after a plan completes.

**Dashboards**
Region switch includes dashboards where you can track details about plan executions in
real time.
