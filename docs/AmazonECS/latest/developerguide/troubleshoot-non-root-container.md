# Container can't write to Amazon EBS volume

Non-root user without proper permissions

When you specify a non-root user in your container definition, Amazon ECS automatically configures the volume with group-based permissions to allow write access. However, if you're still experiencing permission issues:

- Verify that the `user` parameter is correctly specified in your container definition using the format `uid:gid` (for example, `1001:1001`).
- Ensure your container image doesn't override the user permissions after the volume is mounted.
- Check that your application is running with the expected user ID by examining the container logs or using Amazon ECS Exec to inspect the running container.

Root user with permission issues

If no user is specified in your container definition, the container runs as root and should have full access to the volume. If you're experiencing issues:

- Verify that the volume is properly mounted by checking the mount points inside the container.
- Ensure the volume isn't configured as read-only in your mount point configuration.

Multi-container tasks with different users

In tasks with multiple containers running as different users, Amazon ECS automatically manages group permissions to allow all specified users to write to the volume. If containers can't write:

- Verify that all containers requiring write access have the `user` parameter properly configured.
- Check that the volume is mounted in all containers that need access to it.

For more information about configuring users in container definitions, see
[Amazon ECS task definition parameters for Fargate](../../../task_definition_parameters.md "../../../task_definition_parameters.md") .
