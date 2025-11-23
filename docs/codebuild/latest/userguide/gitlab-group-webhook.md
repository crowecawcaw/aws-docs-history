# GitLab group webhooks

You can use CodeBuild GitLab group webhooks to start builds on webhook events from any repository
within a GitLab group. Group webhooks work with any of the existing GitLab webhook event
types, and can be configured by adding a scope configuration when creating a CodeBuild webhook. You can also
use group webhooks to [set up self-hosted GitLab
runners within CodeBuild](gitlab-runner.md "gitlab-runner.md") in order to receive `WORKFLOW_JOB_QUEUED` events
from multiple repositories within a single project.

###### Topics

- [Set up a group GitLab webhook](gitlab-group-webhook-setup.md "gitlab-group-webhook-setup.md")
- [Filter GitLab group webhook events (console)](gitlab-group-webhook-events-console.md "gitlab-group-webhook-events-console.md")
- [Filter GitLab group
  webhook events (CloudFormation)](gitlab-group-webhook-events-cfn.md "gitlab-group-webhook-events-cfn.md")
