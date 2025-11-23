# Benchmark Amazon EBS volumes

You can test the performance of Amazon EBS volumes by simulating I/O workloads. The process is
as follows:

1. Launch an EBS-optimized instance.
2. Create new EBS volumes.
3. Attach the volumes to your EBS-optimized instance.
4. Configure and mount the block device.
5. Install a tool to benchmark I/O performance.
6. Benchmark the I/O performance of your volumes.
7. Delete your volumes and terminate your instance so that you don't continue to incur
   charges.

###### Important

Some of the procedures result in the destruction of existing data on the EBS volumes you benchmark.
The benchmarking procedures are intended for use on volumes specially created for testing purposes,
not production volumes.

## Set up your instance

To get optimal performance from EBS volumes, we recommend that you use an EBS-optimized
instance. EBS-optimized instances deliver dedicated throughput between Amazon EC2 and Amazon EBS, with
instance. EBS-optimized instances deliver dedicated bandwidth between Amazon EC2 and Amazon EBS, with
specifications depending on the instance type.

To create an EBS-optimized instance, choose **Launch as an EBS-optimized
instance** when launching the instance using the Amazon EC2 console, or specify
**--ebs-optimized** when using the command line. Be sure that you select an
instance type that supports this option.

### Set up Provisioned IOPS SSD or General Purpose SSD volumes

To create Provisioned IOPS SSD (`io1` and `io2`) or General Purpose SSD (`gp2` and `gp3`) volumes using the Amazon EC2 console,
for **Volume type**, choose **Provisioned IOPS SSD (io1)**,
**Provisioned IOPS SSD (io2)**, **General Purpose SSD (gp2)**, or
**General Purpose SSD (gp3)**. At the command line, specify `io1`, `io2`,
`gp2`, or `gp3` for the **--volume-type** parameter.
For `io1`, `io2`, and `gp3` volumes, specify the number of I/O operations per second (IOPS)
for the **--iops** parameter. For more information, see
[Amazon EBS volume types](ebs-volume-types.md "ebs-volume-types.md") and
[Create an Amazon EBS volume](ebs-creating-volume.md "ebs-creating-volume.md").

(_Linux instances only_) For the example tests, we recommend that
you create a RAID 0 array with 6 volumes, which offers a high level of performance. Because
you are charged by gigabytes provisioned (and the number of provisioned IOPS for io1, io2,
and gp3 volumes), not the number of volumes, there is no additional cost for creating
multiple, smaller volumes and using them to create a stripe set. If you're using Oracle
Orion to benchmark your volumes, it can simulate striping the same way that Oracle ASM does,
so we recommend that you let Orion do the striping. If you are using a different benchmarking
tool, you need to stripe the volumes yourself.

