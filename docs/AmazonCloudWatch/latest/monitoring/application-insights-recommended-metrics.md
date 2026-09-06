

# Recommended metrics
<a name="application-insights-recommended-metrics"></a>

The following table lists the recommended metrics for each component type.



- ** EC2 instance (Windows servers) **
  - **Workload type:** Default/Custom / **Recommended metric:** CPUUtilization<br />StatusCheckFailed<br />Processor % Processor Time<br />Memory % Committed Bytes In Use<br />LogicalDisk % Free Space<br />Memory Available Mbytes
  - **Workload type:** Active Directory / **Recommended metric:** CPUUtilization<br />StatusCheckFailed<br />Processor % Processor Time<br />Memory % Committed Bytes In Use<br />Memory Available MbytesDatabase ==> Instances Database Cache % Hit<br />DirectoryServices DRA Pending Replication Operations<br />DirectoryServices DRA Pending Replication Synchronizations<br />DNS Recursive Query Failure/sec<br />LogicalDisk Avg. Disk Queue Length
  - **Workload type:** Java Application / **Recommended metric:** CPUUtilization<br />StatusCheckFailed<br />Processor % Processor Time<br />Memory % Committed Bytes In Use<br />Memory Available Mbytes<br />java\_lang\_threading\_threadcount<br />java\_lang\_classloading\_loadedclasscount<br />java\_lang\_memory\_heapmemoryusage\_used<br />java\_lang\_memory\_heapmemoryusage\_committed<br />java\_lang\_operatingsystem\_freephysicalmemorysize<br />java\_lang\_operatingsystem\_freeswapspacesize
  - **Workload type:**  Microsoft IIS/.NET Web Front-End / **Recommended metric:** CPUUtilization<br />StatusCheckFailed<br />Processor % Processor Time<br />Memory % Committed Bytes In Use<br />Memory Available Mbytes<br />.NET CLR Exceptions \# of Exceps Thrown/Sec<br />.NET CLR Memory \# Total Committed Bytes<br />.NET CLR Memory % Time in GC<br />ASP.NET Applications Requests in Application Queue<br />ASP.NET Requests Queued<br />ASP.NET Application Restarts
  - **Workload type:** Microsoft SQL Server Database Tier / **Recommended metric:** CPUUtilization<br />StatusCheckFailed<br />Processor % Processor Time<br />Memory % Committed Bytes In Use<br />Memory Available Mbytes<br />Paging File % Usage<br />System Processor Queue Length<br />Network Interface Bytes Total/Sec<br />PhysicalDisk % Disk Time<br />SQLServer:Buffer Manager Buffer Cache Hit ratio<br />SQLServer:Buffer Manager Page Life Expectancy<br />SQLServer:General Statistics Processes Blocked<br />SQLServer:General Statistics User Connections<br />SQLServer:Locks Number of Deadlocks/Sec<br />SQLServer:SQL Statistics Batch Requests/Sec
  - **Workload type:** MySQL / **Recommended metric:** CPUUtilization<br />StatusCheckFailed<br />Processor % Processor Time<br />Memory % Committed Bytes In Use<br />LogicalDisk % Free Space<br />Memory Available Mbytes
  - **Workload type:** .NET workerpool/Mid-Tier / **Recommended metric:** CPUUtilization<br />StatusCheckFailed<br />Processor % Processor Time<br />Memory % Committed Bytes In Use<br />Memory Available Mbytes<br />.NET CLR Exceptions \# of Exceps Thrown/Sec<br />.NET CLR Memory \# Total Committed Bytes<br />.NET CLR Memory % Time in GC
  - **Workload type:** .NET Core Tier / **Recommended metric:** CPUUtilization<br />StatusCheckFailed<br />Processor % Processor Time<br />Memory % Committed Bytes In Use<br />Memory Available Mbytes
  - **Workload type:** Oracle / **Recommended metric:** CPUUtilization<br />StatusCheckFailed<br />Processor % Processor Time<br />Memory % Committed Bytes In Use<br />LogicalDisk % Free Space<br />Memory Available Mbytes
  - **Workload type:** Postgres / **Recommended metric:** CPUUtilization<br />StatusCheckFailed<br />Processor % Processor Time<br />Memory % Committed Bytes In Use<br />LogicalDisk % Free Space<br />Memory Available Mbytes
  - **Workload type:** SharePoint / **Recommended metric:** CPUUtilization<br />StatusCheckFailed<br />Processor % Processor Time<br />Memory % Committed Bytes In Use<br />Memory Available Mbytes<br />ASP.NET Applications Cache API trims<br />ASP.NET Requests Rejected<br />ASP.NET Worker Process Restarts<br />Memory Pages/sec<br />SharePoint Publishing Cache Publishing cache flushes / second<br />SharePoint Foundation Executing Time/Page Request<br />SharePoint Disk-Based Cache Total number of cache compactions<br />SharePoint Disk-Based Cache Blob cache hit ratio <br />SharePoint Disk-Based Cache Blob Cache fill ratio <br />SharePoint Disk-Based Cache Blob cache flushes / second <br />ASP.NET Requests Queued<br />ASP.NET Applications Requests in Application Queue<br />ASP.NET Application Restarts<br />LogicalDisk Avg. Disk sec/Write <br />LogicalDisk Avg. Disk sec/Read <br />Processor % Interrupt Time 

