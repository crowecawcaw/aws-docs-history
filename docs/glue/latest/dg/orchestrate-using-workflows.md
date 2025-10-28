# Performing complex ETL activities using

blueprints and workflows in AWS Glue

Some of your organization's complex extract, transform, and load (ETL) processes might best
be implemented by using multiple, dependent AWS Glue jobs and crawlers. Using AWS Glue _workflows_, you can design a complex multi-job, multi-crawler ETL process
that AWS Glue can run and track as single entity. After you create a workflow and specify the
jobs, crawlers, and triggers in the workflow, you can run the workflow on demand or on a
schedule.

###### Topics

- [Overview of workflows in AWS Glue](workflows_overview.md "workflows_overview.md")
- [Creating and building out a workflow manually
  in AWS Glue](creating_running_workflows.md "creating_running_workflows.md")
- [Starting an AWS Glue workflow with an Amazon EventBridge event](starting-workflow-eventbridge.md "starting-workflow-eventbridge.md")
- [Viewing the EventBridge events that started a
  workflow](viewing-start-event-info.md "viewing-start-event-info.md")
- [Running and monitoring a workflow in
  AWS Glue](running_monitoring_workflow.md "running_monitoring_workflow.md")
- [Stopping a workflow run](workflow-stopping.md "workflow-stopping.md")
- [Repairing and resuming a workflow run](resuming-workflow.md "resuming-workflow.md")
- [Getting and setting workflow run properties in
  AWS Glue](workflow-run-properties-code.md "workflow-run-properties-code.md")
- [Querying workflows using the AWS Glue API](workflows_api_concepts.md "workflows_api_concepts.md")
- [Blueprint and workflow restrictions in
  AWS Glue](blueprint_workflow_restrictions.md "blueprint_workflow_restrictions.md")
- [Troubleshooting blueprint errors in
  AWS Glue](blueprint_workflow_troubleshoot.md "blueprint_workflow_troubleshoot.md")
- [Permissions for personas and roles for
  AWS Glue blueprints](blueprints-personas-permissions.md "blueprints-personas-permissions.md")
