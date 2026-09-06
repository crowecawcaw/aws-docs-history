

# OS metrics in Enhanced Monitoring
<a name="USER_Monitoring-Available-OS-Metrics"></a>

Amazon Aurora provides metrics in real time for the operating system (OS) that your DB cluster runs on. Aurora delivers the metrics from Enhanced Monitoring to your Amazon CloudWatch Logs account. The following tables list the OS metrics available using Amazon CloudWatch Logs.



**Topics**
+ [OS metrics for Aurora](#USER_Monitoring-Available-OS-Metrics-RDS)

## OS metrics for Aurora
<a name="USER_Monitoring-Available-OS-Metrics-RDS"></a>

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

- **`mountPoint`**
  - **Metric:** Not applicable
  - **Console name:** The path to the file system.

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

