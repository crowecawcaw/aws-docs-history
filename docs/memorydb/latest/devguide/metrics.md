# Host-Level Metrics

The `AWS/MemoryDB` namespace includes the following host-level metrics for individual nodes.

See Also

- [Metrics for MemoryDB](metrics.md "metrics.md")

| Metric                                     | Description                                                                                                                                                                                                      | Unit    |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `CPUUtilization`                           | The percentage of CPU utilization for the entire host. Because Valkey and Redis OSS are<br>single-threaded, we recommend you monitor<br>`EngineCPUUtilization` metric for nodes with 4 or more<br>vCPUs.         | Percent |
| `FreeableMemory`                           | The amount of free memory available on the host. This number is derived from the memory in RAM and buffers that the OS reports as freeable.                                                                      | Bytes   |
| `NetworkBytesIn`                           | The number of bytes the host has read from the network.                                                                                                                                                          | Bytes   |
| `NetworkBytesOut`                          | The number of bytes sent out on all network interfaces by the instance.                                                                                                                                          | Bytes   |
| `NetworkPacketsIn`                         | The number of packets received on all network interfaces by the instance. This metric identifies the volume of incoming traffic in terms of the number of packets on a single instance.                          | Count   |
| `NetworkPacketsOut`                        | The number of packets sent out on all network interfaces by the instance. This metric identifies the volume of outgoing traffic in terms of the number of packets on a single instance.                          | Count   |
| `NetworkBandwidthInAllowanceExceeded`      | The number of packets shaped because the inbound aggregate bandwidth exceeded the maximum for the instance.                                                                                                      | Count   |
| `NetworkConntrackAllowanceExceeded`        | The number of packets shaped because connection tracking exceeded the maximum for the instance and new connections could not be established. This can result in packet loss for traffic to or from the instance. | Count   |
| `NetworkBandwidthOutAllowanceExceeded`     | The number of packets shaped because the outbound aggregate bandwidth exceeded the maximum for the instance.                                                                                                     | Count   |
| `NetworkPacketsPerSecondAllowanceExceeded` | The number of packets shaped because the bidirectional packets per second exceeded the maximum for the instance.                                                                                                 | Count   |
| `NetworkMaxBytesIn`                        | The maximum per second burst of received bytes within each minute.                                                                                                                                               | Bytes   |
| `NetworkMaxBytesOut`                       | The maximum per second burst of transmitted bytes within each minute.                                                                                                                                            | Bytes   |
| `NetworkMaxPacketsIn`                      | The maximum per second burst of received packets within each minute.                                                                                                                                             | Count   |
| `NetworkMaxPacketsOut`                     | The maximum per second burst of transmitted packets within each minute.                                                                                                                                          | Count   |
| `SwapUsage`                                | The amount of swap used on the host.                                                                                                                                                                             | Bytes   |
