# Collect network performance metrics

EC2 instances running on Linux that use the Elastic Network Adapter (ENA) publish
network performance metrics. Version 1.246396.0 and later of the CloudWatch agent enable you to
import these network performance metrics into CloudWatch. When you import these network
performance metrics into CloudWatch, they are charged as CloudWatch custom metrics.

For more information about the ENA driver, see [Enabling enhanced networking
with the Elastic Network Adapter (ENA) on Linux instances](../../../AWSEC2/latest/UserGuide/enhanced-networking-ena.md "../../../AWSEC2/latest/UserGuide/enhanced-networking-ena.md") and [Enabling enhanced networking with the Elastic Network Adapter (ENA) on Windows
instances](../../../AWSEC2/latest/WindowsGuide/enhanced-networking-ena.md "../../../AWSEC2/latest/WindowsGuide/enhanced-networking-ena.md").

How you set up the collection of network performance metrics differs on Linux servers
and Windows servers.

The following table lists these network performance metrics enabled by the ENA
adapter. When the CloudWatch agent imports these metrics into CloudWatch from Linux instances, it
prepends `ethtool_` at the beginning of each of these metric names.

| Metric                                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name on Linux servers: `**bw\_in\_allowance\_exceeded**`<br>Name on Windows servers: `**Aggregate inbound BW<br>allowance exceeded**`      | The number of packets queued and/or dropped because the inbound aggregate<br>bandwidth exceeded the maximum for the instance.<br>This metric is collected only if you have listed it in the<br>`ethtool` subsection of the `metrics_collected` section<br>of the CloudWatch agent configuration file. For more information, see Collect network performance metrics<br>Unit: None                                                                                                                                                                                                                                                                                                      |
| Name on Linux servers: `**bw\_out\_allowance\_exceeded**`<br>Name on Windows servers: `**Aggregate outbound BW<br>allowance exceeded**`    | The number of packets queued and/or dropped because the outbound aggregate<br>bandwidth exceeded the maximum for the instance.<br>This metric is collected only if you have listed it in the<br>`ethtool` subsection of the `metrics_collected` section<br>of the CloudWatch agent configuration file. For more information, see Collect network performance metrics<br>Unit: None                                                                                                                                                                                                                                                                                                     |
| Name on Linux servers:`**conntrack\_allowance\_available**`<br>Name on Windows servers: `**Available connection<br>tracking allowance**`   | Reports the number of tracked connections that can be established by the<br>instance before hitting the Connections Tracked allowance of that instance type.<br>This metric is available only on Nitro-based EC2 instances using the Linux<br>driver for Elastic Network Adapter (ENA) starting from version 2.8.1, and on<br>computers using the Windows driver for Elastic Network Adapter (ENA) starting<br>from version 2.6.0.<br>This metric is collected only if you have listed it in the<br>`ethtool` subsection of the `metrics_collected` section<br>of the CloudWatch agent configuration file. For more information, see Collect network performance metrics<br>Unit: None |
| Name on Linux servers:`**ena\_srd\_mode**`<br>Name on Windows servers: `**ena srd<br>mode**`                                               | Describes which ENA Express features are enabled. For more information about<br>ENA Express, see [Improve network performance<br>with ENA Express on Linux instances](../../../AWSEC2/latest/UserGuide/ena-express.md "../../../AWSEC2/latest/UserGuide/ena-express.md") Values are as follows:<br>• `0` = ENA Express off, UDP off<br>• `1` = ENA Express on, UDP off<br>• `2` = ENA Express off, UDP on<br>NoteThis happens only when ENA Express was originally enabled, and UDP was<br>configured to use it. The prior value is retained for UDP traffic.<br>• `3` = ENA Express on, UDP on                                                                                        |
| Name on Linux servers:`**ena\_srd\_eligible\_tx\_pkts**`<br>Name on Windows servers: `**ena srd eligible tx<br>pkts**`                     | The number of network packets sent within a given time period that meet<br>AWS Scalable Reliable Datagram (SRD) requirements for eligibility, as<br>follows:<br>• Both sending and receiving instance types are supported.<br>• Both sending and receiving instances must have ENA Express<br>configured.<br>• The sending and receiving instances must be on the same subnet.<br>• The network path between the instances must not include middleware<br>boxes. ENA Express doesn't currently support middleware boxes.                                                                                                                                                               |
| Name on Linux servers:`**ena\_srd\_tx\_pkts**`<br>Name on Windows servers: `**ena srd tx<br>pkts**`                                        | The number of SRD packets transmitted within a given time period.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Name on Linux servers:`**ena\_srd\_rx\_pkts**`<br>Name on Windows servers: `**ena srd rx<br>pkts**`                                        | The number of SRD packets received within a given time period.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Name on Linux servers:`**ena\_srd\_resource\_utilization**`<br>Name on Windows servers: `**ena srd resource<br>utilization**`              | The percentage of the maximum allowed memory utilization for concurrent SRD<br>connections that the instance has consumed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Name on Linux servers: `**linklocal\_allowance\_exceeded**`<br>Name on Windows servers: `**Link local packet rate<br>allowance exceeded**` | The number of packets dropped because the PPS of the traffic to local proxy<br>services exceeded the maximum for the network interface. This impacts traffic to<br>the DNS service, the Instance Metadata Service, and the Amazon Time Sync<br>Service, but does not impact traffic to custom DNS resolvers.<br>This metric is collected only if you have listed it in the<br>`ethtool` subsection of the `metrics_collected` section<br>of the CloudWatch agent configuration file. For more information, see Collect network performance metrics<br>Unit: None                                                                                                                       |
| Name on Linux servers: `**pps\_allowance\_exceeded**`<br>Name on Windows servers: `**PPS allowance<br>exceeded**`                          | The number of packets queued and/or dropped because the bidirectional PPS<br>exceeded the maximum for the instance.<br>This metric is collected only if you have listed it in the<br>`ethtool` subsection of the `metrics_collected` section<br>of the CloudWatch agent configuration file. For more information, see Collect network performance metrics<br>Unit: None                                                                                                                                                                                                                                                                                                                |

