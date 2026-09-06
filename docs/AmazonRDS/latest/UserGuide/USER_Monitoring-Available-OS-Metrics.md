

# OS metrics in Enhanced Monitoring
<a name="USER_Monitoring-Available-OS-Metrics"></a>

Amazon RDS provides metrics in real time for the operating system (OS) that your DB instance runs on. RDS delivers the metrics from Enhanced Monitoring to your Amazon CloudWatch Logs account. The following tables list the OS metrics available using Amazon CloudWatch Logs.



**Topics**
+ [OS metrics for Db2, MariaDB, MySQL, Oracle, and PostgreSQL](#USER_Monitoring-Available-OS-Metrics-RDS)
+ [OS metrics for Microsoft SQL Server](#USER_Monitoring-Available-OS-Metrics-RDS.SQLServer)

## OS metrics for Db2, MariaDB, MySQL, Oracle, and PostgreSQL
<a name="USER_Monitoring-Available-OS-Metrics-RDS"></a>

RDS collects disk metrics for `rdsdbdata` as well as additional storage volumes present in the OS. To view OS metrics in CloudWatch Logs, see [Viewing OS metrics using CloudWatch Logs](USER_Monitoring.OS.CloudWatchLogs.md).

<a name="cloudwatch-os-metrics"></a>

- **  `General`  **
  - **Metric:**  `engine`  / **Console name:**  Not applicable  / **Description:** The database engine for the DB instance.
  - **Metric:**  `instanceID`  / **Console name:**  Not applicable  / **Description:** The DB instance identifier.
  - **Metric:**  `instanceResourceID`  / **Console name:**  Not applicable  / **Description:** An immutable identifier for the DB instance that is unique to an AWS Region, also used as the log stream identifier. 
  - **Metric:**  `numVCPUs`  / **Console name:**  Not applicable  / **Description:** The number of virtual CPUs for the DB instance.
  - **Metric:**  `timestamp`  / **Console name:**  Not applicable  / **Description:** The time at which the metrics were taken.
  - **Metric:**  `uptime`  / **Console name:**  Not applicable  / **Description:** The amount of time that the DB instance has been active.
  - **Metric:**  `version`  / **Console name:**  Not applicable  / **Description:** The version of the OS metrics' stream JSON format.

- **  `cpuUtilization`  **
  - **Metric:**  `guest`  / **Console name:**  **CPU Guest**  / **Description:** The percentage of CPU in use by guest programs.
  - **Metric:**  `idle`  / **Console name:**  **CPU Idle**  / **Description:** The percentage of CPU that is idle.
  - **Metric:**  `irq`  / **Console name:**  **CPU IRQ**  / **Description:** The percentage of CPU in use by software interrupts.
  - **Metric:**  `nice`  / **Console name:**  **CPU Nice**  / **Description:** The percentage of CPU in use by programs running at lowest priority.
  - **Metric:**  `steal`  / **Console name:**  **CPU Steal**  / **Description:** The percentage of CPU in use by other virtual machines.
  - **Metric:**  `system`  / **Console name:**  **CPU System**  / **Description:** The percentage of CPU in use by the kernel.
  - **Metric:**  `total`  / **Console name:**  **CPU Total**  / **Description:** The total percentage of the CPU in use. This value includes the `nice` value. 
  - **Metric:**  `user`  / **Console name:**  **CPU User**  / **Description:** The percentage of CPU in use by user programs.
  - **Metric:**  `wait`  / **Console name:**  **CPU Wait**  / **Description:** The percentage of CPU unused while waiting for I/O access.

- **  `diskIO`  **
  - **Metric:**  `avgQueueLen`  / **Console name:**  **Avg Queue Size**  / **Description:** The number of requests waiting in the I/O device's queue.
  - **Metric:**  `avgReqSz`  / **Console name:**  **Ave Request Size**  / **Description:** The average request size, in kilobytes.
  - **Metric:**  `await`  / **Console name:**  **Disk I/O Await**  / **Description:** The number of milliseconds required to respond to requests, including queue time and service time.
  - **Metric:**  `device`  / **Console name:**  Not applicable  / **Description:** The identifier of the disk device in use.
  - **Metric:**  `readIOsPS`  / **Console name:**  **Read IO/s**  / **Description:** The number of read operations per second. 
  - **Metric:**  `readKb`  / **Console name:**  **Read Total**  / **Description:** The total number of kilobytes read. 
  - **Metric:**  `readKbPS`  / **Console name:**  **Read Kb/s**  / **Description:** The number of kilobytes read per second.
  - **Metric:**  `readLatency`  / **Console name:**  **Read Latency**  / **Description:** The elapsed time between the submission of a read I/O request and its completion, in milliseconds.<br />This metric is only available for Amazon Aurora.
  - **Metric:**  `readThroughput`  / **Console name:**  **Read Throughput**  / **Description:** The amount of network throughput used by requests to the DB cluster, in bytes per second.<br />This metric is only available for Amazon Aurora.
  - **Metric:**  `rrqmPS`  / **Console name:**  **Rrqms**  / **Description:** The number of merged read requests queued per second. 
  - **Metric:**  `tps`  / **Console name:**  **TPS**  / **Description:** The number of I/O transactions per second.
  - **Metric:**  `util`  / **Console name:**  **Disk I/O Util**  / **Description:** The percentage of CPU time during which requests were issued. 
  - **Metric:**  `writeIOsPS`  / **Console name:**  **Write IO/s**  / **Description:** The number of write operations per second.
  - **Metric:**  `writeKb`  / **Console name:**  **Write Total**  / **Description:** The total number of kilobytes written.
  - **Metric:**  `writeKbPS`  / **Console name:**  **Write Kb/s**  / **Description:** The number of kilobytes written per second.
  - **Metric:**  `writeLatency`  / **Console name:**  **Write Latency**  / **Description:** The average elapsed time between the submission of a write I/O request and its completion, in milliseconds.<br />This metric is only available for Amazon Aurora.
  - **Metric:**  `writeThroughput`  / **Console name:**  **Write Throughput**  / **Description:** The amount of network throughput used by responses from the DB cluster, in bytes per second.<br />This metric is only available for Amazon Aurora.
  - **Metric:**  `wrqmPS`  / **Console name:**  **Wrqms**  / **Description:** The number of merged write requests queued per second.

- **  `physicalDeviceIO`  **
  - **Metric:**  `avgQueueLen`  / **Console name:**  **Physical Devices Avg Queue Size**  / **Description:** The number of requests waiting in the I/O device's queue.
  - **Metric:**  `avgReqSz`  / **Console name:**  **Physical Devices Ave Request Size**  / **Description:** The average request size, in kilobytes.
  - **Metric:**  `await`  / **Console name:**  **Physical Devices Disk I/O Await**  / **Description:** The number of milliseconds required to respond to requests, including queue time and service time.
  - **Metric:**  `device`  / **Console name:**  Not applicable  / **Description:** The identifier of the disk device in use.
  - **Metric:** mountPoint / **Console name:** Not applicable / **Description:** The path to the file system.
  - **Metric:**  `readIOsPS`  / **Console name:**  **Physical Devices Read IO/s**  / **Description:** The number of read operations per second. 
  - **Metric:**  `readKb`  / **Console name:**  **Physical Devices Read Total**  / **Description:** The total number of kilobytes read. 
  - **Metric:**  `readKbPS`  / **Console name:**  **Physical Devices Read Kb/s**  / **Description:** The number of kilobytes read per second.
  - **Metric:**  `rrqmPS`  / **Console name:**  **Physical Devices Rrqms**  / **Description:** The number of merged read requests queued per second. 
  - **Metric:**  `tps`  / **Console name:**  **Physical Devices TPS**  / **Description:** The number of I/O transactions per second.
  - **Metric:**  `util`  / **Console name:**  **Physical Devices Disk I/O Util**  / **Description:** The percentage of CPU time during which requests were issued. 
  - **Metric:**  `writeIOsPS`  / **Console name:**  **Physical Devices Write IO/s**  / **Description:** The number of write operations per second.
  - **Metric:**  `writeKb`  / **Console name:**  **Physical Devices Write Total**  / **Description:** The total number of kilobytes written.
  - **Metric:**  `writeKbPS`  / **Console name:**  **Physical Devices Write Kb/s**  / **Description:** The number of kilobytes written per second.
  - **Metric:**  `wrqmPS`  / **Console name:**  **Physical Devices Wrqms**  / **Description:** The number of merged write requests queued per second.

- **  `fileSys`  **
  - **Metric:**  `maxFiles`  / **Console name:**  **Max Inodes**  / **Description:** The maximum number of files that can be created for the file system.
  - **Metric:**  `mountPoint`  / **Console name:**  Not applicable  / **Description:** The path to the file system. When this is `/rdsdbdata*`, it represents the aggregate of all storage volumes. 
  - **Metric:**  `name`  / **Console name:**  Not applicable  / **Description:** The name of the file system.
  - **Metric:**  `total`  / **Console name:**  **Total Filesystem**  / **Description:** The total number of disk space available for the file system, in kilobytes.
  - **Metric:**  `used`  / **Console name:**  **Used Filesystem**  / **Description:** The amount of disk space used by files in the file system, in kilobytes.
  - **Metric:**  `usedFilePercent`  / **Console name:**  **Used Inodes**  / **Description:** The percentage of available files in use.
  - **Metric:**  `usedFiles`  / **Console name:**  **Used%**  / **Description:** The number of files in the file system.
  - **Metric:**  `usedPercent`  / **Console name:**  **Used Filesystem**  / **Description:** The percentage of the file-system disk space in use.

- **  `loadAverageMinute`  **
  - **Metric:**  `fifteen`  / **Console name:**  **Load Avg 15 min**  / **Description:** The number of processes requesting CPU time over the last 15 minutes.
  - **Metric:**  `five`  / **Console name:**  **Load Avg 5 min**  / **Description:** The number of processes requesting CPU time over the last 5 minutes.
  - **Metric:**  `one`  / **Console name:**  **Load Avg 1 min**  / **Description:** The number of processes requesting CPU time over the last minute.

- **  `memory`  **
  - **Metric:**  `active`  / **Console name:**  **Active Memory**  / **Description:** The amount of assigned memory, in kilobytes.
  - **Metric:**  `buffers`  / **Console name:**  **Buffered Memory**  / **Description:**  The amount of memory used for buffering I/O requests prior to writing to the storage device, in kilobytes. 
  - **Metric:**  `cached`  / **Console name:**  **Cached Memory**  / **Description:** The amount of memory used for caching file system–based I/O.
  - **Metric:**  `dirty`  / **Console name:**  **Dirty Memory**  / **Description:**  The amount of memory pages in RAM that have been modified but not written to their related data block in storage, in kilobytes. 
  - **Metric:**  `free`  / **Console name:**  **Free Memory**  / **Description:** The amount of unassigned memory, in kilobytes.
  - **Metric:**  `hugePagesFree`  / **Console name:**  **Huge Pages Free**  / **Description:**  The number of free huge pages. Huge pages are a feature of the Linux kernel. 
  - **Metric:**  `hugePagesRsvd`  / **Console name:**  **Huge Pages Rsvd**  / **Description:** The number of committed huge pages.
  - **Metric:**  `hugePagesSize`  / **Console name:**  **Huge Pages Size**  / **Description:** The size for each huge pages unit, in kilobytes.
  - **Metric:**  `hugePagesSurp`  / **Console name:**  **Huge Pages Surp**  / **Description:** The number of available surplus huge pages over the total.
  - **Metric:**  `hugePagesTotal`  / **Console name:**  **Huge Pages Total**  / **Description:** The total number of huge pages.
  - **Metric:**  `inactive`  / **Console name:**  **Inactive Memory**  / **Description:** The amount of least-frequently used memory pages, in kilobytes.
  - **Metric:**  `mapped`  / **Console name:**  **Mapped Memory**  / **Description:**  The total amount of file-system contents that is memory mapped inside a process address space, in kilobytes. 
  - **Metric:**  `pageTables`  / **Console name:**  **Page Tables**  / **Description:** The amount of memory used by page tables, in kilobytes.
  - **Metric:**  `slab`  / **Console name:**  **Slab Memory**  / **Description:** The amount of reusable kernel data structures, in kilobytes.
  - **Metric:**  `total`  / **Console name:**  **Total Memory**  / **Description:** The total amount of memory, in kilobytes.
  - **Metric:**  `writeback`  / **Console name:**  **Writeback Memory**  / **Description:**  The amount of dirty pages in RAM that are still being written to the backing storage, in kilobytes. 

- **  `network`  **
  - **Metric:**  `interface`  / **Console name:**  Not applicable  / **Description:** The identifier for the network interface being used for the DB instance.
  - **Metric:**  `rx`  / **Console name:**  **RX**  / **Description:** The number of bytes received per second.
  - **Metric:**  `tx`  / **Console name:**  **TX**  / **Description:** The number of bytes uploaded per second.

- **  `processList`  **
  - **Metric:**  `cpuUsedPc`  / **Console name:**  **CPU %**  / **Description:** The percentage of CPU used by the process.
  - **Metric:**  `id`  / **Console name:**  Not applicable  / **Description:** The identifier of the process.
  - **Metric:**  `memoryUsedPc`  / **Console name:**  **MEM%**  / **Description:** The percentage of memory used by the process.
  - **Metric:**  `name`  / **Console name:**  Not applicable  / **Description:** The name of the process.
  - **Metric:**  `parentID`  / **Console name:**  Not applicable  / **Description:** The process identifier for the parent process of the process.
  - **Metric:**  `rss`  / **Console name:**  **RES**  / **Description:** The amount of RAM allocated to the process, in kilobytes.
  - **Metric:**  `tgid`  / **Console name:**  Not applicable  / **Description:** The thread group identifier, which is a number representing the process ID to which a thread belongs. This identifier is used to group threads from the same process. 
  - **Metric:**  `vss`  / **Console name:**  **VIRT**  / **Description:** The amount of virtual memory allocated to the process, in kilobytes.

- **  `swap`  **
  - **Metric:**  `total`  / **Console name:**  **Swap**  / **Description:** The amount of swap memory available, in kilobytes. 
  - **Metric:**  `in`  / **Console name:**  **Swaps in**  / **Description:** The amount of memory, in kilobytes, swapped in from disk. 
  - **Metric:**  `out`  / **Console name:**  **Swaps out**  / **Description:** The amount of memory, in kilobytes, swapped out to disk. 
  - **Metric:**  `free`  / **Console name:**  **Free Swap**  / **Description:** The amount of swap memory free, in kilobytes. 
  - **Metric:**  `cached`  / **Console name:**  **Committed Swap**  / **Description:** The amount of swap memory, in kilobytes, used as cache memory. 

- **  `tasks`  **
  - **Metric:**  `blocked`  / **Console name:**  **Tasks Blocked**  / **Description:** The number of tasks that are blocked.
  - **Metric:**  `running`  / **Console name:**  **Tasks Running**  / **Description:** The number of tasks that are running.
  - **Metric:**  `sleeping`  / **Console name:**  **Tasks Sleeping**  / **Description:** The number of tasks that are sleeping.
  - **Metric:**  `stopped`  / **Console name:**  **Tasks Stopped**  / **Description:** The number of tasks that are stopped.
  - **Metric:**  `total`  / **Console name:**  **Tasks Total**  / **Description:** The total number of tasks.
  - **Metric:**  `zombie`  / **Console name:**  **Tasks Zombie**  / **Description:** The number of child tasks that are inactive with an active parent task.



## OS metrics for Microsoft SQL Server
<a name="USER_Monitoring-Available-OS-Metrics-RDS.SQLServer"></a>

RDS collects disk metrics for `rdsdbdata` as well as additional storage volumes present in the OS. To view OS metrics in CloudWatch Logs, see [Viewing OS metrics using CloudWatch Logs](USER_Monitoring.OS.CloudWatchLogs.md).

<a name="cloudwatch-sql-server-metrics"></a>

- **  `General`  **
  - **Metric:**  `engine`  / **Console name:**  Not applicable  / **Description:** The database engine for the DB instance.
  - **Metric:**  `instanceID`  / **Console name:**  Not applicable  / **Description:** The DB instance identifier.
  - **Metric:**  `instanceResourceID`  / **Console name:**  Not applicable  / **Description:** An immutable identifier for the DB instance that is unique to an AWS Region, also used as the log stream identifier.
  - **Metric:**  `numVCPUs`  / **Console name:**  Not applicable  / **Description:** The number of virtual CPUs for the DB instance.
  - **Metric:**  `timestamp`  / **Console name:**  Not applicable  / **Description:** The time at which the metrics were taken.
  - **Metric:**  `uptime`  / **Console name:**  Not applicable  / **Description:** The amount of time that the DB instance has been active.
  - **Metric:**  `version`  / **Console name:**  Not applicable  / **Description:** The version of the OS metrics' stream JSON format.

- **  `cpuUtilization`  **
  - **Metric:**  `idle`  / **Console name:**  **CPU Idle**  / **Description:** The percentage of CPU that is idle.
  - **Metric:**  `kern`  / **Console name:**  **CPU Kernel**  / **Description:** The percentage of CPU in use by the kernel.
  - **Metric:**  `user`  / **Console name:**  **CPU User**  / **Description:** The percentage of CPU in use by user programs.

- **  `disks`  **
  - **Metric:**  `name`  / **Console name:**  Not applicable  / **Description:** The identifier for the disk.
  - **Metric:**  `totalKb`  / **Console name:**  **Total Disk Space**  / **Description:** The total space of the disk, in kilobytes.
  - **Metric:**  `usedKb`  / **Console name:**  **Used Disk Space**  / **Description:** The amount of space used on the disk, in kilobytes.
  - **Metric:**  `usedPc`  / **Console name:**  **Used Disk Space %**  / **Description:** The percentage of space used on the disk.
  - **Metric:**  `availKb`  / **Console name:**  **Available Disk Space**  / **Description:** The space available on the disk, in kilobytes.
  - **Metric:**  `availPc`  / **Console name:**  **Available Disk Space %**  / **Description:** The percentage of space available on the disk.
  - **Metric:**  `rdCountPS`  / **Console name:**  **Reads/s**  / **Description:** The number of read operations per second
  - **Metric:**  `rdBytesPS`  / **Console name:**  **Read Kb/s**  / **Description:** The number of bytes read per second.
  - **Metric:**  `wrCountPS`  / **Console name:**  **Write IO/s**  / **Description:** The number of write operations per second.
  - **Metric:**  `wrBytesPS`  / **Console name:**  **Write Kb/s**  / **Description:** The amount of bytes written per second.

- **  `memory`  **
  - **Metric:**  `commitTotKb`  / **Console name:**  **Commit Total**  / **Description:** The amount of pagefile-backed virtual address space in use, that is, the current commit charge. This value is composed of main memory (RAM) and disk (pagefiles). 
  - **Metric:**  `commitLimitKb`  / **Console name:**  **Maximum Commit**  / **Description:** The maximum possible value for the `commitTotKb` metric. This value is the sum of the current pagefile size plus the physical memory available for pageable contents, excluding RAM that is assigned to nonpageable areas. 
  - **Metric:**  `commitPeakKb`  / **Console name:**  **Commit Peak**  / **Description:** The largest value of the `commitTotKb` metric since the operating system was last started. 
  - **Metric:**  `kernTotKb`  / **Console name:**  **Total Kernel Memory**  / **Description:** The sum of the memory in the paged and nonpaged kernel pools, in kilobytes. 
  - **Metric:**  `kernPagedKb`  / **Console name:**  **Paged Kernel Memory**  / **Description:** The amount of memory in the paged kernel pool, in kilobytes. 
  - **Metric:**  `kernNonpagedKb`  / **Console name:**  **Nonpaged Kernel Memory**  / **Description:** The amount of memory in the nonpaged kernel pool, in kilobytes. 
  - **Metric:**  `pageSize`  / **Console name:**  **Page Size**  / **Description:** The size of a page, in bytes. 
  - **Metric:**  `physTotKb`  / **Console name:**  **Total Memory**  / **Description:** The amount of physical memory, in kilobytes. 
  - **Metric:**  `physAvailKb`  / **Console name:**  **Available Memory**  / **Description:** The amount of available physical memory, in kilobytes. 
  - **Metric:**  `sqlServerTotKb`  / **Console name:**  **SQL Server Total Memory**  / **Description:** The amount of memory committed to SQL Server, in kilobytes. 
  - **Metric:**  `sysCacheKb`  / **Console name:**  **System Cache**  / **Description:** The amount of system cache memory, in kilobytes. 

- **  `network`  **
  - **Metric:**  `interface`  / **Console name:**  Not applicable  / **Description:** The identifier for the network interface being used for the DB instance.
  - **Metric:**  `rdBytesPS`  / **Console name:**  **Network Read Kb/s**  / **Description:** The number of bytes received per second.
  - **Metric:**  `wrBytesPS`  / **Console name:**  **Network Write Kb/s**  / **Description:** The number of bytes sent per second.

- **  `processList`  **
  - **Metric:**  `cpuUsedPc`  / **Console name:**  **Used %**  / **Description:** The percentage of CPU used by the process.
  - **Metric:**  `memUsedPc`  / **Console name:**  **MEM%**  / **Description:** The percentage of total memory used by the process.
  - **Metric:**  `name`  / **Console name:**  Not applicable  / **Description:** The name of the process.
  - **Metric:**  `pid`  / **Console name:**  Not applicable  / **Description:** The identifier of the process. This value is not present for processes that are owned by Amazon RDS.
  - **Metric:**  `ppid`  / **Console name:**  Not applicable  / **Description:** The process identifier for the parent of this process. This value is only present for child processes. 
  - **Metric:**  `tid`  / **Console name:**  Not applicable  / **Description:**  The thread identifier. This value is only present for threads. The owning process can be identified by using the `pid` value. 
  - **Metric:**  `workingSetKb`  / **Console name:**  Not applicable  / **Description:**  The amount of memory in the private working set plus the amount of memory that is in use by the process and can be shared with other processes, in kilobytes. 
  - **Metric:**  `workingSetPrivKb`  / **Console name:**  Not applicable  / **Description:** The amount of memory that is in use by a process, but can't be shared with other processes, in kilobytes. 
  - **Metric:**  `workingSetShareableKb`  / **Console name:**  Not applicable  / **Description:** The amount of memory that is in use by a process and can be shared with other processes, in kilobytes. 
  - **Metric:**  `virtKb`  / **Console name:**  Not applicable  / **Description:**  The amount of virtual address space the process is using, in kilobytes. Use of virtual address space doesn't necessarily imply corresponding use of either disk or main memory pages. 

- **  `system`  **
  - **Metric:**  `handles`  / **Console name:**  **Handles**  / **Description:** The number of handles that the system is using.
  - **Metric:**  `processes`  / **Console name:**  **Processes**  / **Description:** The number of processes running on the system.
  - **Metric:**  `threads`  / **Console name:**  **Threads**  / **Description:** The number of threads running on the system.

