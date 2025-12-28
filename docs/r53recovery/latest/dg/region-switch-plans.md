# About Region switch

With Region switch, you can orchestrate the specific steps to switch the AWS Region that your
multi-Region application is running in.

Region switch is built around the concept of a _plan_, which you design and configure for your
specific recovery needs. Each plan includes _workflows_ that are made up of steps. A step runs
one or more _execution blocks_, which Region switch runs in parallel or in sequence,
to complete an application recovery. Each execution block handles a different task, such as switching
over resources or managing traffic redirection for your application. For even more flexibility, you can
create nested plans, by adding child plans.

Whenever you create, or update, a plan, Region switch performs a plan evaluation, to ensure that there
aren't issues with IAM permissions, resource configurations, or running capacity.
Region switch runs these evaluations regularly, and generates a warning for any issues that it finds.

Region switch also calculates an actual recovery time value for each plan execution,
to help you evaluate if the plan is meeting your objectives. You can view recovery time and other
details about plan executions in Region switch dashboards in the AWS Management Console. For more information, see
[Region switch dashboards](region-switch.md "region-switch.md").

To learn more about each of these areas in Region switch, see the following sections.

## Region switch plans

A Region switch plan is the top-level resource in Region switch. You should scope your plan to a
specific multi-Region application. A plan enables you to build _workflows_
to recover your applications by running a series of Region switch _execution blocks_
that activate or deactivate your application and its resources, including cross-account resources,
in the AWS Region that you specify.

A plan is made up of one or more workflows, to enable you to activate or deactivate a specific AWS Region.
You can configure execution blocks in a workflow to run sequentially, or you can specify that
some of the blocks run in parallel.

For a plan that you configure for an active/passive multi-Region approach, you create
either one workflow that can be used to activate either of your Regions, or two separate
activation workflows, one for each Region. For a plan that you configure for an
active/active approach, you create one workflow to activate your Regions and
one workflow to deactivate your Regions.

AWS Regions are geographic locations worldwide where AWS clusters data centers. Each
Region is designed to be completely isolated from the other Regions, providing fault
tolerance and stability. When you use Region switch, you need to consider which Regions
your application is deployed in and which Regions you want to use for recovery.

Region switch supports recovery between any two AWS Regions where the service is
available. When you configure a Region switch plan, you specify the Regions that your
application is deployed in and the recovery approach that you want to use: active/passive or
active/active.

For example, you might have an active/passive multi-Region approach with us-east-1 as the
primary Region and us-west-2 as the standby Region. To recover your application from an
operational issue that impacts the application in us-east-1, you could execute your
Region switch plan to activate us-west-2. This would result in the application
switching from resources in us-east-1 to resources in us-west-2.

Region switch plans run using the permissions associated with the IAM role that you
specify when you create the plan.

You can create multiple plans, one for each of your multi-Region
applications, and then orchestrate recovery across these plans in your required order
by creating a _parent plan_. A parent plan is a plan that uses
the Region switch plan execution blocks as steps. The hierarchy of plans is limited to two levels (parent and child), but you can
include multiple child plans under the same parent plan.

## Workflows and execution blocks

After you create a Region switch plan, you must add one or more workflows to the plan, to define the
steps you want the plan to perform for your application recovery. For each workflow,
you add execution blocks to complete specific tasks, like scaling up
resources or updating routing controls to reroute traffic. Execution blocks enable
you to specify these tasks and the order in which they're completed. By creating nested plans, you can
also orchestrate the order in which multiple applications recover into the Region that you're activating.

You can add execution blocks in a workflow sequentially, or you can add one or more execution blocks in parallel.
Also, depending on the resource, you can have the option to run an execution block with graceful (planned) or
ungraceful (unplanned) execution.

- Graceful execution: A planned execution workflow. When your environment is
  healthy, you can use the graceful workflow to run all steps for an orderly plan
  execution.
- Ungraceful execution: An unplanned execution. The ungraceful workflow mode
  uses only the necessary steps and actions. This mode either changes the behavior
  of the execution blocks in a workflow or skips specific execution blocks.

