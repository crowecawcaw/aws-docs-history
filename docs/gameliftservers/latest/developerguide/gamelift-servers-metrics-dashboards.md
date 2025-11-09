# Dashboard organization and usage

View your metrics on comprehensive dashboards in [Amazon Managed Grafana](../../../grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.md "../../../grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.md"). The available dashboards depend on your fleet type:

## Dashboard availability by fleet type

The following table shows which dashboards are available for each fleet type:

| Dashboard                | Fleet Type      | Description                                                                                                                              |
| ------------------------ | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| EC2 Fleet Overview       | EC2 Fleet       | Displays information on concurrent players (CCU), instances and player capacity                                                          |
| Instances Overview       | EC2 Fleet       | Displays average CPU, memory, and network utilization across all fleet instances                                                         |
| Instance Performance     | EC2 Fleet       | Displays detailed metrics (CPU, memory, disk, network) for an individual instance                                                        |
| Container Fleet Overview | Container Fleet | Displays average resource utilization of all containers in a managed container fleet                                                     |
| Container Performance    | Container Fleet | Displays detailed metrics of individual containers within a specific ECS task                                                            |
| Server Performance       | Both            | Displays the network, memory and runtime performance of a specified game server process (separate versions for EC2 and Container fleets) |

**Managed EC2 Fleets:**

- EC2 Fleet Overview provides high-level fleet capacity and scaling insights.
- Use Instances Overview and Instance Performance dashboards for host-level monitoring.
- Metrics collected via hostmetrics receiver for system-level visibility.
- Focus on EC2 instance resource utilization and performance.
- Server Performance (EC2) monitors game server application metrics independent of underlying infrastructure.

**Managed Container Fleets:**

- Use Container Fleet Overview and Container Performance dashboards for ECS task and container-level monitoring.
- Metrics collected via ECS Container Receiver for containerized workload visibility.
- Focus on task-level aggregation and container resource isolation.
- Server Performance (Container) monitors game server application metrics independent of underlying infrastructure.

## EC2 Fleet Overview dashboard

This dashboard provides a high-level overview of your fleet's utilization and capacity globally and by location. It features graphs showing counts for game server stops, starts, and crashes, as well as the percentage of healthy game servers. You can filter by FleetID and Location.

### Fleet Overview metrics

The following table shows the metrics available on the Fleet Overview dashboard:

| Dashboard               | Metric name                                                                                                                                 | Definition                                                                                                                  |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Global CCU and Capacity | CCU                                                                                                                                         | Shows the number of concurrent users in all the game servers over all the instances in all locations                        |
| Global CCU              | Shows the number of concurrent users in all the game servers over all the instances globally                                                |
| Active Instances        | Shows the total number of instances in the fleet that are active                                                                            |
| Active Processes        | Shows the number of active game server processes that are ready to host a game session                                                      |
| Game Server Starts      | Shows the number of game sessions that started across the fleet                                                                             |
| Global CCU and Capacity | Healthy Game Servers                                                                                                                        | Shows the average percentage of game servers that report healthy to Amazon GameLift Servers across the fleet                |
| Crashed Game Sessions   | Shows the game session IDs of the crashed game sessions. Click the link of game session ARN to navigate to the Server Performance dashboard |
| Location CCU            | Location Players                                                                                                                            | Shows the number of concurrent players in a location, including all the game servers over all the instances in the location |
| Location Capacity       | Shows capacity utilization (%) in a location, and the percentage of game servers in use in the location                                     |

###### Note

CCU metrics require implementation in your game server code. These metrics are not automatically collected and must be implemented and reported by your application.

## Instances Overview dashboard

This dashboard provides aggregated host-level metrics across all instances in your fleet. Current averages show overall health of the instances. When performance degrades, check CPU usage, memory consumption, network and disk consumption for bottlenecks. You can filter by FleetID and Location.

### Instances Overview metrics

The following table shows the metrics available on the Instances Overview dashboard:

