# Troubleshoot Amazon ECS Exec issues

The following are troubleshooting notes to help diagnose why you may be getting an
error when using ECS Exec.

## Verify using the Exec Checker

The ECS Exec Checker script provides a way to verify and validate that your
Amazon ECS cluster and task have met the prerequisites for using the ECS Exec feature.
The ECS Exec Checker script verifies both your AWS CLI environment and cluster and tasks
are ready for ECS Exec, by calling various APIs on your behalf. The tool requires
the latest version of the AWS CLI and that the `jq` is available. For more
information, see [ECS Exec
Checker](https://github.com/aws-containers/amazon-ecs-exec-checker "https://github.com/aws-containers/amazon-ecs-exec-checker") on GitHub.

## Error when calling

`execute-command`

If a `The execute command failed` error occurs, the following are
possible causes.

- The task does not have the required permissions. Verify that the task
  definition used to launch your task has a task IAM role defined and that
  the role has the required permissions. For more information, see [ECS Exec permissions](task-iam-roles.md#ecs-exec-required-iam-permissions "task-iam-roles.md#ecs-exec-required-iam-permissions").
- The SSM agent isn't installed or isn't running.
- There is an interface Amazon VPC endpoint for Amazon ECS, but there isn't one
  for Systems Manager Session Manager.