Finally, you can also configure cross-account resources for an execution block. First, you must configure
permissions, by following the guidance in [Cross-account support in Region switch](cross-account-resources-rs.md "cross-account-resources-rs.md"). After you've set up the required IAM roles,
then you can add cross-acount resources in the execution blocks in your plan workflows. To add
cross-account resources, when you add an execution block, you specify a
target IAM role that has permissions to the resource of other AWS accounts. You also must
specify the external ID that you provided in the trust policy for the cross-account role.
For details about creating the required IAM roles, see [Cross-account resource permissions](security_iam_region_switch_cross_account.md "security_iam_region_switch_cross_account.md").

To learn more about workflows, see [Create Region switch plan workflows](working-with-rs-workflows.md "working-with-rs-workflows.md"). For details about each type of execution block,
including configuration steps, how it works, and what is evaluated as part of plan evaluation, see [Add execution blocks](working-with-rs-execution-blocks.md "working-with-rs-execution-blocks.md").

## Plan evaluation

Plan evaluation is an automated process that Region switch runs when a plan is created
or updated, and then every 30 minutes after that, during steady state. The evaluation
process verifies several critical aspects of plan configuration and resource configurations.
The evaluations include verifying IAM permissions, resource configurations, and running capacity.

If Region switch finds an issue that might prevent a successful plan execution, it
generates a plan evaluation warning, which is highlighted on the plan details page in the console.
You can also consume plan evaluation warnings with Amazon EventBridge, or you can view warnings by
using the Region switch API.

You can see details and suggested remediation for issues that plan evaluation surfaces in the
**Plan evaluation** tab on the plan details page. We recommend that you also
test application recovery by executing your Region switch plan, and that you don't rely
solely on Region switch plan evaluation to test that your recovery plan will work as you expect
it to.

## Automatic plan execution reports

Region switch can automatically generate comprehensive PDF reports for plan executions to help you meet
regulatory compliance requirements. These reports provide evidence of your disaster recovery
tests and actual recovery events, including detailed execution timelines, plan configurations, and
resource states.

When you configure automatic report generation for a plan, Region switch creates a PDF report after each
plan execution completes and delivers it to an Amazon S3 bucket that you specify. Reports are typically
available within 30 minutes of execution completion. S3 storage costs apply.

Each report includes:

- Executive summary with service overview and report creation date
- Plan configuration details as they existed at execution time
- Detailed execution timeline with steps, affected resources, and statuses
- Plan warnings that were present when the execution started
- Amazon CloudWatch alarm states and alarm history for associated alarms
- For parent plans, configuration and execution details of child plans
- Glossary of terms and concepts

To enable automatic report generation, you configure a report output destination when you create or
update a plan. You must also ensure that your plan's execution IAM role has the necessary permissions
to write reports to your Amazon S3 bucket and access the resources needed to generate the report content.
For more information about required permissions, see [Automatic plan execution reports permissions](security_iam_region_switch_reports.md "security_iam_region_switch_reports.md").

You can view the status of report generation and download completed reports from the plan execution
details page in the console. If report generation encounters errors, such as insufficient permissions or
misconfigured Amazon S3 buckets, Region switch provides error details to help you troubleshoot the issue.

Plan evaluation continuously validates your report configuration, including verifying that the
execution role has the required IAM permissions. If Region switch detects configuration issues that would
prevent successful report generation, it generates warnings that you can view on the plan details page.

## Regional alarms and actual recovery time

Region switch calculates an _actual recovery time_ value for each plan execution,
which you can view after a plan execution. Actual recovery time is shown on the plan execution
details page, so that you can compare the actual time to the recovery time objective you
specified when you created the plan.

Actual recovery time is calculated as the total of the time is takes for a plan execution
to complete, and any additional time that elapses before specific Amazon CloudWatch alarms that you configure
return to a green state.

To support calculating an accurate actual recovery time for plan execution, add Regional
Amazon CloudWatch alarms to a Region switch plan that provide a signal about the health of your application in each
Region. When a plan is executed, Region switch uses these application health alarms to determine when
your application is healthy again. Then, Region switch calculates actual recovery time based on
the time it takes for your plan to execute added to the time it takes for your application
to return to healthy, based on the application health alarms that you specify.

Before you add CloudWatch alarms to a Region switch plan, make sure that you have the correct IAM policy in place.
For more information, see [CloudWatch alarms for application health permissions](security_iam_region_switch_cloudwatch.md "security_iam_region_switch_cloudwatch.md").
