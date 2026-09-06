

# Troubleshooting Amazon ECS ContainerRuntimeTimeoutError errors
<a name="container-runtime-timeout-error"></a>

The following are some ContainerRuntimeTimeoutError error messages and actions that you can take to fix the errors.

To check your stopped tasks for an error message using the AWS Management Console, see [Viewing Amazon ECS stopped task errors](stopped-task-errors.md).

## Could not transition to running; timed out after waiting 1m or Docker timeout error
<a name="container-runtime-timeout-error-1"></a>

This error occurs when a container can't transition to either a `RUNNING` or `STOPPED` state within the timeout period. The reason and timeout value is provided in the error message.