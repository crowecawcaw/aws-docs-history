

# Available metrics
<a name="gamelift-servers-metrics-types"></a>

Metrics fall into three categories:
+ Automatically collected metrics
+ SDK-provided metrics
+ Custom metrics

## Automatic metrics collection
<a name="metrics-automatic-collection"></a>

No code changes required for these metrics:

### Instance metrics
<a name="metrics-instance-level"></a>


| Metric Type | Description | Use Case | 
| --- | --- | --- | 
| CPU | Percentage utilization per instance | Resource monitoring | 
| Memory | Physical memory usage and percentage | Capacity planning | 
| Network I/O | Bytes and packets sent/received | Connection health | 
| Disk I/O | Read/write operations and throughput | Storage performance | 

### Fleet metrics
<a name="metrics-fleet-level"></a>


| Metric Type | Description | Use Case | 
| --- | --- | --- | 
| Active Instances | Running instances count | Fleet scaling | 
| Game Sessions | Active and available sessions | Capacity management | 
| Crashed game sessions | Game sessions that have crashed | Error monitoring | 

## SDK-provided metrics
<a name="metrics-sdk-functions"></a>

Requires SDK function calls in your code:

### Server timing metrics
<a name="metrics-server-timings"></a>


| Metric | Description | Implementation | 
| --- | --- | --- | 
| Server Delta Time | Difference in time between the current server tick and the previous server tick. Measures the consistency of the server's tick rate | Call GetDeltaTime() | 
| Server Tick Rate | Shows the number of times per second the server is processing updates | Automatically calculated | 
| Server Tick Time | The amount of time it takes for the server to process a single tick or update | Call GetTickTime() | 
| Server World Tick Time | The amount of time it takes for the server to update the game world with each tick | Call GetWorldUpdateTime() | 

**Implementation:** For engine-agnostic SDKs (C\+\+, C\#, Go), you implement these metrics by calling SDK functions from your game loop with calculated timing values. For engine plugins (Unreal, Unity), these metrics are captured automatically through engine integration.

### Network metrics
<a name="metrics-networking"></a>


| Metric | Description | Implementation | 
| --- | --- | --- | 
| Connections | The total number of network connections the server has established | Automatic after InitMetrics() | 
| Network I/O (Bytes) | The total number of bytes being sent and received by the server over the network | Automatic after InitMetrics() | 
| Network I/O (Packets) | The total number of network packets being sent and received by the server | Automatic after InitMetrics() | 
| Packet Loss | The percentage of network packets that are being lost during transmission | Automatic after InitMetrics() | 

**Implementation:** Integrate SDK function calls with your networking library. The SDK provides guidance for different network implementations.

### Process metrics
<a name="metrics-process-level"></a>


| Metric | Description | Implementation | 
| --- | --- | --- | 
| CPU Usage (%) | The percentage of CPU resources being utilized by the game server process | Automatic after InitMetrics() | 
| Memory Usage (Units) | The total amount of memory being consumed by the server processes | Automatic after InitMetrics() | 
| Physical Memory Usage (%) | The percentage of the server's total physical memory that is currently being utilized | Automatic after InitMetrics() | 
| Server Status | Game server health state | Automatic after InitMetrics() | 

**Implementation:** These metrics are automatically collected by the SDK for each game session process.

#### Per-process dashboard organization
<a name="process-metrics-dashboards"></a>

Per-process metrics are available in two specialized dashboards:
+ **Server Performance dashboard** — Contains server timings (delta time, tick rate, tick time, world tick time), network metrics (connections, I/O bytes/packets, packet loss), memory usage, and CPU usage for individual game sessions.
+ **Instance Performance dashboard** — Features "Top N Memory Consuming Game Sessions" and "Top N CPU Consuming Game Sessions" tables that help identify which processes contribute most to instance resource consumption. Clicking on Game Session links enables deeper investigation of detailed metrics.

#### Per-process metrics use cases
<a name="process-metrics-use-cases"></a>

The per-process/per-game-session metrics support the following monitoring scenarios:
+ **Dive deep performance investigation** — When a host/instance has degraded performance due to specific processes or game sessions, per-process metrics help identify which process caused the issue through Top CPU and Memory consuming Game Sessions tables.
+ **Game server crash investigation** — When a game session crashes, these metrics help determine if the crash was due to out of memory, CPU overload, or network bandwidth problems.
+ **Investigate player reported issues** — When players report lag or interruptions during gameplay, per-process metrics help identify bottlenecks in CPU, memory, network, tick time, or world update time.
+ **Identify performance changes in different builds** — Tick time, tick rate, and world update time metrics allow developers to measure how game performance changes across different server builds.
+ **Detect delays and slowness in gameplay** — Tick time, tick rate, and world update time metrics reflect how fast the server updates the game, directly impacting customer experience.
+ **Benchmarking** — Identify how different game scenarios affect server performance based on factors like player count, game mode, and other variables.

## Dashboard organization
<a name="metrics-dashboard-usage"></a>

Metrics are organized into specialized dashboards in [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.html) for different monitoring scenarios. The available dashboards depend on your fleet type:

### EC2 Fleet dashboards
<a name="ec2-fleet-dashboards"></a>
+ **EC2 Fleet Overview dashboard** — High-level fleet capacity, scaling insights, concurrent players (CCU), instances, player capacity, and crashed game sessions.
+ **Instances Overview dashboard** — Aggregated host-level metrics across all instances including average CPU, memory, network, and disk utilization.
+ **Instance Performance dashboard** — Detailed metrics for individual instances with "Top N Memory Consuming Game Sessions" and "Top N CPU Consuming Game Sessions" tables for identifying resource-intensive processes.
+ **Server Performance dashboard (EC2)** — Game loop timing, network performance, memory, and CPU metrics for individual game sessions on EC2 instances.

### Container Fleet dashboards
<a name="container-fleet-dashboards"></a>
+ **Container Fleet Overview dashboard** — High-level overview of container fleet resource utilization including CPU reservation, memory utilization, and container group status.
+ **Container Performance dashboard** — Detailed metrics for individual containers within specific ECS tasks including CPU utilization, memory usage, network I/O, and storage performance.
+ **Server Performance dashboard (Container)** — Game loop timing, network performance, memory, and CPU metrics for individual game sessions in containers.

For detailed dashboard information and usage instructions, see [Dashboard organization and usage](gamelift-servers-metrics-dashboards.md).