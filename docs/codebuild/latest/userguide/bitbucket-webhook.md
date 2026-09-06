

# Bitbucket webhook events
<a name="bitbucket-webhook"></a>

You can use webhook filter groups to specify which Bitbucket webhook events trigger a build. For example, you can specify that a build is only triggered for changes to specific branches. 

You can create one or more webhook filter groups to specify which webhook events trigger a build. A build is triggered if any filter group evaluates to true, which occurs when all the filters in the group evaluate to true. When you create a filter group, you specify: 

**An event**  
For Bitbucket, you can choose one or more of the following events:  
+ `PUSH`
+ `PULL_REQUEST_CREATED`
+ `PULL_REQUEST_UPDATED`
+ `PULL_REQUEST_MERGED`
+ `PULL_REQUEST_CLOSED`
The webhook's event type is in its header in the `X-Event-Key` field. The following table shows how `X-Event-Key` header values map to the event types.  
You must enable the `merged` event in your Bitbucket webhook setting if you create a webhook filter group that uses the `PULL_REQUEST_MERGED` event type. You must also enable the `declined` event in your Bitbucket webhook setting if you create a webhook filter group that uses the `PULL_REQUEST_CLOSED` event type.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/codebuild/latest/userguide/bitbucket-webhook.html)
For `PULL_REQUEST_MERGED`, if a pull request is merged with the squash strategy and the pull request branch is closed, the original pull request commit no longer exists. In this case, the `CODEBUILD_WEBHOOK_MERGE_COMMIT` environment variable contains the identifier of the squashed merge commit.

**One or more optional filters**  
Use a regular expression to specify a filter. For an event to trigger a build, every filter within the group associated with it must evaluate to true.  
CodeBuild evaluates filter patterns using RE2 regular expression syntax, which does not support lookahead, lookbehind, backreferences, or atomic groups. For more information, see the RE2 [Syntax](https://github.com/google/re2/wiki/Syntax) page on the GitHub website.    
`ACTOR_ACCOUNT_ID` (`ACTOR_ID` in the console)  
A webhook event triggers a build when a Bitbucket account ID matches the regular expression pattern. This value appears in the `account_id` property of the `actor` object in the webhook filter payload.  
`HEAD_REF`  
A webhook event triggers a build when the head reference matches the regular expression pattern (for example, `refs/heads/branch-name` and `refs/tags/tag-name`). A `HEAD_REF` filter evaluates the Git reference name for the branch or tag. The branch or tag name appears in the `name` field of the `new` object in the `push` object of the webhook payload. For pull request events, the branch name appears in the `name` field in the `branch` object of the `source` object in the webhook payload.  
`BASE_REF`  
A webhook event triggers a build when the base reference matches the regular expression pattern. A `BASE_REF` filter works with pull request events only (for example, `refs/heads/branch-name`). A `BASE_REF` filter evaluates the Git reference name for the branch. The branch name appears in the `name` field of the `branch` object in the `destination` object in the webhook payload.  
`FILE_PATH`  
A webhook triggers a build when the path of a changed file matches the regular expression pattern.  
The `FILE_PATH` filter is evaluated against the first 3,000 changed files in a push or pull request. To make sure the filter is applied as intended, keep the number of changed files within this limit. For pull request events, we also recommend using a pull request build policy to control which pull requests can start a build.  
`COMMIT_MESSAGE`  
A webhook triggers a build when the head commit message matches the regular expression pattern.  
`WORKFLOW_NAME`  
A webhook triggers a build when the workflow name matches the regular expression pattern.

**Note**  
You can find the webhook payload in the webhook settings of your Bitbucket repository. 

**Topics**
+ [Filter Bitbucket webhook events (console)](bitbucket-webhook-events-console.md)
+ [Filter Bitbucket webhook events (SDK)](bitbucket-webhook-events-sdk.md)
+ [Filter Bitbucket webhook events (CloudFormation)](bitbucket-webhook-events-cfn.md)