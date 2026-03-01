# Create the CloudWatch agent configuration file with the wizard

The agent configuration file wizard,
`amazon-cloudwatch-agent-config-wizard`, asks a series of questions to help you
configure the CloudWatch agent for your needs. This section describes the credentials required for
the configuration file. It describes how to run the CloudWatch agent configuration wizard. It also
describes the metrics that are predefined in the wizard.

## Required credentials

The wizard can autodetect the credentials and AWS Region to use if you have the
AWS credentials and configuration files in place before you start the wizard. For more
information about these files, see [Configuration and Credential Files](../../../cli/latest/userguide/cli-config-files.md "../../../cli/latest/userguide/cli-config-files.md") in the
_AWS Systems Manager User Guide_.

In the AWS credentials file, the wizard checks for default credentials and also
looks for an `AmazonCloudWatchAgent` section such as the following:

```
[AmazonCloudWatchAgent]
aws_access_key_id = `my_access_key`
aws_secret_access_key = `my_secret_key`

```

The wizard displays the default credentials, the credentials from the
`AmazonCloudWatchAgent`, and an `Others` option. You can select
which credentials to use. If you choose `Others`, you can input
credentials.

For `my_access_key` and
`my_secret_key`, use the keys from the IAM user that has the
permissions to write to Systems Manager Parameter Store.

In the AWS configuration file, you can specify the Region that the agent sends
metrics to if it's different than the `[default]` section. The default is to
publish the metrics to the Region where the Amazon EC2 instance is located. If the metrics
should be published to a different Region, specify the Region here. In the following
example, the metrics are published to the `us-west-1` Region.

```
[AmazonCloudWatchAgent]
region = us-west-1

```

## Run the CloudWatch agent configuration wizard

###### To create the CloudWatch agent configuration file

1. Start the CloudWatch agent configuration wizard by entering the following:

```
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-config-wizard
```

On a server running Windows Server, run the following commands to launch the
wizard:

```
cd "C:\Program Files\Amazon\AmazonCloudWatchAgent"
```

```
.\amazon-cloudwatch-agent-config-wizard.exe
```

2. Answer the questions to customize the configuration file for your server.
3. If you're storing the configuration file locally, the configuration file
   `config.json` is stored in
   `/opt/aws/amazon-cloudwatch-agent/bin/` on Linux servers, and is stored
   in `C:\Program Files\Amazon\AmazonCloudWatchAgent` on Windows Server. You
   can then copy this file to other servers where you want to install the agent.

If you're going to use Systems Manager to install and configure the
agent, be sure to answer **Yes** when prompted whether to store the
file in Systems Manager Parameter Store. You can also choose to store the file in Parameter Store even if you
aren't using the SSM Agent to install the CloudWatch agent. To be able to store the file in
Parameter Store, you must use an IAM role with sufficient permissions.

## CloudWatch agent predefined metric sets

The wizard is configured with predefined sets of metrics, with different detail
levels. These sets of metrics are shown in the following tables. For more information
about these metrics, see [Metrics collected by the CloudWatch agent](metrics-collected-by-CloudWatch-agent.md "metrics-collected-by-CloudWatch-agent.md").

###### Note

Parameter Store supports parameters in Standard and Advanced tiers. These parameter tiers
are not related to the Basic, Standard, and Advanced levels of metric details that are
described in these tables.

**Amazon EC2 instances running Linux**

