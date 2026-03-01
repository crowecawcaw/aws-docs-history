# Troubleshooting Amazon ECS CannotStartContainerError errors

The following are some CannotStartContainerError error messages and actions that you can take to fix the errors.

To check your stopped tasks for an error message using the AWS Management Console, see [Viewing Amazon ECS stopped task errors](stopped-task-errors.md "stopped-task-errors.md").

## failed to get container status: `<reason>`

This error occurs when a container can't be started.

If your container attempts to exceed the memory specified here, the container is
stopped. Increase the memory presented to the container. This is the `memory`
parameter in the task definition. For more information, see [Memory](task_definition_parameters.md#container_definition_memory "task_definition_parameters.md#container_definition_memory").
