# Probe dashboards

You can use a **Probe** dashboard in Network Synthetic Monitor to view the network health indicator (NHI)
for a probe, as well as information about round-trip time and packet loss for specific probes. There are two
dashboards for probes: an **Overview** page and **Probe details** page.

You can create CloudWatch alarms to set packet loss and round-trip time metric thresholds. When a
threshold is reached for a metric, a CloudWatch alarm notifies you. For information on creating probe
alarms, see [Probe alarms](cw-nwm-create-alarm.md "cw-nwm-create-alarm.md").

###### To access a probe dashboard

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/"), and then, under **Network
   Monitoring**, choose **Synthetic monitors**.
2. In the **Monitors** section, choose the
   **Name** link to open the dashboard for a specific monitor.
3. To view the dashboard for a specific probe, choose the **ID** link for the probe.

## Overview page

The **Overview** page displays the following information for a probe:

- **Network health** — Network health displays the network health indicator (NHI)
  value, which pertains only to health of the AWS network. The NHI status is provided as **Healthy** or
  **Degraded**. A **Healthy** status indicates that Network Synthetic Monitor
  did not observe issues with the AWS network for a probe. A **Degraded** status
  indicates that Network Synthetic Monitor observed an issue with the AWS network. The status bar in this
  section shows the status of the network health indicator over a default time of one hour. Hover over any point
  in the status bar to view additional details.
- **Packet loss** — The number of packets that were lost from
  the source subnet to the destination IP address for this probe.
- **Round-trip time** — The time it takes, in milliseconds, for a
  packet from the source subnet to reach the destination IP address, and then come back
  again. Round-trip time (RTT) is the average RTT observed during the aggregation period.

## Probe details

The **Probe details** page displays information about a probe, including the
source and destination. You can also edit the probe, for example, to activate or deactivate it.
For more information, see [Working with monitors and probes in Network Synthetic Monitor](nw-monitor-working-with.md "nw-monitor-working-with.md").

- **Probe details** — This section provides general information about the
  probe, which can't be edited.
- **Probe source and destination** — This section displays
  details about the probe. Choose a **VPC** or **Subnet ID**
  link to open the VPC or subnet details in the Amazon VPC Console. You can modify a probe, for example,
  to activate or deactivate it.
- **Tags** — View the current tags for a monitor. You can add or remove
  tags by choosing **Manage tags**. This opens the **Edit
  probe** page. For more information on editing tags, see [Edit a probe](nw-monitor-probe-edit.md "nw-monitor-probe-edit.md").