| Detail level | Metrics included                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Basic**    | **Mem:\*<br>• mem_used_percent<br>**Disk:\*<br>• disk_used_percent<br>The `disk` metrics such as `disk_used_percent` have a<br>dimension for `Partition`, which means that the number of custom<br>metrics generated is dependent on the number of partitions associated with your<br>instance. The number of disk partitions you have depends on which AMI you are<br>using and the number of Amazon EBS volumes you attach to the server. |
| **Standard** | **CPU:**<br>`cpu_usage_idle`, `cpu_usage_iowait`,<br>`cpu_usage_user`, `cpu_usage_system`<br>**Disk:**<br>`disk_used_percent`, `disk_inodes_free`<br>**Diskio:**<br>`diskio_io_time`<br>**Mem:**<br>`mem_used_percent`<br>**Swap:**<br>`swap_used_percent`                                                                                                                                                                                  |
| **Advanced** | **CPU:**<br>`cpu_usage_idle`, `cpu_usage_iowait`,<br>`cpu_usage_user`, `cpu_usage_system`<br>**Disk:**<br>`disk_used_percent`, `disk_inodes_free`<br>**Diskio:**<br>`diskio_io_time`, `diskio_write_bytes`,<br>`diskio_read_bytes`, `diskio_writes`,<br>`diskio_reads`<br>**Mem:**<br>`mem_used_percent`<br>**Netstat:**<br>`netstat_tcp_established`, `netstat_tcp_time_wait`<br>**Swap:**<br>`swap_used_percent`                          |

**On-premises servers running Linux**

| Detail level | Metrics included                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Basic**    | **Disk:**<br>`disk_used_percent`<br>**Diskio:**<br>`diskio_write_bytes`, `diskio_read_bytes`,<br>`diskio_writes`, `diskio_reads`<br>**Mem:**<br>`mem_used_percent`<br>**Net:**<br>`net_bytes_sent`, `net_bytes_recv`,<br>`net_packets_sent`, `net_packets_recv`<br>**Swap:**<br>`swap_used_percent`                                                                                                                                                                                                                                                      |
| **Standard** | **CPU:**<br>`cpu_usage_idle`, `cpu_usage_iowait`<br>**Disk:**<br>`disk_used_percent`, `disk_inodes_free`<br>**Diskio:**<br>`diskio_io_time`, `diskio_write_bytes`,<br>`diskio_read_bytes`, `diskio_writes`,<br>`diskio_reads`<br>**Mem:**<br>`mem_used_percent`<br>**Net:**<br>`net_bytes_sent`, `net_bytes_recv`,<br>`net_packets_sent`, `net_packets_recv`<br>**Swap:**<br>`swap_used_percent`                                                                                                                                                         |
| **Advanced** | **CPU:**<br>`cpu_usage_guest`, `cpu_usage_idle`,<br>`cpu_usage_iowait`, `cpu_usage_steal`,<br>`cpu_usage_user`, `cpu_usage_system`<br>**Disk:**<br>`disk_used_percent`, `disk_inodes_free`<br>**Diskio:**<br>`diskio_io_time`, `diskio_write_bytes`,<br>`diskio_read_bytes`, `diskio_writes`,<br>`diskio_reads`<br>**Mem:**<br>`mem_used_percent`<br>**Net:**<br>`net_bytes_sent`, `net_bytes_recv`,<br>`net_packets_sent`, `net_packets_recv`<br>**Netstat:**<br>`netstat_tcp_established`, `netstat_tcp_time_wait`<br>**Swap:**<br>`swap_used_percent` |

**Amazon EC2 instances running Windows Server**

###### Note

The metric names listed in this table display how the metric appears when viewed in
the console. The actual metric name might not include the first word. For example, the
actual metric name for `LogicalDisk % Free Space` is just `% Free
 Space`.

