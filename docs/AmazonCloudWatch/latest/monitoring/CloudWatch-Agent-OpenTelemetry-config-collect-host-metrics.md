

# Collect host metrics

The `host_metrics` source collects host-level system metrics, such as CPU, memory, disk, file system, network, and process metrics, and sends them to the CloudWatch OTLP metrics endpoint. You query the metrics with PromQL. This source can include the following field:
+ `collection_interval` – Optional. Specifies how often the agent collects the metrics, in seconds. If you omit this field, the agent uses the `metrics_collection_interval` value from the `agent` section, or 30 seconds if that is also omitted.

The following `opentelemetry` section collects host metrics:

```json
{
  "opentelemetry": {
    "collect": {
      "host_metrics": {}
    }
  }
}
```

For the complete list of metrics that this source collects on each platform, see the following table. For the prerequisites, see [Prerequisites](CloudWatch-Agent-OpenTelemetry-config.md#CloudWatch-Agent-OpenTelemetry-config-prereqs). For how to start the agent and verify data, see [Start the agent and verify data](CloudWatch-Agent-OpenTelemetry-config.md#CloudWatch-Agent-OpenTelemetry-config-start).

## Host metrics that the agent collects
<a name="CloudWatch-Agent-OpenTelemetry-config-host-metrics"></a>

The `host_metrics` source collects metrics that use OpenTelemetry semantic conventions. On Amazon EC2, each metric has resource labels that identify the host, such as `@resource.host.id`, `@resource.host.type`, and `@resource.cloud.availability_zone`. The metrics that the agent collects depend on the operating system.


| Category | Metrics | Platforms | 
| --- | --- | --- | 
| CPU | system.cpu.time, system.cpu.utilization, system.cpu.logical.count, system.cpu.physical.count, system.cpu.load\_average.1m, system.cpu.load\_average.5m, system.cpu.load\_average.15m | Linux, Windows Server, and macOS | 
|  | system.cpu.frequency | Linux | 
| Memory | system.memory.usage, system.memory.utilization, system.memory.limit, system.memory.page\_size | Linux, Windows Server, and macOS | 
|  | system.linux.memory.available, system.linux.memory.dirty | Linux | 
| Disk | system.disk.io, system.disk.io\_time, system.disk.operations, system.disk.operation\_time, system.disk.pending\_operations | Linux, Windows Server, and macOS | 
|  | system.disk.merged, system.disk.weighted\_io\_time | Linux | 
| File system | system.filesystem.usage, system.filesystem.utilization | Linux, Windows Server, and macOS | 
|  | system.filesystem.inodes.usage | Linux and macOS | 
| Network | system.network.io, system.network.packets, system.network.errors, system.network.dropped, system.network.connections | Linux, Windows Server, and macOS | 
| Processes | system.processes.count | Linux and macOS | 
|  | system.processes.created | Linux | 