# Use job attachments with service-managed fleets

Job attachments transfer files between your workstation and Deadline Cloud workers using Amazon Simple Storage Service (Amazon S3). You can use job attachments alone or together with shared storage to attach auxiliary data to jobs that isn't shared with other jobs, such as job scripts, configuration files, or project assets stored locally.

For information about how job attachments work, see [Job attachments](../userguide/storage-job-attachments.md "../userguide/storage-job-attachments.md") in the _Deadline Cloud User Guide_. For details about specifying input and output files in job bundles, see [Use job attachments to share files](build-job-attachments.md "build-job-attachments.md").

## Choose a filesystem mode

When submitting a job with attachments, you can choose how workers load files from Amazon S3 by setting the `fileSystem` property:

- **COPIED** (default) – Downloads all files to local disk before tasks begin. Best when every task needs most input files.
- **VIRTUAL** – Mounts a virtual filesystem that downloads files on-demand. Best when tasks only need a subset of input files. Available on Linux SMF workers only.

###### Important

VIRTUAL mode caching can increase memory consumption and is not optimized for all workloads. We recommend that you test your workload before running production jobs.

For detailed information about configuring the filesystem mode, see [Virtual file system](../userguide/storage-virtual.md "../userguide/storage-virtual.md") in the _Deadline Cloud User Guide_.

## Optimize transfer performance

The speed of synchronizing files from Amazon S3 to SMF workers depends on the Amazon Elastic Block Store (Amazon EBS) volume configuration of your fleet. By default, SMF workers use gp3 Amazon EBS volumes with baseline performance settings. For workloads with large input files or many small files, you can improve transfer speeds by increasing the Amazon EBS throughput and IOPS settings. You can update these settings using the AWS Command Line Interface (AWS CLI).

Throughput (MiB/s)

The rate at which data can be read from or written to the volume. Default is 125 MiB/s, maximum is 1,000 MiB/s for gp3 volumes. Increase for large sequential file transfers.

IOPS

Input/output operations per second. Default is 3,000 IOPS, maximum is 16,000 IOPS for gp3 volumes. Increase when transferring many small files.

###### Note

Increasing Amazon EBS throughput and IOPS increases fleet cost. For pricing information, see [Deadline Cloud pricing](https://aws.amazon.com/deadline-cloud/pricing/ "https://aws.amazon.com/deadline-cloud/pricing/").

###### To update Amazon EBS settings on an existing fleet using the AWS CLI

- Run the following command:

```
aws deadline update-fleet \
  --farm-id `farm-0123456789abcdef0` \
  --fleet-id `fleet-0123456789abcdef0` \
  --configuration '{
    "serviceManagedEc2": {
      "instanceCapabilities": {
        "vCpuCount": {"min": 4},
        "memoryMiB": {"min": 8192},
        "osFamily": "linux",
        "cpuArchitectureType": "x86_64",
        "rootEbsVolume": {
          "sizeGiB": 250,
          "iops": 6000,
          "throughputMiB": 500
        }
      },
      "instanceMarketOptions": {"type": "spot"}
    }
  }'
```

## Download job outputs

After your job completes, download output files using the Deadline Cloud CLI or AWS Deadline Cloud monitor (Deadline Cloud monitor):

```
deadline job download-output --job-id `job-0123456789abcdef0`
```

For automatic downloading of outputs as jobs complete, see [Automatic downloads](../userguide/auto-downloads.md "../userguide/auto-downloads.md") in the _Deadline Cloud User Guide_.
