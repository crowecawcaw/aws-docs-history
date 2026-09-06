

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# How AWS Migration Hub Orchestrator works
<a name="how-mho-works"></a>

You can simplify and automate the migration of your on-premises servers and applications to AWS Cloud using AWS Migration Hub Orchestrator.

**Topics**
+ [Home Region](#setting-up-home-region)
+ [Select a template](#select-template)
+ [Create a workflow](#create-workflow)
+ [Run the workflow](#run-workflow)

## Home Region
<a name="setting-up-home-region"></a>

The data stored in the AWS Migration Hub (Migration Hub) home Region provides a single repository of discovery and migration planning information for your entire migration portfolio. The data stored in the home Region from the discovery and migration tools is used to track the progress of your migrations regardless of the migrating application’s target Region. For more information, see [Migration Hub home Region](https://docs.aws.amazon.com/migrationhub/latest/ug/home-region.html).

## Select a template
<a name="select-template"></a>

Based on your migration requirements, select a template to begin your migration journey with Migration Hub Orchestrator. You can see the steps of a template by selecting a template card, and then choosing **Preview**.

For more information about the different templates offered by Migration Hub Orchestrator, see [Templates.](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/templates.html)

## Create a workflow
<a name="create-workflow"></a>

After selecting your template, you can start configuring your migration workflow. Ensure that you meet the prerequisites of your selected template, and that you have defined the applications you want to migrate in [AWS Application Discovery Service](https://console.aws.amazon.com/discovery/home).

## Run the workflow
<a name="run-workflow"></a>

After you have configured your workflow, you can run the workflow. You can now track the progress of your migration and customize your workflow. For more information, see [Migration workflows](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/migration-workflows.html).