

# Mount persistent storage in a container
<a name="containers-mount-persistent-storage"></a>

When persistent storage is mounted on a service-managed fleet worker, Deadline Cloud sets `DEADLINE_PERSISTENT_MOUNT` to its host mount path. A custom Docker queue environment can detect the variable and mount the same path into the session container.

First, configure persistent storage on the service-managed fleet. For configuration and lifecycle details, see [Persistent storage for service-managed fleets](smf-persistent-storage-dev.md).

Add a Bash array to the queue environment's enter script, and pass the array to `docker container run`:

```
PERSISTENT_MOUNT_ARGS=()
if [ -n "${DEADLINE_PERSISTENT_MOUNT:-}" ]; then
    PERSISTENT_MOUNT_ARGS=(
        --mount
        "type=bind,src=${DEADLINE_PERSISTENT_MOUNT},dst=${DEADLINE_PERSISTENT_MOUNT}"
    )
fi

docker container run \
    --rm \
    --detach \
    "${PERSISTENT_MOUNT_ARGS[@]}" \
    {{other-options}} \
    {{image-uri}}
```

Use persistent storage for data that can be regenerated, such as container layers, downloaded model files, compiled shaders, package installations, and application caches. Write authoritative job output to the session paths configured for your workflow.

Persistent storage isn't a shared filesystem. A volume is attached to one worker at a time and is reused within the same fleet and Availability Zone. Use network storage when concurrent workers must read and write the same data.

Deadline Cloud configures the rootless Docker data directory on the resolved physical `job-user` home path. You don't need to relocate the Docker data directory when persistent storage rehomes that user directory.