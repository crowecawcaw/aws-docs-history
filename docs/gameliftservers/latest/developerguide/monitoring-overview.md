# Monitoring Amazon GameLift Servers

If you're using Amazon GameLift Servers FleetIQ as a standalone feature with Amazon EC2, see [Security in Amazon EC2](../../../AWSEC2/latest/UserGuide/ec2-security.md "../../../AWSEC2/latest/UserGuide/ec2-security.md") in the
_Amazon EC2 User Guide_.

Monitoring is an important part of maintaining the reliability,
availability, and performance of Amazon GameLift Servers and your other AWS solutions. There are three
primary uses for metrics with Amazon GameLift Servers: to monitor system health and set up alarms, to
track game server performance and usage, and to manage capacity using manual or
auto-scaling.

AWS provides the following monitoring tools to watch Amazon GameLift Servers, report when something is
wrong, and take automatic actions when appropriate:

- **Amazon GameLift Servers console** – Use the graphical
  interface to manage your Amazon GameLift Servers resources and track game hosting activity.
- **Amazon CloudWatch** – You can monitor Amazon GameLift Servers
  metrics in real time, as well as metrics for other AWS resources and applications
  that you're running on AWS services. CloudWatch offers a suite of monitoring
  features, including tools to create customized dashboards and the ability to set
  alarms that notify or take action when a metric reaches a specified
  threshold.
- **AWS CloudTrail** – captures all API calls and
  related events made by or on behalf of your AWS account for Amazon GameLift Servers and other
  AWS services. Data is delivered as log files to an Amazon S3 bucket that you specify.
  You can identify which users and accounts called AWS, the source IP address from
  which the calls were made, and when the calls occurred.
- **Game session logs** – You can output custom
  server messages for your game sessions to log files that are stored in Amazon S3.

## Metrics comparison across monitoring sources

Amazon GameLift Servers provides metrics through three primary sources: the Amazon GameLift Servers console Fleet Activity metrics, the Amazon GameLift Servers Servers Metrics Plugin for Unreal, and Amazon CloudWatch Amazon GameLift Servers metrics. Understanding the overlap and unique capabilities of each source helps you choose the right monitoring approach for your needs.

### Metrics availability by source

The following sections describe which metrics are available across the different monitoring sources, highlighting overlaps and unique capabilities.

#### Metrics available in all sources

The following metric is consistently available across the console, plugin, and CloudWatch:

- `Active Instances`/`ActiveInstances` – The number of instances with ACTIVE status that are running active server processes

#### Metrics available in Console and CloudWatch

The following metrics are available in both the Amazon GameLift Servers console and Amazon CloudWatch, providing consistent fleet management and capacity monitoring:

- `Idle instances`/`IdleInstances` – Active instances currently hosting zero game sessions
- `Percent idle instances`/`PercentIdleInstances` – Percentage of active instances that are idle
- `Desired instances`/`DesiredInstances` – Target number of active instances that Amazon GameLift Servers maintains
- `Max instances`/`MaxInstances` – Maximum number of instances allowed for the fleet
- `Min instances`/`MinInstances` – Minimum number of instances allowed for the fleet
- `Instance interruptions`/`InstanceSpotInterruptions` – Number of spot instances that have been interrupted
- `Recycled instances`/`RecycledSpotInstances` – Number of spot instances that have been recycled and replaced
- `Game session interruptions`/`GameSessionSpotInterruptions` – Game sessions that were interrupted due to spot instance interruption
- `Unhealthy instances replaced`/`UnhealthyInstancesReplaced` – Instances that were replaced due to health issues
- `Activating game sessions` – Game sessions currently in the process of starting
- `Active game sessions` – Game sessions currently running and hosting players
- `Available game sessions` – Game sessions that can accept additional players
- `Concurrent activatable game sessions` – Game sessions that can be activated simultaneously
- `Percent available game sessions` – Percentage of game sessions available for new players

#### Metrics unique to CloudWatch

Amazon CloudWatch provides specific operational metrics:

- `Unhealthy instances replaced` – Instances that were replaced due to health issues

#### Metrics unique to Container Fleets

Container fleets provide additional metrics specific to containerized game servers:

##### Container group metrics

- `ActiveGameServerContainerGroups` – Number of active game server container groups
- `IdleGameServerContainerGroups` – Number of idle game server container groups
- `PendingGameServerContainerGroups` – Number of pending game server container groups
- `TerminatingGameServerContainerGroups` – Number of terminating game server container groups
- `UnhealthyGameServerContainerGroupsReplaced` – Number of unhealthy container groups that were replaced

##### Container performance metrics

- `ContainerCPUUtilizationPerInstance` – CPU utilization per container instance
- `ContainerCPUReservation` – Reserved CPU capacity for containers
- `ContainerMemoryReservation` – Reserved memory capacity for containers
- `ContainerMemoryUtilization` – Memory utilization by containers
- `ContainerNetworkIn` – Incoming network traffic for containers
- `ContainerNetworkOut` – Outgoing network traffic for containers
- `ContainerStorageReadBytes` – Storage read bytes for containers
- `ContainerStorageWriteBytes` – Storage write bytes for containers

##### Renamed instance metrics

- `InstanceCPUUtilization` – Instance-level CPU utilization (renamed from CPUUtilization)
- `InstanceNetworkIn` – Instance-level incoming network traffic (renamed from NetworkIn)
- `InstanceNetworkOut` – Instance-level outgoing network traffic (renamed from NetworkOut)
- `InstanceStorageReadBytes` – Instance-level storage read bytes (renamed from DiskReadBytes)
- `InstanceStorageWriteBytes` – Instance-level storage write bytes (renamed from DiskWriteBytes)
- `InstanceStorageReadOps` – Instance-level storage read operations (renamed from DiskReadOps)
- `InstanceStorageWriteOps` – Instance-level storage write operations (renamed from DiskWriteOps)

### Choosing the right monitoring source

Select your monitoring approach based on your specific needs:

- **Use the Amazon GameLift Servers console** for fleet management, capacity planning, and general operational oversight. The console provides an integrated view of fleet health and player activity. For more information, see [Track game hosting in the Amazon GameLift Servers console](gamelift-console-intro.md "gamelift-console-intro.md").
- **Use Amazon CloudWatch** for automated monitoring, alerting, and integration with other AWS services. CloudWatch enables custom dashboards and alarm-based automation. For more information, see [Monitor Amazon GameLift Servers with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
- **Use multiple sources** for comprehensive monitoring. Combine console oversight, plugin technical details, and CloudWatch automation for complete visibility into your game hosting infrastructure.

For additional monitoring capabilities, you can also use:

- [Logging Amazon GameLift Servers API calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md") – Track API calls and related events for auditing and compliance.
- [Logging server messages in Amazon GameLift Servers](logging-server-messages.md "logging-server-messages.md") – Capture custom server messages and game session logs.

## Topics

- [Track game hosting in the Amazon GameLift Servers console](gamelift-console-intro.md "gamelift-console-intro.md")
- [Monitor Amazon GameLift Servers with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md")
- [Logging Amazon GameLift Servers API calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
- [Logging server messages in Amazon GameLift Servers](logging-server-messages.md "logging-server-messages.md")
