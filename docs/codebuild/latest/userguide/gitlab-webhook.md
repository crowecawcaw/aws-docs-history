# GitLab webhook events

You can use webhook filter groups to specify which GitLab webhook events trigger a build.
For example, you can specify that a build is only triggered for changes to specific
branches.

You can create one or more webhook filter groups to specify which webhook events trigger a
build. A build is triggered if any filter group evaluates to true, which occurs when all the
filters in the group evaluate to true. When you create a filter group, you specify:

**An event**

For GitLab, you can choose one or more of the following events:
`PUSH`, `PULL_REQUEST_CREATED`,
`PULL_REQUEST_UPDATED`, `PULL_REQUEST_MERGED`,
`PULL_REQUEST_REOPENED`, `PULL_REQUEST_CLOSED`,
`RELEASED`, and `WORKFLOW_JOB_QUEUED`.

The webhook's event type is in its header in the `X-GitLab-Event`
field. The following table shows how `X-GitLab-Event` header values
map to the event types. For the `Merge Request Hook` webhook event,
the payload's `object_atttributes.action` will contain additional
information on merge request type.

| `X-GitLab-Event` Header value | `object_atttributes.action` | Event type              |
| ----------------------------- | --------------------------- | ----------------------- |
| `Push Hook`                   | N/A                         | `PUSH`                  |
| `Merge Request Hook`          | open                        | `PULL_REQUEST_CREATED`  |
| `Merge Request Hook`          | update                      | `PULL_REQUEST_UPDATED`  |
| `Merge Request Hook`          | merge                       | `PULL_REQUEST_MERGED`   |
| `Merge Request Hook`          | reopen                      | `PULL_REQUEST_REOPENED` |
| `Merge Request Hook`          | close                       | `PULL_REQUEST_CLOSED`   |
| `Release Hook`                | create, update              | `RELEASED`              |
| `Job Hook`                    | N/A                         | `WORKFLOW_JOB_QUEUED`   |

For `PULL_REQUEST_MERGED`, if a pull request is merged with the
squash strategy and the pull request branch is closed, the original pull request
commit no longer exists. In this case, the
`CODEBUILD_WEBHOOK_MERGE_COMMIT` environment variable contains
the identifier of the squashed merge commit.

**One or more optional filters**

Use a regular expression to specify a filter. For an event to trigger a build,
every filter within the group associated with it must evaluate to true.

`ACTOR_ACCOUNT_ID` (`ACTOR_ID` in the
console)

A webhook event triggers a build when a GitLab account ID matches
the regular expression pattern. This value appears in the
`account_id` property of the `actor`
object in the webhook filter payload.

`HEAD_REF`

A webhook event triggers a build when the head reference matches
the regular expression pattern (for example,
`refs/heads/branch-name` and
`refs/tags/tag-name`). A `HEAD_REF` filter
evaluates the Git reference name for the branch or tag. The branch
or tag name appears in the `name` field of the
`new` object in the `push` object of the
webhook payload. For pull request events, the branch name appears in
the `name` field in the `branch` object of the
`source` object in the webhook payload.

`BASE_REF`

A webhook event triggers a build when the base reference matches
the regular expression pattern. A `BASE_REF` filter works
with pull request events only (for example,
`refs/heads/branch-name`). A `BASE_REF`
filter evaluates the Git reference name for the branch. The branch
name appears in the `name` field of the
`branch` object in the `destination`
object in the webhook payload.

`FILE_PATH`

A webhook triggers a build when the path of a changed file matches
the regular expression pattern.

`COMMIT_MESSAGE`

A webhook triggers a build when the head commit message matches
the regular expression pattern.

`WORKFLOW_NAME`

A webhook triggers a build when the workflow name matches
the regular expression pattern.

###### Note

You can find the webhook payload in the webhook settings of your GitLab repository.

###### Topics

- [Filter GitLab webhook events
  (console)](gitlab-webhook-events-console.md "gitlab-webhook-events-console.md")
- [Filter GitLab webhook events (SDK)](gitlab-webhook-events-sdk.md "gitlab-webhook-events-sdk.md")
- [Filter GitLab webhook events (CloudFormation)](gitlab-webhook-events-cfn.md "gitlab-webhook-events-cfn.md")