- ** EC2 instance (Linux servers) **
  - **Workload type:** Default/Custom / **Recommended metric:** CPUUtilization<br />StatusCheckFailed<br />disk\_used\_percent<br />mem\_used\_percent
  - **Workload type:**  Java Application / **Recommended metric:** CPUUtilization<br />StatusCheckFailed<br />disk\_used\_percent<br />mem\_used\_percent<br />java\_lang\_threading\_threadcount<br />java\_lang\_classloading\_loadedclasscount<br />java\_lang\_memory\_heapmemoryusage\_used<br />java\_lang\_memory\_heapmemoryusage\_committed<br />java\_lang\_operatingsystem\_freephysicalmemorysize<br />java\_lang\_operatingsystem\_freeswapspacesize
  - **Workload type:** .NET Core Tier or SQL Server Database Tier / **Recommended metric:** CPUUtilization<br />StatusCheckFailed<br />disk\_used\_percent<br />mem\_used\_percent
  - **Workload type:** Oracle / **Recommended metric:** CPUUtilization<br />StatusCheckFailed<br />disk\_used\_percent<br />mem\_used\_percent
  - **Workload type:** Postgres / **Recommended metric:** CPUUtilization<br />StatusCheckFailed<br />disk\_used\_percent<br />mem\_used\_percent

- **EC2 instance group**
  - **Workload type:** SAP HANA multi-node or single node
  - **Recommended metric:**  +  hanadb\_server\_startup\_time\_variations\_seconds  <br />+  hanadb\_level\_5\_alerts\_count  <br />+  hanadb\_level\_4\_alerts\_count  <br />+  hanadb\_out\_of\_memory\_events\_count <br />+  hanadb\_max\_trigger\_read\_ratio\_percent <br />+  hanadb\_max\_trigger\_write\_ratio\_percent  <br />+  hanadb\_log\_switch\_race\_ratio\_percent <br />+  hanadb\_time\_since\_last\_savepoint\_seconds <br />+  hanadb\_disk\_usage\_highlevel\_percent <br />+  hanadb\_current\_allocation\_limit\_used\_percent <br />+  hanadb\_table\_allocation\_limit\_used\_percent <br />+  hanadb\_cpu\_usage\_percent <br />+  hanadb\_plan\_cache\_hit\_ratio\_percent <br />+  hanadb\_last\_data\_backup\_age\_days  

- **EBS volume**
  - **Workload type:** Any
  - **Recommended metric:** VolumeReadBytes<br />VolumeWriteBytes<br />VolumeReadOps<br />VolumeWriteOps<br />VolumeQueueLength<br />VolumeThroughputPercentage<br />VolumeConsumedReadWriteOps<br />BurstBalance

