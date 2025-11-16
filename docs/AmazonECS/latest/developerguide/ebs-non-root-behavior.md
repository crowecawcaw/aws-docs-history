# Non-root user behavior

When you specify a non-root user in your container definition, Amazon ECS automatically
configures the Amazon EBS volume with group-based permissions that allow the specified user
to read and write to the volume. The volume is mounted with the following characteristics:

- The volume is owned by the root user and root group.
- Group permissions are set to allow read and write access.
- The non-root user is added to the appropriate group to access the volume.
  Follow these best practices when using Amazon EBS volumes with non-root containers:

- Use consistent user IDs (UIDs) and group IDs (GIDs) across your container images
  to ensure consistent permissions.
- Pre-create mount point directories in your container image and set appropriate
  ownership and permissions.
- Test your containers with Amazon EBS volumes in a development environment to
  confirm that file system permissions work as expected.
- If multiple containers in the same task share a volume, ensure they either use
  compatible UIDs/GIDs or mount the volume with consistent access expectations.