For more information about how to create a RAID 0 array, see
[Create a RAID 0 array](raid-config.md#create-raid-array "raid-config.md#create-raid-array").

### Set up Throughput Optimized HDD (`st1`) or Cold HDD (`sc1`) volumes

To create an `st1` volume, choose **Throughput Optimized HDD** when creating the
volume using the Amazon EC2 console, or specify **--type `st1`** when
using the command line. To create an `sc1` volume, choose Cold HDD when creating the volume
using the Amazon EC2 console, or specify **--type `sc1`** when using the command
line. For information about creating EBS volumes, see [Create an Amazon EBS volume](ebs-creating-volume.md "ebs-creating-volume.md"). For information about attaching these volumes to
your instance, see [Attach an Amazon EBS volume to an Amazon EC2 instance](ebs-attaching-volume.md "ebs-attaching-volume.md").

(_Linux instances only_) AWS provides a JSON template for use with CloudFormation that simplifies this setup procedure.
Access the [template](https://s3.amazonaws.com/cloudformation-examples/community/st1_cloudformation_template.json "https://s3.amazonaws.com/cloudformation-examples/community/st1_cloudformation_template.json") and save it as a JSON file. CloudFormation allows you to configure your own SSH
keys and offers an easier way to set up a performance test environment to evaluate `st1`
volumes. The template creates a current-generation instance and a 2 TiB `st1` volume, and
attaches the volume to the instance at `/dev/xvdf`.

###### (_Linux instances only_) To create an HDD volume using the template

1. Open the CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. Choose **Create Stack**.
3. Choose **Upload a Template to Amazon S3** and select the JSON
   template you previously obtained.
4. Give your stack a name like “ebs-perf-testing”, and select an instance type (the
   default is r3.8xlarge) and SSH key.
5. Choose **Next** twice, and then choose **Create
   Stack**.
6. After the status for your new stack moves from **CREATE_IN_PROGRESS**
   to **COMPLETE**, choose **Outputs** to get the public
   DNS entry for your new instance, which will have a 2 TiB `st1` volume attached to it.
7. Connect using SSH to your new stack as user `ec2-user`, with
   the hostname obtained from the DNS entry in the previous step.
8. Proceed to [Install benchmark tools](#install_tools "#install_tools").

## Install benchmark tools

The following tables lists some of the possible tools you can use to benchmark the
performance of EBS volumes.

| Tool                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| fio                                                                                                                                                                                          | For benchmarking I/O performance. (Note that **fio\*<br>• has a<br>dependency on `libaio-devel`.)<br>To install **fio*<br>• on Amazon Linux, run the following command:<br>``<br>`$` `sudo yum install -y fio`<br>``<br>To install \*\*fio*<br>• on Ubuntu, run the following command:<br>``<br>`sudo apt-get install -y fio`<br>`` |
| [Oracle Orion Calibration Tool](https://docs.oracle.com/cd/E18283_01/server.112/e16638/iodesign.htm#BABFCFBC "https://docs.oracle.com/cd/E18283_01/server.112/e16638/iodesign.htm#BABFCFBC") | For calibrating the I/O performance of storage systems to be used with Oracle<br>databases.                                                                                                                                                                                                                                         |

| Tool                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [DiskSpd](https://github.com/microsoft/diskspd/releases "https://github.com/microsoft/diskspd/releases") | DiskSpd is a storage performance tool from the Windows, Windows Server, and Cloud Server<br>Infrastructure engineering teams at Microsoft. It is available for download at<br>[https://github.com/Microsoft/diskspd/releases](https://github.com/Microsoft/diskspd/releases "https://github.com/Microsoft/diskspd/releases").<br>After you download the `diskspd.exe` executable file, open a<br>command prompt with administrative rights (by choosing "Run as Administrator"),<br>and then navigate to the directory where you copied the `diskspd.exe` file.<br>Copy the<br>desired `diskspd.exe` executable file from the appropriate executable folder<br>(`amd64fre`, `armfre` or `x86fre)` to a short, simple path like `C:\DiskSpd`. In most cases<br>you will want the 64-bit version of DiskSpd from the `amd64fre` folder.<br>The source<br>code for DiskSpd is hosted on GitHub at: [https://github.com/Microsoft/diskspd](https://github.com/Microsoft/diskspd "https://github.com/Microsoft/diskspd"). |
| CrystalDiskMark                                                                                          | CrystalDiskMark is a simple disk benchmark software. It is available for download at<br>[https://crystalmark.info/en/software/crystaldiskmark/](https://crystalmark.info/en/software/crystaldiskmark/ "https://crystalmark.info/en/software/crystaldiskmark/").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

These benchmarking tools support a wide variety of test parameters. You should use
commands that approximate the workloads your volumes will support. These commands provided
below are intended as examples to help you get started.

## Choose the volume queue length

Choosing the best volume queue length based on your workload and volume type.

### Queue length on SSD-backed volumes

To determine the optimal queue length for your workload on SSD-backed volumes, we
recommend that you target a queue length of 1 for every 1000 IOPS available (baseline for
General Purpose SSD volumes and the provisioned amount for Provisioned IOPS SSD volumes). Then you can monitor your
application performance and tune that value based on your application requirements.

Increasing the queue length is beneficial until you achieve the provisioned IOPS,
throughput or optimal system queue length value, which is currently set to 32.
For example, a volume with 3,000 provisioned IOPS should target a queue length
of 3. You should experiment with tuning these values up or down to see what
performs best for your application.

### Queue length on HDD-backed volumes

To determine the optimal queue length for your workload on HDD-backed volumes, we
recommend that you target a queue length of at least 4 while performing 1MiB sequential
I/Os. Then you can monitor your application performance and tune that value based on your
application requirements. For example, a 2 TiB `st1` volume with burst throughput of 500
MiB/s and IOPS of 500 should target a queue length of 4, 8, or 16 while performing 1,024
KiB, 512 KiB, or 256 KiB sequential I/Os respectively. You should experiment with tuning
these values value up or down to see what performs best for your application.

## Disable C-states

Before you run benchmarking, you should disable processor C-states. Temporarily idle
cores in a supported CPU can enter a C-state to save power. When the core is called on to
resume processing, a certain amount of time passes until the core is again fully
operational. This latency can interfere with processor benchmarking routines. For more
information about C-states and which EC2 instance types support them, see [Processor state control for your EC2
instance](../../../AWSEC2/latest/UserGuide/processor_state_control.md "../../../AWSEC2/latest/UserGuide/processor_state_control.md").

You can disable C-states on Amazon Linux, RHEL, and CentOS as follows:

1. Get the number of C-states.

```
`$` `cpupower idle-info | grep "Number of idle states:"`
```

2. Disable the C-states from c1 to cN. Ideally, the cores should be in state c0.

```
`$` `for i in `seq 1 $((N-1))`; do cpupower idle-set -d $i; done`
```

You can disable C-states on Windows as follows:

1. In PowerShell, get the current active power scheme.

```
$current_scheme = powercfg /getactivescheme
```

2. Get the power scheme GUID.

```
(Get-WmiObject -class Win32_PowerPlan -Namespace "root\cimv2\power" -Filter "ElementName='High performance'").InstanceID
```

3. Get the power setting GUID.

```
(Get-WmiObject -class Win32_PowerSetting -Namespace "root\cimv2\power" -Filter "ElementName='Processor idle disable'").InstanceID
```

4. Get the power setting subgroup GUID.

```
(Get-WmiObject -class Win32_PowerSettingSubgroup -Namespace "root\cimv2\power" -Filter "ElementName='Processor power management'").InstanceID
```

5. Disable C-states by setting the value of the index to 1. A value of 0 indicates that C-states
   are disabled.

```
powercfg /setacvalueindex `<power_scheme_guid>` `<power_setting_subgroup_guid>` `<power_setting_guid>` 1
```

6. Set active scheme to ensure the settings are saved.

```
powercfg /setactive `<power_scheme_guid>`
```

## Perform benchmarking

The following procedures describe benchmarking commands for various EBS volume types.

Run the following commands on an EBS-optimized instance with attached EBS volumes. If
the EBS volumes were created from snapshots, be sure to initialize them before
benchmarking. For more information, see [Manually initialize the volumes after creation](initalize-volume.md#ebs-initialize "initalize-volume.md#ebs-initialize").

###### Tip

You can use the I/O latency histograms provided by the EBS detailed performance statistics to
compare the distribution of I/O performance in your benchmarking tests. For more information,
see [Amazon EBS detailed performance statistics](nvme-detailed-performance-stats.md "nvme-detailed-performance-stats.md").

When you are finished testing your volumes, see the following topics for help cleaning
up: [Delete an Amazon EBS volume](ebs-deleting-volume.md "ebs-deleting-volume.md") and [Terminate your instance](../../../AWSEC2/latest/UserGuide/terminating-instances.md "../../../AWSEC2/latest/UserGuide/terminating-instances.md").

### Benchmark Provisioned IOPS SSD and General Purpose SSD volumes

Run **fio** on the RAID 0 array that you created.

The following command performs 16 KB random write operations.

```
`$` sudo fio `--directory=/mnt/``p_iops_vol0` --ioengine=psync `--name` `fio_test_file` `--direct=1 --rw=randwrite --bs=16k --size=1G --numjobs=16 --time_based --runtime=180 --group_reporting --norandommap`
```

The following command performs 16 KB random read operations.

```
`$` sudo fio `--directory=/mnt/``p_iops_vol0` `--name` `fio_test_file` `--direct=1 --rw=randread --bs=16k --size=1G --numjobs=16 --time_based --runtime=180 --group_reporting --norandommap`
```

For more information about interpreting the results, see this tutorial: [Inspecting disk IO performance with fio](https://www.linux.com/training-tutorials/inspecting-disk-io-performance-fio/ "https://www.linux.com/training-tutorials/inspecting-disk-io-performance-fio/").

Run **DiskSpd** on the volume that you created.

The following command will run a 30 second random I/O test using a 20GB
test file located on the `C:` drive, with a 25% write and 75% read ratio, and
an 8K block size. It will use eight worker threads, each with four outstanding I/Os, and a
write entropy value seed of 1GB. The results of the test will be saved to a text file
called `DiskSpeedResults.txt`. These parameters simulate a SQL Server OLTP
workload.

```
`diskspd -b8K -d30 -o4 -t8 -h -r -w25 -L -Z1G -c20G C:\iotest.dat > DiskSpeedResults.txt`
```

For more information about interpreting the results, see this tutorial: [Inspecting disk IO performance with DiskSPd](https://sqlperformance.com/2015/08/io-subsystem/diskspd-test-storage "https://sqlperformance.com/2015/08/io-subsystem/diskspd-test-storage").

### Benchmark `st1` and `sc1` volumes (Linux instances)

Run **fio** on your `st1` or `sc1` volume.

###### Note

Prior to running these tests, set buffered I/O on your instance as described in
[Increase read-ahead for high-throughput, read-heavy workloads on st1 and sc1 (Linux instances only)](ebs-performance.md#read_ahead "ebs-performance.md#read_ahead").

The following command performs 1 MiB sequential read operations against an attached
`st1` block device (for example, `/dev/xvdf`):

```
`$` **sudo fio** `--filename=/dev/``<device>` `--direct=1 --rw=read` `--randrepeat=0 --ioengine=libaio --bs=1024k --iodepth=8 --time_based=1 --runtime=180` `--name=fio_direct_read_test`
```

The following command performs 1 MiB sequential write operations against an attached
`st1` block device:

```
`$` **sudo fio** `--filename=/dev/``<device>` `--direct=1 --rw=write` `--randrepeat=0 --ioengine=libaio --bs=1024k --iodepth=8 --time_based=1 --runtime=180` `--name=fio_direct_write_test`
```

Some workloads perform a mix of sequential reads and sequential writes to different
parts of the block device. To benchmark such a workload, we recommend that you use
separate, simultaneous **fio** jobs for reads and writes, and use the
**fio**
`offset_increment` option to target different block device locations for each
job.

Running this workload is a bit more complicated than a sequential-write or
sequential-read workload. Use a text editor to create a fio job file,
called `fio_rw_mix.cfg` in this example, that contains the following:

```
[global]
clocksource=clock_gettime
randrepeat=0
runtime=180

[sequential-write]
bs=1M
ioengine=libaio
direct=1
iodepth=8
filename=/dev/`<device>`
do_verify=0
rw=write
rwmixread=0
rwmixwrite=100

[sequential-read]
bs=1M
ioengine=libaio
direct=1
iodepth=8
filename=/dev/`<device>`
do_verify=0
rw=read
rwmixread=100
rwmixwrite=0
offset=100g
```

Then run the following command:

```
`$` sudo fio `fio_rw_mix.cfg`
```

For more information about interpreting the results, see this tutorial: [Inspecting disk I/O performance with fio](https://www.linux.com/training-tutorials/inspecting-disk-io-performance-fio/ "https://www.linux.com/training-tutorials/inspecting-disk-io-performance-fio/").

Multiple **fio** jobs for direct I/O, even though using sequential read
or write operations, can result in lower than expected throughput for `st1` and `sc1`
volumes. We recommend that you use one direct I/O job and use the `iodepth`
parameter to control the number of concurrent I/O operations.