| Dashboard                 | Metric name                                                                                               | Definition                                                                                                                                                                                                                                                      |
| ------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Instance Summary          | Average CPU Usage                                                                                         | Instance summary tracks average resource usage by instances. Average percentage of CPU resources being used across all fleet instances. High utilization patterns require checking individual instance metrics and resource distribution                        |
| Peak CPU Usage            | Highest CPU utilization recorded across any instance in the fleet during the time period                  |
| CPU Usage by Instance     | Individual CPU utilization for each instance in the fleet, enabling identification of resource hotspots   |
| Instance Summary          | Average Memory Usage                                                                                      | Average percentage of RAM being used across all fleet instances. High utilization patterns require checking individual instance metrics and resource distribution like memory consumption                                                                       |
| Peak Memory Usage         | Highest memory utilization recorded across any instance in the fleet during the time period               |
| Memory Usage by Instance  | Individual memory utilization for each instance in the fleet, helping identify memory-intensive workloads |
| Network Summary           | Network I/O (Bytes)                                                                                       | Network summary reflects average instance connectivity. Average network traffic volume (sent and received) across all fleet instances. For latency or connectivity issues, check individual instance metrics like Network I/O and Packet rates                  |
| Network I/O (Packets)     | Average network packet rate (sent and received) across all fleet instances                                |
| Network Usage by Instance | Individual network utilization for each instance, useful for identifying network bottlenecks              |
| Disk Summary              | Disk I/O Operations                                                                                       | Disk summary indicates average disk performance of the instances. Average disk read/write operations across all fleet instances. Slow response times suggest examining Disk operations, I/O wait times, and Pending operations at the individual instance level |
| Disk I/O Throughput       | Average disk read/write throughput across all fleet instances                                             |
| Disk Usage by Instance    | Individual disk utilization for each instance, helping identify storage performance issues                |

###### Note

Instance-level metrics are collected via the hostmetrics receiver and provide system-level visibility into your fleet's infrastructure performance. Use this dashboard to identify overall fleet health trends and drill down to individual instances when performance issues are detected.

## Instance Performance dashboard

This dashboard provides detailed performance metrics for individual instances. Current averages show overall instance health. When performance degrades, check CPU usage, memory consumption, and file system consumption for bottlenecks. It features "Top N Memory Consuming Game Sessions" and "Top N CPU Consuming Game Sessions" tables that help identify which processes contribute the most to instance resource consumption. Clicking on Game Session links enables deeper investigation of detailed metrics. You can filter by specific Instance ID.

### Instance Performance metrics

The following table shows the metrics available on the Instance Performance dashboard:

| Dashboard                         | Metric name                                                                                                                                                                                                                                                                          | Definition                                                                                                                                                                                                                                                                                                              |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Load Summary                      | Top N Memory Consuming Game Sessions                                                                                                                                                                                                                                                 | Load summary tracks resource usage by game servers. Ranked list of game sessions consuming the most memory resources on this instance. High utilization patterns require checking individual session metrics and resource distribution. Clicking on Game Session links enables deeper investigation of detailed metrics |
| Top N CPU Consuming Game Sessions | Ranked list of game sessions consuming the most CPU resources on this instance. High utilization patterns require checking individual session metrics and resource distribution like CPU and memory. Clicking on Game Session links enables deeper investigation of detailed metrics |
| CPU Usage per Game Session        | Individual CPU utilization breakdown showing resource consumption by each active game session                                                                                                                                                                                        |
| Memory Usage per Game Session     | Individual memory utilization breakdown showing resource consumption by each active game session                                                                                                                                                                                     |
| Current Averages                  | Instance CPU Usage                                                                                                                                                                                                                                                                   | Overall CPU utilization for the selected instance over time                                                                                                                                                                                                                                                             |
| Instance Memory Usage             | Overall memory utilization for the selected instance over time                                                                                                                                                                                                                       |
| Instance File System Usage        | File system consumption for the selected instance, useful for identifying storage capacity issues                                                                                                                                                                                    |
| Network                           | Instance Network I/O                                                                                                                                                                                                                                                                 | Network reflects instance connectivity. Network traffic volume and packet rates for the selected instance. For latency or connectivity issues, investigate Network I/O, Packet rates, and Error counts                                                                                                                  |
| Network Connections               | Number of active network connections on the selected instance                                                                                                                                                                                                                        |
| Network Error Counts              | Network error statistics for identifying connectivity problems                                                                                                                                                                                                                       |
| Disk                              | Disk I/O Operations                                                                                                                                                                                                                                                                  | Disk indicates disk performance. Disk read/write activity and utilization for the selected instance. Slow response times suggest examining Disk operations, I/O wait times, and Pending operations                                                                                                                      |
| Disk I/O Wait Times               | Time spent waiting for disk operations to complete                                                                                                                                                                                                                                   |
| Pending Disk Operations           | Number of disk operations waiting to be processed                                                                                                                                                                                                                                    |

