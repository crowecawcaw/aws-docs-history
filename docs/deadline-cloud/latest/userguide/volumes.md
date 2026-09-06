

# Persistent storage for service-managed fleets
<a name="volumes"></a>

AWS Deadline Cloud (Deadline Cloud) persistent storage provides dedicated Amazon Elastic Block Store (Amazon EBS) gp3 volumes, separate from the root boot volume, for service-managed fleet (SMF) workers. These volumes preserve data across worker lifecycle events. With persistent storage, conda package installations, application caches, and asset files remain available when workers are replaced during routine maintenance or scaling operations.

## How persistent storage works
<a name="volumes-how-it-works"></a>

When you enable persistent storage on a service-managed fleet, Deadline Cloud automatically manages the lifecycle of Amazon EBS volumes for your workers:

1. When a worker launches, Deadline Cloud creates or reuses an available Amazon EBS volume in the same Availability Zone and attaches the volume to the worker.

1. Deadline Cloud formats the volume (if new) and mounts it at the path you specify in the fleet configuration.

1. When the worker terminates or is replaced, Deadline Cloud detaches the volume and makes it available for reuse by a future worker in the same fleet and Availability Zone.

Because volumes are reused within the same fleet and Availability Zone, subsequent workers benefit from data that was previously written to the volume. The volume provides dedicated bandwidth and IOPS without contention between workers.

**Note**  
Persistent storage is available only for service-managed fleets. For customer-managed fleets, you manage your own storage infrastructure.

## Benefits of persistent storage
<a name="volumes-benefits"></a>

Persistent storage provides the following benefits for service-managed fleet workloads:
+ **Faster job startup** – Conda package installations, compiled shaders, and processed assets persist across worker replacement, eliminating repeated downloads and installations.
+ **Dedicated performance** – Each worker receives its own Amazon EBS volume with dedicated IOPS and throughput, avoiding the contention that occurs with shared network storage.
+ **Automatic management** – Deadline Cloud handles volume creation, attachment, formatting, mounting, and cleanup without requiring manual intervention.
+ **Runtime integration** – Supported runtime consumers such as conda queue environments and the virtual file system (VFS) immutable cache automatically use persistent storage when available, without requiring changes to your job configuration.
+ **Cost control** – Configure a time-to-live (TTL) to automatically clean up unused volumes and reduce storage costs during idle periods.

## When to use persistent storage
<a name="volumes-use-cases"></a>

Consider enabling persistent storage for your service-managed fleet in the following scenarios:
+ Your jobs use conda packages that require significant download and installation time.
+ Your rendering workloads compile shaders or process assets that can be reused across subsequent renders.
+ You use Perforce or other version control systems where workspace sync state reduces data transfer on subsequent updates.
+ Your jobs use the virtual file system (VFS) and would benefit from a persistent immutable asset cache.
+ You want dedicated storage performance without the operational overhead of managing shared network file systems.
+ You install custom renderers or other software on workers through host configuration scripts and want those installations cached to the persistent volume.

## Configuring persistent storage for a fleet
<a name="volumes-configure"></a>

You can configure persistent storage when you create a new service-managed fleet or update an existing fleet.

### Configuring persistent storage (console)
<a name="volumes-configure-console"></a>

Before you begin, you must have an existing farm with at least one service-managed fleet, or be ready to create a new fleet.

**To configure persistent storage for a fleet**

