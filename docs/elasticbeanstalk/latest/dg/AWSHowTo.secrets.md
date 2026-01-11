# Troubleshooting secrets integration with Elastic Beanstalk environment variables

###### Try Amazon Q Developer CLI for AI-assisted troubleshooting

Amazon Q Developer CLI can help you troubleshoot environment issues quickly. The Q CLI provides
solutions by checking environment status, reviewing events, analyzing logs, and asking clarifying questions. For
more information and detailed walkthroughs, see [Troubleshooting Elastic Beanstalk Environments with Amazon Q Developer CLI](https://aws.amazon.com/blogs/devops/troubleshooting-elastic-beanstalk-environments-with-amazon-q-developer-cli/ "https://aws.amazon.com/blogs/devops/troubleshooting-elastic-beanstalk-environments-with-amazon-q-developer-cli/") in the AWS blogs.

This section provides guidance for troubleshooting issues with secrets in your Elastic Beanstalk environment.

**Event:**
_Instance deployment failed to get one or more secrets_

This message indicates that Elastic Beanstalk was not able to fetch one or more of the secrets specified during your application deployment.

- Check that the resources specified by the ARN values in your environment variable configuration exist.
- Confirm that your Elastic Beanstalk EC2 instance profile role has the [required IAM
  permissions](AWSHowTo.secrets.md#AWSHowTo.secrets.IAM-permissions.secrets-manager "AWSHowTo.secrets.md#AWSHowTo.secrets.IAM-permissions.secrets-manager") to access the resources.
- If this event was triggered through the `RestartAppServer` operation, once the issue is fixed, retry the `RestartAppServer`
  call to resolve the issue.
- If the event was triggered through an `UpdateEnvironment` call, retry the `UpdateEnvironment` operation.
  For examples of these commands, see [_AWS CLI
  examples for Elastic Beanstalk_](../../../cli/latest/userguide/cli_elastic-beanstalk_code_examples.md "../../../cli/latest/userguide/cli_elastic-beanstalk_code_examples.md"). For more information about the API actions for these operations, see the
  _[AWS Elastic Beanstalk API Reference](../api.md "../api.md")_.

**Event:**
_Instance deployment detected one or more multiline environment values, which are not supported for this platform_

Multiline variables are not supported for Amazon Linux 2 platforms, excluding Docker and ECS managed Docker platforms. For available options to proceed, see
[Multiline values](AWSHowTo.secrets.md#AWSHowTo.secrets.multiline "AWSHowTo.secrets.md#AWSHowTo.secrets.multiline").

**Event:**
_CreateEnvironment fails when a secret is specified_

When `CreateEnvironment` fails and you have secrets as environment variables, you need to address the underlying issue and then use
`UpdateEnvironment` to complete the environment setup. Do not use `RestartAppServer`, as it will not be sufficient to bring the
environment up in this situation. For examples of these commands, see [_AWS CLI examples for Elastic Beanstalk_](../../../cli/latest/userguide/cli_elastic-beanstalk_code_examples.md "../../../cli/latest/userguide/cli_elastic-beanstalk_code_examples.md"). For more information about
the API actions for these operations, see the _[AWS Elastic Beanstalk API Reference](../api.md "../api.md")_.
