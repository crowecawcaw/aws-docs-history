

# Updating an Amazon FSx for OpenZFS volume
<a name="updating-volumes"></a>

This section provides information on how to update a volume using the Amazon FSx console, the AWS CLI, and the Amazon FSx API, and details on the volume properties that you can modify.

**Topics**
+ [Modifiable volume properties](#updateable-volume-properties)
+ [Updating a volume](#updating-a-volume)

## Modifiable volume properties
<a name="updateable-volume-properties"></a>

You can update the following FSx for OpenZFS [volume properties](creating-volumes.md#volume-properties):
+ **Volume name** — You can change the name of the volume, except for volumes that are attached to an S3 access point.
+ **Storage capacity quota** – You can change an existing quota setting, set a new quota, or unset the capacity quota.
+ **Storage capacity reservation** – You can change an existing storage capacity setting, enable storage capacity reservation, or unset the capacity reservation.
+ **Data compression type** – You can enable compression, change the compression type, and turn compression off. Changing this property affects only newly-written data.
+ **NFS exports** – You can manage access to the volume by modifying **Client addresses** and **NFS options**. For more information, see [NFS exports](creating-volumes.md#nfs-exports).
+ **User and group quotas** – You can change or remove existing quotas and add new quotas.
+ **Volume record size** – You can change the record size for the volume. Changing the volume record size affects only files created afterward; existing files are unaffected. For more information, see [ZFS record size](performance.md#record-size-performance).
+ **ReadOnly** – You can set a volume's access to be read-only using the AWS CLI or API. The default is `ReadOnly: "FALSE"`. This setting is not available in the AWS Management Console.
**Note**  
You cannot set a volume to be read-only if it is attached to an S3 access point.

## Updating a volume
<a name="updating-a-volume"></a>

### To update a volume configuration (console)
<a name="update-volume-console"></a>

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. Navigate to **File systems** and choose the FSx for OpenZFS file system that you want to update a volume for.

1. Choose the **Volumes** tab.

1. Choose the volume that you want to update.

1. For **Actions**, choose **Update volume**.

   The **Update volume** dialog box displays with the volume's current settings.

1. For **Storage capacity quota - optional**, you can set a quota that will be the maximum storage size for the volume. This quota cannot be larger than the parent volume quota. To set no quota and allow this volume to consume any available capacity in your file system, set this property to `-1`.

1. For **Storage capacity reservation - optional**, you can enter the reservation for the volume. This reserves dedicated space on the file system storage pool, meaning the space available to all other volumes is reduced by the amount specified. It cannot be set to a value that's greater than the parent volume quota or the remaining reservation space on the file system storage. To set no reservation and allow this volume to consume any available capacity in your file system, set this property to `0` or `-1`.

1. For **Data compression type**, choose the type of compression to use for your volume—either **Zstandard**, **LZ4**, or **No compression**. Zstandard compression provides more data compression and higher read throughput than LZ4 compression. LZ4 compression provides less compression and higher write throughput performance than Zstandard compression. Changing this property affects only newly-written data. For more information about the storage and performance benefits of volume data compression options, see [Data compression](performance.md#perf-data-compression).

1. For **NFS exports**, you can modify or remove the existing client configurations that define which clients can access the volume and what permissions they have.

   You can provide additional client configurations for the volume:

   1. In the **Client addresses** field, specify which clients can access the volume. Enter an asterisk (`*`) for any client, a specific IP address, or a CIDR range of IP addresses.

   1. In the **NFS options** field, enter a comma-delimited set of exports options. For example, enter `rw` to allow read and write permissions to the volume.

   1. Choose **Add client configuration**.

   1. Repeat the procedure to add another client configuration.

   For more information, see [NFS exports](creating-volumes.md#nfs-exports).

1. For **Record size**, choose whether to use the default suggested record size of 128 KiB, or to set a **User-configured** suggested record size for the volume. Generally, workloads that write in fixed small or large record sizes may benefit from setting a custom record size, like database workloads (small record size) or media streaming workloads (large record size). We recommend the default setting for the majority of use cases. For more information about the record size setting, see [Configurable volume properties](creating-volumes.md#volume-properties). 

1. For **User and group quotas**, you can change or set a storage quota for a user or group:

   1. For **Quota type**, choose `USER` or `GROUP`.

   1. For **User or group ID**, enter a number that is the ID of the user or group.

   1. For **Usage quota**, enter a number that is the storage quota in GiB of the user or group.

   1. To create additional user or group quotas, choose **Add quota** and repeat the procedure to change or add a quota for another user or group.

1. For **Record size**, enter the desired maximum size of a logical block in a ZFS dataset. Valid values are 4, 8, 16, 32, 64, 128, 256, 512, or 1024 KiB. The default is 128 KiB. Most file systems will use the default value. Database workflows can benefit from a smaller record size, while streaming workflows can benefit from a larger record size. For more information about Record size and file system performance, see [ZFS record size](performance.md#record-size-performance).

1. Choose **Update** to update the volume.

### To update a volume configuration (CLI)
<a name="update-volume-cli"></a>
+ To update the configuration of an FSx for OpenZFS volume, use the [update-volume](https://docs.aws.amazon.com/cli/latest/reference/fsx/update-volume.html) CLI command (or the equivalent [UpdateVolume](https://docs.aws.amazon.com/fsx/latest/APIReference/API_UpdateVolume.html) API operation), as shown in the following example. In this example, the `StorageCapacityQuota` and `StorageCapacityReservationGiB` properties are unset, turning off the quota capacity reservation for the volume.

  ```
  aws fsx update-volume \
      --volume-id fsxvol-0123456789abcdef0 \
      --open-zfs-configuration '{ 
        "DataCompressionType": "ZSTD",
        "NfsExports": [ 
           { 
              "ClientConfigurations": [ 
                 { 
                    "Clients": "192.0.2.0/24",
                    "Options": [ "crossmnt" ]
                 }
              ]
           }
        ],
        "RecordSizeKiB": 128,
        "StorageCapacityQuotaGiB": -1,
        "StorageCapacityReservationGiB": -1,
        "UserAndGroupQuotas": [ 
           { 
              "Id": 1102,
              "StorageCapacityQuotaGiB": 2000,
              "Type": "GROUP"
           }
        ]
     }'
  ```