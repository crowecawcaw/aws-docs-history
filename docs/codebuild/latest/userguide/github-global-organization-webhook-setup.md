# Set up a global or

organization GitHub webhook

The high-level steps to set up a global or organization GitHub webhook are as follows.
For more information about global and organization GitHub webhooks, see [GitHub global and organization
webhooks](github-global-organization-webhook.md "github-global-organization-webhook.md").

1. Set your project's source location to
   `CODEBUILD_DEFAULT_WEBHOOK_SOURCE_LOCATION`.
2. In the webhook's scope configuration, set the scope to either
   `GITHUB_ORGANIZATION` or `GITHUB_GLOBAL` depending on
   whether it should be an organization or [global webhook](https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/exploring-user-activity-in-your-enterprise/managing-global-webhooks "https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/exploring-user-activity-in-your-enterprise/managing-global-webhooks"). For more information, see [Types of
   webhooks](https://docs.github.com/en/webhooks/types-of-webhooks "https://docs.github.com/en/webhooks/types-of-webhooks").
3. Specify a name as part of the webhook's scope configuration. For organization
   webhooks, this is the organization name, and for global webhooks this is the
   enterprise name.

###### Note

If the project's source type is `GITHUB_ENTERPRISE`, you will
also need to specify a domain as part of the webhook scope
configuration. 4. (Optional) If you would only like to receive webhook events for specific
repositories within your organization or enterprise, you can specify
`REPOSITORY_NAME` as a filter when creating the webhook. 5. If you are creating an organization webhook, ensure that CodeBuild has permissions
to create organization level webhooks within GitHub. You can create a GitHub
personal access token with organization webhook permissions, or use CodeBuild OAuth.
For more information, see [GitHub and GitHub Enterprise Server access
token](access-tokens-github.md "access-tokens-github.md").

Note that organization webhooks work with any of the existing GitHub webhook
event types. 6. If you are creating a global webhook, the webhook will need to be created
manually. For more information about how to manually create a webhook within
GitHub, see [GitHub manual webhooks](github-manual-webhook.md "github-manual-webhook.md").

Note that global webhooks only support the `WORKFLOW_JOB_QUEUED`
event type. For more information, see [Tutorial: Configure a CodeBuild-hosted GitHub
Actions runner](action-runner.md "action-runner.md").
