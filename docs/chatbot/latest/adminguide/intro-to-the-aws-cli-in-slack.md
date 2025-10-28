AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# AWS CLI command syntax in Amazon Q Developer in chat applications

After you set up the Amazon Q Developer in chat applications, you run commands with the
following prefix:

`@Amazon Q`

###### Note

If you are using Slack and AWS is not listed as a valid member of the channel, you need to add the Amazon Q Developer in chat applications app to the Slack workspace and invite it to the channel. For more information, see the [Getting started guide for
Amazon Q Developer in chat applications](getting-started.md "getting-started.md").

###### Tip

Instead of entering `@Amazon Q`, you can enter `@Q` and choose the autocomplete recommendation that matches the app name.

The Amazon Q Developer in chat applications command syntax is the same as you would use in a terminal:

`@Amazon Q `service`
`command --options``

###### Note

You can specify parameters with either a double hyphen (`--option`) or a single hyphen (`-option`).
This allows you to use a mobile device to run commands without running into issues with the mobile device automatically converting a double hyphen to a long dash.

###### Note

AWS CLI commands run from AWS Chatbot have an execution [timeout](../../../whitepapers/latest/serverless-architectures-lambda/timeout.md "../../../whitepapers/latest/serverless-architectures-lambda/timeout.md") of 15 seconds. If a command response is not received within 15 seconds, you receive a timeout error message.
If you have longer running jobs, such as AWS Lambda functions, you should invoke them asynchronously from Amazon Q Developer in chat applications.
The maximum allowable Lambda function execution timeout is 900 seconds (15 minutes).
For more information about asynchronous invocation, see [Asynchronous invocation](../../../lambda/latest/dg/invocation-async.md "../../../lambda/latest/dg/invocation-async.md") in the _AWS Lambda Developer Guide_.

For example, enter the following read-only command to view a list of your Lambda
functions:

`@Amazon Q lambda list-functions`

Enter the following commands to list and chart CloudWatch alarms:

`@Amazon Q cloudwatch describe-alarms --state ALARM`

You can also use CLI commands to change you AWS resources. For example, enter the following command to change your Kinesis shards:

`@Amazon Q kinesis update-shard-count 
 --stream-name samplestream 
 --scaling-type UNIFORM_SCALING 
 --target-shard-count 6`

You can enter a complete AWS CLI command with all the parameters, or you can enter the command
without parameters and Amazon Q Developer in chat applications prompts you for missing parameters.

For more information on commonly used CLI commands, see [Using CLI commands with Amazon Q Developer in chat applications - Common
use
cases](common-use-cases.md "common-use-cases.md"). For an exhaustive list of CLI commands, see the [AWS CLI Command Reference](../../../cli/latest/index.md "../../../cli/latest/index.md").

###### Note

If you find you are unable to run commands, you may need to switch your user role or contact your administrator to find out what actions are permissible.

The following limitations apply to running AWS CLI commands in your chat rooms:

- You may experience some latency when invoking commands through Amazon Q Developer in chat applications.
- Regardless of their Amazon Q Developer in chat applications role permissions, users cannot run IAM, AWS Security Token Service, or AWS Key Management Service
  commands within chat channels.
- Amazon S3 service commands support Linux-style command aliases such as **ls** and **cp**. Amazon Q Developer in chat applications does not support Amazon S3 command
  aliases for commands in Slack.
- Users cannot display or decrypt secret keys or key pairs for any AWS service, or pass
  IAM credentials.
- You can't use AWS CLI command memory (that is, recent commands appear when the user presses
  up arrow or down arrow keys) in the chat channel. You must enter, or copy and paste each AWS CLI
  command in the chat channel.
- You can create AWS support cases through your chat channels. You cannot add attachments
  to these cases from the chat channel.
- Chat channels do not support standard AWS CLI pagination.
