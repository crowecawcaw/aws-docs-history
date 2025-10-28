# Bitbucket webhook events

You can use webhook filter groups to specify which Bitbucket webhook events trigger a
build. For example, you can specify that a build is only triggered for changes to specific
branches.

You can create one or more webhook filter groups to specify which webhook events trigger a
build. A build is triggered if any filter group evaluates to true, which occurs when all the
filters in the group evaluate to true. When you create a filter group, you specify:

**An event**

For Bitbucket, you can choose one or more of the following events:

- `PUSH`
- `PULL_REQUEST_CREATED`
- `PULL_REQUEST_UPDATED`
- `PULL_REQUEST_MERGED`
- `PULL_REQUEST_CLOSED`

The webhook's event type is in its header in the `X-Event-Key`
field. The following table shows how `X-Event-Key` header values map
to the event types.

###### Note

You must enable the `merged` event in your Bitbucket webhook
setting if you create a webhook filter group that uses the
`PULL_REQUEST_MERGED` event type. You must also enable
the `declined` event in your Bitbucket webhook setting
if you create a webhook filter group that uses the `PULL_REQUEST_CLOSED` event type.

| `X-Event-Key` Header value | Event type             |
| -------------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `repo:push`                | `PUSH`                 |
| `pullrequest:created`      | `PULL_REQUEST_CREATED` |
| `pullrequest:updated`      | `PULL_REQUEST_UPDATED` |
| `pullrequest:fulfilled`    | `PULL_REQUEST_MERGED`  |
| `pullrequest:rejected`     | `PULL_REQUEST_CLOSED`  | For `PULL_REQUEST_MERGED`, if a pull request is merged with the squash strategy and the pull request branch is closed, the original pull request commit no longer exists. In this case, the `CODEBUILD_WEBHOOK_MERGE_COMMIT` environment variable contains the identifier of the squashed merge commit. **One or more optional filters** Use a regular expression to specify a filter. For an event to trigger a build, every filter within the group associated with it must evaluate to true. `ACTOR_ACCOUNT_ID` (`ACTOR_ID` in the console) A webhook event triggers a build when a Bitbucket account ID matches the regular expression pattern. This value appears in the `account_id` property of the `actor` object in the webhook filter payload. `HEAD_REF` A webhook event triggers a build when the head reference matches the regular expression pattern (for example, `refs/heads/branch-name` and `refs/tags/tag-name`). A `HEAD_REF` filter evaluates the Git reference name for the branch or tag. The branch or tag name appears in the `name` field of the `new` object in the `push` object of the webhook payload. For pull request events, the branch name appears in the `name` field in the `branch` object of the `source` object in the webhook payload. `BASE_REF` A webhook event triggers a build when the base reference matches the regular expression pattern. A `BASE_REF` filter works with pull request events only (for example, `refs/heads/branch-name`). A `BASE_REF` filter evaluates the Git reference name for the branch. The branch name appears in the `name` field of the `branch` object in the `destination` object in the webhook payload. `FILE_PATH` A webhook triggers a build when the path of a changed file matches the regular expression pattern. `COMMIT_MESSAGE` A webhook triggers a build when the head commit message matches the regular expression pattern. `WORKFLOW_NAME` A webhook triggers a build when the workflow name matches the regular expression pattern. ###### Note You can find the webhook payload in the webhook settings of your Bitbucket repository. ###### Topics <br>• [Filter Bitbucket webhook events (console)](bitbucket-webhook-events-console.md "bitbucket-webhook-events-console.md") <br>• [Filter Bitbucket webhook events (SDK)](bitbucket-webhook-events-sdk.md "bitbucket-webhook-events-sdk.md") <br>• [Filter Bitbucket webhook events (AWS CloudFormation)](bitbucket-webhook-events-cfn.md "bitbucket-webhook-events-cfn.md") |