- ** Classic ELB **
  - **Workload type:** Any
  - **Recommended metric:** HTTPCode\_Backend\_4XX<br />HTTPCode\_Backend\_5XX<br />Latency<br />SurgeQueueLength<br />UnHealthyHostCount

- ** Application ELB **
  - **Workload type:** Any
  - **Recommended metric:** HTTPCode\_Target\_4XX\_Count<br />HTTPCode\_Target\_5XX\_Count<br />TargetResponseTime<br />UnHealthyHostCount

- ** RDS Database instance **
  - **Workload type:** Any
  - **Recommended metric:** CPUUtilization<br />ReadLatency<br />WriteLatency<br />BurstBalance<br />FailedSQLServerAgentJobsCount

- **RDS Database cluster**
  - **Workload type:** Any
  - **Recommended metric:** CPUUtilization<br />CommitLatency<br />DatabaseConnections<br />Deadlocks<br />FreeableMemory<br />NetworkThroughput<br />VolumeBytesUsed

- ** Lambda Function **
  - **Workload type:** Any
  - **Recommended metric:** Duration<br />Errors<br />IteratorAge<br />ProvisionedConcurrencySpilloverInvocations<br />Throttles

- ** SQS Queue **
  - **Workload type:** Any
  - **Recommended metric:** ApproximateAgeOfOldestMessage<br />ApproximateNumberOfMessagesVisible<br />NumberOfMessagesSent

- **Amazon DynamoDB table**
  - **Workload type:** Any
  - **Recommended metric:** SystemErrors<br />UserErrors<br />ConsumedReadCapacityUnits<br />ConsumedWriteCapacityUnits<br />ReadThrottleEvents<br />WriteThrottleEvents<br />ConditionalCheckFailedRequests<br />TransactionConflict

- ** Amazon S3 bucket **
  - **Workload type:** Any
  - **Recommended metric:** If replication configuration with Replication Time Control (RTC) is enabled:<br />ReplicationLatency<br />BytesPendingReplication<br />OperationsPendingReplication<br />If request metrics are turned on:<br />5xxErrors<br />4xxErrors<br />BytesDownloaded<br />BytesUploaded

- **AWS Step Functions**
  - **Workload type:** Any
  - **Recommended metric:**  +  ExecutionThrottled <br />+  ExecutionsAborted <br />+  ProvisionedBucketSize <br />+  ProvisionedRefillRate <br />+  ConsumedCapacity  +  ExecutionsFailed <br />+  ExecutionsTimedOut  +  LambdaFunctionsFailed <br />+  LambdaFunctionsTimedOut  +  ActivitiesFailed <br />+  ActivitiesTimedOut <br />+  ActivitiesHeartbeatTimedOut  +  ServiceIntegrationsFailed <br />+  ServiceIntegrationsTimedOut  

- **API Gateway REST API stage**
  - **Workload type:** Any
  - **Recommended metric:**  +  4XXErrors <br />+  5XXErrors <br />+  Latency  

- ** ECS Cluster **
  - **Workload type:**  Any / **Recommended metric:** CpuUtilized<br />MemoryUtilized<br />NetworkRxBytes<br />NetworkTxBytes<br />RunningTaskCount<br />PendingTaskCount<br />StorageReadBytes<br />StorageWriteBytes<br />CPUReservation (EC2 Launch Type only)<br />CPUUtilization (EC2 Launch Type only)<br />MemoryReservation (EC2 Launch Type only)<br />MemoryUtilization (EC2 Launch Type only)<br />GPUReservation (EC2 Launch Type only)<br />instance\_cpu\_utilization (EC2 Launch Type only)<br />instance\_filesystem\_utilization (EC2 Launch Type only)<br />instance\_memory\_utilization (EC2 Launch Type only)<br />instance\_network\_total\_bytes (EC2 Launch Type only)
  - **Workload type:** Java Application / **Recommended metric:** CpuUtilized<br />MemoryUtilized<br />NetworkRxBytes<br />NetworkTxBytes<br />RunningTaskCount<br />PendingTaskCount<br />StorageReadBytes<br />StorageWriteBytes<br />CPUReservation (EC2 Launch Type only)<br />CPUUtilization (EC2 Launch Type only)<br />MemoryReservation (EC2 Launch Type only)<br />MemoryUtilization (EC2 Launch Type only)<br />GPUReservation (EC2 Launch Type only)<br />instance\_cpu\_utilization (EC2 Launch Type only)<br />instance\_filesystem\_utilization (EC2 Launch Type only)<br />instance\_memory\_utilization (EC2 Launch Type only)<br />instance\_network\_total\_bytes (EC2 Launch Type only)<br />java\_lang\_threading\_threadcount<br />java\_lang\_classloading\_loadedclasscount<br />java\_lang\_memory\_heapmemoryusage\_used<br />java\_lang\_memory\_heapmemoryusage\_committed<br />java\_lang\_operatingsystem\_freephysicalmemorysize<br />java\_lang\_operatingsystem\_freeswapspacesize

