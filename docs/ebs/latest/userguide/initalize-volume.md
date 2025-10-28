# Initialize Amazon EBS volumes

When you create an Amazon EBS volume, either from an EBS snapshot or from another EBS volume
(volume copy), the data blocks must be written to the volume before you can access them. For
volumes created from snapshots, the data blocks must be downloaded from Amazon S3 to the new volume.
For volume copies, the data blocks must be copied from the source volume to the volume copy.
This process is called _volume initialization_. During this time, the volume
being initialized might experience increased I/O latency and decreased performance. Full volume
performance is achieved only once all storage blocks have been downloaded and written to the
volume.

###### Note

Empty volumes deliver their maximum performance immediately after creation and do
not require initialization.

The default volume initialization rate fluctuates throughout the initialization process,
which could make completion times unpredictable. To minimize the performance impacts associated
with volume initialization, you could use the following options:

###### Note

volume initialization rate and fast snapshot restore are not supported for volume copies. For more
information, see [Volume copy initialization](ebs-copying-volume.md#copy-volume-initialization "ebs-copying-volume.md#copy-volume-initialization").

###### Topics

- [Use an Amazon EBS Provisioned Rate for Volume Initialization](#volume-initialization-rate "#volume-initialization-rate")
- [Use a snapshot that is enabled for fast snapshot restore](#volume-initialization-fsr "#volume-initialization-fsr")
- [Manually initialize volumes](#ebs-initialize "#ebs-initialize")
- [Monitor volume initialization](ebs-initialize-monitor.md "ebs-initialize-monitor.md")

## Use an Amazon EBS Provisioned Rate for Volume Initialization

When you create an Amazon EBS volume from a snapshot, you can optionally specify an Amazon EBS Provisioned Rate for Volume Initialization
(volume initialization rate) that ranges from 100 to 300 MiB/s. If you specify a volume initialization rate, the snapshot
blocks are downloaded from Amazon S3 and written to the volume at the specified rate after creation.
This enables you to create volumes that become fully initialized and fully performant in a
predictable amount of time.

Using a volume initialization rate is especially useful when you are creating multiple volumes simultaneously
and you need all of them to be initialized in a predictable amount of time.

###### Note

Amazon EBS Provisioned Rate for Volume Initialization is supported with all Amazon EBS volume types, and all Amazon EC2 instance types,
including Amazon EC2 Mac instances.

You can specify a volume initialization rate:

- For individual volume creation requests
- For EBS volume block device mappings in instance launch requests
- For EBS volume block device mappings in launch templates
- For EBS volumes created by root volume replacement tasks
- For EBS volumes on Amazon EKS clusters (created by EBS CSI Driver) and Amazon ECS clusters

###### Topics

- [How it works](#consistent-rate-how "#consistent-rate-how")
- [Considerations](#consistent-rate-considerations "#consistent-rate-considerations")
- [Quotas](#consistent-rate-quota "#consistent-rate-quota")
- [Billing](#consistent-rate-billing "#consistent-rate-billing")

### How it works

When you create a volume with a volume initialization rate, the snapshot blocks are downloaded from
Amazon S3 to the volume at the rate you specify.

The amount of time taken to initialize the volume depends on the following:

- The size of the snapshot data, not the size of the volume being created.

###### Tip

To find a snapshot's data size, check the `FullSnapshotSizeInBytes` field in
the [describe-snapshots](../../../cli/latest/reference/ec2/describe-snapshots.md "../../../cli/latest/reference/ec2/describe-snapshots.md") command output, or the **Full snapshot size**
field in the console.

- The volume initialization rate that you specify

For example, if you create a 20 GiB volume using a snapshot that has 10 GiB of data, and
you specify a volume initialization rate of 300 MiB/s, the volume will be fully initialized in approximately
34.1 seconds (10 GiB / 300 MiB/s = 34.1 seconds). Similarly, if you create 10 volumes with
that same snapshot and volume initialization rate concurrently, all 10 volumes will be fully initialized in
34.1 seconds.

### Considerations

- You can specify a volume initialization rate of between 100 and 300 MiB/s.
- When you specify a volume initialization rate, the charges and completion time are based on the size
  of the snapshot data (not the size of the volume) and the rate you specify. For more
  information, see [Billing](#consistent-rate-billing "#consistent-rate-billing").
- Amazon EBS delivers an average rate that is within 10 percent of the volume initialization rate that you
  specify for 99 percent of the time.
- If you specify a volume initialization rate and use a snapshot that is enabled for fast snapshot
  restore, Amazon EBS uses the specified rate instead of fast snapshot restore. To use fast
  snapshot restore instead, do not specify a volume initialization rate.
- If Amazon EBS can't initialize the volume at the specified volume initialization rate due to capacity
  constraints or because you have exceeded your [quota](#consistent-rate-quota "#consistent-rate-quota"), the request fails.
- You can't specify a volume initialization rate for volumes created on AWS Outposts, or in Local Zones or
  Wavelength Zones.

### Quotas

There is a limit of 5,000 MiB/s on the cumulative volume initialization rate that you can request across
concurrent volume creation requests. For example, you can make 50 concurrent volume creation
requests with a rate of 100 MiB/s (50 simultaneous requests \* 100 MiB/s rate), or 25 concurrent
requests with a rate of 200 MiB/s (25 simultaneous requests \* 200 MiB/s rate). This limit
applies on a per Region basis. If a request exceeds this limit, it fails. Either wait for some
of the in-progress requests to complete or request a quota increase. For more information, see
[Quotas for Amazon EBS](ebs-resource-quotas.md "ebs-resource-quotas.md").

### Billing

When you create a volume with a volume initialization rate, you are charged a rate per GiB of snapshot data,
per MiB of specified initialization rate. The rate varies by Region. For more information, see
[Amazon EBS pricing](https://aws.amazon.com/ebs/pricing/ "https://aws.amazon.com/ebs/pricing/").

You are charged based on the size of the snapshot data, not the size of the volume. For example,
if you create a snapshot of a volume that is 100 GiB in size, but has only 50 GiB of data, the snapshot
has a volume size of 100 GiB, but the snapshot data size is 50 GiB. If you use that snapshot to create
a volume and specify a volume initialization rate, your charges are based on the 50 GiB of snapshot data.

###### Tip

To find a snapshot's data size, check the `FullSnapshotSizeInBytes` field in
the [describe-snapshots](../../../cli/latest/reference/ec2/describe-snapshots.md "../../../cli/latest/reference/ec2/describe-snapshots.md") command output, or the **Full snapshot size**
field in the console.

The formula is as follows:

```
`rate for Region` x `snapshot data size` x `volume initialization rate`
```

You are billed the full amount as soon as the volume enters the `active` state.
Failed requests are not billed.

If you delete a volume before the volume initialization completes, you are still billed for
the requested volume initialization rate.

## Use a snapshot that is enabled for fast snapshot restore

If you create a volume from a snapshot that is enabled for fast snapshot restore, the
volume is fully initialized at creation and it immediately delivers its full performance.
For more information about using fast snapshot restore, see [Amazon EBS fast snapshot restore](ebs-fast-snapshot-restore.md "ebs-fast-snapshot-restore.md").

## Manually initialize the volumes after creation

You can manually initialize an Amazon EBS volume after creation to help minimize the performance
impacts of volume initialization.

You can use the following procedures to manually initialize an Amazon EBS volume after
creation.

###### Important

While initializing Provisioned IOPS SSD volumes that were created from snapshots, the performance
of the volume may drop below 50 percent of its expected level, which causes the volume
to display a `warning` state in the **I/O Performance**
status check. This is expected, and you can ignore the `warning` state on
Provisioned IOPS SSD volumes while you are initializing them. For more information, see [Amazon EBS volume status checks](monitoring-volume-checks.md "monitoring-volume-checks.md").

###### To initialize a volume created from a snapshot on Linux

1. Attach the newly-restored volume to your Linux instance.
2. Use the **lsblk** command to list the block devices on your
   instance.

```
`$` `lsblk``NAME MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
xvdf 202:80 0 30G 0 disk
xvda1 202:1 0 8G 0 disk /`
```

Here you can see that the new volume, `/dev/xvdf`, is attached, but not
mounted (because there is no path listed under the `MOUNTPOINT`
column). 3. Use the **dd** or **fio** utilities to read all of the
blocks on the device. The **dd** command is installed by default on Linux
systems, but **fio** is considerably faster because it allows
multi-threaded reads.

###### Note

This step may take several minutes up to several hours, depending on your EC2
instance bandwidth, the IOPS provisioned for the volume, and the size of the
volume.

[**dd**] The `if` (input file) parameter should be set to
the drive you wish to initialize. The `of` (output file) parameter should be
set to the Linux null virtual device, `/dev/null`. The
`bs` parameter sets the block size of the read operation; for optimal
performance, this should be set to 1 MB.

###### Important

Incorrect use of **dd** can easily destroy a volume's data. Be sure
to follow precisely the example command below. Only the
`if=/dev/`xvdf`` parameter will vary depending
on the name of the device you are reading.

```
`$` `sudo dd if=/dev/`xvdf` of=/dev/null bs=1M`
```

[**fio**] If you have **fio** installed on your
system, use the following command to initialize your volume. The `--filename`
(input file) parameter should be set to the drive you wish to initialize.

```
`$` `sudo fio --filename=/dev/`xvdf` --rw=read --bs=1M --iodepth=32 --ioengine=libaio --direct=1 --name=volume-initialize`
```

To install **fio** on Amazon Linux, use the following command:

```
sudo yum install -y fio
```

To install **fio** on Ubuntu, use the following command:

```
sudo apt-get install -y fio
```

When the operation is finished, you will see a report of the read operation. Your
volume is now ready for use. For more information, see [Make an Amazon EBS volume available for use](ebs-using-volumes.md "ebs-using-volumes.md").
Before using either tool, gather information about the disks on your system as
follows:

###### To gather information about the system disks

1. Use the **wmic** command to list the available disks on your system:

```
`wmic diskdrive get size,deviceid`
```

The following is example output:

```
DeviceID            Size
\\.\PHYSICALDRIVE2  80517265920
\\.\PHYSICALDRIVE1  80517265920
\\.\PHYSICALDRIVE0  128849011200
\\.\PHYSICALDRIVE3  107372805120
```

2. Identify the disk to initialize using **dd** or
   **fio**. The `C:` drive is on
   `\\.\PHYSICALDRIVE0`. You can use the `diskmgmt.msc`
   utility to compare drive letters to disk drive numbers if you are not sure which drive
   number to use.

Use the dd utility
Complete the following procedures to install and use **dd** to
initialize a volume.

###### Important considerations

- Initializing a volume takes from several minutes up to several hours, depending
  on your EC2 instance bandwidth, the IOPS provisioned for the volume, and the size of
  the volume.
- Incorrect use of **dd** can easily destroy a volume's data. Be
  sure to follow this procedure precisely.

###### To install dd for Windows

The **dd** for Windows program provides a similar experience to the
**dd** program that is commonly available for Linux and Unix systems,
and it enables you to initialize Amazon EBS volumes that have been created from snapshots.
The most recent beta versions support the `/dev/null` virtual device.
If you install an earlier version, you can use the `nul` virtual
device instead. Full documentation is available at [http://www.chrysocome.net/dd](http://www.chrysocome.net/dd "http://www.chrysocome.net/dd").

1. Download the most recent binary version of **dd** for Windows from
   [http://www.chrysocome.net/dd](http://www.chrysocome.net/dd "http://www.chrysocome.net/dd").
2. (Optional) Create a folder for command line utilities that is easy to locate and
   remember, such as `C:\bin`. If you already have a designated folder
   for command line utilities, you can use that folder instead in the following
   step.
3. Unzip the binary package and copy the `dd.exe` file to your
   command line utilities folder (for example, `C:\bin`).
4. Add the command line utilities folder to your Path environment variable so you can
   run the programs in that folder from anywhere.
   1. Choose **Start**, open the context (right-click) menu for
      **Computer**, and then choose
      **Properties**.
   2. Choose **Advanced system settings**, **Environment
      Variables**.
   3. For **System Variables**, select the variable
      **Path** and choose **Edit**.
   4. For **Variable value**, append a semicolon and the location
      of your command line utility folder (`;C:\bin\)` to the end
      of the existing value.
   5. Choose **OK** to close the **Edit System Variable** window.

5. Open a new command prompt window. The previous step doesn't update the environment
   variables in your current command prompt windows. The command prompt windows that you
   open now that you completed the previous step are updated.

###### To initialize a volume using dd for Windows

Run the following command to read all blocks on the specified device (and send the
output to the `/dev/null` virtual device). This command safely
initializes your existing data.

```
`dd if=\\.\PHYSICALDRIVE`n` of=/dev/null bs=1M --progress --size`
```

You might get an error if **dd** attempts to read beyond the end of the
volume. You can safely ignore this error.

If you used an earlier version of the **dd** command, it does not
support the `/dev/null` device. Instead, you can use the `nul`
device as follows.

```
`dd if=\\.\PHYSICALDRIVE`n` of=nul bs=1M --progress --size`
```

Use the fio utility
Complete the following procedures to install and use **fio** to initialize a volume.

###### To install **fio** for Windows

The **fio** for Windows program provides a similar experience to the
**fio** program that is commonly available for Linux and Unix
systems, and it allows you to initialize Amazon EBS volumes created from snapshots. For more
information, see [https://github.com/axboe/fio](https://github.com/axboe/fio "https://github.com/axboe/fio").

1. Download the [**fio**
   MSI](https://github.com/axboe/fio/releases "https://github.com/axboe/fio/releases") installer by expanding **Assets** for the latest
   release and selecting the MSI installer.
2. Install **fio**.

###### To initialize a volume using **fio** for Windows

1. Run a command similar to the following to initialize a volume:

```
fio --filename=\\.\PHYSICALDRIVE`n`  --rw=read --bs=1M --iodepth=32 --direct=1 --name=volume-initialize
```

2. When the operation completes, you are ready to use your new volume. For more
   information, see [Make an Amazon EBS volume available for use](ebs-using-volumes.md "ebs-using-volumes.md").
