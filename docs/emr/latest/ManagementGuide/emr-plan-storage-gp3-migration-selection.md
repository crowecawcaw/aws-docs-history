# Selecting IOPS and throughput

when migrating to gp3 Amazon EBS volume types

When provisioning a gp2 volume, you must figure out the size of the volume in order to
get the proportional IOPS and throughput. With gp3, you don’t have to provision a bigger
volume to get higher performance. You can choose your desired size and performance
according to application need. Selecting the right size and right performance parameters
(IOPS, throughput) can provide you maximum cost reduction, without affecting
performance.

Here is a table to help you select gp3 configuration options:

| Volume size  | IOPS                                                                         | Throughput                                                                                                        |
| ------------ | ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| 1–170 GiB    | 3000                                                                         | 125 MiB/s                                                                                                         |
| 170–334 GiB  | 3000                                                                         | 125 MiB/s if the chosen EC2 instance type supports 125MiB/s or less,<br>use higher as per usage, Max 250 MiB/s\*. |
| 334–1000 GiB | 3000                                                                         | 125 MiB/s if the chosen EC2 instance type supports 125MiB/s or less,<br>Use higher as per usage, Max 250 MiB/s\*. |
| 1000+ GiB    | Match gp2 IOPS (Size in GiB x 3) or Max IOPS driven by current gp2<br>volume | 125 MiB/s if the chosen EC2 instance type supports 125MiB/s or less,<br>Use higher as per usage, Max 250 MiB/s\*. |

\*Gp3 has the capability to provide throughput up to 2000 MiB/s. Since gp2 provides a
maximum of 250MiB/s throughput, you may not need to go beyond this limit when you use
gp3. Gp3 volumes deliver a consistent baseline throughput performance of 125 MiB/s, which is included with
the price of storage. You can provision additional throughput (up to a maximum of 2,000 MiB/s) for an additional cost at a
ratio of 0.25 MiB/s per provisioned IOPS. Maximum throughput can be provisioned at 8,000 IOPS or higher and
16 GiB or larger (8,000 IOPS × 0.25 MiB/s per IOPS = 2,000 MiB/s).