- ** ECS Service **
  - **Workload type:**  Any / **Recommended metric:** CPUUtilization<br />MemoryUtilization<br />CpuUtilized<br />MemoryUtilized<br />NetworkRxBytes<br />NetworkTxBytes<br />RunningTaskCount<br />PendingTaskCount<br />StorageReadBytes<br />StorageWriteBytes
  - **Workload type:** Java Application / **Recommended metric:** CPUUtilization<br />MemoryUtilization<br />CpuUtilized<br />MemoryUtilized<br />NetworkRxBytes<br />NetworkTxBytes<br />RunningTaskCount<br />PendingTaskCount<br />StorageReadBytes<br />StorageWriteBytes<br />java\_lang\_threading\_threadcount<br />java\_lang\_classloading\_loadedclasscount<br />java\_lang\_memory\_heapmemoryusage\_used<br />java\_lang\_memory\_heapmemoryusage\_committed<br />java\_lang\_operatingsystem\_freephysicalmemorysize<br />java\_lang\_operatingsystem\_freeswapspacesize

- ** EKS Cluster **
  - **Workload type:**  Any / **Recommended metric:** cluster\_failed\_node\_count<br />node\_cpu\_reserved\_capacity<br />node\_cpu\_utilization<br />node\_filesystem\_utilization<br />node\_memory\_reserved\_capacity<br />node\_memory\_utilization<br />node\_network\_total\_bytes<br />pod\_cpu\_reserved\_capacity<br />pod\_cpu\_utilization<br />pod\_cpu\_utilization\_over\_pod\_limit<br />pod\_memory\_reserved\_capacity<br />pod\_memory\_utilization<br />pod\_memory\_utilization\_over\_pod\_limit<br />pod\_network\_rx\_bytes<br />pod\_network\_tx\_bytes
  - **Workload type:** Java Application / **Recommended metric:** cluster\_failed\_node\_count<br />node\_cpu\_reserved\_capacity<br />node\_cpu\_utilization<br />node\_filesystem\_utilization<br />node\_memory\_reserved\_capacity<br />node\_memory\_utilization<br />node\_network\_total\_bytes<br />pod\_cpu\_reserved\_capacity<br />pod\_cpu\_utilization<br />pod\_cpu\_utilization\_over\_pod\_limit<br />pod\_memory\_reserved\_capacity<br />pod\_memory\_utilization<br />pod\_memory\_utilization\_over\_pod\_limit<br />pod\_network\_rx\_bytes<br />pod\_network\_tx\_bytes<br />java\_lang\_threading\_threadcount<br />java\_lang\_classloading\_loadedclasscount<br />java\_lang\_memory\_heapmemoryusage\_used<br />java\_lang\_memory\_heapmemoryusage\_committed<br />java\_lang\_operatingsystem\_freephysicalmemorysize<br />java\_lang\_operatingsystem\_freeswapspacesize

