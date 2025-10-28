# CloudWatch agent credentials

preference

This section outlines the credentials provider chain the CloudWatch agent uses to obtain
credentials when communicating with other AWS services and APIs. The ordering is as follows:

###### Note

The preferences listed in numbers two through five are the same preference order as
defined in the AWS SDK. For more information, see [Specifying
Credentials](../../../sdk-for-go/v1/developer-guide/configuring-sdk.md#specifying-credentials "../../../sdk-for-go/v1/developer-guide/configuring-sdk.md#specifying-credentials") in the SDK documentation.

1. Shared config and credentials files as defined in the CloudWatch agent’s
   `common-config.toml` file. For more information, see [Install the CloudWatch agent using
   AWS Systems Manager](installing-cloudwatch-agent-ssm.md "installing-cloudwatch-agent-ssm.md").
2. AWS SDK environment variables

###### Important

On Linux, if you run the CloudWatch agent using the
`amazon-cloudwatch-agent-ctl` script, the script starts the agent as a
`systemd` service. In this case, environment variables such as
`HOME`, `AWS_ACCESS_KEY_ID`, and
`AWS_SECRET_ACCESS_KEY` are not accessible by the agent. 3. Shared configuration and credentials files found in
`$HOME/%USERPROFILE%`

###### Note

The CloudWatch agent looks for `.aws/credentials` in `$HOME` for
Linux and MacOS and looks in `%USERPROFILE%` for Windows. Unlike the AWS
SDK, the CloudWatch agent does not have fallback methods to determine the home directory if
the environment variables are inaccessible. This difference in behavior is to maintain
backwards compatibility with earlier implementations of the AWS SDK.

Furthermore, unlike with the shared credentials found in
`common-config.toml`, if the AWS SDK-derived shared credentials
expire and are rotated, the renewed credentials are not automatically picked up by the
CloudWatch agent and require a restart of the agent to do so. 4. An AWS Identity and Access Management role for tasks if an application is present that uses an Amazon Elastic Container Service task
definition or a RunTask API operation. 5. An instance profile attached to an Amazon EC2 instance.
As a best practice, we recommend that you specify credentials in the following order when
you use the CloudWatch agent.

1. Use IAM roles for tasks if your application uses an Amazon Elastic Container Service task definition or a
   RunTask API operation.
2. Use IAM roles if your application runs on an Amazon EC2 instance.
3. Use the CloudWatch agent `common-config.toml` file to specify the
   credentials file. This credentials file is the same one used by other AWS SDKs and the
   AWS CLI. If you’re already using a shared credentials file, you can also use it for this
   purpose. If you provide it by using the CloudWatch agent’s
   `common-config.toml` file, you ensure that the agent will consume
   rotated credentials when they expire and get replaced without requiring you to restart the
   agent.
4. Use environment variables. Setting environment variables is useful if you’re doing
   development work on a computer other than an Amazon EC2 instance.

###### Note

If you send telemetry to a different account as explained in [Sending metrics, logs, and
traces to a different account](CloudWatch-Agent-common-scenarios.md#CloudWatch-Agent-send-to-different-AWS-account "CloudWatch-Agent-common-scenarios.md#CloudWatch-Agent-send-to-different-AWS-account"), the CloudWatch agent uses the
credentials provider chain described in this section to obtain the initial set of
credentials. It then uses those credentials when assuming the IAM role specified by
`role_arn` in the CloudWatch agent configuration file.
