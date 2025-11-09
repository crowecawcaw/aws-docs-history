# Performance characteristics of SSD and HDD storage classes

The throughput that an FSx for Lustre file system provisioned with SSD or HDD storage class
supports is proportional to its storage capacity. Amazon FSx for Lustre file systems scale to multiple TBps
of throughput and millions of IOPS.
Amazon FSx for Lustre also supports concurrent access to the same file or directory from thousands of compute
instances. This access enables rapid data checkpointing from application memory to storage,
which is a common technique in high performance computing (HPC). You can increase the amount
of storage and throughput capacity as needed at any time after you create the file system. For
more information, see [Managing storage capacity](managing-storage-capacity.md "managing-storage-capacity.md").

FSx for Lustre file systems provide burst read throughput using a network I/O credit mechanism
to allocate network bandwidth based on average bandwidth utilization. The file systems accrue credits
when their network bandwidth usage is below their baseline limits, and can use these credits when they
perform network data transfers.

The following tables show performance that the FSx for Lustre deployment options using SSD and HDD
storage classes are designed for.

| File system performance for SSD storage options | Deployment Type | **Network throughput (MBps/TiB of storage<br>provisioned)** | **Network IOPS (IOPS/TiB of storage provisioned)**    | **Cache storage (GiB of RAM/TiB of storage provisioned)** | **Disk latencies per file operation (milliseconds, P50)** | **Disk throughput (MBps/TiB of storage or SSD cache<br>provisioned)** |
| ----------------------------------------------- | --------------- | ----------------------------------------------------------- | ----------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------------------- | --------- |
|                                                 | **Baseline**    | **Burst**                                                   |                                                       |                                                           |                                                           | **Baseline**                                                          | **Burst** |
| SCRATCH_2                                       | 200             | 1300                                                        | Tens of thousands baselineHundreds of thousands burst | 6.7                                                       | Metadata: sub-ms<br>Data: sub-ms                          | 200 (read)<br>100 (write)                                             | ‐         |
| PERSISTENT-125                                  | 320             | 1300                                                        | 3.4                                                   | 125                                                       | 500                                                       |
| PERSISTENT-250                                  | 640             | 1300                                                        | 6.8                                                   | 250                                                       | 500                                                       |
| PERSISTENT-500                                  | 1300            | ‐                                                           | 13.7                                                  | 500                                                       | ‐                                                         |
| PERSISTENT-1000                                 | 2600            | ‐                                                           | 27.3                                                  | 1000                                                      | ‐                                                         |

| File system performance for HDD storage options | Deployment Type | **Network throughput (MBps/TiB of storage<br>or SSD cache provisioned)** | **Network IOPS (IOPS/TiB of storage provisioned)**        | **Cache storage (GiB of RAM/TiB of storage provisioned)** | **Disk latencies per file operation (milliseconds, P50)** | **Disk throughput (MBps/TiB of storage or SSD cache<br>provisioned)** |
| ----------------------------------------------- | --------------- | ------------------------------------------------------------------------ | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------------------- | ------------------------- |
|                                                 | **Baseline**    | **Burst**                                                                |                                                           | **Baseline**                                              | **Burst**                                                 |
| PERSISTENT-12                                   |
| HDD storage                                     | 40              | 375\*                                                                    | Tens of thousands baseline<br>Hundreds of thousands burst | 0.4 memory                                                | Metadata: sub-ms<br>Data: single-digit ms                 | 12                                                                    | 80 (read)<br>50 (write)   |
| SSD read cache                                  | 200             | 1,900                                                                    | 200 SSD cache                                             | Data: sub-ms                                              | 200                                                       | -                                                                     |
| PERSISTENT-40                                   |
| HDD storage                                     | 150             | 1,300\*                                                                  | Tens of thousands baseline<br>Hundreds of thousands burst | 1.5                                                       | Metadata: sub-ms<br>Data: single-digit ms                 | 40                                                                    | 250 (read)<br>150 (write) |
| SSD read cache                                  | 750             | 6500                                                                     | 200 SSD cache                                             | Data: sub-ms                                              | 200                                                       | -                                                                     |

| File system performance for previous generation SSD storage options | Deployment Type | **Network throughput (MBps per TiB of storage<br>provisioned)** | **Network IOPS (IOPS per TiB of storage provisioned)** | **Cache storage (GiB per TiB of storage provisioned)** | **Disk latencies per file operation (milliseconds, P50)** | **Disk throughput (MBps per TiB of storage or SSD cache<br>provisioned)** |
| ------------------------------------------------------------------- | --------------- | --------------------------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------ | --------------------------------------------------------- | ------------------------------------------------------------------------- | --------- |
|                                                                     | **Baseline**    | **Burst**                                                       |                                                        |                                                        |                                                           | **Baseline**                                                              | **Burst** |
| PERSISTENT-50                                                       | 250             | 1,300\*                                                         | Tens of thousands baselineHundreds of thousands burst  | 2.2 RAM                                                | Metadata: sub-ms<br>Data: sub-ms                          | 50                                                                        | 240       |
| PERSISTENT-100                                                      | 500             | 1,300\*                                                         | 4.4 RAM                                                | 100                                                    | 240                                                       |
| PERSISTENT-200                                                      | 750             | 1,300\*                                                         | 8.8 RAM                                                | 200                                                    | 240                                                       |

###### Note

\* Persistent file systems in the following AWS Regions provide network burst up to 530 MBps per
TiB of storage: Africa (Cape Town), Asia Pacific (Hong Kong), Asia Pacific (Osaka), Asia Pacific (Singapore), Canada (Central),
Europe (Frankfurt), Europe (London), Europe (Milan), Europe (Stockholm), Middle East (Bahrain),
South America (São Paulo), China, and US West (Los Angeles).

## Example: Aggregate baseline and burst

throughput

The following example illustrates how storage capacity and disk throughput impact file system performance.

A persistent file system with a storage capacity of 4.8 TiB and 50 MBps per TiB of throughput per unit of storage
provides an aggregate baseline disk throughput of 240 MBps and a burst disk throughput of 1.152 GBps.

Regardless of file system size, Amazon FSx for Lustre provides consistent, sub-millisecond
latencies for file operations.
