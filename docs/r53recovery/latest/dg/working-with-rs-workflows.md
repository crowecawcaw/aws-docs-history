

# Create Region switch plan workflows
<a name="working-with-rs-workflows"></a>

After you create a Region switch plan, you need to define and create workflows that specify the recovery process for your application. For each plan, you define one or more workflows that complete recovery for your application. In each workflow, you add steps that include *execution blocks* that define each action you want Region switch to perform for your application recovery.

The number of workflows that you create depends on your application deployment scenario and your preferences for managing recovery. For example:
+ If your Region switch plan is for an active/active application deployment, you also need to create a deactivation workflow. This means that for or active/active deployments, you'll have a minimum of two workflows: an activation workflow and a deactivation workflow.
+ If your Region switch plan is for an active/passive application deployment, you have a primary and a secondary Region. If you choose to have separate activation workflows for each Region, you'll create two workflows: one for each Region.

# To create Region switch plan workflows


1. In the Region switch plan that you created, choose **Build workflows**.

1. Select one of the following workflow options:
   + **Build the same activation workflow for all Regions** - Enables you to use the same activation workflow across Regions.
   + **Build workflows separately for each Region** - Builds an individual activation workflow for each Region.

1. Optionally, provide a description for each workflow.

1. Define the workflow required to recover your application. In your workflow, you add *execution blocks* to define the steps that you want Region switch to perform for your recovery. Each execution block defines actions, such as application traffic rerouting or database recovery in an activating Region, and supports resources in another AWS account. You can opt to have execution blocks run in parallel or sequentially. For detailed information about the specific execution blocks that you can add to workflows, see [Add execution blocks](working-with-rs-execution-blocks.md).

1. Depending on the workflow option that you selected, do the following:
   + If you selected **Build the same activation workflow for all Regions**, one activation workflow is required.
   + If you selected **Build workflows separately for each Region**, two activation workflows are required.

   For active/active plans, you must define both an activation workflow and a deactivation workflow.