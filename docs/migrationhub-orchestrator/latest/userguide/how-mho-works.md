AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# How AWS Migration Hub Orchestrator works

You can simplify and automate the migration of your on-premises servers and applications to
AWS Cloud using AWS Migration Hub Orchestrator.

###### Contents

- [Home Region](#setting-up-home-region "#setting-up-home-region")
- [Select a template](#select-template "#select-template")
- [Create a workflow](#create-workflow "#create-workflow")
- [Run the workflow](#run-workflow "#run-workflow")

## Home Region

The data stored in the AWS Migration Hub (Migration Hub) home Region provides a single repository of
discovery and migration planning information for your entire migration portfolio. The data
stored in the home Region from the discovery and migration tools is used to track the progress
of your migrations regardless of the migrating application’s target Region. For more
information, see [Migration Hub home Region](../../../migrationhub/latest/ug/home-region.md "../../../migrationhub/latest/ug/home-region.md").

## Select a template

Based on your migration requirements, select a template to begin your migration journey
with Migration Hub Orchestrator. You can see the steps of a template by selecting a template card, and then
choosing **Preview**.

For more information about the different templates offered by Migration Hub Orchestrator, see [Templates.](templates.md "templates.md")

## Create a workflow

After selecting your template, you can start configuring your migration workflow. Ensure
that you meet the prerequisites of your selected template, and that you have defined the
applications you want to migrate in [AWS Application Discovery Service](https://console.aws.amazon.com/discovery/home "https://console.aws.amazon.com/discovery/home").

## Run the workflow

After you have configured your workflow, you can run the workflow. You can now track the
progress of your migration and customize your workflow. For more information, see [Migration
workflows](migration-workflows.md "migration-workflows.md").