| Detail level | Metrics included                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Basic**    | **Memory:**<br>`Memory % Committed Bytes In Use`<br>**LogicalDisk:**<br>`LogicalDisk % Free Space`                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Standard** | **Memory:**<br>`Memory % Committed Bytes In Use`<br>**Paging:**<br>`Paging File % Usage`<br>**Processor:**<br>`Processor % Idle Time`, `Processor % Interrupt Time`,<br>`Processor % User Time`<br>**PhysicalDisk:**<br>`PhysicalDisk % Disk Time`<br>**LogicalDisk:**<br>`LogicalDisk % Free Space`                                                                                                                                                                                                                                     |
| **Advanced** | **Memory:**<br>`Memory % Committed Bytes In Use`<br>**Paging:**<br>`Paging File % Usage`<br>**Processor:**<br>`Processor % Idle Time`, `Processor % Interrupt Time`,<br>`Processor % User Time`<br>**LogicalDisk:**<br>`LogicalDisk % Free Space`<br>**PhysicalDisk:**<br>`PhysicalDisk % Disk Time`, `PhysicalDisk Disk Write<br>Bytes/sec`, `PhysicalDisk Disk Read Bytes/sec`,<br>`PhysicalDisk Disk Writes/sec`, `PhysicalDisk Disk<br>Reads/sec`<br>**TCP:**<br>`TCPv4 Connections Established`, `TCPv6 Connections<br>Established` |

**On-premises server running Windows Server**

###### Note

The metric names listed in this table display how the metric appears when viewed in
the console. The actual metric name might not include the first word. For example, the
actual metric name for `LogicalDisk % Free Space` is just `% Free
 Space`.

| Detail level | Metrics included                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Basic**    | **Paging:\*<br>• `Paging File %<br>Usage`<br>**Processor:**<br>`Processor % Processor Time`<br>**LogicalDisk:**`LogicalDisk % Free<br>Space`<br>**PhysicalDisk:**<br>`PhysicalDisk Disk Write Bytes/sec`, `PhysicalDisk Disk Read<br>Bytes/sec`, `PhysicalDisk Disk Writes/sec`,<br>`PhysicalDisk Disk Reads/sec`<br>**Memory:**<br>`Memory % Committed Bytes In Use`<br>**Network Interface:\*\*<br>`Network Interface Bytes Sent/sec`, `Network Interface Bytes<br>Received/sec`, `Network Interface Packets Sent/sec`,<br>`Network Interface Packets Received/sec`                                                                                                                                                                                                  |
| **Standard** | **Paging:**<br>`Paging File % Usage`<br>**Processor:**<br>`Processor % Processor Time`, `Processor % Idle Time`,<br>`Processor % Interrupt Time`<br>**LogicalDisk:**<br>`LogicalDisk % Free Space`<br>**PhysicalDisk:**<br>`PhysicalDisk % Disk Time`, `PhysicalDisk Disk Write<br>Bytes/sec`, `PhysicalDisk Disk Read Bytes/sec`,<br>`PhysicalDisk Disk Writes/sec`, `PhysicalDisk Disk<br>Reads/sec`<br>**Memory:**<br>`Memory % Committed Bytes In Use`<br>**Network Interface:**<br>`Network Interface Bytes Sent/sec`, `Network Interface Bytes<br>Received/sec`, `Network Interface Packets Sent/sec`,<br>`Network Interface Packets Received/sec`                                                                                                               |
| **Advanced** | **Paging:**`Paging File %<br>Usage`<br>**Processor:**<br>`Processor % Processor Time`, `Processor % Idle Time`,<br>`Processor % Interrupt Time`, `Processor % User<br>Time`<br>**LogicalDisk:**<br>`LogicalDisk % Free Space`<br>**PhysicalDisk:**<br>`PhysicalDisk % Disk Time`, `PhysicalDisk Disk Write<br>Bytes/sec`, `PhysicalDisk Disk Read Bytes/sec`,<br>`PhysicalDisk Disk Writes/sec`, `PhysicalDisk Disk<br>Reads/sec`<br>**Memory:**<br>`Memory % Committed Bytes In Use`<br>**Network Interface:**<br>`Network Interface Bytes Sent/sec`, `Network Interface Bytes<br>Received/sec`, `Network Interface Packets Sent/sec`,<br>`Network Interface Packets Received/sec`<br>**TCP:**<br>`TCPv4 Connections Established`, `TCPv6 Connections<br>Established` |
