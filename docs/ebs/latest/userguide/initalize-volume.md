

# Initialize Amazon EBS volumes
<a name="initalize-volume"></a>

When you create an Amazon EBS volume, either from an EBS snapshot or from another EBS volume (volume copy), the data blocks must be written to the volume before you can access them. For volumes created from snapshots, the data blocks must be downloaded from Amazon S3 to the new volume. For volume copies, the data blocks must be copied from the source volume to the volume copy. This process is called *volume initialization*. During this time, the volume being initialized might experience increased I/O latency and decreased performance. Full volume performance is achieved only once all storage blocks have been downloaded and written to the volume.

**Note**  
Empty volumes deliver their maximum performance immediately after creation and do not require initialization.

The default volume initialization rate fluctuates throughout the initialization process, which could make completion times unpredictable. To minimize the performance impacts associated with volume initialization, you could use the following options:

**Topics**
+ [Use an Amazon EBS Provisioned Rate for Volume Initialization](#volume-initialization-rate)
+ [Use a snapshot that is enabled for fast snapshot restore](#volume-initialization-fsr)
+ [Manually initialize volumes](#ebs-initialize)
+ [Monitor volume initialization](ebs-initialize-monitor.md)

**Note**  
Amazon EBS Provisioned Rate for Volume Initialization and fast snapshot restore are not supported for volume copies. For more information, see [Volume copy initialization](ebs-copying-volume.md#copy-volume-initialization).

## Use an Amazon EBS Provisioned Rate for Volume Initialization
<a name="volume-initialization-rate"></a>

When you create an Amazon EBS volume from a snapshot, you can optionally specify an Amazon EBS Provisioned Rate for Volume Initialization (volume initialization rate) that ranges from 100 to 300 MiB/s. If you specify a volume initialization rate, the snapshot blocks are downloaded from Amazon S3 and written to the volume at the specified rate after creation. This enables you to create volumes that become fully initialized and fully performant in a predictable amount of time.

Using a volume initialization rate is especially useful when you are creating multiple volumes simultaneously and you need all of them to be initialized in a predictable amount of time.

**Note**  
Amazon EBS Provisioned Rate for Volume Initialization is supported with all Amazon EBS volume types, and all Amazon EC2 instance types, including Amazon EC2 Mac instances.

You can specify a volume initialization rate:
+ For individual volume creation requests
+ For EBS volume block device mappings in instance launch requests
+ For EBS volume block device mappings in launch templates
+ For EBS volumes created by root volume replacement tasks
+ For EBS volumes on Amazon EKS clusters (created by EBS CSI Driver) and Amazon ECS clusters

**Topics**
+ [How it works](#consistent-rate-how)
+ [Considerations](#consistent-rate-considerations)
+ [Quotas](#consistent-rate-quota)
+ [Billing](#consistent-rate-billing)
+ [Specify a volume initialization rate](#consistent-rate-specify)

### How it works
<a name="consistent-rate-how"></a>

When you create a volume with a volume initialization rate, the snapshot blocks are downloaded from Amazon S3 to the volume at the rate you specify.

The amount of time taken to initialize the volume depends on the following:
+ The size of the snapshot data, not the size of the volume being created.
**Tip**  
To find a snapshot's data size, check the `FullSnapshotSizeInBytes` field in the [ describe-snapshots](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-snapshots.html) command output, or the **Full snapshot size** field in the console.
+ The volume initialization rate that you specify

For example, if you create a 20 GiB volume using a snapshot that has 10 GiB of data, and you specify a volume initialization rate of 300 MiB/s, the volume will be fully initialized in approximately 34.1 seconds (10 GiB / 300 MiB/s = 34.1 seconds). Similarly, if you create 10 volumes with that same snapshot and volume initialization rate concurrently, all 10 volumes will be fully initialized in 34.1 seconds.

### Considerations
<a name="consistent-rate-considerations"></a>
+ You can specify a volume initialization rate of between 100 and 300 MiB/s.
+ When you specify a volume initialization rate, the charges and completion time are based on the size of the snapshot data (not the size of the volume) and the rate you specify. For more information, see [Billing](#consistent-rate-billing).
+ Amazon EBS delivers an average rate that is within 10 percent of the volume initialization rate that you specify for 99 percent of the time.
+ If you specify a volume initialization rate and use a snapshot that is enabled for fast snapshot restore, Amazon EBS uses the specified rate instead of fast snapshot restore. To use fast snapshot restore instead, do not specify a volume initialization rate.
+ If Amazon EBS can't initialize the volume at the specified volume initialization rate due to capacity constraints or because you have exceeded your [ quota](#consistent-rate-quota), the request fails.
+ You can't specify a volume initialization rate for volumes created on AWS Outposts, or in Local Zones or Wavelength Zones.

### Quotas
<a name="consistent-rate-quota"></a>

There is a limit of 5,000 MiB/s on the cumulative volume initialization rate that you can request across concurrent volume creation requests. For example, you can make 50 concurrent volume creation requests with a rate of 100 MiB/s (50 simultaneous requests \* 100 MiB/s rate), or 25 concurrent requests with a rate of 200 MiB/s (25 simultaneous requests \* 200 MiB/s rate). This limit applies on a per Region basis. If a request exceeds this limit, it fails. Either wait for some of the in-progress requests to complete or request a quota increase. For more information, see [Quotas for Amazon EBS](ebs-resource-quotas.md).

### Billing
<a name="consistent-rate-billing"></a>

When you create a volume with a volume initialization rate, you are charged a per-GiB rate based on the selected initialization tier. The rate varies by Region. To determine the rate for your selected initialization tier, open [Amazon EBS pricing](https://aws.amazon.com/ebs/pricing/), select your Region, and find the **Provisioned Rate for Volume Initialization** section.

You are charged based on the full snapshot data size, not the size of the volume. For example, if you create a snapshot of a 100 GiB volume that contains 50 GiB of written data, the full snapshot data size is 50 GiB. If you use that snapshot to create a volume and specify a volume initialization rate, your charges are based on 50 GiB.

**Tip**  
To find the full snapshot data size, check the `FullSnapshotSizeInBytes` field in the [ describe-snapshots](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-snapshots.html) command output, or the **Full snapshot size** field in the console.

The formula is as follows:

```
{{Rate for the selected initialization tier in the Region}} × {{full snapshot data size}}
```

You are billed the full amount as soon as the volume enters the `active` state. Failed requests are not billed.

If you delete a volume before initialization completes, you are still billed for the requested volume initialization rate.

### Specify a volume initialization rate
<a name="consistent-rate-specify"></a>

Use one of the following methods to create a volume from a snapshot with a volume initialization rate.

------
#### [ Console ]

**To create a volume**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Volumes**, and then choose **Create volume**.

1. For **Volume type**, choose the type of volume to create.

1. For **Size**, enter a size that is equal to or larger than the source snapshot's volume size.

1. For **Availability Zone**, choose the Availability Zone in which to create the volume.

1. For **Snapshot ID**, select the snapshot to use.

1. For **Volume initialization rate**, enter a rate of `100`–`300` MiB/s. Specifying a rate incurs additional charges. To use the default initialization rate or fast snapshot restore, if it is enabled for the selected snapshot, leave this field empty.
**Note**  
For information about how the rate and full snapshot data size affect initialization time, see [How it works](#consistent-rate-how). For pricing information, see [Billing](#consistent-rate-billing).

1. Configure any other required volume settings and add tags as needed.

1. Choose **Create volume**.

1. In the **Volumes** grid, view the volume's **Initialization state** and progress.

------
#### [ AWS CLI ]

**To create a volume**  
Use the [create-volume](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-volume.html) command. The following example creates a `gp3` volume from a snapshot in the specified Availability Zone with a volume initialization rate of `300` MiB/s. Replace the example Region, Availability Zone, and snapshot ID with the values for your resources:

```
aws ec2 create-volume \
    --region {{us-east-1}} \
    --availability-zone {{us-east-1a}} \
    --volume-type gp3 \
    --snapshot-id {{snap-0abcdef1234567890}} \
    --volume-initialization-rate 300
```

If you omit `--size`, the volume uses the source snapshot's volume size. If you specify `--size`, the value must be equal to or larger than the source snapshot's volume size.

------
#### [ PowerShell ]

**To create a volume**  
Use the [New-EC2Volume](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2Volume.html) cmdlet. The following example creates a `gp3` volume from a snapshot in the specified Availability Zone with a volume initialization rate of `300` MiB/s. The command stores the returned volume object in `$volume`. Replace the example Region, Availability Zone, and snapshot ID with the values for your resources:

```
$volume = New-EC2Volume `
    -Region {{us-east-1}} `
    -AvailabilityZone {{us-east-1a}} `
    -VolumeType gp3 `
    -SnapshotId {{snap-0abcdef1234567890}} `
    -VolumeInitializationRate 300
```

------

#### Monitor initialization
<a name="consistent-rate-monitor"></a>

Volume initialization information can take up to 5 minutes to update. For instructions on monitoring initialization, see [Monitor the status of Amazon EBS volume initialization](ebs-initialize-monitor.md).

## Use a snapshot that is enabled for fast snapshot restore
<a name="volume-initialization-fsr"></a>

If you create a volume from a snapshot that is enabled for fast snapshot restore, the volume is fully initialized at creation and it immediately delivers its full performance. For more information about using fast snapshot restore, see [Amazon EBS fast snapshot restore](ebs-fast-snapshot-restore.md).

## Manually initialize the volumes after creation
<a name="ebs-initialize"></a>

You can manually initialize an Amazon EBS volume after creation to help minimize the performance impacts of volume initialization. 

You can use the following procedures to manually initialize an Amazon EBS volume after creation.

**Important**  
While initializing Provisioned IOPS SSD volumes that were created from snapshots, the performance of the volume may drop below 50 percent of its expected level, which causes the volume to display a `warning` state in the **I/O Performance** status check. This is expected, and you can ignore the `warning` state on Provisioned IOPS SSD volumes while you are initializing them. For more information, see [Amazon EBS volume status checks](monitoring-volume-checks.md).

### Linux instances
<a name="ebs-initialize-linux"></a>

**To initialize a volume created from a snapshot on Linux**

1. Attach the newly-restored volume to your Linux instance.

1. Use the **lsblk** command to list the block devices on your instance.

   ```
   $ lsblk
   NAME  MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
   xvdf  202:80   0  30G  0 disk
   xvda1 202:1    0   8G  0 disk /
   ```

   Here you can see that the new volume, `/dev/xvdf`, is attached, but not mounted (because there is no path listed under the `MOUNTPOINT` column).

1. <a name="initialize-snapshot-step"></a>Use the **dd** or **fio** utilities to read all of the blocks on the device. The **dd** command is installed by default on Linux systems, but **fio** is considerably faster because it allows multi-threaded reads.
**Note**  
This step may take several minutes up to several hours, depending on your EC2 instance bandwidth, the IOPS provisioned for the volume, and the size of the volume.

   [**dd**] The `if` (input file) parameter should be set to the drive you wish to initialize. The `of` (output file) parameter should be set to the Linux null virtual device, `/dev/null`. The `bs` parameter sets the block size of the read operation; for optimal performance, this should be set to 1 MB.
**Important**  
Incorrect use of **dd** can easily destroy a volume's data. Be sure to follow precisely the example command below. Only the `if=/dev/{{xvdf}}` parameter will vary depending on the name of the device you are reading.

   ```
   $ sudo dd if=/dev/{{xvdf}} of=/dev/null bs=1M
   ```

   [**fio**] If you have **fio** installed on your system, use the following command to initialize your volume. The `--filename` (input file) parameter should be set to the drive you wish to initialize.

   ```
   $ sudo fio --filename=/dev/{{xvdf}} --rw=read --bs=1M --iodepth=32 --ioengine=libaio --direct=1 --name=volume-initialize
   ```

   To install **fio** on Amazon Linux, use the following command:

   ```
   sudo yum install -y fio
   ```

   To install **fio** on Ubuntu, use the following command:

   ```
   sudo apt-get install -y fio
   ```

   When the operation is finished, you will see a report of the read operation. Your volume is now ready for use. For more information, see [Make an Amazon EBS volume available for use](ebs-using-volumes.md).

### Windows instances
<a name="ebs-initialize-windows"></a>

Before using either tool, gather information about the disks on your system as follows:

**To gather information about the system disks**

1. Use the **wmic** command to list the available disks on your system:

   ```
   wmic diskdrive get size,deviceid
   ```

   The following is example output:

   ```
   DeviceID            Size
   \\.\PHYSICALDRIVE2  80517265920
   \\.\PHYSICALDRIVE1  80517265920
   \\.\PHYSICALDRIVE0  128849011200
   \\.\PHYSICALDRIVE3  107372805120
   ```

1. Identify the disk to initialize using **dd** or **fio**. The `C:` drive is on `\\.\PHYSICALDRIVE0`. You can use the `diskmgmt.msc` utility to compare drive letters to disk drive numbers if you are not sure which drive number to use. 

------
#### [ Use the dd utility ]

Complete the following procedures to install and use **dd** to initialize a volume.

**Important considerations**
+ Initializing a volume takes from several minutes up to several hours, depending on your EC2 instance bandwidth, the IOPS provisioned for the volume, and the size of the volume.
+ Incorrect use of **dd** can easily destroy a volume's data. Be sure to follow this procedure precisely.

**To install dd for Windows**

The **dd** for Windows program provides a similar experience to the **dd** program that is commonly available for Linux and Unix systems, and it enables you to initialize Amazon EBS volumes that have been created from snapshots. The most recent beta versions support the `/dev/null` virtual device. If you install an earlier version, you can use the `nul` virtual device instead. Full documentation is available at [http://www.chrysocome.net/dd](http://www.chrysocome.net/dd).

1. Download the most recent binary version of **dd** for Windows from [http://www.chrysocome.net/dd](http://www.chrysocome.net/dd).

1. (Optional) Create a folder for command line utilities that is easy to locate and remember, such as `C:\bin`. If you already have a designated folder for command line utilities, you can use that folder instead in the following step.

1. Unzip the binary package and copy the `dd.exe` file to your command line utilities folder (for example, `C:\bin`).

1. Add the command line utilities folder to your Path environment variable so you can run the programs in that folder from anywhere.

   1. Choose **Start**, open the context (right-click) menu for **Computer**, and then choose **Properties**.

   1. Choose **Advanced system settings**, **Environment Variables**.

   1. For **System Variables**, select the variable **Path** and choose **Edit**.

   1. For **Variable value**, append a semicolon and the location of your command line utility folder (**;C:\\bin\\)** to the end of the existing value.

   1. Choose **OK** to close the **Edit System Variable ** window.

1. Open a new command prompt window. The previous step doesn't update the environment variables in your current command prompt windows. The command prompt windows that you open now that you completed the previous step are updated.
<a name="prewarm_snapshot_command"></a>
**To initialize a volume using dd for Windows**  
Run the following command to read all blocks on the specified device (and send the output to the `/dev/null` virtual device). This command safely initializes your existing data.

```
dd if=\\.\PHYSICALDRIVE{{n}} of=/dev/null bs=1M --progress --size
```

You might get an error if **dd** attempts to read beyond the end of the volume. You can safely ignore this error.

If you used an earlier version of the **dd** command, it does not support the `/dev/null` device. Instead, you can use the `nul` device as follows.

```
dd if=\\.\PHYSICALDRIVE{{n}} of=nul bs=1M --progress --size
```

------
#### [ Use the fio utility ]

Complete the following procedures to install and use **fio** to initialize a volume.

**To install **fio** for Windows**

The **fio** for Windows program provides a similar experience to the **fio** program that is commonly available for Linux and Unix systems, and it allows you to initialize Amazon EBS volumes created from snapshots. For more information, see [https://github.com/axboe/fio](https://github.com/axboe/fio).

1. Download the [**fio** MSI](https://github.com/axboe/fio/releases) installer by expanding **Assets** for the latest release and selecting the MSI installer.

1. Install **fio**.

**To initialize a volume using **fio** for Windows**

1. Run a command similar to the following to initialize a volume:

   ```
   fio --filename=\\.\PHYSICALDRIVE{{n}}  --rw=read --bs=1M --iodepth=32 --direct=1 --name=volume-initialize
   ```

1. When the operation completes, you are ready to use your new volume. For more information, see [Make an Amazon EBS volume available for use](ebs-using-volumes.md).

------