###### Note

The Top N Memory and CPU Consuming Game Sessions tables are essential for identifying performance bottlenecks and resource-intensive processes that may impact overall instance performance. These rankings enable quick identification of problematic game sessions for further investigation.

## Container Fleet Overview dashboard

This dashboard provides a high-level overview of your container fleet's resource utilization and capacity. It displays average resource utilization of all containers in a managed container fleet, including CPU reservation, memory utilization, and container group status. You can filter by FleetID and Location.

### Container Fleet Overview metrics

The following table shows the metrics available on the Container Fleet Overview dashboard:

| Dashboard                                | Metric name                                                              | Definition                                                                 |
| ---------------------------------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| Container Group Status                   | Active Game Server Container Groups                                      | Container groups that are currently active and ready to host game sessions |
| Idle Game Server Container Groups        | Container groups that are active but not currently hosting game sessions |
| Pending Game Server Container Groups     | Container groups that are in the process of starting up                  |
| Terminating Game Server Container Groups | Container groups that are in the process of shutting down                |
| Resource Utilization                     | Container CPU Utilization                                                | Average CPU utilization across all containers in the fleet                 |
| Container Memory Utilization             | Average memory utilization across all containers in the fleet            |
| Container CPU Reservation                | Percentage of CPU resources reserved by containers across the fleet      |
| Network Activity                         | Container Network In                                                     | Average network bytes received by containers across the fleet              |
| Container Network Out                    | Average network bytes sent by containers across the fleet                |

###### Note

Container fleet metrics are collected via ECS Container Receiver and provide containerized workload visibility with focus on task-level aggregation and container resource isolation.

## Container Performance dashboard

This dashboard provides detailed performance metrics for individual containers within specific ECS tasks. It displays detailed metrics of individual containers including CPU utilization, memory usage, network I/O, and storage performance. You can filter by specific Container ID or ECS Task.

### Container Performance metrics

The following table shows the metrics available on the Container Performance dashboard:

| Dashboard                        | Metric name                                                          | Definition                                                       |
| -------------------------------- | -------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Resource Performance             | Container CPU Utilization                                            | CPU utilization for the selected container over time             |
| Container Memory Utilization     | Memory utilization for the selected container over time              |
| Container Memory Reservation     | Percentage of memory resources reserved by the selected container    |
| Network Performance              | Container Network I/O                                                | Network traffic volume (bytes in/out) for the selected container |
| Network Connections              | Number of active network connections for the selected container      |
| Storage Performance              | Container Storage Read/Write                                         | Storage read and write activity for the selected container       |
| Container Storage I/O Operations | Number of storage I/O operations performed by the selected container |

###### Note

Container performance metrics provide detailed visibility into individual container resource consumption and performance characteristics within ECS tasks.

## Server Performance dashboard

The Server Performance dashboard shows metrics related to server timings, network activity, memory, and CPU usage for individual game sessions. You can filter by Game Session ID and export metrics directly to Amazon CloudWatch or [Amazon Managed Grafana](../../../grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.md "../../../grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.md").

### Server Performance metrics

The following table shows the metrics available on the Server Performance dashboard:

| Dashboard                 | Metric name                                                                           | Definition                                                                                                                                   |
| ------------------------- | ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Server Timings            | Server Delta Time                                                                     | Difference in time between the current server tick and the previous server tick. It's a measure of the consistency of the server's tick rate |
| Server Tick Rate          | Shows the number of times per second the server is processing updates                 |
| Server Tick Time          | The amount of time it takes for the server to process a single tick or update         |
| Server World Tick Time    | The amount of time it takes for the server to update the game world with each tick    |
| Network                   | Connections                                                                           | The total number of network connections the server has established                                                                           |
| Network I/O (Bytes)       | The total number of bytes being sent and received by the server over the network      |
| Network I/O (Packets)     | The total number of network packets being sent and received by the server             |
| Packet Loss               | The percentage of network packets that are being lost during transmission             |
| Memory                    | Memory Usage (Units)                                                                  | The total amount of memory being consumed by the server processes                                                                            |
| Physical Memory Usage (%) | The percentage of the server's total physical memory that is currently being utilized |
| CPU Usage                 | CPU Usage (%)                                                                         | The percentage of CPU resources being utilized by the game server process                                                                    |
