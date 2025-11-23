# GitHub global and organization

webhooks

You can use CodeBuild GitHub global or organization webhooks to start builds on webhook events
from any repository within a GitHub organization or enterprise. Global and organization
webhooks work with any of the existing GitHub webhook event types, and can be configured by
adding a scope configuration when creating a CodeBuild webhook. You can also use global and
organization webhooks to [set up self-hosted GitHub Action
runners within CodeBuild](action-runner.md "action-runner.md") in order to receive `WORKFLOW_JOB_QUEUED` events
from multiple repositories within a single project.

###### Topics

- [Set up a global or
  organization GitHub webhook](github-global-organization-webhook-setup.md "github-global-organization-webhook-setup.md")
- [Filter GitHub global
  or organization webhook events (console)](github-global-organization-webhook-events-console.md "github-global-organization-webhook-events-console.md")
- [Filter GitHub organization
  webhook events (CloudFormation)](github-organization-webhook-events-cfn.md "github-organization-webhook-events-cfn.md")
