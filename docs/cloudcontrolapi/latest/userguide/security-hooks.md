# CloudFormation Hooks

AWS CloudFormation Hooks is a feature that you can use to ensure that your AWS Cloud Control API resources are compliant with your
organization's security, operational, and cost optimization best practices. With Hooks, you can provide code
that proactively inspects the configuration of your resources before provisioning. If non-compliant resources
are found, Cloud Control API either fails the operation and prevents the resources from being provisioned, or emits a
warning and allows the provisioning operation to continue. You can use Hooks to evaluate your Cloud Control API resource
configurations prior to create and update operations.

## Creating a Hook to validate Cloud Control API resource configurations

You can create a Hook to validate your Cloud Control API resource configuration using either the CloudFormation console,
the AWS Command Line Interface (AWS CLI), or CloudFormation. For more information, see
[Creating and managing AWS CloudFormation Hooks](../../../cloudformation-cli/latest/hooks-userguide/creating-and-managing-hooks.md "../../../cloudformation-cli/latest/hooks-userguide/creating-and-managing-hooks.md").

## Targeting Cloud Control API for validation

You can configure your CloudFormation Hooks to target `CLOUD_CONTROL` operations in your Hook’s
`TargetOperations` configuration.

For more information on using `TargetOperations` with Guard Hooks, see [Write Guard rules to evaluate resources for Guard Hooks](../../../cloudformation-cli/latest/hooks-userguide/guard-hooks-write-rules.md "../../../cloudformation-cli/latest/hooks-userguide/guard-hooks-write-rules.md").

For more information on using `TargetOperations` with Lambda Hooks, see [Create Lambda functions to evaluate resources for Lambda Hooks](../../../cloudformation-cli/latest/hooks-userguide/lambda-hooks-create-lambda-function.md "../../../cloudformation-cli/latest/hooks-userguide/lambda-hooks-create-lambda-function.md").

## Reviewing Hook invocation results

You can view the results of your invocation by calling `GetResourceRequestStatus` using the `RequestToken`.
