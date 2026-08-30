# Job event Slack notifications with Lambda and EventBridge

The
[job\_events\_slack\_lambda](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/notification_templates/job_events_slack_lambda "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/notification_templates/job_events_slack_lambda")
CloudFormation template on the GitHub website sends a Slack notification whenever a job completes
(`SUCCEEDED`) or fails (`FAILED`). Use it as a
starting point for connecting a Lambda function to Deadline Cloud job events
through EventBridge. You can adapt the function to send an email, open a
ticket, update a dashboard, or trigger a downstream workflow.

The template creates the following resources:

- A Lambda function is defined inline in the template using only
  the Python standard library. It formats the job event and posts it
  to a Slack Incoming Webhook URL stored in its
  `SLACK_WEBHOOK_URL` environment variable.
- An EventBridge rule matches `Job Run Status Change` events
  with a `taskRunStatus` of `SUCCEEDED` or
  `FAILED`, and invokes the function. You can scope the
  rule to a single farm.
- An execution role grants the function only CloudWatch Logs write access.
  A permission allows EventBridge to invoke the function.
  Many messaging apps expose the same style of incoming webhook. To
  target Microsoft Teams, Discord, Google Chat, or Mattermost instead, set
  that app's webhook URL and adjust the JSON body the function builds; the
  README links each app's webhook documentation.

For more information about the events Deadline Cloud publishes to EventBridge, see
[Managing Deadline Cloud events using Amazon EventBridge](eventbridge-integration.md "eventbridge-integration.md"). For budget threshold
notifications, see [Budget threshold notifications to email and Slack with CloudFormation](examples-cfn-budget-notifications.md "examples-cfn-budget-notifications.md").
