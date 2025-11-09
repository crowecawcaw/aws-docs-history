# Docker volume examples for Amazon ECS

The following examples show how to provide ephemeral storage for a container and how
to provide a shared volume for multiple containers, and how to provide NFS persistent
storage for a container.

###### To provide ephemeral storage for a container using a Docker

volume

In this example, a container uses an empty data volume that is disposed of
after the task is finished. One example use case is that you might have a
container that needs to access some scratch file storage location during a task.
This task can be achieved using a Docker volume.

1. In the task definition `volumes` section, define a data volume
   with `name` and `DockerVolumeConfiguration` values. In
   this example, we specify the scope as `task` so the volume is
   deleted after the task stops and use the built-in `local`
   driver.

```
"volumes": [
    {
        "name": "`scratch`",
        "dockerVolumeConfiguration" : {
            "scope": "`task`",
            "driver": "`local`",
            "labels": {
                "`scratch`": "`space`"
            }
        }
    }
]
```

2. In the `containerDefinitions` section, define a container with
   `mountPoints` values that reference the name of the defined
   volume and the `containerPath` value to mount the volume at on
   the container.

```
"containerDefinitions": [
    {
        "name": "`container-1`",
        "mountPoints": [
            {
              "sourceVolume": "`scratch`",
              "containerPath": "`/var/scratch`"
            }
        ]
    }
]
```

###### To provide persistent storage for multiple containers using a Docker

volume

In this example, you want a shared volume for multiple containers to use and
you want it to persist after any single task that use it stopped. The built-in
`local` driver is being used. This is so the volume is still tied
to the lifecycle of the container instance.

1. In the task definition `volumes` section, define a data volume
   with `name` and `DockerVolumeConfiguration` values. In
   this example, specify a `shared` scope so the volume persists,
   set autoprovision to `true`. This is so that the volume is
   created for use. Then, also use the built-in `local`
   driver.

```
"volumes": [
    {
        "name": "`database`",
        "dockerVolumeConfiguration" : {
            "scope": "`shared`",
            "autoprovision": true,
            "driver": "`local`",
            "labels": {
                "`database`": "`database_name`"
            }
        }
    }
]
```

2. In the `containerDefinitions` section, define a container with
   `mountPoints` values that reference the name of the defined
   volume and the `containerPath` value to mount the volume at on
   the container.

```
"containerDefinitions": [
    {
        "name": "`container-1`",
        "mountPoints": [
        {
          "sourceVolume": "`database`",
          "containerPath": "`/var/database`"
        }
      ]
    },
    {
      "name": "`container-2`",
      "mountPoints": [
        {
          "sourceVolume": "`database`",
          "containerPath": "`/var/database`"
        }
      ]
    }
  ]
```

###### To provide NFS persistent storage for a container using a Docker

volume

In this example, a container uses an NFS data volume that is automatically
mounted when the task starts and unmounted when the task stops. This uses the
Docker built-in `local` driver. One example use case is that you
might have a local NFS storage and need to access it from an ECS Anywhere task.
This can be achieved using a Docker volume with NFS driver option.

1. In the task definition `volumes` section, define a data volume
   with `name` and `DockerVolumeConfiguration` values. In
   this example, specify a `task` scope so the volume is unmounted
   after the task stops. Use the `local` driver and configure the
   `driverOpts` with the `type`, `device`,
   and `o` options accordingly. Replace `NFS_SERVER` with
   the NFS server endpoint.

```
"volumes": [
       {
           "name": "NFS",
           "dockerVolumeConfiguration" : {
               "scope": "task",
               "driver": "local",
               "driverOpts": {
                   "type": "nfs",
                   "device": "$`NFS_SERVER`:/mnt/nfs",
                   "o": "addr=$`NFS_SERVER`"
               }
           }
       }
   ]
```

2. In the `containerDefinitions` section, define a container with
   `mountPoints` values that reference the name of the defined
   volume and the `containerPath` value to mount the volume on the
   container.

```
"containerDefinitions": [
       {
           "name": "`container-1`",
           "mountPoints": [
               {
                 "sourceVolume": "`NFS`",
                 "containerPath": "`/var/nfsmount`"
               }
           ]
       }
   ]
```
