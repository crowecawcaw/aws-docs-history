# Persistent storage for service-managed fleets

AWS Deadline Cloud (Deadline Cloud) persistent storage attaches dedicated Amazon Elastic Block Store (Amazon EBS) gp3 volumes to
service-managed fleet workers. These volumes preserve data such as conda package installations,
application caches, and version control workspaces across worker lifecycle events. For a
conceptual overview, see [Persistent storage for
service-managed fleets](../userguide/volumes.md "../userguide/volumes.md") in the _AWS Deadline Cloud User Guide_.

## Fleet configuration

To enable persistent storage, include the `persistentVolumeConfiguration`
object in the `serviceManagedEc2FleetConfiguration` when you call
`CreateFleet` or `UpdateFleet`.

### Configuration parameters

The `persistentVolumeConfiguration` object accepts the following
parameters. For valid ranges and default values, see [CreateFleet](../APIReference/API_CreateFleet.md "../APIReference/API_CreateFleet.md") in
the _Deadline Cloud API Reference_.

| Parameter          | Type    | Required | Description                                                                                                                                                            |
| ------------------ | ------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sizeGiB`          | Integer | No       | The size of the persistent volume in GiB.                                                                                                                              |
| `iops`             | Integer | No       | The provisioned IOPS for the gp3 volume.                                                                                                                               |
| `throughputMiB`    | Integer | No       | The provisioned throughput in MiB/s for the gp3 volume.                                                                                                                |
| `mountPath`        | String  | Yes      | The mount location on the worker. For Linux, specify an absolute path<br>(for example, `/mnt/persistent`). For Windows, specify a drive<br>letter (for example, `D:`). |
| `lastUsedTtlHours` | Integer | No       | The number of hours after a volume was last used before automatic<br>cleanup.                                                                                          |

### Create a fleet with persistent storage

The following AWS CLI example creates a service-managed fleet with persistent storage
enabled:

```
aws deadline create-fleet \
    --farm-id `farm-0123456789abcdef0` \
    --display-name "Rendering Fleet" \
    --max-worker-count 20 \
    --configuration '{
      "serviceManagedEc2FleetConfiguration": {
        "instanceCapabilities": {
          "vCpuCount": {"min": 4, "max": 16},
          "memoryMiB": {"min": 16384, "max": 65536},
          "osFamily": "LINUX",
          "rootEbsVolume": {"sizeGiB": 250}
        },
        "instanceMarketOptions": {"type": "spot"},
        "persistentVolumeConfiguration": {
          "sizeGiB": 2048,
          "iops": 16000,
          "throughputMiB": 500,
          "mountPath": "/mnt/persistent",
          "lastUsedTtlHours": 168
        }
      }
    }'
```

### Update persistent storage configuration

The following AWS CLI example adds persistent storage to an existing fleet:

```
aws deadline update-fleet \
    --farm-id `farm-0123456789abcdef0` \
    --fleet-id `fleet-0123456789abcdef0` \
    --configuration '{
      "serviceManagedEc2FleetConfiguration": {
        "instanceCapabilities": {
          "vCpuCount": {"min": 4, "max": 16},
          "memoryMiB": {"min": 16384, "max": 65536},
          "osFamily": "LINUX",
          "rootEbsVolume": {"sizeGiB": 250}
        },
        "instanceMarketOptions": {"type": "spot"},
        "persistentVolumeConfiguration": {
          "sizeGiB": 2048,
          "iops": 16000,
          "throughputMiB": 500,
          "mountPath": "/mnt/persistent",
          "lastUsedTtlHours": 168
        }
      }
    }'
```

To disable persistent storage, omit the `persistentVolumeConfiguration`
object from the fleet configuration in an `UpdateFleet` call. Deadline Cloud
automatically cleans up existing volumes when they are no longer attached to a
worker.

## Volume management operations

You can use the following operations to manage persistent volumes:

### GetVolume

Retrieves detailed information about a specific persistent volume.

**Request**

```
aws deadline get-volume \
    --farm-id `farm-0123456789abcdef0` \
    --fleet-id `fleet-0123456789abcdef0` \
    --volume-id `volume-0123456789abcdef0`
```

**Response**

```
{
  "volumeId": "volume-0123456789abcdef0",
  "fleetId": "fleet-0123456789abcdef0",
  "farmId": "farm-0123456789abcdef0",
  "state": "AVAILABLE",
  "volumeType": "gp3",
  "sizeGiB": 2048,
  "iops": 16000,
  "throughputMiB": 500,
  "availabilityZone": "us-west-2a",
  "attachedWorkerId": null,
  "createdAt": "2024-01-15T10:30:00Z",
  "lastAttachedAt": "2024-11-15T14:22:00Z",
  "ttl": "2024-11-22T14:22:00Z"
}
```

The `state` field indicates the current volume state. Possible values
are:

- `AVAILABLE` – The volume is detached and ready for
  attachment.
- `IN_USE` – The volume is currently attached to a
  worker.
- `PENDING_CREATION` – The volume is being created.
- `PENDING_ATTACHMENT` – The volume is reserved for attachment
  to a worker.
- `PENDING_DELETION` – The volume is marked for
  deletion.

## Environment variable

When persistent storage is successfully mounted, Deadline Cloud sets the following environment
variable on the worker:

```
DEADLINE_PERSISTENT_MOUNT=`/mnt/persistent`
```

The value of the environment variable is the mount path you specified in the fleet
configuration. This environment variable is available to all job processes running on the
worker, including host configuration scripts and job template actions.

The following runtime consumers automatically use persistent storage when the
environment variable is present:

- **Conda queue environments** – Stores package
  installations on the persistent volume.
- **VFS immutable cache** – Stores the asset
  cache on the persistent volume.

You can reference the environment variable in your Open Job Description job templates to store
custom data on the persistent volume. The following example shows a step that writes
output to persistent storage:

```
steps:
  - name: ProcessAssets
    script:
      actions:
        onRun:
          command: bash
          args:
            - "-c"
            - |
              CACHE_DIR="${DEADLINE_PERSISTENT_MOUNT}/my-app-cache"
              mkdir -p "$CACHE_DIR"
              # Your processing logic here
```

## Configuration change behavior

The following table describes how configuration changes affect existing persistent
volumes:

| Change                      | Behavior                                                                                                                          |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Increase IOPS or throughput | Deadline Cloud applies changes before the next volume attachment.                                                                 |
| Decrease IOPS or throughput | Deadline Cloud applies changes before the next volume attachment.                                                                 |
| Increase volume size        | Deadline Cloud enlarges the volume before the next attachment and expands the file<br>system automatically during worker startup. |
| Decrease volume size        | Not supported. Amazon EBS volumes cannot be reduced in size.                                                                      |
| Change mount path           | Applies only to new workers. Existing workers retain their current mount<br>path.                                                 |
| Remove persistent storage   | Deadline Cloud marks existing volumes for deletion and cleans them up when they<br>are no longer attached to a worker.            |
