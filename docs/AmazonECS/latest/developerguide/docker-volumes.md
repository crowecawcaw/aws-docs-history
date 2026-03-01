# Use Docker volumes with Amazon ECS

When using Docker volumes, the built-in `local` driver or a third-party
volume driver can be used. Docker volumes are managed by Docker and a directory is
created in `/var/lib/docker/volumes` on the container instance that contains
the volume data.

To use Docker volumes, specify a `dockerVolumeConfiguration` in your task
definition. For more information, see [Volumes](https://docs.docker.com/engine/storage/volumes/ "https://docs.docker.com/engine/storage/volumes/") in the Docker documentation.

Some common use cases for Docker volumes are the following:

- To provide persistent data volumes for use with containers
- To share a defined data volume at different locations on different containers
  on the same container instance
- To define an empty, nonpersistent data volume and mount it on multiple
  containers within the same task
- To provide a data volume to your task that's managed by a third-party
  driver

## Considerations for using Docker volumes

Consider the following when using Docker volumes:

- Docker volumes are only supported when using the EC2 launch
  type or external instances.
- Windows containers only support the use of the `local`
  driver.
- If a third-party driver is used, make sure it's installed and active on
  the container instance before the container agent is started. If the
  third-party driver isn't active before the agent is started, you can restart
  the container agent using one of the following commands:
  - For the Amazon ECS-optimized Amazon Linux 2 AMI:

  ```
  `sudo systemctl restart ecs`
  ```

  - For the Amazon ECS-optimized Amazon Linux AMI:

  ```
  `sudo stop ecs && sudo start ecs`
  ```

For information about how to specify a Docker volume in a task definition, see [Specify a Docker volume in an Amazon ECS task definition](specify-volume-config.md "specify-volume-config.md").
