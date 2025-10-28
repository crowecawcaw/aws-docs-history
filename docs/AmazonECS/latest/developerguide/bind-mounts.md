# Use bind mounts with Amazon ECS

With bind mounts, a file or directory on a host, such as an Amazon EC2 instance, is mounted
into a container. Bind mounts are supported for tasks that are hosted on both Fargate and
Amazon EC2 instances. Bind mounts are tied to the lifecycle of the container that uses them.
After all of the containers that use a bind mount are stopped, such as when a task is
stopped, the data is removed. For tasks that are hosted on Amazon EC2 instances, the data can be
tied to the lifecycle of the host Amazon EC2 instance by specifying a `host` and
optional `sourcePath` value in your task definition. For more information, see
[Bind mounts](https://docs.docker.com/engine/storage/bind-mounts/ "https://docs.docker.com/engine/storage/bind-mounts/") in
the Docker documentation.

The following are common use cases for bind mounts.

- To provide an empty data volume to mount in one or more containers.
- To mount a host data volume in one or more containers.
- To share a data volume from a source container with other containers in the
  same task.
- To expose a path and its contents from a Dockerfile to one or more
  containers.

## Considerations when using bind

mounts

When using bind mounts, consider the following.

- By default, tasks that are hosted on AWS Fargate using platform version
  `1.4.0` or later (Linux) or `1.0.0` or later
  (Windows) receive a minimum of 20 GiB of ephemeral storage
  for bind mounts. You can increase the total amount of ephemeral storage up to a
  maximum of 200 GiB by specifying the `ephemeralStorage` parameter
  in your task definition.
- To expose files from a Dockerfile to a data volume when a task is run, the
  Amazon ECS data plane looks for a `VOLUME` directive. If the absolute
  path that's specified in the `VOLUME` directive is the same as
  the `containerPath` that's specified in the task definition, the
  data in the `VOLUME` directive path is copied to the data volume.
  In the following Dockerfile example, a file that's named
  `examplefile` in the `/var/log/exported` directory
  is written to the host and then mounted inside the container.

```
FROM public.ecr.aws/amazonlinux/amazonlinux:latest
RUN mkdir -p `/var/log/exported`
RUN touch `/var/log/exported/examplefile`
VOLUME ["`/var/log/exported`"]
```

By default, the volume permissions are set to `0755` and the
owner as `root`. You can customize these permissions in the
Dockerfile. The following example defines the owner of the directory as
`node`.

```
FROM public.ecr.aws/amazonlinux/amazonlinux:latest
RUN yum install -y shadow-utils && yum clean all
RUN useradd `node`
RUN mkdir -p /var/log/exported && chown `node`:`node` /var/log/exported
RUN touch /var/log/exported/examplefile
USER `node`
VOLUME ["/var/log/exported"]
```

- For tasks that are hosted on Amazon EC2 instances, when a `host` and
  `sourcePath` value aren't specified, the Docker daemon
  manages the bind mount for you. When no containers reference this bind
  mount, the Amazon ECS container agent task cleanup service eventually deletes it.
  By default, this happens three hours after the container exits. However, you
  can configure this duration with the
  `ECS_ENGINE_TASK_CLEANUP_WAIT_DURATION` agent variable. For
  more information, see [Amazon ECS container agent configuration](ecs-agent-config.md "ecs-agent-config.md"). If you need this data to persist
  beyond the lifecycle of the container, specify a `sourcePath`
  value for the bind mount.
