

# Troubleshooting Amazon ECS ContainerRuntimeError errors
<a name="container-runtime-error"></a>

The following are some ContainerRuntimeError error messages and actions that you can take to fix the errors.

To check your stopped tasks for an error message using the AWS Management Console, see [Viewing Amazon ECS stopped task errors](stopped-task-errors.md).

## ContainerRuntimeError
<a name="container-runtime-error-1"></a>

This error occurs when the agent receives an unexpected error from `containerd` for a runtime-specific operation. This error is usually caused by an internal failure in the agent or the `containerd` runtime.

This error only occurs if you use platform version `1.4.0` or later (Linux) or `1.0.0` or later (Windows).

For information about how to debug and fix this issue, see [Why is my Amazon ECS task Stopped](https://repost.aws/knowledge-center/ecs-task-stopped) on AWS re:Post.