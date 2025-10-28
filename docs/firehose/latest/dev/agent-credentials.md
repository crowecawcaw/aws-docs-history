# Manage AWS credentials

Manage your AWS credentials using one of the following methods:

- Create a custom credentials provider. For details, see [Create custom credential providers](custom-cred-provider.md "custom-cred-provider.md").
- Specify an IAM role when you launch your EC2 instance.
- Specify AWS credentials when you configure the agent (see the entries for
  `awsAccessKeyId` and `awsSecretAccessKey` in the
  configuration table under [Specify agent configuration settings](agent-config-settings.md "agent-config-settings.md")).
- Edit `/etc/sysconfig/aws-kinesis-agent` to specify your AWS Region
  and AWS access keys.
- If your EC2 instance is in a different AWS account, create an IAM role to
  provide access to the Amazon Data Firehose service. Specify that role when you configure the
  agent (see [assumeRoleARN](agent-config-settings.md#assumeRoleARN "agent-config-settings.md#assumeRoleARN") and [assumeRoleExternalId](agent-config-settings.md#assumeRoleExternalId "agent-config-settings.md#assumeRoleExternalId")). Use one of the
  previous methods to specify the AWS credentials of a user in the other account
  who has permission to assume this role.
