# Performance tips

When using Amazon FSx for Lustre, keep the following performance tips in mind. For service limits, see
[Service quotas for Amazon FSx for Lustre](limits.md "limits.md").

- **Average I/O size** – Because Amazon FSx for Lustre is a network
  file system, each file operation goes through a round trip between the client and Amazon FSx for Lustre,
  incurring a small latency overhead. Due to this per-operation latency, overall throughput
  generally increases as the average I/O size increases, because the overhead is amortized
  over a larger amount of data.
- **Request model** – By enabling asynchronous writes
  to your file system, pending write operations are buffered on the Amazon EC2 instance before
  they are written to Amazon FSx for Lustre asynchronously. Asynchronous writes typically have lower
  latencies. When performing asynchronous writes, the kernel uses additional memory for
  caching. A file system that has enabled synchronous writes issues synchronous requests to
  Amazon FSx for Lustre. Every operation goes through a round trip between the client and Amazon FSx for Lustre.

###### Note

Your chosen request model has tradeoffs in consistency (if you're using multiple
Amazon EC2 instances) and speed.

- **Limit directory size** – To achieve optimal
  metadata performance on Persistent 2 FSx for Lustre file systems, limit each directory to
  less than 100K files. Limiting the number of files in a directory reduces the time
  required for the file system to acquire a lock on the parent directory.
- **Amazon EC2 instances** – Applications that perform a
  large number of read and write operations likely need more memory or computing capacity
  than applications that don't. When launching your Amazon EC2 instances for your
  compute-intensive workload, choose instance types that have the amount of these resources
  that your application needs. The performance characteristics of Amazon FSx for Lustre file systems don't
  depend on the use of Amazon EBS–optimized instances.
- **Recommended client instance tuning for optimal performance**

      1. For client instance types with memory of more than 64 GiB, we recommend
       applying the following tuning:



      ```
      sudo lctl set_param ldlm.namespaces.*.lru_max_age=600000
      sudo lctl set_param ldlm.namespaces.*.lru_size=<100 * `number_of_CPUs`>
      ```
      2. For client instance types with more than 64 vCPU cores, we recommend
       applying the following tuning:



      ```
      echo "options ptlrpc ptlrpcd_per_cpt_max=32" >> /etc/modprobe.d/modprobe.conf
      echo "options ksocklnd credits=2560" >> /etc/modprobe.d/modprobe.conf

      # reload all kernel modules to apply the above two settings
      sudo reboot
      ```

      After the client is mounted, the following tuning needs to be applied:



      ```
      sudo lctl set_param osc.*OST*.max_rpcs_in_flight=32
      sudo lctl set_param mdc.*.max_rpcs_in_flight=64
      sudo lctl set_param mdc.*.max_mod_rpcs_in_flight=50
      ```
      3. To optimize performance for directory listing (ls), the following tuning needs to be applied:



      ```
      sudo lctl set_param llite.*.statahead_max=512
      sudo lctl set_param llite.*.statahead_agl=1
      if sudo lctl get_param llite.*.statahead_xattr > /dev/null 2>&1; then
          sudo lctl set_param llite.*.statahead_xattr=1
      else
          echo "Warning: Xattr statahead is not supported on this Lustre client. Please upgrade to the latest Lustre 2.15 client to apply this tuning"
      fi
      ```

  Note that `lctl set_param` is known to not persist over reboot.
  Since these parameters cannot be set permanently from the client side, it is
  recommended to implement a boot cron job to set the configuration with the
  recommended tunings.

- **Workload balance across OSTs** – In some cases,
  your workload isn’t driving the aggregate throughput that your file system can provide
  (200 MBps per TiB of storage). If so, you can use CloudWatch metrics to troubleshoot if
  performance is affected by an imbalance in your workload’s I/O patterns. To identify if
  this is the cause, look at the Maximum CloudWatch metric for Amazon FSx for Lustre.

In some cases, this statistic shows a load at or above 240 MBps of throughput (the
throughput capacity of a single 1.2-TiB Amazon FSx for Lustre disk). In such cases, your workload is not
evenly spread out across your disks. If this is the case, you can use the `lfs
 setstripe` command to modify the striping of files your workload is most
frequently accessing. For optimal performance, stripe files with high throughput
requirements across all the OSTs comprising your file system.

If your files are imported from a data repository, you can take another approach to
stripe your high-throughput files evenly across your OSTs. To do this, you can modify the
`ImportedFileChunkSize` parameter when creating your next Amazon FSx for Lustre file
system.

For example, suppose that your workload uses a 7.0-TiB file system (which is made up
of 6x 1.17-TiB OSTs) and needs to drive high throughput across 2.4-GiB files. In this
case, you can set the `ImportedFileChunkSize` value to `(2.4 GiB / 6 OSTs)
 = 400 MiB` so that your files are spread evenly across your file system’s
OSTs.

- **Lustre client for Metadata IOPS** – If
  your file system has a metadata configuration specified, we recommend you install
  a Lustre 2.15 client or a Lustre 2.12 client with one of these OS versions:
  Amazon Linux 2023; Amazon Linux 2; Red Hat/Rocky Linux 8.9, 8.10, or 9.x; CentOS 8.9 or 8.10;
  Ubuntu 22+ with 6.2, 6.5, or 6.8 kernel; or Ubuntu 20.

## Intelligent-Tiering performance considerations

Here are a few important performance considerations when working with file systems using the Intelligent-Tiering storage class:

- Workloads reading data with smaller I/O sizes will require higher concurrency and incur more request costs
  to achieve the same throughput as workloads using large I/O sizes due to higher latency from Intelligent-Tiering storage
  tiers. We recommend configuring your SSD read cache large enough to support the higher concurrency and throughput when
  working with smaller IO sizes.
- The maximum disk IOPS your clients can drive with an Intelligent-Tiering file system depends on the
  specific access patterns of your workload and whether you have provisioned an SSD read cache. For workloads with
  random access, clients can typically drive much higher IOPS if the data is cached in the SSD read cache than if
  the data is not in the cache.
- Intelligent-Tiering storage class supports read-ahead to optimize performance for sequential read requests.
  We recommend configuring your data access pattern sequentially when possible to allow for pre-fetching data and higher
  performance.
