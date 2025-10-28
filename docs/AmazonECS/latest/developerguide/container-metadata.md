# Amazon ECS container metadata file

Beginning with version 1.15.0 of the Amazon ECS container agent, various container metadata is
available within your containers or the host container instance. By enabling this feature,
you can query the information about a task, container, and container instance from within
the container or the host container instance. The metadata file is created on the host
instance and mounted in the container as a Docker volume and therefore is not available when
a task is hosted on AWS Fargate.

The container metadata file is cleaned up on the host instance when the container is
cleaned up. You can adjust when this happens with the
`ECS_ENGINE_TASK_CLEANUP_WAIT_DURATION` container agent variable. For more
information, see [Automatic Amazon ECS task and image cleanup](automated_image_cleanup.md "automated_image_cleanup.md").

###### Topics

- [Container metadata file locations](#metadata-file-locations "#metadata-file-locations")
- [Turning on Amazon ECS container metadata](enable-metadata.md "enable-metadata.md")
- [Amazon ECS container metadata file format](metadata-file-format.md "metadata-file-format.md")

## Container metadata file locations

By default, the container metadata file is written to the following host and container
paths.

- **For Linux instances:**
  - Host path:
    `/var/lib/ecs/data/metadata/`cluster_name`/`task_id`/`container_name`/ecs-container-metadata.json`

  ###### Note

  The Linux host path assumes that the default data directory mount
  path (`/var/lib/ecs/data`) is used when the agent
  is started. If you are not using an Amazon ECS-optimized AMI (or the
  `ecs-init` package to start and maintain the
  container agent), be sure to set the `ECS_HOST_DATA_DIR`
  agent configuration variable to the host path where the container
  agent's state file is located. For more information, see [Amazon ECS container agent configuration](ecs-agent-config.md "ecs-agent-config.md").
  - Container path:
    `/opt/ecs/metadata/`random_ID`/ecs-container-metadata.json`

- **For Windows instances:**
  - Host path:
    `C:\ProgramData\Amazon\ECS\data\metadata\`task_id`\`container_name`\ecs-container-metadata.json`
  - Container path:
    `C:\ProgramData\Amazon\ECS\metadata\`random_ID`\ecs-container-metadata.json`

However, for easy access, the container metadata file location is set to the
`ECS_CONTAINER_METADATA_FILE` environment variable inside the container.
You can read the file contents from inside the container with the following
command:

- **For Linux instances:**

```
`cat $ECS_CONTAINER_METADATA_FILE`
```

- **For Windows instances (PowerShell):**

```
`Get-Content -path $env:ECS_CONTAINER_METADATA_FILE`
```
