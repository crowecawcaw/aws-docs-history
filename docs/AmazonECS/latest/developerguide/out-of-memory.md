# Troubleshooting Amazon ECS OutOfMemoryError errors

The following are some OutOfMemoryError error messages and actions that you can take to
fix the errors.

To check your stopped tasks for an error message using the AWS Management Console, see [Viewing Amazon ECS stopped task errors](stopped-task-errors.md "stopped-task-errors.md").

## container killed due to memory usage

This error occurs when a container exits due to processes in the container consuming
more memory than was allocated in the task definition, or due to host or operating
system constraints.
