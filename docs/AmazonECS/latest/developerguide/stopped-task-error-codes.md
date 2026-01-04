# Amazon ECS stopped tasks error messages

The following are the possible error messages you may receive when your task stops
unexpectedly.

To check your stopped tasks for an error message using the AWS Management Console, see [Viewing Amazon ECS stopped task errors](stopped-task-errors.md "stopped-task-errors.md").

###### Tip

You can use the [Amazon ECS MCP server](ecs-mcp-introduction.md "ecs-mcp-introduction.md")
with AI assistants to analyze task failures and container logs using natural language.

Stopped task error codes have a category associated with them, for example
"ResourceInitializationError". To get more information about each category, see the
following:

| Category                     | Learn more                                                                                                                                |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| TaskFailedToStart            | [Troubleshooting Amazon ECS TaskFailedToStart<br>errors](failed-to-start-error.md "failed-to-start-error.md")                             |
| ResourceInitializationError  | [Troubleshooting Amazon ECS<br>ResourceInitializationError errors](resource-initialization-error.md "resource-initialization-error.md")   |
| ResourceNotFoundException    | [Troubleshooting Amazon ECS ResourceNotFoundException<br>errors](resource-not-found-error.md "resource-not-found-error.md")               |
| SpotInterruptionError        | [Troubleshooting Amazon ECS SpotInterruption errors](spot-interruption-errors.md "spot-interruption-errors.md")                           |
| InternalError                | [Troubleshooting Amazon ECS InternalError errors](internal-error.md "internal-error.md")                                                  |
| OutOfMemoryError             | [Troubleshooting Amazon ECS OutOfMemoryError errors](out-of-memory.md "out-of-memory.md")                                                 |
| ContainerRuntimeError        | [Troubleshooting Amazon ECS ContainerRuntimeError errors](container-runtime-error.md "container-runtime-error.md")                        |
| ContainerRuntimeTimeoutError | [Troubleshooting Amazon ECS ContainerRuntimeTimeoutError errors](container-runtime-timeout-error.md "container-runtime-timeout-error.md") |
| CannotStartContainerError    | [Troubleshooting Amazon ECS CannotStartContainerError errors](cannot-start-container.md "cannot-start-container.md")                      |
| CannotStopContainerError     | [Troubleshooting Amazon ECS CannotStopContainerError errors](cannot-stop-container.md "cannot-stop-container.md")                         |
| CannotInspectContainerError  | [Troubleshooting Amazon ECS CannotInspectContainerError errors](cannot-inspect-container.md "cannot-inspect-container.md")                |
| CannotCreateVolumeError      | [Troubleshooting Amazon ECS CannotCreateVolumeError errors](cannot-create-volume.md "cannot-create-volume.md")                            |
| CannotPullContainer          | [CannotPullContainer task errors in Amazon ECS](task_cannot_pull_image.md "task_cannot_pull_image.md")                                    |
