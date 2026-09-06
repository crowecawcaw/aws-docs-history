

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# Setting up to use Migration Hub Orchestrator
<a name="setting-up"></a>

Before you get started with AWS Migration Hub Orchestrator, ensure that users have the required permissions.

## Permissions
<a name="setting-up-create-iam-user"></a>

By default, an IAM administrator has all the permissions that are required to access Migration Hub Orchestrator.

The following managed policies grant permissions required to use Migration Hub Orchestrator to a **non-administrative** IAM user.
+ **Console access** – AWSMigrationHubFullAccess and AWSMigrationHubOrchestratorConsoleFullAccess
+ **Plugin** – AWSMigrationHubOrchestratorPlugin
+ **Instances** – AWSMigrationHubOrchestratorInstanceRolePolicy

For more information, see [AWS managed policies for Migration Hub Orchestrator](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/security-iam-awsmanpol.html).