## Linux setup

On Linux servers, the _ethtool plugin_ enables you to import the
network performance metrics into CloudWatch.

ethtool is a standard Linux utility that can collect statistics about Ethernet
devices on Linux servers. The statistics it collects depend on the network device and
driver. Examples of these statistics include `tx_cnt`, `rx_bytes`,
`tx_errors`, and `align_errors`. When you use the ethtool plugin
with the CloudWatch agent, you can also import these statistics into CloudWatch, along with the EC2
network performance metrics listed earlier in this section.

###### Tip

To find the statistics available on our operating system and network device, use
the `ethtool –S` command.

When the CloudWatch agent imports metrics into CloudWatch, it adds an `ethtool_`
prefix to the names of all imported metrics. So the standard ethtool statistic
`rx_bytes` is called `ethtool_rx_bytes` in CloudWatch, and the EC2
network performance metric `bw_in_allowance_exceeded` is called
`ethtool_bw_in_allowance_exceeded` in CloudWatch.

On Linux servers, to import ethtool metrics, add an `ethtool` section to
the `metrics_collected` section of the CloudWatch agent configuration file. The
`ethtool` section can include the following subsections:

- **interface_include**— Including this
  section causes the agent to collect metrics from only the interfaces that have names
  listed in this section. If you omit this section, metrics are collected from all
  Ethernet interfaces that aren't listed in `interface_exclude`.

The default ethernet interface is `eth0`.

- **interface_exclude**— If you include this
  section, list the Ethernet interfaces that you don't want to collect metrics
  from.

The ethtool plugin always ignores loopback interfaces.

- **metrics_include**— This section lists the
  metrics to import into CloudWatch. It can include both standard statistics collected by
  ethtool and Amazon EC2 high-resolution network metrics.

The following example displays part of the CloudWatch agent configuration file. This
configuration collects the standard ethtool metrics `rx_packets` and
`tx_packets`, and the Amazon EC2 network performance metrics from only the
`eth1` interface.

For more information about the CloudWatch agent configuration file, see [Manually create or edit the CloudWatch agent configuration file](CloudWatch-Agent-Configuration-File-Details.md "CloudWatch-Agent-Configuration-File-Details.md").

```
{
"metrics": {
    "append_dimensions": {
      "InstanceId": "${aws:InstanceId}"
    },
    "metrics_collected": {
      "ethtool": {
        "interface_include": [
          "eth1"
        ],
        "metrics_include": [
          "bw_in_allowance_exceeded",
          "bw_out_allowance_exceeded",
          "conntrack_allowance_exceeded",
          "linklocal_allowance_exceeded",
          "pps_allowance_exceeded"
         ]
      }
   }
}
}

```

## Windows setup

On Windows servers, the network performance metrics are available through Windows
Performance Counters, which the CloudWatch agent already collects metrics from. So you do not
need a plugin to collect these metrics from Windows servers.

The following is a sample configuration file to collect network performance metrics
from Windows. For more information about editing the CloudWatch agent configuration file, see
[Manually create or edit the CloudWatch agent configuration file](CloudWatch-Agent-Configuration-File-Details.md "CloudWatch-Agent-Configuration-File-Details.md").

```
{
    "metrics": {
        "append_dimensions": {
            "InstanceId": "${aws:InstanceId}"
        },
        "metrics_collected": {
            "ENA Packets Shaping": {
                "measurement": [
                    "Aggregate inbound BW allowance exceeded",
                    "Aggregate outbound BW allowance exceeded",
                    "Connection tracking allowance exceeded",
                    "Link local packet rate allowance exceeded",
                    "PPS allowance exceeded"
                ],
                "metrics_collection_interval": 60,
                "resources": [
                    "*"
                ]
            }
        }
    }
}
```

## Viewing network performance metrics

After importing network performance metrics into CloudWatch, you can view these metrics as
time series graphs, and create alarms that can watch these metrics and notify you if
they breach a threshold that you specify. The following procedure shows how to view
ethtool metrics as a time series graph. For more information about setting alarms, see
[Using Amazon CloudWatch alarms](CloudWatch_Alarms.md "CloudWatch_Alarms.md").

Because all of these metrics are aggregate counters, you can use CloudWatch metric math
functions such as `RATE(METRICS())` to calculate the rate for these metrics
in graphs or use them to set alarms. For more information about metric math functions,
see [Using math expressions with CloudWatch metrics](using-metric-math.md "using-metric-math.md").

###### To view network performance metrics in the CloudWatch console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**.
3. Choose the namespace for the metrics collected by the agent. By default, this is
   **CWAgent**, but you may have specified a different namespace in
   the CloudWatch agent configuration file.
4. Choose a metric dimension (for example, **Per-Instance
   Metrics**).
5. The **All metrics** tab displays all metrics for that dimension
   in the namespace. You can do the following:
   1. To graph a metric, select the check box next to the metric. To select all
      metrics, select the check box in the heading row of the table.
   2. To sort the table, use the column heading.
   3. To filter by resource, choose the resource ID, and then choose **Add
      to search**.
   4. To filter by metric, choose the metric name, and then choose **Add
      to search**.

6. (Optional) To add this graph to a CloudWatch dashboard, choose
   **Actions**, and then choose **Add to
   dashboard**.
