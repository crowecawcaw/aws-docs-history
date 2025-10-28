# Troubleshooting Amazon ECS CannotInspectContainerError errors

The following are some CannotInspectContainerError error messages and actions that you can take to fix the errors.

To check your stopped tasks for an error message using the AWS Management Console, see [Viewing Amazon ECS stopped task errors](stopped-task-errors.md "stopped-task-errors.md").

## CannotInspectContainerError

This error occurs when the container agent can't describe the container
through the container runtime.

When using platform version `1.3` or earlier, the Amazon ECS
agent returns the reason from Docker.

When using platform version `1.4.0` or later (Linux) or
`1.0.0` or later (Windows), the Fargate agent returns the
reason from `containerd`.

For information about how to debug and fix this issue, see [Why is my
Amazon ECS task Stopped](https://repost.aws/knowledge-center/ecs-task-stopped "https://repost.aws/knowledge-center/ecs-task-stopped") on AWS re:Post.
