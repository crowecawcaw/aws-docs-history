# Working with Region switch

This section provides step-by-step instructions for working with Region switch plans, which you can use to recover
multi-Region applications. Region switch enables you to create plans for both active/passive and active/active recovery approaches.

To create a recovery plan for your application, you do the following:

1. Create a Region switch plan. A plan is a structure with certain attributes, such as the
   specific AWS Regions that your application runs in. Each plan includes one or more _workflows_.

Optionally, you can create several plans, and nest those _child plans_
within an overall recovery plan. 2. Create a workflow for the plan. You can’t execute a plan without creating a workflow first. 3. In the workflow, add one or more steps that are each an _execution block_.

For example, you could add a step to scale up EC2 Auto Scaling groups in a destination Region. 4. After you add steps to your workflow, additional steps might be required, such as
configuring health checks in Amazon Route 53. Each execution block section includes the configuration information
that you need. For more information, see [Add execution blocks](working-with-rs-execution-blocks.md "working-with-rs-execution-blocks.md"). 5. To recover your application when it's running in an impaired AWS Region, execute the plan.

You can track the progress of a plan execution by viewing information in the global dashboard or a Regional
dashboard.
The following sections provide detailed information and steps for creating a plan and workflows, and
adding execution block steps in your workflows.

###### Contents

- [Create a plan](working-with-rs-create-plan.md "working-with-rs-create-plan.md")
- [Create workflows](working-with-rs-workflows.md "working-with-rs-workflows.md")
- [Add execution blocks](working-with-rs-execution-blocks.md "working-with-rs-execution-blocks.md")
- [Create child plans](working-with-rs-child-plan.md "working-with-rs-child-plan.md")
- [Create triggers](working-with-rs-triggers.md "working-with-rs-triggers.md")
- [Execute a plan](plan-execution-rs.md "plan-execution-rs.md")
  The procedures in this section illustrate how to work with plans, workflows, execution blocks, and triggers
  by using the AWS Management Console. To work with Region switch API operations instead, see [Region switch API operations](actions.md "actions.md").
