# Set up a group GitLab webhook

The high-level steps to set up a group GitLab webhook are as follows.
For more information about group GitLab webhooks, see [GitLab group webhooks](gitlab-group-webhook.md "gitlab-group-webhook.md").

1. Set your project's source location to
   `CODEBUILD_DEFAULT_WEBHOOK_SOURCE_LOCATION`.
2. In the webhook's scope configuration, set the scope to `GITLAB_GROUP`.
3. Specify a name as part of the webhook's scope configuration. For group
   webhooks, this is the group name.

###### Note

If the project's source type is `GITLAB_SELF_MANAGED`, you will
also need to specify a domain as part of the webhook scope
configuration. 4. (Optional) If you would only like to receive webhook events for specific
repositories within your organization or enterprise, you can specify
`REPOSITORY_NAME` as a filter when creating the webhook. 5. When creating a group webhook, ensure that CodeBuild has permissions
to create group level webhooks within GitLab. To do so, you can
use CodeBuild OAuth though CodeConnections.
For more information, see [GitLab access in CodeBuild](access-tokens-gitlab-overview.md "access-tokens-gitlab-overview.md").

Note that group webhooks work with any of the existing GitLab webhook
event types.