1. Sign in to the AWS Management Console and open the [Deadline Cloud console](https://console.aws.amazon.com/deadlinecloud/home).

1. In the navigation pane, choose **Farms**, and then select your farm.

1. Choose the **Fleets** tab, and then choose **Create fleet**, or select an existing service-managed fleet and choose **Edit**.

1. Under **Storage capabilities**, for **Storage mode**, choose **Persistent storage**.

1. Configure the **Root storage** settings for the boot volume (Size, IOPS, and Throughput).

1. Under **Persistent storage**, configure the following settings:
   + **Size** – The size of the persistent volume. The valid range is 1–65,536 GiB. Verify that the default size is suitable for your render workloads, and consider increasing the volume size for workflows that use larger assets or caches.
   + **Mount path** – The absolute path where the volume is mounted on the worker (for example, `/mnt/persistent` for Linux). For Windows workers, specify a drive letter such as `D:`.
   + **Throughput** – The provisioned throughput for the volume. Valid range is 125–2,000 MiB/s.
   + **Max idle time** – How long an available volume can sit idle before it is deleted. Select a value from the dropdown (for example, 12 hours).
   + **IOPS** – The provisioned IOPS for the volume. Valid range is 3,000–80,000 IOPS. IOPS must be at least 4× throughput.

1. Complete the remaining fleet configuration steps and choose **Create fleet** or **Save changes**.

### Configuring persistent storage (AWS CLI)
<a name="volumes-configure-cli"></a>

To configure persistent storage using the AWS Command Line Interface (AWS CLI), include the `persistentVolumeConfiguration` object in the `serviceManagedEc2FleetConfiguration` when you call `CreateFleet` or `UpdateFleet`.

The `persistentVolumeConfiguration` object accepts the following parameters. For valid ranges and default values, see [CreateFleet](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateFleet.html) in the *Deadline Cloud API Reference*.


| Parameter | Type | Required | Description | 
| --- | --- | --- | --- | 
| sizeGiB | Integer | No | The size of the persistent volume in GiB. | 
| iops | Integer | No | The provisioned IOPS for the gp3 volume. | 
| throughputMiB | Integer | No | The provisioned throughput in MiB/s for the gp3 volume. | 
| mountPath | String | Yes | The mount location on the worker. For Linux, specify an absolute path (for example, /mnt/persistent). For Windows, specify a drive letter (for example, D:). | 
| lastUsedTtlHours | Integer | No | The number of hours after a volume was last used before automatic cleanup. | 

The following AWS CLI example creates a service-managed fleet with persistent storage enabled:

```
aws deadline create-fleet \
    --farm-id {{farm-0123456789abcdef0}} \
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

To add persistent storage to an existing fleet, include the same `persistentVolumeConfiguration` object in an `update-fleet` call. To disable persistent storage, omit the `persistentVolumeConfiguration` object from the fleet configuration in an `UpdateFleet` call. Deadline Cloud automatically cleans up existing volumes when they are no longer attached to a worker.

## Runtime integration
<a name="volumes-runtime"></a>

When persistent storage is successfully mounted on a worker, Deadline Cloud sets the `DEADLINE_PERSISTENT_MOUNT` environment variable to the configured mount path. This environment variable is available to all job processes running on the worker, including host configuration scripts and job template actions. The following runtime consumers automatically use persistent storage when the environment variable is present:
+ **Conda queue environments** – Package installations are stored on the persistent volume, so subsequent workers reuse previously installed packages instead of downloading and installing them again.
+ **Virtual file system (VFS) immutable cache** – The VFS stores its immutable asset cache on the persistent volume, so previously downloaded assets are available without re-downloading from Amazon Simple Storage Service (Amazon S3).

You can also reference the `DEADLINE_PERSISTENT_MOUNT` environment variable in your own Open Job Description job templates and scripts to store data that should persist across worker lifecycle events. The following example shows a step that writes output to persistent storage:

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

## Managing persistent volumes
<a name="volumes-manage"></a>

You can view and manage persistent volumes for your fleet using the Deadline Cloud console, AWS CLI, or API. The following operations are available:
+ **List volumes** – View all persistent volumes associated with a fleet, including their state, size, and Availability Zone.
+ **Get volume details** – Retrieve detailed information about a specific volume, including its current state, attachment status, and configuration.
+ **Delete a volume** – Permanently delete an unattached persistent volume that is no longer needed. You cannot delete a volume that is currently attached to a worker.

The following AWS CLI example retrieves the details of a persistent volume:

```
aws deadline get-volume \
    --farm-id {{farm-0123456789abcdef0}} \
    --fleet-id {{fleet-0123456789abcdef0}} \
    --volume-id {{volume-0123456789abcdef0}}
```

The `state` field in the response indicates the current volume state. Possible values are:
+ `AVAILABLE` – The volume is detached and ready for attachment.
+ `IN_USE` – The volume is currently attached to a worker.
+ `PENDING_CREATION` – The volume is being created.
+ `PENDING_ATTACHMENT` – The volume is reserved for attachment to a worker.
+ `PENDING_DELETION` – The volume is marked for deletion.

## Updating persistent storage configuration
<a name="volumes-update"></a>

You can update the persistent storage configuration on an existing fleet. The following table describes how configuration changes affect existing persistent volumes:


| Change | Behavior | 
| --- | --- | 
| Increase or decrease IOPS or throughput | Deadline Cloud applies changes before the next volume attachment. | 
| Increase volume size | Deadline Cloud enlarges the volume before the next attachment and expands the file system automatically during worker startup. | 
| Decrease volume size | Not supported. Amazon EBS volumes cannot be reduced in size. | 
| Change mount path | Applies only to new workers. Existing workers retain their current mount path. | 
| Remove persistent storage | Deadline Cloud marks existing volumes for deletion and cleans them up when they are no longer attached to a worker. | 

**Important**  
Configuration changes do not affect existing workers. Changes apply only to new workers that launch after the update.

## Encryption
<a name="volumes-encryption"></a>

Persistent volumes use the encryption settings configured at the farm level. If you configured a customer-managed AWS Key Management Service (AWS KMS) key for your farm, persistent volumes are encrypted with that key. Otherwise, persistent volumes are encrypted with a service-owned key.

## Considerations
<a name="volumes-considerations"></a>

Keep the following considerations in mind when using persistent storage:
+ Persistent volumes are a caching optimization, not durable primary storage. Use persistent volumes only for data that you can recreate, such as package installations, compiled shaders, and asset caches. Deadline Cloud can replace a volume at any time, and you can't access persistent volumes directly.
+ Deadline Cloud configures the worker's home directory to use the persistent volume. Software that stores data in the home directory (such as conda packages and application caches) automatically benefits from persistence. If your software writes to paths outside the home directory, you must reconfigure it to use the persistent mount path, or those files do not persist across worker lifecycle events.
+ Persistent volumes are not attached to multiple workers simultaneously. Each volume serves one worker at a time, but is reused by different workers across lifecycle events.
+ Volumes are scoped to a specific fleet and Availability Zone. A volume created in one Availability Zone cannot be reused by a worker in a different Availability Zone.
+ A specific worker isn't guaranteed to receive the same volume it used previously. Any available volume in the same fleet and Availability Zone can be assigned.
+ If persistent storage cannot be provisioned (for example, due to quota limits), the job fails. Workers do not fall back to running without persistent storage.
+ You are billed for persistent storage based on the number of active volumes and their configuration. To control costs during idle periods, configure a TTL or remove the persistent storage configuration from your fleet.