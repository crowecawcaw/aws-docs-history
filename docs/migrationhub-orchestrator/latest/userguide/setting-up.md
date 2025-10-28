AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Setting up to use Migration Hub Orchestrator

Before you get started with AWS Migration Hub Orchestrator, ensure that users have the required
permissions.

## Permissions

By default, an IAM administrator has all the permissions that are required to
access Migration Hub Orchestrator.

The following managed policies grant permissions required to use Migration Hub Orchestrator to a
**non-administrative** IAM user.

- Console access –
  AWSMigrationHubFullAccess and
  AWSMigrationHubOrchestratorConsoleFullAccess
- Plugin –
  AWSMigrationHubOrchestratorPlugin
- Instances –
  AWSMigrationHubOrchestratorInstanceRolePolicy

For more information, see [AWS managed
policies for Migration Hub Orchestrator](security-iam-awsmanpol.md "security-iam-awsmanpol.md").