- ** Kubernetes Cluster on EC2 **
  - **Workload type:**  Any / **Recommended metric:** cluster\_failed\_node\_count<br />node\_cpu\_reserved\_capacity<br />node\_cpu\_utilization<br />node\_filesystem\_utilization<br />node\_memory\_reserved\_capacity<br />node\_memory\_utilization<br />node\_network\_total\_bytes<br />pod\_cpu\_reserved\_capacity<br />pod\_cpu\_utilization<br />pod\_cpu\_utilization\_over\_pod\_limit<br />pod\_memory\_reserved\_capacity<br />pod\_memory\_utilization<br />pod\_memory\_utilization\_over\_pod\_limit<br />pod\_network\_rx\_bytes<br />pod\_network\_tx\_bytes
  - **Workload type:** Java Application / **Recommended metric:** cluster\_failed\_node\_count<br />node\_cpu\_reserved\_capacity<br />node\_cpu\_utilization<br />node\_filesystem\_utilization<br />node\_memory\_reserved\_capacity<br />node\_memory\_utilization<br />node\_network\_total\_bytes<br />pod\_cpu\_reserved\_capacity<br />pod\_cpu\_utilization<br />pod\_cpu\_utilization\_over\_pod\_limit<br />pod\_memory\_reserved\_capacity<br />pod\_memory\_utilization<br />pod\_memory\_utilization\_over\_pod\_limit<br />pod\_network\_rx\_bytes<br />pod\_network\_tx\_bytes<br />java\_lang\_threading\_threadcount<br />java\_lang\_classloading\_loadedclasscount<br />java\_lang\_memory\_heapmemoryusage\_used<br />java\_lang\_memory\_heapmemoryusage\_committed<br />java\_lang\_operatingsystem\_freephysicalmemorysize<br />java\_lang\_operatingsystem\_freeswapspacesize



The following table lists the recommended processes and process metrics for each component type. CloudWatch Application Insights does not recommend process monitoring for processes that do not run on an instance.



- ** EC2 instance (Windows servers) **
  - **Workload type:** Microsoft IIS/.NET Web Front-End / **Recommended process:** `w3wp` / **Recommended metric:** `procstat cpu_usage`,<br />`procstat memory_rss`,<br />`procstat memory_vms`,<br />`procstat read_bytes`,<br />`procstat write_bytes`
  - **Workload type:** Microsoft SQL Server Database Tier / **Recommended process:** `SQLAgent` / **Recommended metric:** `procstat cpu_usage`,<br />`procstat memory_rss`,<br />`procstat memory_vms`,<br />`procstat read_bytes`,<br />`procstat write_bytes`
  - **Recommended process:** `sqlservr` / **Recommended metric:** `procstat cpu_usage`,<br />`procstat memory_rss`,<br />`procstat memory_vms`,<br />`procstat read_bytes`,<br />`procstat write_bytes`
  - **Recommended process:** `sqlwriter` / **Recommended metric:** `procstat cpu_usage`,<br />`procstat memory_rss`
  - **Recommended process:** `ReportingServicesService` / **Recommended metric:** `procstat cpu_usage`,<br />`procstat memory_rss`
  - **Recommended process:** `MsDtsServr` / **Recommended metric:** `procstat cpu_usage`,<br />`procstat memory_rss`,<br />`procstat memory_vms`,<br />`procstat read_bytes`,<br />`procstat write_bytes`
  - **Recommended process:** `Msmdsrv` / **Recommended metric:** `procstat cpu_usage`,<br />`procstat memory_rss`,<br />`procstat memory_vms`,<br />`procstat read_bytes`,<br />`procstat write_bytes`
  - **Workload type:** .NET workerpool/Mid-Tier / **Recommended process:** `w3wp` / **Recommended metric:** `procstat cpu_usage`,<br />`procstat memory_rss`,<br />`procstat memory_vms`,<br />`procstat read_bytes`,<br />`procstat write_bytes`
  - **Workload type:** .NET Core Tier / **Recommended process:** `w3wp` / **Recommended metric:** `procstat cpu_usage`,<br />`procstat memory_rss`,<br />`procstat memory_vms`,<br />`procstat read_bytes`,<br />`procstat write_bytes`

